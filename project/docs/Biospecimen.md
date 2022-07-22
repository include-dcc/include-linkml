
# Class: Biospecimen


A Biospecimen Collected from A Participant

URI: [include:Biospecimen](https://w3id.org/include/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[Study]<has_study%200..1-++[Biospecimen&#124;age_at_biospecimen_collection:string%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string%20%3F;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F],[Participant]<has_participant%200..1-++[Biospecimen],[DataFile]<has_datafile%200..1-++[Biospecimen],[DataFile]++-%20has_biospecimen%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Participant],[NamedThing],[DataFile],[Study]<has_study%200..1-++[Biospecimen&#124;age_at_biospecimen_collection:string%20%3F;biospecimen_storage:string%20%3F;collection_id:string%20%3F;collection_sample_type:string%20%3F;container_id:string%20%3F;laboratory_procedure:string%20%3F;parent_sample_id:string%20%3F;parent_sample_type:string%20%3F;sample_availability:enum_sample_availability%20%3F;sample_id:string%20%3F;sample_type:string%20%3F;volume:string%20%3F;volume_unit:string%20%3F],[Participant]<has_participant%200..1-++[Biospecimen],[DataFile]<has_datafile%200..1-++[Biospecimen],[DataFile]++-%20has_biospecimen%200..1>[Biospecimen],[NamedThing]^-[Biospecimen])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **None** *[has_biospecimen](has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [age_at_biospecimen_collection](age_at_biospecimen_collection.md)  <sub>0..1</sub>
     * Description: Age in days of participant at time of biospecimen collection
     * Range: [String](types/String.md)
 * [biospecimen_storage](biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Method by which Container is stored (e.g. -80C freezer, Liquid nitrogen, etc.)
     * Range: [String](types/String.md)
 * [collection_id](collection_id.md)  <sub>0..1</sub>
     * Description: Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed).
     * Range: [String](types/String.md)
 * [collection_sample_type](collection_sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the collected sample (e.g. Whole blood, Bone marrow, Saliva, etc.)
     * Range: [String](types/String.md)
 * [container_id](container_id.md)  <sub>0..1</sub>
     * Description: Identifier for specific container/aliquot of sample, if applicable. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.
     * Range: [String](types/String.md)
 * [has_datafile](has_datafile.md)  <sub>0..1</sub>
     * Description: Link to a DataFile
     * Range: [DataFile](DataFile.md)
 * [has_participant](has_participant.md)  <sub>0..1</sub>
     * Description: Link to a Participant
     * Range: [Participant](Participant.md)
 * [has_study](has_study.md)  <sub>0..1</sub>
     * Description: Link to a Study
     * Range: [Study](Study.md)
 * [laboratory_procedure](laboratory_procedure.md)  <sub>0..1</sub>
     * Description: Procedure by which Sample was derived from Parent Sample (e.g. RBC lysis, Centrifugation, Ficoll, etc.)
     * Range: [String](types/String.md)
 * [parent_sample_id](parent_sample_id.md)  <sub>0..1</sub>
     * Description: Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable)
     * Range: [String](types/String.md)
 * [parent_sample_type](parent_sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the parent sample (e.g. Plasma, Serum, White blood cells, etc.)
     * Range: [String](types/String.md)
 * [sample_availability](sample_availability.md)  <sub>0..1</sub>
     * Description: Whether or not the sample is potentially available for sharing through the Virtual Biorepository
     * Range: [enum_sample_availability](enum_sample_availability.md)
 * [sample_id](sample_id.md)  <sub>0..1</sub>
     * Description: Identifier for sample. A sample is a unique biological material; two samples with two different IDs are biologically distinct.
     * Range: [String](types/String.md)
 * [sample_type](sample_type.md)  <sub>0..1</sub>
     * Description: Type of biological material comprising the sample (e.g. Plasma, Serum, White blood cells, DNA, RNA, etc.)
     * Range: [String](types/String.md)
 * [volume](volume.md)  <sub>0..1</sub>
     * Description: Amount of sample in container
     * Range: [String](types/String.md)
 * [volume_unit](volume_unit.md)  <sub>0..1</sub>
     * Description: Unit of sample volume
     * Range: [String](types/String.md)
 * [has_study](has_study.md)  <sub>0..1</sub>
     * Description: Link to a Study
     * Range: [Study](Study.md)
