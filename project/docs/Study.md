
# Class: Study


A Study

URI: [include:Study](https://w3id.org/include/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program;study_code:enum_study_code;study_name:string],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[Thing]^-[Study],[Participant],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program;study_code:enum_study_code;study_name:string],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[Thing]^-[Study],[Participant],[DataFile],[Biospecimen])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[has_study](has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [dbgap](dbgap.md)  <sub>0..1</sub>
     * Description: dbGaP study accession code
     * Range: [String](types/String.md)
 * [program](program.md)  <sub>1..1</sub>
     * Description: Funding source for the study
     * Range: [enum_program](enum_program.md)
 * [study_code](study_code.md)  <sub>1..1</sub>
     * Description: Unique identifer for the study, assigned by DCC
     * Range: [enum_study_code](enum_study_code.md)
 * [study_name](study_name.md)  <sub>1..1</sub>
     * Description: Name of the study, chosen by data contributor
     * Range: [String](types/String.md)
