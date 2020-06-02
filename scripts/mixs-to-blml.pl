#!/usr/bin/perl -w
use strict;

print "id: https://microbiomedata/schema/mixs\n";
print "slots:\n";

while(<>) {
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
    my ($name, $item, $def, $expected, $value_syntax, $example, $section) = @vals;
    next unless $name;
    my $unit = $vals[18];

    my $range = "text value";

    # hacks... need special inference
    if ($value_syntax eq '{text}') {
        $range = "text value";
    }
    if ($value_syntax eq '{timestamp}') {
        $range = "timestamp value";
    }
    if ($name eq 'lat_lon') {
        $range = 'geolocation value';
    }
    if ($value_syntax =~ m@\{termLabel\}@) {
        $range = "controlled term value";
    }
    if ($value_syntax =~ m@\{unit\}@) {
        $range = "quantity value";
    }
    if ($expected eq 'measurement value') {
        $range = "quantity value";
    }

    if ($example =~ m@\'@) {
        $example = ''; # TODO escap
    }
    
    print "  $name:\n";
    print "    aliases:\n";
    print "      - $item\n";
    print "    description: >-\n";
    print "       $def\n";
    print "    multivalued: false\n"; # TODO
    print "    is_a: attribute\n";
    print "    range: $range\n";
    print "    mappings:\n";
    print "      - MIxS:$name\n";
    print "    #domain: $section:\n";
    print "    #examples: ['$example']\n" if $example;
    print "\n";
}
