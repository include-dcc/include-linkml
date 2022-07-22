# IncludePortalV1

Initial Include Portal Schema

URI: https://w3id.org/include_portal_v1_schema

## Classes

| Class | Description |
| --- | --- |
| [Biospecimen](Biospecimen.md) | A Biospecimen Collected from A Participant | 
| [DataFile](DataFile.md) | A DataFile Associated with a Participant or Study or Biospecimen | 
| [Participant](Participant.md) | A Participant in a Study | 
| [Study](Study.md) | A Study | 
| [NamedThing](NamedThing.md) | None | 


## Slots

| Slot | Description |
| --- | --- |
| [access_url](access_url.md) | Storage location for this file | 
| [age_at_biospecimen_collection](age_at_biospecimen_collection.md) | Age in days of participant at time of biospecimen collection | 
| [age_at_diagnosis](age_at_diagnosis.md) | Age in days at which phenotype was assigned | 
| [age_at_phenotype_assignment](age_at_phenotype_assignment.md) | Age in days at which phenotype was recorded | 
| [age_at_the_last_vital_status](age_at_the_last_vital_status.md) | None | 
| [biospecimen_storage](biospecimen_storage.md) | Method by which Container is stored (e.g. -80C freezer, Liquid nitrogen, etc.) | 
| [collection_id](collection_id.md) | Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed). | 
| [collection_sample_type](collection_sample_type.md) | Type of biological material comprising the collected sample (e.g. Whole blood, Bone marrow, Saliva, etc.) | 
| [container_id](container_id.md) | Identifier for specific container/aliquot of sample, if applicable. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs. | 
| [data_access](data_access.md) | Type of access control on this file, determined by DCC | 
| [data_category](data_category.md) | General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune maps, Transcriptomics, etc.) | 
| [data_type](data_type.md) | Specific type of data contained in file (e.g. Aligned reads, Unaligned reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification, Structural variations, Cytokine profiles, Operation reports, Pathology reports, Histology images, Clinical supplement, Protein expression quantification, etc.) | 
| [dbgap](dbgap.md) | dbGaP study accession code | 
| [diagnosis_icd](diagnosis_icd.md) | ICD-10 code (annotated by data contributor or DCC) | 
| [diagnosis_mondo](diagnosis_mondo.md) | Mondo disease ontology code (annotated by data contributor or DCC) | 
| [diagnosis_ncit](diagnosis_ncit.md) | NCI Thesaurus code (annotated by data contributor or DCC) | 
| [diagnosis_source_text](diagnosis_source_text.md) | Diagnosis as described by data contributor | 
| [diagnosis_type](diagnosis_type.md) | How diagnosis was assigned | 
| [down_syndrome_status](down_syndrome_status.md) | Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid) | 
| [ethnicity](ethnicity.md) | Ethnicity of participant | 
| [experimental_strategy](experimental_strategy.md) | Experimental method used to obtain data in file (e.g. WGS, RNAseq, WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay, Meso Scale Discovery, etc.) | 
| [external_id](external_id.md) | Unique identifier for the participant, assigned by data contributor | 
| [family_id](family_id.md) | Unique identifer for family to which Participant belongs | 
| [family_relationship](family_relationship.md) | Relationship of Participant to other family members | 
| [family_type](family_type.md) | Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)  | 
| [father_id](father_id.md) | Participant ID for Participant's father | 
| [file_id](file_id.md) | File identifier, assigned by DCC | 
| [file_name](file_name.md) | Synapse ID for file | 
| [format](format.md) | Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf, dicom, etc.) | 
| [has_biospecimen](has_biospecimen.md) | Link to a Biospecimen | 
| [has_datafile](has_datafile.md) | Link to a DataFile | 
| [has_participant](has_participant.md) | Link to a Participant | 
| [has_study](has_study.md) | Link to a Study | 
| [laboratory_procedure](laboratory_procedure.md) | Procedure by which Sample was derived from Parent Sample (e.g. RBC lysis, Centrifugation, Ficoll, etc.) | 
| [mother_id](mother_id.md) | Participant ID for Participant's mother | 
| [outcomes_vital_status](outcomes_vital_status.md) | Whether participant is alive or dead | 
| [parent_sample_id](parent_sample_id.md) | Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable) | 
| [parent_sample_type](parent_sample_type.md) | Type of biological material comprising the parent sample (e.g. Plasma, Serum, White blood cells, etc.) | 
| [participant_id](participant_id.md) | Unique identifier for the participant, assigned by DCC | 
| [phenotype_hpo](phenotype_hpo.md) | Human Phenotype Ontology code (annotated by data contributor or DCC) | 
| [phenotype_interpretation](phenotype_interpretation.md) | Whether phenotype was observed or not | 
| [phenotype_source_text](phenotype_source_text.md) | Phenotype as described by data contributor | 
| [program](program.md) | Funding source for the study | 
| [race](race.md) | Race of participant | 
| [sample_availability](sample_availability.md) | Whether or not the sample is potentially available for sharing through the Virtual Biorepository | 
| [sample_id](sample_id.md) | Identifier for sample. A sample is a unique biological material; two samples with two different IDs are biologically distinct. | 
| [sample_type](sample_type.md) | Type of biological material comprising the sample (e.g. Plasma, Serum, White blood cells, DNA, RNA, etc.) | 
| [sex](sex.md) | Sex of participant | 
| [size](size.md) | Size of file | 
| [study_code](study_code.md) | Unique identifer for the study, assigned by DCC | 
| [study_name](study_name.md) | Name of the study, chosen by data contributor | 
| [volume](volume.md) | Amount of sample in container | 
| [volume_unit](volume_unit.md) | Unit of sample volume | 


## Enums

| Enums | Description |
| --- | --- |
| [EnumDataAccess](EnumDataAccess.md) | None | 
| [EnumDownSyndromeStatus](EnumDownSyndromeStatus.md) | None | 
| [EnumEthnicity](EnumEthnicity.md) | None | 
| [EnumFamilyType](EnumFamilyType.md) | None | 
| [EnumPhenotypeInterpretation](EnumPhenotypeInterpretation.md) | None | 
| [EnumProgram](EnumProgram.md) | None | 
| [EnumRace](EnumRace.md) | None | 
| [EnumSampleAvailability](EnumSampleAvailability.md) | None | 
| [EnumSex](EnumSex.md) | None | 
| [EnumStudyCode](EnumStudyCode.md) | None | 

