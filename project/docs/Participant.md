
# Class: Participant




URI: [include:Participant](https://w3id.org/include/Participant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_diagnosis__days:integer%20%3F;age_at_phenotype_assignment__days:integer%20%3F;age_at_the_last_vital_status__days:integer%20%3F;diagnosis__icd:string%20%3F;diagnosis__mondo:string%20%3F;diagnosis__ncit:string%20%3F;diagnosis__source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_relationship:string%20%3F;family_type:enum_family_type%20%3F;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype__hpo:string%20%3F;phenotype__source_text:string%20%3F;phenotype_interpretation:enum_phenotype_interpretation%20%3F;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-%20[Participant],[Biospecimen]-%20has_participant%200..1>[Participant],[DataFile]-%20has_participant%200..1>[Participant],[Biospecimen]-%20has_participant(i)%200..1>[Participant],[DataFile]-%20has_participant(i)%200..1>[Participant],[NamedThing]^-[Participant],[NamedThing],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_diagnosis__days:integer%20%3F;age_at_phenotype_assignment__days:integer%20%3F;age_at_the_last_vital_status__days:integer%20%3F;diagnosis__icd:string%20%3F;diagnosis__mondo:string%20%3F;diagnosis__ncit:string%20%3F;diagnosis__source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_relationship:string%20%3F;family_type:enum_family_type%20%3F;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype__hpo:string%20%3F;phenotype__source_text:string%20%3F;phenotype_interpretation:enum_phenotype_interpretation%20%3F;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-%20[Participant],[Biospecimen]-%20has_participant%200..1>[Participant],[DataFile]-%20has_participant%200..1>[Participant],[Biospecimen]-%20has_participant(i)%200..1>[Participant],[DataFile]-%20has_participant(i)%200..1>[Participant],[NamedThing]^-[Participant],[NamedThing],[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞has_participant](Biospecimen_has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **[DataFile](DataFile.md)** *[DataFile➞has_participant](DataFile_has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **None** *[has_participant](has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**

## Attributes


### Own

 * [Participant➞age_at_diagnosis__days](Participant_age_at_diagnosis__days.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was assigned (or onset??)
     * Range: [Integer](types/Integer.md)
 * [Participant➞age_at_phenotype_assignment__days](Participant_age_at_phenotype_assignment__days.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was recorded (or onset??)
     * Range: [Integer](types/Integer.md)
 * [Participant➞age_at_the_last_vital_status__days](Participant_age_at_the_last_vital_status__days.md)  <sub>0..1</sub>
     * Description: Age in days when participant's vital status was last recorded (or actual death date??)
     * Range: [Integer](types/Integer.md)
 * [Participant➞diagnosis__icd](Participant_diagnosis__icd.md)  <sub>0..1</sub>
     * Description: ICD-10 code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [Participant➞diagnosis__mondo](Participant_diagnosis__mondo.md)  <sub>0..1</sub>
     * Description: Mondo disease ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [Participant➞diagnosis__ncit](Participant_diagnosis__ncit.md)  <sub>0..1</sub>
     * Description: NCI Thesaurus code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [Participant➞diagnosis__source_text](Participant_diagnosis__source_text.md)  <sub>0..1</sub>
     * Description: Diagnosis as described by data contributor
     * Range: [String](types/String.md)
 * [Participant➞diagnosis_type](Participant_diagnosis_type.md)  <sub>0..1</sub>
     * Description: How diagnosis was assigned ??
     * Range: [String](types/String.md)
 * [Participant➞down_syndrome_status](Participant_down_syndrome_status.md)  <sub>1..1</sub>
     * Description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
     * Range: [enum_down_syndrome_status](enum_down_syndrome_status.md)
 * [Participant➞ethnicity](Participant_ethnicity.md)  <sub>1..1</sub>
     * Description: Ethnicity of participant
     * Range: [enum_ethnicity](enum_ethnicity.md)
 * [Participant➞external_id](Participant_external_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by data contributor
     * Range: [String](types/String.md)
 * [Participant➞family_id](Participant_family_id.md)  <sub>0..1</sub>
     * Description: Unique identifer for family to which Participant belongs
     * Range: [String](types/String.md)
 * [Participant➞family_relationship](Participant_family_relationship.md)  <sub>0..1</sub>
     * Description: Relationship of Participant to other family members
     * Range: [String](types/String.md)
 * [Participant➞family_type](Participant_family_type.md)  <sub>0..1</sub>
     * Description: Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)
     * Range: [enum_family_type](enum_family_type.md)
 * [Participant➞father_id](Participant_father_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's father
     * Range: [String](types/String.md)
 * [Participant➞has_datafile](Participant_has_datafile.md)  <sub>0..1</sub>
     * Description: Semantic link to a DataFile
     * Range: [DataFile](DataFile.md)
 * [Participant➞has_study](Participant_has_study.md)  <sub>0..1</sub>
     * Description: Semantic link to a Study
     * Range: [Study](Study.md)
 * [Participant➞mother_id](Participant_mother_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's mother
     * Range: [String](types/String.md)
 * [Participant➞outcomes_vital_status](Participant_outcomes_vital_status.md)  <sub>0..1</sub>
     * Description: Whether participant is alive or dead [need valid values]
     * Range: [String](types/String.md)
 * [Participant➞participant_id](Participant_participant_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by DCC
     * Range: [String](types/String.md)
 * [Participant➞phenotype__hpo](Participant_phenotype__hpo.md)  <sub>0..1</sub>
     * Description: Human Phenotype Ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [Participant➞phenotype__source_text](Participant_phenotype__source_text.md)  <sub>0..1</sub>
     * Description: Phenotype as described by data contributor
     * Range: [String](types/String.md)
 * [Participant➞phenotype_interpretation](Participant_phenotype_interpretation.md)  <sub>0..1</sub>
     * Description: Whether phenotype was observed or not
     * Range: [enum_phenotype_interpretation](enum_phenotype_interpretation.md)
 * [Participant➞race](Participant_race.md)  <sub>1..1</sub>
     * Description: Race of participant
     * Range: [enum_race](enum_race.md)
 * [Participant➞sex](Participant_sex.md)  <sub>1..1</sub>
     * Description: Sex of participant
     * Range: [enum_sex](enum_sex.md)
