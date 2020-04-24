# Identifiers in NMDC

Identifiers are crucial for the NMDC, both for any data objects *created* and for any external objects *referenced*

Examples of entities that require identifiers:

 * Samples
 * Data objects (e.g. sequence files)
 * Taxa
 * Genes
 * Ontology terms and other descriptors

Identifiers should be:

 * Permanent
 * Unique
 * Resolvable
 * Opaque

See [McMurry et al, PMID:28662064](https://www.ncbi.nlm.nih.gov/pubmed/28662064) for more desiderata.

Following McMurry et al we adopt the use of *prefixed identifiers*

For example: `biosample:SAMEA2397676`

All prefixes should be registered with a standard identifier prefix system. These include:

 * http://n2t.net
 * http://identifiers.org

These prefixed identifiers can also act as [CURIEs](https://www.w3.org/TR/curie/) (Compact URIs).

Examples:

 * https://registry.identifiers.org/registry/biosample

https://identifiers.org/biosample:SAMEA2397676

http://n2t.net/biosample:SAMEA2397676

# GOLD identifiers

Please check this section later

# identifiers for ontology terms

Most of the ontologies we use are in OBO. All OBO IDs are prefixed
using the ontology ID space. The list of ID spaces can be found on
http://obofoundry.org

For example the ID/CURIE `ENVO:00002007` represents the class `sediment` and is expanded to a URI of http://purl.obolibrary.org/obo/ENVO_00002007

# MIxS identifiers

Please check this section later

# Identifier mapping

Please check this section later
