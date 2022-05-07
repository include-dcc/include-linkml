
# Class: DataFile




URI: [include:DataFile](https://w3id.org/include/DataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[Biospecimen]<has_biospecimen%200..1-%20[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:string%20%3F;data_category:string%20%3F;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string%20%3F;file_name:string%20%3F;format:string%20%3F;participant_id:string%20%3F;size:string%20%3F;id(i):string],[Participant]<has_participant%200..1-%20[DataFile],[Study]<has_study%200..1-%20[DataFile],[Biospecimen]-%20has_datafile%200..1>[DataFile],[Participant]-%20has_datafile%200..1>[DataFile],[NamedThing]^-[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[Biospecimen]<has_biospecimen%200..1-%20[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:string%20%3F;data_category:string%20%3F;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string%20%3F;file_name:string%20%3F;format:string%20%3F;participant_id:string%20%3F;size:string%20%3F;id(i):string],[Participant]<has_participant%200..1-%20[DataFile],[Study]<has_study%200..1-%20[DataFile],[Biospecimen]-%20has_datafile%200..1>[DataFile],[Participant]-%20has_datafile%200..1>[DataFile],[NamedThing]^-[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - root class

## Referenced by Class

 *  **None** *[has_datafile](has_datafile.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**

## Attributes


### Own

 * [has_study](has_study.md)  <sub>0..1</sub>
     * Range: [Study](Study.md)
 * [has_participant](has_participant.md)  <sub>0..1</sub>
     * Range: [Participant](Participant.md)
 * [has_biospecimen](has_biospecimen.md)  <sub>0..1</sub>
     * Range: [Biospecimen](Biospecimen.md)
 * [➞access_url](dataFile__access_url.md)  <sub>0..1</sub>
     * Description: Storage location for this file ??
     * Range: [String](types/String.md)
 * [➞collection_id](dataFile__collection_id.md)  <sub>0..1</sub>
     * Description: List of Collection?? IDs for biospecimens associated with this file
     * Range: [String](types/String.md)
 * [➞data_access](dataFile__data_access.md)  <sub>0..1</sub>
     * Description: Type of access control on this file
     * Range: [String](types/String.md)
 * [➞data_category](dataFile__data_category.md)  <sub>0..1</sub>
     * Description: General category of data in file, e.g. Clinical; Genomic; Proteomic; Metabolomic
     * Range: [String](types/String.md)
 * [➞data_type](dataFile__data_type.md)  <sub>0..1</sub>
     * Description: Specific type of data contained in file, e.g. Simple nucleotide variations; aligned reads; gVCF
     * Range: [String](types/String.md)
 * [➞experimental_strategy](dataFile__experimental_strategy.md)  <sub>0..1</sub>
     * Description: Specific experimental method used to obtain data in file, e.g. Whole-genome sequencing; LCMS metabolomics
     * Range: [String](types/String.md)
 * [➞file_id](dataFile__file_id.md)  <sub>0..1</sub>
     * Description: File identifier, assigned by DCC??
     * Range: [String](types/String.md)
 * [➞file_name](dataFile__file_name.md)  <sub>0..1</sub>
     * Description: Name of file, assigned by data contributor??
     * Range: [String](types/String.md)
 * [➞format](dataFile__format.md)  <sub>0..1</sub>
     * Description: Format of file
     * Range: [String](types/String.md)
 * [➞participant_id](dataFile__participant_id.md)  <sub>0..1</sub>
     * Description: List of Participant IDs for participants associated with this file
     * Range: [String](types/String.md)
 * [➞size](dataFile__size.md)  <sub>0..1</sub>
     * Description: Size of file
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
