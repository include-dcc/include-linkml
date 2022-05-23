
# Class: Study




URI: [include:Study](https://w3id.org/include/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program;study_code:enum_study_code;study_name:string],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[Biospecimen]++-%20has_study(i)%200..1>[Study],[DataFile]++-%20has_study(i)%200..1>[Study],[Participant]++-%20has_study(i)%200..1>[Study],[NamedThing]^-[Study],[Participant],[NamedThing],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program;study_code:enum_study_code;study_name:string],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[Biospecimen]++-%20has_study(i)%200..1>[Study],[DataFile]++-%20has_study(i)%200..1>[Study],[Participant]++-%20has_study(i)%200..1>[Study],[NamedThing]^-[Study],[Participant],[NamedThing],[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞has_study](Biospecimen_has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**
 *  **[DataFile](DataFile.md)** *[DataFile➞has_study](DataFile_has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**
 *  **[Participant](Participant.md)** *[Participant➞has_study](Participant_has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**
 *  **None** *[has_study](has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [Study➞dbgap](Study_dbgap.md)  <sub>0..1</sub>
     * Description: dbGaP study accession code
     * Range: [String](types/String.md)
 * [Study➞program](Study_program.md)  <sub>1..1</sub>
     * Description: Funding source for the study ??
     * Range: [enum_program](enum_program.md)
 * [Study➞study_code](Study_study_code.md)  <sub>1..1</sub>
     * Description: Unique identifer for the study, assigned by DCC
     * Range: [enum_study_code](enum_study_code.md)
 * [Study➞study_name](Study_study_name.md)  <sub>1..1</sub>
     * Description: Name of the study, chosen by data contributor
     * Range: [String](types/String.md)
