
# Class: Participant


A Participant in a Study

URI: [include:Participant](https://w3id.org/include/Participant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_last_vital_status:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_type:enum_family_type;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-++[Participant],[Participant]<family_relationship%200..1-++[Participant],[Biospecimen]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_participant%200..1>[Participant],[Condition]++-%20has_participant%200..1>[Participant],[FamilyGroup]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_subject(i)%201..1>[Participant],[Thing]^-[Participant],[FamilyGroup],[DataFile],[Condition],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Study]<has_study%200..1-++[Participant&#124;age_at_last_vital_status:string%20%3F;down_syndrome_status:enum_down_syndrome_status;ethnicity:enum_ethnicity;external_id:string;family_id:string%20%3F;family_type:enum_family_type;father_id:string%20%3F;mother_id:string%20%3F;outcomes_vital_status:string%20%3F;participant_id:string;race:enum_race;sex:enum_sex],[DataFile]<has_datafile%200..1-++[Participant],[Participant]<family_relationship%200..1-++[Participant],[Biospecimen]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_participant%200..1>[Participant],[Condition]++-%20has_participant%200..1>[Participant],[FamilyGroup]++-%20has_participant%200..1>[Participant],[DataFile]++-%20has_subject(i)%201..1>[Participant],[Thing]^-[Participant],[FamilyGroup],[DataFile],[Condition],[Biospecimen])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[family_relationship](family_relationship.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **None** *[has_participant](has_participant.md)*  <sub>0..1</sub>  **[Participant](Participant.md)**
 *  **None** *[has_subject](has_subject.md)*  <sub>1..1</sub>  **[Participant](Participant.md)**

## Attributes


### Own

 * [age_at_last_vital_status](age_at_last_vital_status.md)  <sub>0..1</sub>
     * Description: Age in days when participant's vital status was last recorded
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
 * [race](race.md)  <sub>1..1</sub>
     * Description: Race of participant
     * Range: [enum_race](enum_race.md)
 * [sex](sex.md)  <sub>1..1</sub>
     * Description: Sex of participant
     * Range: [enum_sex](enum_sex.md)
