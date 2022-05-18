
# Class: Biospecimen




URI: [include:Biospecimen](https://w3id.org/include/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[DataFile]<has_datafile%200..1-%20[Biospecimen&#124;age_at_biospecimen_collection__days:integer%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string%20%3F;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F;id(i):string],[Participant]<has_participant%200..1-%20[Biospecimen],[Study]<has_study%200..1-%20[Biospecimen],[DataFile]-%20has_biospecimen%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[DataFile]<has_datafile%200..1-%20[Biospecimen&#124;age_at_biospecimen_collection__days:integer%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string%20%3F;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F;id(i):string],[Participant]<has_participant%200..1-%20[Biospecimen],[Study]<has_study%200..1-%20[Biospecimen],[DataFile]-%20has_biospecimen%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - root class

## Referenced by Class

 *  **None** *[has_biospecimen](has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [has_study](has_study.md)  <sub>0..1</sub>
     * Range: [Study](Study.md)
 * [has_participant](has_participant.md)  <sub>0..1</sub>
     * Range: [Participant](Participant.md)
 * [has_datafile](has_datafile.md)  <sub>0..1</sub>
     * Range: [DataFile](DataFile.md)
 * [➞age_at_biospecimen_collection__days](biospecimen__age_at_biospecimen_collection__days.md)  <sub>0..1</sub>
     * Description: Age (in days) of participant at time of biospecimen collection
     * Range: [Integer](types/Integer.md)
 * [➞biospecimen_storage](biospecimen__biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Method by which Sample is stored
     * Range: [String](types/String.md)
 * [➞collection_id](biospecimen__collection_id.md)  <sub>0..1</sub>
     * Description: Identifier for a collection event, during which one or more primary samples are collected, assigned by DCC. Referenced in time with respect to clinical course or to other collection events.
     * Range: [String](types/String.md)
 * [➞collection_sample_type](biospecimen__collection_sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the collected sample
     * Range: [String](types/String.md)
 * [➞container_id](biospecimen__container_id.md)  <sub>0..1</sub>
     * Description: Unique identifier for specific container of sample, assigned by DCC or contributor??. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
     * Range: [String](types/String.md)
 * [➞laboratory_procedure](biospecimen__laboratory_procedure.md)  <sub>0..1</sub>
     * Description: Procedure by which Sample was derived from Parent Sample
     * Range: [String](types/String.md)
 * [➞parent_sample_id](biospecimen__parent_sample_id.md)  <sub>0..1</sub>
     * Description: Identifier from Parent Sample from which Sample was derived (if applicable)
     * Range: [String](types/String.md)
 * [➞parent_sample_type](biospecimen__parent_sample_type.md)  <sub>0..1</sub>
     * Description: Type of Parent Sample
     * Range: [String](types/String.md)
 * [➞sample_availability](biospecimen__sample_availability.md)  <sub>0..1</sub>
     * Description: Whether or not the container (or sample??) is available for sharing through the Virtual Biorepository
     * Range: [enum_sample_availability](enum_sample_availability.md)
 * [➞sample_id](biospecimen__sample_id.md)  <sub>0..1</sub>
     * Description: Identifier for sample, assigned (by DCC or contributor??) at time of collection, processing, treatment, or derivation. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
     * Range: [String](types/String.md)
 * [➞sample_type](biospecimen__sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the sample
     * Range: [String](types/String.md)
 * [➞volume](biospecimen__volume.md)  <sub>0..1</sub>
     * Description: Amount of sample in container
     * Range: [String](types/String.md)
 * [➞volume_unit](biospecimen__volume_unit.md)  <sub>0..1</sub>
     * Description: Unit of sample volume
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
