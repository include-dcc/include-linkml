
# Class: Participant




URI: [include:Participant](https://w3id.org/include/Participant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[DataFile]<has_datafile%200..1-%20[Participant&#124;age_at_diagnosis__days:integer%20%3F;age_at_phenotype_assignment__days:integer%20%3F;age_at_the_last_vital_status__days:integer%20%3F;diagnosis__icd:string%20%3F;diagnosis__mondo:string%20%3F;diagnosis__ncit:string%20%3F;diagnosis__source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:string;ethnicity:string;external_id:string;family_id:string%20%3F;family_relationship:string%20%3F;family_type:string%20%3F;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype__hpo:string%20%3F;phenotype__source_text:string%20%3F;phenotype_interpretation:string%20%3F;race:string;sex:string;id(i):string],[Study]<has_study%200..1-%20[Participant],[Biospecimen]-%20has_participant%200..1>[Participant],[DataFile]-%20has_participant%200..1>[Participant],[NamedThing]^-[Participant],[NamedThing],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[DataFile]<has_datafile%200..1-%20[Participant&#124;age_at_diagnosis__days:integer%20%3F;age_at_phenotype_assignment__days:integer%20%3F;age_at_the_last_vital_status__days:integer%20%3F;diagnosis__icd:string%20%3F;diagnosis__mondo:string%20%3F;diagnosis__ncit:string%20%3F;diagnosis__source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:string;ethnicity:string;external_id:string;family_id:string%20%3F;family_relationship:string%20%3F;family_type:string%20%3F;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype__hpo:string%20%3F;phenotype__source_text:string%20%3F;phenotype_interpretation:string%20%3F;race:string;sex:string;id(i):string],[Study]<has_study%200..1-%20[Participant],[Biospecimen]-%20has_participant%200..1>[Participant],[DataFile]-%20has_participant%200..1>[Participant],[NamedThing]^-[Participant],[NamedThing],[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - root class

## Referenced by Class

 *  **None** *[has_participant](has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**

## Attributes


### Own

 * [has_study](has_study.md)  <sub>0..1</sub>
     * Range: [Study](Study.md)
 * [has_datafile](has_datafile.md)  <sub>0..1</sub>
     * Range: [DataFile](DataFile.md)
 * [➞age_at_diagnosis__days](participant__age_at_diagnosis__days.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was assigned (or onset??)
     * Range: [Integer](types/Integer.md)
 * [➞age_at_phenotype_assignment__days](participant__age_at_phenotype_assignment__days.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was recorded (or onset??)
     * Range: [Integer](types/Integer.md)
 * [➞age_at_the_last_vital_status__days](participant__age_at_the_last_vital_status__days.md)  <sub>0..1</sub>
     * Description: Age in days when participant's vital status was last recorded (or actual death date??)
     * Range: [Integer](types/Integer.md)
 * [➞diagnosis__icd](participant__diagnosis__icd.md)  <sub>0..1</sub>
     * Description: ICD-10 code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [➞diagnosis__mondo](participant__diagnosis__mondo.md)  <sub>0..1</sub>
     * Description: Mondo disease ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [➞diagnosis__ncit](participant__diagnosis__ncit.md)  <sub>0..1</sub>
     * Description: NCI Thesaurus code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [➞diagnosis__source_text](participant__diagnosis__source_text.md)  <sub>0..1</sub>
     * Description: Diagnosis as described by data contributor
     * Range: [String](types/String.md)
 * [➞diagnosis_type](participant__diagnosis_type.md)  <sub>0..1</sub>
     * Description: How diagnosis was assigned ??
     * Range: [String](types/String.md)
 * [➞down_syndrome_status](participant__down_syndrome_status.md)  <sub>1..1</sub>
     * Description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
     * Range: [String](types/String.md)
 * [➞ethnicity](participant__ethnicity.md)  <sub>1..1</sub>
     * Description: Ethnicity of participant
     * Range: [String](types/String.md)
 * [➞external_id](participant__external_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by data contributor
     * Range: [String](types/String.md)
 * [➞family_id](participant__family_id.md)  <sub>0..1</sub>
     * Description: Unique identifer for family to which Participant belongs
     * Range: [String](types/String.md)
 * [➞family_relationship](participant__family_relationship.md)  <sub>0..1</sub>
     * Description: Relationship of Participant to other family members
     * Range: [String](types/String.md)
 * [➞family_type](participant__family_type.md)  <sub>0..1</sub>
     * Description: Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives) 
     * Range: [String](types/String.md)
 * [➞father_id](participant__father_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's father
     * Range: [String](types/String.md)
 * [➞mother_id](participant__mother_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's mother
     * Range: [String](types/String.md)
 * [➞outcomes_vital_status](participant__outcomes_vital_status.md)  <sub>0..1</sub>
     * Description: Whether participant is alive or dead [need valid values]
     * Range: [String](types/String.md)
 * [➞participant_id](participant__participant_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by DCC
     * Range: [String](types/String.md)
 * [➞phenotype__hpo](participant__phenotype__hpo.md)  <sub>0..1</sub>
     * Description: Human Phenotype Ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [➞phenotype__source_text](participant__phenotype__source_text.md)  <sub>0..1</sub>
     * Description: Phenotype as described by data contributor
     * Range: [String](types/String.md)
 * [➞phenotype_interpretation](participant__phenotype_interpretation.md)  <sub>0..1</sub>
     * Description: Whether phenotype was observed or not
     * Range: [String](types/String.md)
 * [➞race](participant__race.md)  <sub>1..1</sub>
     * Description: Race of participant
     * Range: [String](types/String.md)
 * [➞sex](participant__sex.md)  <sub>1..1</sub>
     * Description: Sex of participant
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
