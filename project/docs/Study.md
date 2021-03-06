
# Class: Study


A Study

URI: [include:Study](https://w3id.org/include/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program%20%3F;study_code:enum_study_code%20%3F;study_name:string%20%3F],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[NamedThing]^-[Study],[Participant],[NamedThing],[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has_study%200..1>[Study&#124;dbgap:string%20%3F;program:enum_program%20%3F;study_code:enum_study_code%20%3F;study_name:string%20%3F],[DataFile]++-%20has_study%200..1>[Study],[Participant]++-%20has_study%200..1>[Study],[NamedThing]^-[Study],[Participant],[NamedThing],[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **None** *[has_study](has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [dbgap](dbgap.md)  <sub>0..1</sub>
     * Description: dbGaP study accession code
     * Range: [String](types/String.md)
 * [program](program.md)  <sub>0..1</sub>
     * Description: Funding source for the study
     * Range: [enum_program](enum_program.md)
 * [study_code](study_code.md)  <sub>0..1</sub>
     * Description: Unique identifer for the study, assigned by DCC
     * Range: [enum_study_code](enum_study_code.md)
 * [study_name](study_name.md)  <sub>0..1</sub>
     * Description: Name of the study, chosen by data contributor
     * Range: [String](types/String.md)
