---
parent: Classes
title: nmdc:Reaction
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Reaction


An individual biochemical transformation carried out by a functional unit of an organism, in which a collection of substrates are transformed into a collection of products. Can also represent transporters

URI: [nmdc:Reaction](https://microbiomedata/meta/Reaction)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReactionParticipant],[ReactionParticipant]%3Cright%20participants%200..%2A-++[Reaction%7Cdirection:string%20%3F;smarts_string:string%20%3F;is_diastereoselective:boolean%20%3F;is_stereo:boolean%20%3F;is_balanced:boolean%20%3F;is_transport:boolean%20%3F;is_fully_characterized:boolean%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[ReactionParticipant]%3Cleft%20participants%200..%2A-++[Reaction],[Pathway]-%20has_part%200..%2A%3E[Reaction],[FunctionalAnnotationTerm]%5E-[Reaction],[Pathway],[FunctionalAnnotationTerm])

---


## Identifier prefixes

 * KEGG.REACTION
 * RHEA
 * MetaCyc
 * EC
 * GO
 * MetaNetX
 * SEED
 * RetroRules

## Parents

 *  is_a: [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) - Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).

## Referenced by class

 *  **None** *[has_part](has_part.md)*  <sub>0..*</sub>  **[Reaction](Reaction.md)**
 *  **[Pathway](Pathway.md)** *[pathway➞has_part](pathway_has_part.md)*  <sub>0..*</sub>  **[Reaction](Reaction.md)**

## Attributes


### Own

 * [reaction➞direction](reaction_direction.md)  <sub>OPT</sub>
    * Description: One of l->r, r->l, bidirectional, neutral
    * range: [String](types/String.md)
 * [reaction➞is balanced](reaction_is_balanced.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is diastereoselective](reaction_is_diastereoselective.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is fully characterized](reaction_is_fully_characterized.md)  <sub>OPT</sub>
    * Description: False if includes R-groups
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is stereo](reaction_is_stereo.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is transport](reaction_is_transport.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞left participants](reaction_left_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞right participants](reaction_right_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞smarts string](reaction_smarts_string.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)

### Domain for slot:

 * [reaction➞direction](reaction_direction.md)  <sub>OPT</sub>
    * Description: One of l->r, r->l, bidirectional, neutral
    * range: [String](types/String.md)
 * [reaction➞is balanced](reaction_is_balanced.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is diastereoselective](reaction_is_diastereoselective.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is fully characterized](reaction_is_fully_characterized.md)  <sub>OPT</sub>
    * Description: False if includes R-groups
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is stereo](reaction_is_stereo.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞is transport](reaction_is_transport.md)  <sub>OPT</sub>
    * range: [Boolean](types/Boolean.md)
 * [reaction➞left participants](reaction_left_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞right participants](reaction_right_participants.md)  <sub>0..*</sub>
    * range: [ReactionParticipant](ReactionParticipant.md)
 * [reaction➞smarts string](reaction_smarts_string.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | biolink:MolecularActivity |

