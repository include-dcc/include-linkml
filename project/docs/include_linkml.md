
# IncludePortalV1


**metamodel version:** 1.7.0

**version:** None


Initial Include Portal Schema


### Classes

 * [NamedThing](NamedThing.md)
     * [Biospecimen](Biospecimen.md)
     * [DataFile](DataFile.md)
     * [Participant](Participant.md)
     * [Study](Study.md)

### Mixins


### Slots

 * [access_url](access_url.md)
     * [DataFile➞access_url](DataFile_access_url.md) - Storage location for this file ??
 * [age_at_biospecimen_collection__days](age_at_biospecimen_collection__days.md)
     * [Biospecimen➞age_at_biospecimen_collection__days](Biospecimen_age_at_biospecimen_collection__days.md) - Age (in days) of participant at time of biospecimen collection
 * [age_at_diagnosis__days](age_at_diagnosis__days.md)
     * [Participant➞age_at_diagnosis__days](Participant_age_at_diagnosis__days.md) - Age in days at which phenotype was assigned (or onset??)
 * [age_at_phenotype_assignment__days](age_at_phenotype_assignment__days.md)
     * [Participant➞age_at_phenotype_assignment__days](Participant_age_at_phenotype_assignment__days.md) - Age in days at which phenotype was recorded (or onset??)
 * [age_at_the_last_vital_status__days](age_at_the_last_vital_status__days.md)
     * [Participant➞age_at_the_last_vital_status__days](Participant_age_at_the_last_vital_status__days.md) - Age in days when participant's vital status was last recorded (or actual death date??)
 * [biospecimen_storage](biospecimen_storage.md)
     * [Biospecimen➞biospecimen_storage](Biospecimen_biospecimen_storage.md) - Method by which Sample is stored
 * [collection_id](collection_id.md)
     * [Biospecimen➞collection_id](Biospecimen_collection_id.md) - Identifier for a collection event, during which one or more primary samples are collected, assigned by DCC. Referenced in time with respect to clinical course or to other collection events.
     * [DataFile➞collection_id](DataFile_collection_id.md) - List of Collection?? IDs for biospecimens associated with this file
 * [collection_sample_type](collection_sample_type.md)
     * [Biospecimen➞collection_sample_type](Biospecimen_collection_sample_type.md) - Type of biological material comprising the collected sample
 * [container_id](container_id.md)
     * [Biospecimen➞container_id](Biospecimen_container_id.md) - Unique identifier for specific container of sample, assigned by DCC or contributor??. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
 * [data_access](data_access.md)
     * [DataFile➞data_access](DataFile_data_access.md) - Type of access control on this file
 * [data_category](data_category.md)
     * [DataFile➞data_category](DataFile_data_category.md) - General category of data in file, e.g. Clinical; Genomic; Proteomic; Metabolomic
 * [data_type](data_type.md)
     * [DataFile➞data_type](DataFile_data_type.md) - Specific type of data contained in file, e.g. Simple nucleotide variations; aligned reads; gVCF
 * [dbgap](dbgap.md)
     * [Study➞dbgap](Study_dbgap.md) - dbGaP study accession code
 * [diagnosis__icd](diagnosis__icd.md)
     * [Participant➞diagnosis__icd](Participant_diagnosis__icd.md) - ICD-10 code (annotated by data contributor or DCC)
 * [diagnosis__mondo](diagnosis__mondo.md)
     * [Participant➞diagnosis__mondo](Participant_diagnosis__mondo.md) - Mondo disease ontology code (annotated by data contributor or DCC)
 * [diagnosis__ncit](diagnosis__ncit.md)
     * [Participant➞diagnosis__ncit](Participant_diagnosis__ncit.md) - NCI Thesaurus code (annotated by data contributor or DCC)
 * [diagnosis__source_text](diagnosis__source_text.md)
     * [Participant➞diagnosis__source_text](Participant_diagnosis__source_text.md) - Diagnosis as described by data contributor
 * [diagnosis_type](diagnosis_type.md)
     * [Participant➞diagnosis_type](Participant_diagnosis_type.md) - How diagnosis was assigned ??
 * [down_syndrome_status](down_syndrome_status.md)
     * [Participant➞down_syndrome_status](Participant_down_syndrome_status.md) - Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
 * [ethnicity](ethnicity.md)
     * [Participant➞ethnicity](Participant_ethnicity.md) - Ethnicity of participant
 * [experimental_strategy](experimental_strategy.md)
     * [DataFile➞experimental_strategy](DataFile_experimental_strategy.md) - Specific experimental method used to obtain data in file, e.g. Whole-genome sequencing; LCMS metabolomics
 * [external_id](external_id.md)
     * [Participant➞external_id](Participant_external_id.md) - Unique identifier for the participant, assigned by data contributor
 * [family_id](family_id.md)
     * [Participant➞family_id](Participant_family_id.md) - Unique identifer for family to which Participant belongs
 * [family_relationship](family_relationship.md)
     * [Participant➞family_relationship](Participant_family_relationship.md) - Relationship of Participant to other family members
 * [family_type](family_type.md)
     * [Participant➞family_type](Participant_family_type.md) - Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)
 * [father_id](father_id.md)
     * [Participant➞father_id](Participant_father_id.md) - Participant ID for Participant's father
 * [file_id](file_id.md)
     * [DataFile➞file_id](DataFile_file_id.md) - File identifier, assigned by DCC??
 * [file_name](file_name.md)
     * [DataFile➞file_name](DataFile_file_name.md) - Name of file, assigned by data contributor??
 * [format](format.md)
     * [DataFile➞format](DataFile_format.md) - Format of file
 * [has_biospecimen](has_biospecimen.md) - Semantic link to a Biospecimen
     * [DataFile➞has_biospecimen](DataFile_has_biospecimen.md)
 * [has_datafile](has_datafile.md) - Semantic link to a DataFile
     * [Biospecimen➞has_datafile](Biospecimen_has_datafile.md)
     * [Participant➞has_datafile](Participant_has_datafile.md)
 * [has_participant](has_participant.md) - Semantic link to a Participant
     * [Biospecimen➞has_participant](Biospecimen_has_participant.md)
     * [DataFile➞has_participant](DataFile_has_participant.md)
 * [has_study](has_study.md) - Semantic link to a Study
     * [Biospecimen➞has_study](Biospecimen_has_study.md)
     * [DataFile➞has_study](DataFile_has_study.md)
     * [Participant➞has_study](Participant_has_study.md)
 * [laboratory_procedure](laboratory_procedure.md)
     * [Biospecimen➞laboratory_procedure](Biospecimen_laboratory_procedure.md) - Procedure by which Sample was derived from Parent Sample
 * [mother_id](mother_id.md)
     * [Participant➞mother_id](Participant_mother_id.md) - Participant ID for Participant's mother
 * [outcomes_vital_status](outcomes_vital_status.md)
     * [Participant➞outcomes_vital_status](Participant_outcomes_vital_status.md) - Whether participant is alive or dead [need valid values]
 * [parent_sample_id](parent_sample_id.md)
     * [Biospecimen➞parent_sample_id](Biospecimen_parent_sample_id.md) - Identifier from Parent Sample from which Sample was derived (if applicable)
 * [parent_sample_type](parent_sample_type.md)
     * [Biospecimen➞parent_sample_type](Biospecimen_parent_sample_type.md) - Type of Parent Sample
 * [participant_id](participant_id.md)
     * [DataFile➞participant_id](DataFile_participant_id.md) - List of Participant IDs for participants associated with this file
     * [Participant➞participant_id](Participant_participant_id.md) - Unique identifier for the participant, assigned by DCC
 * [phenotype__hpo](phenotype__hpo.md)
     * [Participant➞phenotype__hpo](Participant_phenotype__hpo.md) - Human Phenotype Ontology code (annotated by data contributor or DCC)
 * [phenotype__source_text](phenotype__source_text.md)
     * [Participant➞phenotype__source_text](Participant_phenotype__source_text.md) - Phenotype as described by data contributor
 * [phenotype_interpretation](phenotype_interpretation.md)
     * [Participant➞phenotype_interpretation](Participant_phenotype_interpretation.md) - Whether phenotype was observed or not
 * [program](program.md)
     * [Study➞program](Study_program.md) - Funding source for the study ??
 * [race](race.md)
     * [Participant➞race](Participant_race.md) - Race of participant
 * [sample_availability](sample_availability.md)
     * [Biospecimen➞sample_availability](Biospecimen_sample_availability.md) - Whether or not the container (or sample??) is available for sharing through the Virtual Biorepository
 * [sample_id](sample_id.md)
     * [Biospecimen➞sample_id](Biospecimen_sample_id.md) - Identifier for sample, assigned (by DCC or contributor??) at time of collection, processing, treatment, or derivation. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
 * [sample_type](sample_type.md)
     * [Biospecimen➞sample_type](Biospecimen_sample_type.md) - Type of biological material comprising the sample
 * [sex](sex.md)
     * [Participant➞sex](Participant_sex.md) - Sex of participant
 * [size](size.md)
     * [DataFile➞size](DataFile_size.md) - Size of file
 * [study_code](study_code.md)
     * [Study➞study_code](Study_study_code.md) - Unique identifer for the study, assigned by DCC
 * [study_name](study_name.md)
     * [Study➞study_name](Study_study_name.md) - Name of the study, chosen by data contributor
 * [volume](volume.md)
     * [Biospecimen➞volume](Biospecimen_volume.md) - Amount of sample in container
 * [volume_unit](volume_unit.md)
     * [Biospecimen➞volume_unit](Biospecimen_volume_unit.md) - Unit of sample volume

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
