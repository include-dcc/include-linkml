
# IncludePortalV1


**metamodel version:** 1.7.0

**version:** None


Initial Include Portal Schema


### Classes

 * [Condition](Condition.md)
 * [Thing](Thing.md) - Highest Level Class
     * [Aliquot](Aliquot.md) - An aliquot of a sample
     * [Assay](Assay.md) - An assay
     * [Biospecimen](Biospecimen.md) - A Biospecimen Collected from A Participant
     * [DataFile](DataFile.md) - A DataFile Associated with a Participant or Study or Biospecimen
     * [FamilyGroup](FamilyGroup.md) - A group of Participants in the same Study
     * [Participant](Participant.md) - A Participant in a Study
     * [Study](Study.md) - A Study

### Mixins


### Slots

 * [access_url](access_url.md) - Storage location for this file
 * [age_at_biospecimen_collection](age_at_biospecimen_collection.md) - Age in days of participant at time of biospecimen collection
 * [age_at_condition_observation](age_at_condition_observation.md) - Age in days at which condition was observed, recorded, or diagnosed
 * [age_at_last_vital_status](age_at_last_vital_status.md) - Age in days when participant's vital status was last recorded
 * [biospecimen_storage](biospecimen_storage.md) - Method by which Container is stored (e.g. -80C freezer, Liquid nitrogen, etc.)
 * [collection_id](collection_id.md) - Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed).
 * [collection_sample_type](collection_sample_type.md) - Type of biological material comprising the collected sample (e.g. Whole blood, Bone marrow, Saliva, etc.)
 * [condition_data_source](condition_data_source.md) - Whether condition information was obtained from medical records (Clinical) or patient survey (Self-Reported)
 * [condition_description](condition_description.md) - Condition as worded by data contributor - this will be displayed in the portal
 * [condition_interpretation](condition_interpretation.md) - Whether condition was observed or not. "Not Observed" indicates participant was specifically examined for that condition, or health record specifically queried for that condition, and found to be negative. Sept. 2022 release will only include positive assertions.
 * [container_id](container_id.md) - Identifier for specific container/aliquot of sample, if applicable. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
 * [data_access](data_access.md) - Type of access control on this file, determined by DCC
 * [data_category](data_category.md) - General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune maps, Transcriptomics, etc.)
 * [data_type](data_type.md) - Specific type of data contained in file (e.g. Aligned reads, Unaligned reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification, Structural variations, Cytokine profiles, Operation reports, Pathology reports, Histology images, Clinical supplement, Protein expression quantification, etc.)
 * [dbgap](dbgap.md) - dbGaP study accession code
 * [down_syndrome_status](down_syndrome_status.md) - Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
 * [ethnicity](ethnicity.md) - Ethnicity of participant
 * [experimental_strategy](experimental_strategy.md) - Experimental method used to obtain data in file (e.g. WGS, RNAseq, WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay, Meso Scale Discovery, etc.)
 * [external_id](external_id.md) - Unique identifier for the participant, assigned by data contributor
 * [family_id](family_id.md) - Unique identifer for family to which Participant belongs
 * [family_relationship](family_relationship.md) - Relationship of Participant to other family members
 * [family_type](family_type.md) - Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)
 * [father_id](father_id.md) - Participant ID for Participant's father
 * [file_id](file_id.md) - File identifier, assigned by DCC
 * [file_name](file_name.md) - Synapse ID for file
 * [format](format.md) - Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf, dicom, etc.)
 * [has_aliquot](has_aliquot.md) - An aliquot of a sample
 * [has_biospecimen](has_biospecimen.md) - Link to a Biospecimen
 * [has_datafile](has_datafile.md) - Link to a DataFile
 * [has_output](has_output.md) - The DataFile Output of an Assay
 * [has_parent_sample](has_parent_sample.md) - Link from a sample to its parent Sample
 * [has_participant](has_participant.md) - Link to a Participant
 * [has_study](has_study.md) - Link to a Study
 * [has_subject](has_subject.md) - Link from Data File to a Participant
 * [hpo_code](hpo_code.md) - Code for condition in the Human Phenotype Ontology (HPO)
 * [hpo_label](hpo_label.md) - Label for condition in the Human Phenotype Ontology (HPO)
 * [laboratory_procedure](laboratory_procedure.md) - Procedure by which Sample was derived from Parent Sample (e.g. RBC lysis, Centrifugation, Ficoll, etc.)
 * [maxo_code](maxo_code.md) - Code for condition in the Medical Action Ontology (MAXO)
 * [maxo_label](maxo_label.md) - Label for condition in the Medical Action Ontology (MAXO)
 * [mondo_code](mondo_code.md) - Code for condition in the Mondo Disease Ontology (MONDO)
 * [mondo_label](mondo_label.md) - Label for condition in the Mondo Disease Ontology (MONDO)
 * [mother_id](mother_id.md) - Participant ID for Participant's mother
 * [original_file_name](original_file_name.md) - Name of file, assigned by data contributor
 * [other_code](other_code.md) - Code for condition in another ontology (if no match in HPO, MONDO, or MAXO)
 * [other_label](other_label.md) - Label for condition in another ontology (if no match in HPO, MONDO, or MAXO)
 * [outcomes_vital_status](outcomes_vital_status.md) - Whether participant is alive or dead
 * [parent_sample_id](parent_sample_id.md) - Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable)
 * [parent_sample_type](parent_sample_type.md) - Type of biological material comprising the parent sample (e.g. Plasma, Serum, White blood cells, etc.)
 * [participant_id](participant_id.md) - Unique identifier for the participant, assigned by DCC
 * [program](program.md) - Funding source for the study
 * [race](race.md) - Race of participant
 * [sample_availability](sample_availability.md) - Whether or not the sample is potentially available for sharing through the Virtual Biorepository
 * [sample_id](sample_id.md) - Identifier for sample. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
 * [sample_type](sample_type.md) - Type of biological material comprising the sample (e.g. Plasma, Serum, White blood cells, DNA, RNA, etc.)
 * [sex](sex.md) - Sex of participant
 * [size](size.md) - Size of file
 * [study_code](study_code.md) - Unique identifer for the study, assigned by DCC
 * [study_name](study_name.md) - Name of the study, chosen by data contributor
 * [uses_biospecimen](uses_biospecimen.md) - The Biospecimen an Assay is performed on
 * [validation_rules](validation_rules.md) - Rules for Validation of Property Constraints and Values
 * [volume](volume.md) - Amount of sample in container
 * [volume_unit](volume_unit.md) - Unit of sample volume

### Enums

 * [enum_condition_data_source](enum_condition_data_source.md)
 * [enum_condition_interpretation](enum_condition_interpretation.md)
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
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
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
