
# Class: DataFile




URI: [include:DataFile](https://w3id.org/include/DataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[Study]<has_study%200..1-++[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:enum_data_access%20%3F;data_category:string%20%3F;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string;file_name:string%20%3F;format:string%20%3F;participant_id:string%20%3F;size:string%20%3F],[Participant]<has_participant%200..1-%20[DataFile],[Biospecimen]<has_biospecimen%200..1-%20[DataFile],[Biospecimen]-%20has_datafile%200..1>[DataFile],[Participant]-%20has_datafile%200..1>[DataFile],[Biospecimen]-%20has_datafile(i)%200..1>[DataFile],[Participant]-%20has_datafile(i)%200..1>[DataFile],[NamedThing]^-[DataFile],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[Study]<has_study%200..1-++[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:enum_data_access%20%3F;data_category:string%20%3F;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string;file_name:string%20%3F;format:string%20%3F;participant_id:string%20%3F;size:string%20%3F],[Participant]<has_participant%200..1-%20[DataFile],[Biospecimen]<has_biospecimen%200..1-%20[DataFile],[Biospecimen]-%20has_datafile%200..1>[DataFile],[Participant]-%20has_datafile%200..1>[DataFile],[Biospecimen]-%20has_datafile(i)%200..1>[DataFile],[Participant]-%20has_datafile(i)%200..1>[DataFile],[NamedThing]^-[DataFile],[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞has_datafile](Biospecimen_has_datafile.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**
 *  **[Participant](Participant.md)** *[Participant➞has_datafile](Participant_has_datafile.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**
 *  **None** *[has_datafile](has_datafile.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**

## Attributes


### Own

 * [DataFile➞access_url](DataFile_access_url.md)  <sub>0..1</sub>
     * Description: Storage location for this file ??
     * Range: [String](types/String.md)
 * [DataFile➞collection_id](DataFile_collection_id.md)  <sub>0..1</sub>
     * Description: List of Collection?? IDs for biospecimens associated with this file
     * Range: [String](types/String.md)
 * [DataFile➞data_access](DataFile_data_access.md)  <sub>0..1</sub>
     * Description: Type of access control on this file
     * Range: [enum_data_access](enum_data_access.md)
 * [DataFile➞data_category](DataFile_data_category.md)  <sub>0..1</sub>
     * Description: General category of data in file, e.g. Clinical; Genomic; Proteomic; Metabolomic
     * Range: [String](types/String.md)
 * [DataFile➞data_type](DataFile_data_type.md)  <sub>0..1</sub>
     * Description: Specific type of data contained in file, e.g. Simple nucleotide variations; aligned reads; gVCF
     * Range: [String](types/String.md)
 * [DataFile➞experimental_strategy](DataFile_experimental_strategy.md)  <sub>0..1</sub>
     * Description: Specific experimental method used to obtain data in file, e.g. Whole-genome sequencing; LCMS metabolomics
     * Range: [String](types/String.md)
 * [DataFile➞file_id](DataFile_file_id.md)  <sub>1..1</sub>
     * Description: File identifier, assigned by DCC??
     * Range: [String](types/String.md)
 * [DataFile➞file_name](DataFile_file_name.md)  <sub>0..1</sub>
     * Description: Name of file, assigned by data contributor??
     * Range: [String](types/String.md)
 * [DataFile➞format](DataFile_format.md)  <sub>0..1</sub>
     * Description: Format of file
     * Range: [String](types/String.md)
 * [DataFile➞has_biospecimen](DataFile_has_biospecimen.md)  <sub>0..1</sub>
     * Description: Semantic link to a Biospecimen
     * Range: [Biospecimen](Biospecimen.md)
 * [DataFile➞has_participant](DataFile_has_participant.md)  <sub>0..1</sub>
     * Description: Semantic link to a Participant
     * Range: [Participant](Participant.md)
 * [DataFile➞has_study](DataFile_has_study.md)  <sub>0..1</sub>
     * Description: Semantic link to a Study
     * Range: [Study](Study.md)
 * [DataFile➞participant_id](DataFile_participant_id.md)  <sub>0..1</sub>
     * Description: List of Participant IDs for participants associated with this file
     * Range: [String](types/String.md)
 * [DataFile➞size](DataFile_size.md)  <sub>0..1</sub>
     * Description: Size of file
     * Range: [String](types/String.md)
