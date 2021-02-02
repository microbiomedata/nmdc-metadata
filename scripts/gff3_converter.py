import os
import sys
import csv
import json


CV_MAP = {
    'CDS': 'SO:0000316'
}


def get_so_term(gff_type: str) -> str:
    """
    Get SO term corresponding to a GFF3 type.

    Parameters
    ----------
    gff_type: str
        A feature type from GFF3

    Returns
    -------
    str
        A CV term corresponding to the given type

    """
    return CV_MAP.get(gff_type, 'SO:0000110')


def prepare_curie(k: str, term: str) -> str:
    """
    Given a key and a term, prepare a CURIE for the term.

    Parameters
    ----------
    k: str
        The key
    term: str
        A database entity

    Returns
    -------
    str
        A CURIE representation of the given term

    """
    if k.lower() == 'ko':
        curie = f"KEGG.ORTHOLOGY:{term}"
    elif k.lower() == 'pfam':
        curie = f"PFAM:{term}"
    elif k.lower() == 'smart':
        curie = f"SMART:{term}"
    elif k.lower() == 'cog':
        curie = f"EGGNOG:{term}"
    elif k.lower() == 'cath_funfam':
        curie = f"CATH:{term}"
    elif k.lower() == 'superfamily':
        curie = f"SUPFAM:{term}"
    else:
        curie = f":{term}"
    return curie


def infer_term_category(curie: str) -> str:
    """
    Infer category for a term based on its prefix.

    Parameters
    ----------
    curie: str
        The CURIE of a database entity

    Returns
    -------
    str
        A category from NMDC schema

    """
    ref = curie.split(':')[0]
    if ref in {'KEGG.ORTHOLOGY', 'EGGNOG', 'PFAM', 'TIGRFAM', 'SUPFAM', 'CATH', 'PANTHER.FAMILY'}:
        category = "NMDC:OrthologyGroup"
    elif ref in {'KEGG.REACTION', 'RHEA', 'MetaCyc', 'EC', 'GO', 'MetaNetX', 'SEED', 'RetroRules'}:
        category = "NMDC:Reaction"
    elif ref in {'KEGG.PATHWAY', 'COG'}:
        category = "NMDC:Pathway"
    else:
        category = "NMDC:FunctionalAnnotationTerm"
    return category


def parse_record(record: list) -> None:
    """
    Parse a record from GFF3

    Parameters
    ----------
    record: list
        A record with list of fields

    """
    attr = record[-1].split(';')
    attr_dict = {x.split('=')[0]: '='.join(x.split('=')[1:]).split(',') for x in attr}

    gene_product = {
        'id': f"NMDC:{attr_dict['ID'][0]}",
        'type': "NMDC:GeneProduct"
    }
    feature_list.append(gene_product)

    genome_feature = {
        'seqid': record[0],
        'start': int(record[3]),
        'end': int(record[4]),
        'strand': record[6],
        'phase': int(record[7]),
        'type': f"NMDC:GenomeFeature",
        'feature_type': get_so_term(record[2]),
        'encodes': f"NMDC:{attr_dict['ID'][0]}"
    }
    feature_list.append(genome_feature)

    for k, v in attr_dict.items():
        if k in {'ko', 'pfam', 'smart', 'superfamily', 'cog', 'cath_funfam'}:
            for t in v:
                term_curie = prepare_curie(k, t)
                # term_category = infer_term_category(term_curie)
                # fa_term = {
                #     'id': term_curie,
                #     'category': [term_category]
                # }

                functional_annotation = {
                    'subject': f"NMDC:{attr_dict['ID'][0]}",
                    'has_function': term_curie,
                    'was_generated_by': 'N/A',
                    'type': "NMDC:FunctionalAnnotation"
                }
                functional_annotation_list.append(functional_annotation)


feature_list = []
functional_annotation_list = []

with open(sys.argv[1]) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        parse_record(line)
    with open('functional_annotation_set.json', 'w') as FH:
        FH.write(json.dumps({'functional_annotation_set': functional_annotation_list}))
    with open('feature_set.json', 'w') as FH:
        FH.write(json.dumps({'feature_set': feature_list}))
