
# include_portal_v1_schema


**metamodel version:** 1.7.0

**version:** 0.0.1


INCLUDE Schema v1 prototype for Portal Data Model


### Classes

 * [NamedThing](NamedThing.md) - root class
     * [Biospecimen](Biospecimen.md)
     * [DataFile](DataFile.md)
     * [Participant](Participant.md)
     * [Study](Study.md)

### Mixins


### Slots

 * [➞age_at_biospecimen_collection__days](biospecimen__age_at_biospecimen_collection__days.md) - Age (in days) of participant at time of biospecimen collection
 * [➞biospecimen_storage](biospecimen__biospecimen_storage.md) - Method by which Sample is stored
 * [➞collection_id](biospecimen__collection_id.md) - Identifier for a collection event, during which one or more primary samples are collected, assigned by DCC. Referenced in time with respect to clinical course or to other collection events.
 * [➞collection_sample_type](biospecimen__collection_sample_type.md) - Type of biological material comprising the collected sample
 * [➞container_id](biospecimen__container_id.md) - Unique identifier for specific container of sample, assigned by DCC or contributor??. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
 * [➞laboratory_procedure](biospecimen__laboratory_procedure.md) - Procedure by which Sample was derived from Parent Sample
 * [➞parent_sample_id](biospecimen__parent_sample_id.md) - Identifier from Parent Sample from which Sample was derived (if applicable)
 * [➞parent_sample_type](biospecimen__parent_sample_type.md) - Type of Parent Sample
 * [➞sample_availability](biospecimen__sample_availability.md) - Whether or not the container (or sample??) is available for sharing through the Virtual Biorepository
 * [➞sample_id](biospecimen__sample_id.md) - Identifier for sample, assigned (by DCC or contributor??) at time of collection, processing, treatment, or derivation. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
 * [➞sample_type](biospecimen__sample_type.md) - Type of biological material comprising the sample
 * [➞volume](biospecimen__volume.md) - Amount of sample in container
 * [➞volume_unit](biospecimen__volume_unit.md) - Unit of sample volume
 * [➞access_url](dataFile__access_url.md) - Storage location for this file ??
 * [➞collection_id](dataFile__collection_id.md) - List of Collection?? IDs for biospecimens associated with this file
 * [➞data_access](dataFile__data_access.md) - Type of access control on this file
 * [➞data_category](dataFile__data_category.md) - General category of data in file, e.g. Clinical; Genomic; Proteomic; Metabolomic
 * [➞data_type](dataFile__data_type.md) - Specific type of data contained in file, e.g. Simple nucleotide variations; aligned reads; gVCF
 * [➞experimental_strategy](dataFile__experimental_strategy.md) - Specific experimental method used to obtain data in file, e.g. Whole-genome sequencing; LCMS metabolomics
 * [➞file_id](dataFile__file_id.md) - File identifier, assigned by DCC??
 * [➞file_name](dataFile__file_name.md) - Name of file, assigned by data contributor??
 * [➞format](dataFile__format.md) - Format of file
 * [➞participant_id](dataFile__participant_id.md) - List of Participant IDs for participants associated with this file
 * [➞size](dataFile__size.md) - Size of file
 * [has_biospecimen](has_biospecimen.md)
 * [has_datafile](has_datafile.md)
 * [has_participant](has_participant.md)
 * [has_study](has_study.md)
 * [id](id.md)
 * [➞age_at_diagnosis__days](participant__age_at_diagnosis__days.md) - Age in days at which phenotype was assigned (or onset??)
 * [➞age_at_phenotype_assignment__days](participant__age_at_phenotype_assignment__days.md) - Age in days at which phenotype was recorded (or onset??)
 * [➞age_at_the_last_vital_status__days](participant__age_at_the_last_vital_status__days.md) - Age in days when participant's vital status was last recorded (or actual death date??)
 * [➞diagnosis__icd](participant__diagnosis__icd.md) - ICD-10 code (annotated by data contributor or DCC)
 * [➞diagnosis__mondo](participant__diagnosis__mondo.md) - Mondo disease ontology code (annotated by data contributor or DCC)
 * [➞diagnosis__ncit](participant__diagnosis__ncit.md) - NCI Thesaurus code (annotated by data contributor or DCC)
 * [➞diagnosis__source_text](participant__diagnosis__source_text.md) - Diagnosis as described by data contributor
 * [➞diagnosis_type](participant__diagnosis_type.md) - How diagnosis was assigned ??
 * [➞down_syndrome_status](participant__down_syndrome_status.md) - Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
 * [➞ethnicity](participant__ethnicity.md) - Ethnicity of participant
 * [➞external_id](participant__external_id.md) - Unique identifier for the participant, assigned by data contributor
 * [➞family_id](participant__family_id.md) - Unique identifer for family to which Participant belongs
 * [➞family_relationship](participant__family_relationship.md) - Relationship of Participant to other family members
 * [➞family_type](participant__family_type.md) - Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives) 
 * [➞father_id](participant__father_id.md) - Participant ID for Participant's father
 * [➞mother_id](participant__mother_id.md) - Participant ID for Participant's mother
 * [➞outcomes_vital_status](participant__outcomes_vital_status.md) - Whether participant is alive or dead [need valid values]
 * [➞participant_id](participant__participant_id.md) - Unique identifier for the participant, assigned by DCC
 * [➞phenotype__hpo](participant__phenotype__hpo.md) - Human Phenotype Ontology code (annotated by data contributor or DCC)
 * [➞phenotype__source_text](participant__phenotype__source_text.md) - Phenotype as described by data contributor
 * [➞phenotype_interpretation](participant__phenotype_interpretation.md) - Whether phenotype was observed or not
 * [➞race](participant__race.md) - Race of participant
 * [➞sex](participant__sex.md) - Sex of participant
 * [➞dbgap](study__dbgap.md) - dbGaP study accession code
 * [➞program](study__program.md) - Funding source for the study ??
 * [➞study_code](study__study_code.md) - Unique identifer for the study, assigned by DCC
 * [➞study_name](study__study_name.md) - Name of the study, chosen by data contributor

### Enums

 * [enum_data_access](enum_data_access.md)
 * [enum_down_syndrome_status](enum_down_syndrome_status.md)
 * [enum_ethnicity](enum_ethnicity.md)
 * [enum_family_type](enum_family_type.md)
 * [enum_phenotype_interpretation](enum_phenotype_interpretation.md)
 * [enum_program](enum_program.md)
 * [enum_race](enum_race.md)
 * [enum_sample_availability](enum_sample_availability.md)
 * [enum_sex](enum_sex.md)
 * [enum_study_code](enum_study_code.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
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
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
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
