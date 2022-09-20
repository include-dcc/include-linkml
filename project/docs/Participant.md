
# Class: Participant


A Participant in a Study

URI: [include:Participant](https://w3id.org/include/Participant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_diagnosis:string%20%3F;age_at_phenotype_assignment:string%20%3F;age_at_the_last_vital_status:string%20%3F;diagnosis_icd:string%20%3F;diagnosis_mondo:string%20%3F;diagnosis_ncit:string%20%3F;diagnosis_source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_type:enum_family_type;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype_hpo:string%20%3F;phenotype_source_text:string%20%3F;phenotype_interpretation:enum_phenotype_interpretation%20%3F;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-++[Participant],[Participant]<family_relationship%200..1-++[Participant],[Biospecimen]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_participant%200..1>[Participant],[FamilyGroup]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_subject(i)%201..1>[Participant],[Thing]^-[Participant],[FamilyGroup],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_diagnosis:string%20%3F;age_at_phenotype_assignment:string%20%3F;age_at_the_last_vital_status:string%20%3F;diagnosis_icd:string%20%3F;diagnosis_mondo:string%20%3F;diagnosis_ncit:string%20%3F;diagnosis_source_text:string%20%3F;diagnosis_type:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_type:enum_family_type;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;phenotype_hpo:string%20%3F;phenotype_source_text:string%20%3F;phenotype_interpretation:enum_phenotype_interpretation%20%3F;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-++[Participant],[Participant]<family_relationship%200..1-++[Participant],[Biospecimen]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_participant%200..1>[Participant],[FamilyGroup]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_subject(i)%201..1>[Participant],[Thing]^-[Participant],[FamilyGroup],[DataFile],[Biospecimen])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[family_relationship](family_relationship.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **None** *[has_participant](has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **None** *[has_subject](has_subject.md)*  <sub>1..1</sub>  **[Participant](Participant.md)**

## Attributes


### Own

 * [age_at_diagnosis](age_at_diagnosis.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was assigned
     * Range: [String](types/String.md)
 * [age_at_phenotype_assignment](age_at_phenotype_assignment.md)  <sub>0..1</sub>
     * Description: Age in days at which phenotype was recorded
     * Range: [String](types/String.md)
 * [age_at_the_last_vital_status](age_at_the_last_vital_status.md)  <sub>0..1</sub>
     * Description: Age of last vital status
     * Range: [String](types/String.md)
 * [diagnosis_icd](diagnosis_icd.md)  <sub>0..1</sub>
     * Description: ICD-10 code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [diagnosis_mondo](diagnosis_mondo.md)  <sub>0..1</sub>
     * Description: Mondo disease ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [diagnosis_ncit](diagnosis_ncit.md)  <sub>0..1</sub>
     * Description: NCI Thesaurus code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [diagnosis_source_text](diagnosis_source_text.md)  <sub>0..1</sub>
     * Description: Diagnosis as described by data contributor
     * Range: [String](types/String.md)
 * [diagnosis_type](diagnosis_type.md)  <sub>0..1</sub>
     * Description: How diagnosis was assigned
     * Range: [String](types/String.md)
 * [down_syndrome_status](down_syndrome_status.md)  <sub>1..1</sub>
     * Description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)
     * Range: [enum_down_syndrome_status](enum_down_syndrome_status.md)
 * [ethnicity](ethnicity.md)  <sub>1..1</sub>
     * Description: Ethnicity of participant
     * Range: [enum_ethnicity](enum_ethnicity.md)
 * [external_id](external_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by data contributor
     * Range: [String](types/String.md)
 * [family_id](family_id.md)  <sub>0..1</sub>
     * Description: Unique identifer for family to which Participant belongs
     * Range: [String](types/String.md)
 * [family_relationship](family_relationship.md)  <sub>0..1</sub>
     * Description: Relationship of Participant to other family members
     * Range: [Participant](Participant.md)
 * [family_type](family_type.md)  <sub>1..1</sub>
     * Description: Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)
     * Range: [enum_family_type](enum_family_type.md)
 * [father_id](father_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's father
     * Range: [String](types/String.md)
 * [has_datafile](has_datafile.md)  <sub>0..1</sub>
     * Description: Link to a DataFile
     * Range: [DataFile](DataFile.md)
 * [has_study](has_study.md)  <sub>0..1</sub>
     * Description: Link to a Study
     * Range: [Study](Study.md)
 * [mother_id](mother_id.md)  <sub>0..1</sub>
     * Description: Participant ID for Participant's mother
     * Range: [String](types/String.md)
 * [outcomes_vital_status](outcomes_vital_status.md)  <sub>0..1</sub>
     * Description: Whether participant is alive or dead
     * Range: [String](types/String.md)
 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by DCC
     * Range: [String](types/String.md)
 * [phenotype_hpo](phenotype_hpo.md)  <sub>0..1</sub>
     * Description: Human Phenotype Ontology code (annotated by data contributor or DCC)
     * Range: [String](types/String.md)
 * [phenotype_source_text](phenotype_source_text.md)  <sub>0..1</sub>
     * Description: Phenotype as described by data contributor
     * Range: [String](types/String.md)
 * [phenotype_interpretation](phenotype_interpretation.md)  <sub>0..1</sub>
     * Description: Whether phenotype was observed or not
     * Range: [enum_phenotype_interpretation](enum_phenotype_interpretation.md)
 * [race](race.md)  <sub>1..1</sub>
     * Description: Race of participant
     * Range: [enum_race](enum_race.md)
 * [sex](sex.md)  <sub>1..1</sub>
     * Description: Sex of participant
     * Range: [enum_sex](enum_sex.md)
