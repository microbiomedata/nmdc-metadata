#!/usr/bin/perl -w
use strict;

# THIS WILL BE REWRITTEN IN PYTHON!

print "id: https://microbiomedata/schema/mixs\n\n";

print "imports:\n";
print "  - core\n\n";

print "slots:\n";

my %done = ();

my $file_no = 1;

while(<>) {
    if (m@Environmental package@) {
        # move onto mixs5e
        $file_no = 2;
        next;
    }
    
    next if m@^Structured comment name@;

        # delete 8th bit
        tr [\200-\377]
          [\000-\177];   # see 'man perlop', section on tr/
        # weird ascii characters should be excluded
        tr/\0-\10//d;   # remove weird characters; ascii 0-8
                        # preserve \11 (9 - tab) and \12 (10-linefeed)
        tr/\13\14//d;   # remove weird characters; 11,12
                        # preserve \15 (13 - carriage return)
        tr/\16-\37//d;  # remove 14-31 (all rest before space)
        tr/\177//d;     # remove DEL character
    
    chomp;
    my @vals = split(/\t/,$_);
    my ($package_name, $name, $item, $def, $expected, $value_syntax, $example, $section, $req);
    $section = '';
    if ($file_no == 1) {
        ($name, $item, $def, $expected, $value_syntax, $example, $section) = @vals;
    }
    else {
        ($package_name, $name, $item, $def, $expected, $value_syntax, $example, $req) = @vals;
    }

    next unless $name;
    
    next if $done{$name};
    
    my $unit = $vals[18];

    my $range = "text value";
    my $string_serialization;

    # hacks... need special inference
    if ($value_syntax eq '{text}') {
        $range = "text value";
    }
    if ($value_syntax eq '{timestamp}') {
        $range = "timestamp value";
    }
    if ($name eq 'lat_lon') {
        $range = 'geolocation value';
        $string_serialization = $value_syntax;
    }
    if ($name eq 'depth') {
        $range = 'quantity value';
        $string_serialization = $value_syntax;
    }
    if ($value_syntax =~ m@\{termLabel\}@) {
        $range = "controlled term value";
    }
    if ($value_syntax =~ m@\{unit\}@) {
        $range = "quantity value";
        $string_serialization = $value_syntax;
    }
    if ($value_syntax eq '{boolean}') {
        $range = "boolean value";
    }
    if ($expected eq 'measurement value') {
        $range = "quantity value";
    }

    if ($example =~ m@\'@) {
        $example = ''; # TODO escap
    }

    # escape
    if ($name =~ m@^[^a-zA-z_]@) {
        $name = '_'.$name;
    }
    $done{$name} = 1;

    my $re = translate_re($value_syntax);
    if ($re) {
        $re =~ s@\\@\\\\@g;
    }
    
    print "  $name:\n";
    print "    aliases:\n";
    print "      - $item\n";
    print "    description: >-\n";
    print "       $def\n";
    print "    multivalued: false\n"; # TODO
    print "    is_a: attribute\n";
    print "    range: $range  ## syntax: $value_syntax\n";
    print "    pattern: \"$re\"\n" if $re;
    print "    string_serialization: \"$string_serialization\"\n" if $string_serialization && $string_serialization =~ m@\{@;
    print "    mappings:\n";
    print "      - MIxS:$name\n";
    print "    in_subset:\n      - $section\n" if $section;
    #print "    examples:\n      - value: $example\n" if $example;
    #print "    examples:\n      - value: $example\n" if $example;
    print "\n";
}

exit 0;

sub translate_re {
    $_ = shift @_;
    s@\{float\}@\\d+[.\\d+]@g;
    s@\{boolean\}@[true|false]@g;
    s@\{unit\}@\\S+@g;
    s@\{termLabel\}@.*@g;
    s@\{\[termID\]\}@\\S+:\\S+@g;
    if ($_ eq '-') {
        return ;
    }
    s@([\'\-\/])@\\$1@g;

    # See: https://github.com/GenomicsStandardsConsortium/mixs/issues/94
    # some mixs regexes are incorrectly quoted
    if (m@^".*"$@) {
        s@^"\s*@@;
        s@\s*"@@;
    }
    # some mixs regexes have double ||s:
    s@\|\|@\|@g;
    
    if (m@\{@) {
        return;
    }
    else {
        return $_;
    }
}
