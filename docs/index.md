
# Nmdc_Schema schema


Schema for National Microbiome Data Collaborative (NMDC)


### Classes

 * [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value
    * [BooleanValue](BooleanValue.md) - A value that is a boolean
    * [ControlledTermValue](ControlledTermValue.md) - A controlled term or class from an ontology
    * [GeolocationValue](GeolocationValue.md) - A normalized value for a location on the earth's surface
    * [IntegerValue](IntegerValue.md) - A value that is an integer
    * [QuantityValue](QuantityValue.md) - A simple quantity, e.g. 2cm
    * [TextValue](TextValue.md) - A basic string value
    * [TimestampValue](TimestampValue.md) - A value that is a timestamp. The range should be ISO-8601
    * [UrlValue](UrlValue.md) - A value that is a string that conforms to URL syntax
 * [NamedThing](NamedThing.md) - a databased entity or concept/class
    * [Biosample](Biosample.md) - A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.  
    * [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
       * [OmicsProcessing](OmicsProcessing.md) - The methods and processes used to generate omics data from a biosample or organism.
    * [DataObject](DataObject.md) - An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects. 
    * [OntologyClass](OntologyClass.md)
       * [EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md)
    * [Person](Person.md) - represents a person, such as a researcher
    * [Study](Study.md) - A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.  
 * [Unit](Unit.md)

### Mixins


### Slots

 * [alternate identifiers](alternate_identifiers.md) - Non-primary identifiers
    * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)
    * [omics processing➞alternate identifiers](omics_processing_alternate_identifiers.md)
    * [study➞alternate identifiers](study_alternate_identifiers.md)
 * [annotations](annotations.md)
 * [attribute](attribute.md) - A attribute of a biosample. Examples: depth, habitat, material. For NMDC, attributes SHOULD be mapped to terms within a MIxS template
    * [16s_recover](16s_recover.md) - Can a 16S gene be recovered from the submitted SAG or MAG?
    * [16s_recover_software](16s_recover_software.md) - Tools used for 16S rRNA gene extraction
    * [adapters](adapters.md) - Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters
    * [alt](alt.md) - "Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earthbs surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air"
    * [annot](annot.md) - "Tool used for annotation, or for cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter"
    * [assembly_name](assembly_name.md) - Name/version of the assembly provided by the submitter that is used in the genome browsers and in the community
    * [assembly_qual](assembly_qual.md) - "The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least 18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling 3 90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated"
    * [assembly_software](assembly_software.md) - "Tool(s) used for assembly, including version number and parameters"
    * [bin_param](bin_param.md) - The parameters that have been applied during the extraction of genomes from metagenomic datasets
    * [bin_software](bin_software.md) - Tool(s) used for the extraction of genomes from metagenomic datasets
    * [biotic_relationship](biotic_relationship.md) - "Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object"
    * [chimera_check](chimera_check.md) - "A chimeric sequence, or chimera for short, is a sequence comprised of two or more phylogenetically distinct parent sequences. Chimeras are usually PCR artifacts thought to occur when a prematurely terminated amplicon reanneals to a foreign DNA strand and is copied to completion in the following PCR cycles. The point at which the chimeric sequence changes from one parent to the next is called the breakpoint or conversion point "
    * [collection_date](collection_date.md) - "The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant"
    * [compl_appr](compl_appr.md) - "The approach used to determine the completeness of a given SAG or MAG, which would typically make use of a set of conserved marker genes or a closely related reference genome. For UViG completeness, include reference genome or group used, and contig feature suggesting a complete genome"
    * [compl_score](compl_score.md) - "Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores"
    * [compl_software](compl_software.md) - "Tools used for completion estimate, i.e. checkm, anvi'o, busco"
    * [contam_score](contam_score.md) - "The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. The following scores are acceptable for; High Quality Draft: < 5%, Medium Quality Draft: < 10%, Low Quality Draft: < 10%. Contamination must be below 5% for a SAG or MAG to be deposited into any of the public databases"
    * [contam_screen_input](contam_screen_input.md) - The type of sequence data used as input
    * [contam_screen_param](contam_screen_param.md) - "Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer"
    * [decontam_software](decontam_software.md) - Tool(s) used in contamination screening
    * [depth](depth.md) - Please refer to the definitions of depth in the environmental packages
       * [biosample➞depth](biosample_depth.md)
    * [detec_type](detec_type.md) - Type of UViG detection
    * [elev](elev.md) - "Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit"
    * [encoded_traits](encoded_traits.md) - "Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage"
    * [env_broad_scale](env_broad_scale.md) - "In this field, report which major environmental system your sample or specimen came from. The systems identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. were you in the desert or a rainforest?). We recommend using subclasses of ENVOUs biome class: http://purl.obolibrary.org/obo/ENVO_00000428. Format (one term): termLabel [termID], Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a water sample from the photic zone in middle of the Atlantic Ocean, consider: oceanic epipelagic zone biome [ENVO:01000033]. Example: Annotating a sample from the Amazon rainforest consider: tropical moist broadleaf forest biome [ENVO:01000228]. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
       * [biosample➞env_broad_scale](biosample_env_broad_scale.md)
    * [env_local_scale](env_local_scale.md) - "In this field, report the entity or entities which are in your sample or specimenUs local vicinity and which you believe have significant causal influences on your sample or specimen. Please use terms that are present in ENVO and which are of smaller spatial grain than your entry for env_broad_scale. Format (one term): termLabel [termID]; Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a pooled sample taken from various vegetation layers in a forest consider: canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336]. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
       * [biosample➞env_local_scale](biosample_env_local_scale.md)
    * [env_medium](env_medium.md) - "In this field, report which environmental material or materials (pipe separated) immediately surrounded your sample or specimen prior to sampling, using one or more subclasses of ENVOUs environmental material class: http://purl.obolibrary.org/obo/ENVO_00010483. Format (one term): termLabel [termID]; Format (multiple terms): termLabel [termID]|termLabel [termID]|termLabel [termID]. Example: Annotating a fish swimming in the upper 100 m of the Atlantic Ocean, consider: ocean water [ENVO:00002151]. Example: Annotating a duck on a pond consider: pond water [ENVO:00002228]|air ENVO_00002005. If needed, request new terms on the ENVO tracker, identified here: http://www.obofoundry.org/ontology/envo.html"
       * [biosample➞env_medium](biosample_env_medium.md)
    * [env_package](env_package.md) - "MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported"
    * [estimated_size](estimated_size.md) - The estimated size of the genome prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period.
    * [experimental_factor](experimental_factor.md) - "Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * [extrachrom_elements](extrachrom_elements.md) - Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids)
    * [feat_pred](feat_pred.md) - "Method used to predict UViGs features such as ORFs, integration site, etc."
    * [file_size](file_size.md) - units should be bytes.. may be overkill to allow different units
    * [geo_loc_name](geo_loc_name.md) - "The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (v 1.512) (http://purl.bioontology.org/ontology/GAZ)"
    * [gold_path_field](gold_path_field.md)
       * [ecosystem](ecosystem.md)
       * [ecosystem_category](ecosystem_category.md)
       * [ecosystem_subtype](ecosystem_subtype.md)
       * [ecosystem_type](ecosystem_type.md)
       * [specific_ecosystem](specific_ecosystem.md)
    * [health_disease_stat](health_disease_stat.md) - Health or disease status of specific host at time of collection
    * [host_pred_appr](host_pred_appr.md) - Tool or approach used for host prediction
    * [host_pred_est_acc](host_pred_est_acc.md) - "For each tool or approach used for host prediction, estimated false discovery rates should be included, either computed de novo or from the literature"
    * [host_spec_range](host_spec_range.md) - The NCBI taxonomy identifier of the specific host if it is known
    * [investigation_type](investigation_type.md) - "Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome"
    * [isol_growth_condt](isol_growth_condt.md) - "Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material"
    * [lat_lon](lat_lon.md) - The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system
       * [biosample➞lat_lon](biosample_lat_lon.md)
    * [lib_layout](lib_layout.md) - "Specify whether to expect single, paired, or other configuration of reads"
    * [lib_reads_seqd](lib_reads_seqd.md) - Total number of clones sequenced from the library
    * [lib_screen](lib_screen.md) - Specific enrichment or screening methods applied before and/or after creating libraries
    * [lib_size](lib_size.md) - Total number of clones in the library prepared for the project
    * [lib_vector](lib_vector.md) - Cloning vector type(s) used in construction of libraries
    * [mag_cov_software](mag_cov_software.md) - Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of genomes from metagenomic datasets
    * [mid](mid.md) - "Molecular barcodes, called Multiplex Identifiers (MIDs), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters"
    * [nucl_acid_amp](nucl_acid_amp.md) - "A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids"
    * [nucl_acid_ext](nucl_acid_ext.md) - "A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample"
    * [num_replicons](num_replicons.md) - "Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote"
    * [number_contig](number_contig.md) - "Total number of contigs in the cleaned/submitted assembly that makes up a given genome, SAG, MAG, or UViG"
    * [pathogenicity](pathogenicity.md) - To what is the entity pathogenic
    * [pcr_cond](pcr_cond.md) - Description of reaction conditions and components of PCR in the form of  'initial denaturation:94degC_1.5min; annealing=...'
    * [pcr_primers](pcr_primers.md) - "PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters"
    * [ploidy](ploidy.md) - "The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology (PATO), and for a browser of PATO (v 2018-03-27) please refer to http://purl.bioontology.org/ontology/PATO"
    * [pred_genome_struc](pred_genome_struc.md) - Expected structure of the viral genome
    * [pred_genome_type](pred_genome_type.md) - Type of genome predicted for the UViG
    * [project_name](project_name.md) - Name of the project within which the sequencing was organized
    * [propagation](propagation.md) - "This field is specific to different taxa. For phages: lytic/lysogenic, for plasmids: incompatibility group, for eukaryotes: sexual/asexual (Note: there is the strong opinion to name phage propagation obligately lytic or temperate, therefore we also give this choice"
    * [reassembly_bin](reassembly_bin.md) - Has an assembly been performed on a genome bin extracted from a metagenomic assembly?
    * [ref_biomaterial](ref_biomaterial.md) - "Primary publication if isolated before genome publication; otherwise, primary genome report"
    * [ref_db](ref_db.md) - "List of database(s) used for ORF annotation, along with version number and reference to website or publication"
    * [rel_to_oxygen](rel_to_oxygen.md) - "Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments"
    * [samp_collect_device](samp_collect_device.md) - The method or device employed for collecting the sample
    * [samp_mat_process](samp_mat_process.md) - "Any processing applied to the sample during or after retrieving the sample from environment. This field accepts OBI, for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * [samp_size](samp_size.md) - "Amount or size of sample (volume, mass or area) that was collected"
    * [seq_meth](seq_meth.md) - "Sequencing method used; e.g. Sanger, pyrosequencing, ABI-solid"
    * [seq_quality_check](seq_quality_check.md) - "Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA"
    * [sim_search_meth](sim_search_meth.md) - "Tool used to compare ORFs with database, along with version and cutoffs used"
    * [single_cell_lysis_appr](single_cell_lysis_appr.md) - Method used to free DNA from interior of the cell(s) or particle(s)
    * [single_cell_lysis_prot](single_cell_lysis_prot.md) - Name of the kit or standard protocol used for cell(s) or particle(s) lysis
    * [size_frac](size_frac.md) - Filtering pore size used in sample preparation
    * [sop](sop.md) - "Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences"
    * [sort_tech](sort_tech.md) - Method used to sort/isolate cells or particles of interest
    * [source_mat_id](source_mat_id.md) - "A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2)."
    * [source_uvig](source_uvig.md) - Type of dataset from which the UViG was obtained
    * [specific_host](specific_host.md) - "If there is a host involved, please provide its taxid (or environmental if not actually isolated from the dead or alive host - i.e. a pathogen could be isolated from a swipe of a bench etc) and report whether it is a laboratory or natural host)"
    * [submitted_to_insdc](submitted_to_insdc.md) - "Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases"
    * [subspecf_gen_lin](subspecf_gen_lin.md) - "This should provide further information about the genetic distinctness of the sequenced organism by recording additional information e.g. serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. It can also contain alternative taxonomic information. It should contain both the lineage name, and the lineage rank, i.e. biovar:abc123"
    * [target_gene](target_gene.md) - Targeted gene or locus name for marker gene studies
    * [target_subfragment](target_subfragment.md) - Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA
    * [tax_class](tax_class.md) - "Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes"
    * [tax_ident](tax_ident.md) - The phylogenetic marker(s) used to assign an organism name to the SAG or MAG
    * [trna_ext_software](trna_ext_software.md) - Tools used for tRNA identification
    * [trnas](trnas.md) - The total number of tRNAs identified from the SAG or MAG
    * [trophic_level](trophic_level.md) - Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph)
    * [url](url.md)
    * [vir_ident_software](vir_ident_software.md) - "Tool(s) used for the identification of UViG as a viral genome, software or protocol name  including version number, parameters, and cutoffs used"
    * [virus_enrich_appr](virus_enrich_appr.md) - "List of approaches used to enrich the sample for viruses, if any"
    * [votu_class_appr](votu_class_appr.md) - "Cutoffs and approach used when clustering new UViGs in Rspecies-levelS vOTUs. Note that results from standard 95% ANI / 85% AF clustering should be provided alongside vOTUS defined from another set of thresholds, even if the latter are the ones primarily used during the analysis"
    * [votu_db](votu_db.md) - "Reference database (i.e. sequences not generated as part of the current study) used to cluster new genomes in ""species-level"" vOTUs, if any"
    * [votu_seq_comp_appr](votu_seq_comp_appr.md) - "Tool and thresholds used to compare sequences when computing ""species-level"" vOTUs"
    * [wga_amp_appr](wga_amp_appr.md) - Method used to amplify genomic DNA in preparation for sequencing
    * [wga_amp_kit](wga_amp_kit.md) - Kit used to amplify genomic DNA in preparation for sequencing
 * [description](description.md) - a human-readable description of a thing
 * [has input](has_input.md) - An input to a process.
    * [biosample processing➞has input](biosample_processing_has_input.md)
 * [has numeric value](has_numeric_value.md) - Links a quantity value to a number
 * [has output](has_output.md) - An output biosample to a processing step
    * [omics processing➞has output](omics_processing_has_output.md)
 * [has raw value](has_raw_value.md) - The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * [geolocation value➞has raw value](geolocation_value_has_raw_value.md)
 * [has unit](has_unit.md) - Links a quantity value to a unit
 * [id](id.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * [biosample➞id](biosample_id.md)
    * [omics processing➞id](omics_processing_id.md)
    * [person➞id](person_id.md)
    * [study➞id](study_id.md)
 * [language](language.md) - Should use standard codes, e.g. "en"
 * [latitude](latitude.md) - latitude
 * [longitude](longitude.md) - longitude
 * [name](name.md) - A human readable label for an entity
    * [biosample➞name](biosample_name.md)
    * [omics processing➞name](omics_processing_name.md)
    * [study➞name](study_name.md)
 * [part of](part_of.md) - Links a resource to another resource that either logically or physically includes it.
    * [omics processing➞part of](omics_processing_part_of.md)

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
