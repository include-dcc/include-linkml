
# Class: Biospecimen




URI: [include:Biospecimen](https://w3id.org/include/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[Study]<has_study%200..1-++[Biospecimen&#124;age_at_biospecimen_collection__days:integer%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F],[Participant]<has_participant%200..1-%20[Biospecimen],[DataFile]<has_datafile%200..1-%20[Biospecimen],[DataFile]-%20has_biospecimen%200..1>[Biospecimen],[DataFile]-%20has_biospecimen(i)%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[Study]<has_study%200..1-++[Biospecimen&#124;age_at_biospecimen_collection__days:integer%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F],[Participant]<has_participant%200..1-%20[Biospecimen],[DataFile]<has_datafile%200..1-%20[Biospecimen],[DataFile]-%20has_biospecimen%200..1>[Biospecimen],[DataFile]-%20has_biospecimen(i)%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **[DataFile](DataFile.md)** *[DataFile➞has_biospecimen](DataFile_has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **None** *[has_biospecimen](has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [Biospecimen➞age_at_biospecimen_collection__days](Biospecimen_age_at_biospecimen_collection__days.md)  <sub>0..1</sub>
     * Description: Age (in days) of participant at time of biospecimen collection
     * Range: [Integer](types/Integer.md)
 * [Biospecimen➞biospecimen_storage](Biospecimen_biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Method by which Sample is stored
     * Range: [String](types/String.md)
 * [Biospecimen➞collection_id](Biospecimen_collection_id.md)  <sub>0..1</sub>
     * Description: Identifier for a collection event, during which one or more primary samples are collected, assigned by DCC. Referenced in time with respect to clinical course or to other collection events.
     * Range: [String](types/String.md)
 * [Biospecimen➞collection_sample_type](Biospecimen_collection_sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the collected sample
     * Range: [String](types/String.md)
 * [Biospecimen➞container_id](Biospecimen_container_id.md)  <sub>0..1</sub>
     * Description: Unique identifier for specific container of sample, assigned by DCC or contributor??. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
     * Range: [String](types/String.md)
 * [Biospecimen➞has_datafile](Biospecimen_has_datafile.md)  <sub>0..1</sub>
     * Description: Semantic link to a DataFile
     * Range: [DataFile](DataFile.md)
 * [Biospecimen➞has_participant](Biospecimen_has_participant.md)  <sub>0..1</sub>
     * Description: Semantic link to a Participant
     * Range: [Participant](Participant.md)
 * [Biospecimen➞has_study](Biospecimen_has_study.md)  <sub>0..1</sub>
     * Description: Semantic link to a Study
     * Range: [Study](Study.md)
 * [Biospecimen➞laboratory_procedure](Biospecimen_laboratory_procedure.md)  <sub>0..1</sub>
     * Description: Procedure by which Sample was derived from Parent Sample
     * Range: [String](types/String.md)
 * [Biospecimen➞parent_sample_id](Biospecimen_parent_sample_id.md)  <sub>0..1</sub>
     * Description: Identifier from Parent Sample from which Sample was derived (if applicable)
     * Range: [String](types/String.md)
 * [Biospecimen➞parent_sample_type](Biospecimen_parent_sample_type.md)  <sub>0..1</sub>
     * Description: Type of Parent Sample
     * Range: [String](types/String.md)
 * [Biospecimen➞sample_availability](Biospecimen_sample_availability.md)  <sub>0..1</sub>
     * Description: Whether or not the container (or sample??) is available for sharing through the Virtual Biorepository
     * Range: [enum_sample_availability](enum_sample_availability.md)
 * [Biospecimen➞sample_id](Biospecimen_sample_id.md)  <sub>1..1</sub>
     * Description: Identifier for sample, assigned (by DCC or contributor??) at time of collection, processing, treatment, or derivation. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
     * Range: [String](types/String.md)
 * [Biospecimen➞sample_type](Biospecimen_sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the sample
     * Range: [String](types/String.md)
 * [Biospecimen➞volume](Biospecimen_volume.md)  <sub>0..1</sub>
     * Description: Amount of sample in container
     * Range: [String](types/String.md)
 * [Biospecimen➞volume_unit](Biospecimen_volume_unit.md)  <sub>0..1</sub>
     * Description: Unit of sample volume
     * Range: [String](types/String.md)
