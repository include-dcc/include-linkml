# Class: Biospecimen
_A Biospecimen Collected from A Participant_





URI: [include:Biospecimen](https://w3id.org/include/Biospecimen)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Biospecimen**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [age_at_biospecimen_collection](age_at_biospecimen_collection.md) | [string](string.md) | 0..1 | Age in days of participant at time of biospecimen collection  | . |
| [biospecimen_storage](biospecimen_storage.md) | [string](string.md) | 0..1 | Method by which Container is stored (e.g. -80C freezer, Liquid nitrogen, etc.)  | . |
| [collection_id](collection_id.md) | [string](string.md) | 0..1 | Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed).  | . |
| [collection_sample_type](collection_sample_type.md) | [string](string.md) | 0..1 | Type of biological material comprising the collected sample (e.g. Whole blood, Bone marrow, Saliva, etc.)  | . |
| [container_id](container_id.md) | [string](string.md) | 0..1 | Identifier for specific container/aliquot of sample, if applicable. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.  | . |
| [has_datafile](has_datafile.md) | [DataFile](DataFile.md) | 0..1 | Link to a DataFile  | . |
| [has_participant](has_participant.md) | [Participant](Participant.md) | 0..1 | Link to a Participant  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Link to a Study  | . |
| [laboratory_procedure](laboratory_procedure.md) | [string](string.md) | 0..1 | Procedure by which Sample was derived from Parent Sample (e.g. RBC lysis, Centrifugation, Ficoll, etc.)  | . |
| [parent_sample_id](parent_sample_id.md) | [string](string.md) | 0..1 | Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable)  | . |
| [parent_sample_type](parent_sample_type.md) | [string](string.md) | 0..1 | Type of biological material comprising the parent sample (e.g. Plasma, Serum, White blood cells, etc.)  | . |
| [sample_availability](sample_availability.md) | [EnumSampleAvailability](EnumSampleAvailability.md) | 0..1 | Whether or not the sample is potentially available for sharing through the Virtual Biorepository  | . |
| [sample_id](sample_id.md) | [string](string.md) | 0..1 | Identifier for sample. A sample is a unique biological material; two samples with two different IDs are biologically distinct.  | . |
| [sample_type](sample_type.md) | [string](string.md) | 0..1 | Type of biological material comprising the sample (e.g. Plasma, Serum, White blood cells, DNA, RNA, etc.)  | . |
| [volume](volume.md) | [string](string.md) | 0..1 | Amount of sample in container  | . |
| [volume_unit](volume_unit.md) | [string](string.md) | 0..1 | Unit of sample volume  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataFile](DataFile.md) | [has_biospecimen](has_biospecimen.md) | range | Biospecimen |



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| requires_component | Study,Participant,DataFile |
| required | False |






## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Biospecimen
definition_uri: include:Biospecimen
annotations:
  requires_component:
    tag: requires_component
    value: Study,Participant,DataFile
  required:
    tag: required
    value: 'False'
description: A Biospecimen Collected from A Participant
title: Biospecimen
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- age_at_biospecimen_collection
- biospecimen_storage
- collection_id
- collection_sample_type
- container_id
- has_datafile
- has_participant
- has_study
- laboratory_procedure
- parent_sample_id
- parent_sample_type
- sample_availability
- sample_id
- sample_type
- volume
- volume_unit
- has_study

```
</details>

### Induced

<details>
```yaml
name: Biospecimen
definition_uri: include:Biospecimen
annotations:
  requires_component:
    tag: requires_component
    value: Study,Participant,DataFile
  required:
    tag: required
    value: 'False'
description: A Biospecimen Collected from A Participant
title: Biospecimen
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
attributes:
  age_at_biospecimen_collection:
    name: age_at_biospecimen_collection
    definition_uri: include:age_at_biospecimen_collection
    description: Age in days of participant at time of biospecimen collection
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_biospecimen_collection
    owner: Biospecimen
    range: string
  biospecimen_storage:
    name: biospecimen_storage
    definition_uri: include:biospecimen_storage
    description: Method by which Container is stored (e.g. -80C freezer, Liquid nitrogen,
      etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: biospecimen_storage
    owner: Biospecimen
    range: string
  collection_id:
    name: collection_id
    definition_uri: include:collection_id
    description: Identifier for the eldest sample in a lineage of processed, pooled,
      or aliquoted samples. This may be the same as Parent Sample ID or Sample ID
      (if no processing was performed).
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_id
    owner: Biospecimen
    range: string
  collection_sample_type:
    name: collection_sample_type
    definition_uri: include:collection_sample_type
    description: Type of biological material comprising the collected sample (e.g.
      Whole blood, Bone marrow, Saliva, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_sample_type
    owner: Biospecimen
    range: string
  container_id:
    name: container_id
    definition_uri: include:container_id
    description: Identifier for specific container/aliquot of sample, if applicable.
      For example, distinct aliquots of a sample will have the same Sample ID but
      different Container IDs.
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: container_id
    owner: Biospecimen
    range: string
  has_datafile:
    name: has_datafile
    definition_uri: include:has_datafile
    description: Link to a DataFile
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_datafile
    owner: Biospecimen
    range: DataFile
  has_participant:
    name: has_participant
    definition_uri: include:has_participant
    description: Link to a Participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_participant
    owner: Biospecimen
    range: Participant
  has_study:
    name: has_study
    definition_uri: include:has_study
    description: Link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: Biospecimen
    range: Study
  laboratory_procedure:
    name: laboratory_procedure
    definition_uri: include:laboratory_procedure
    description: Procedure by which Sample was derived from Parent Sample (e.g. RBC
      lysis, Centrifugation, Ficoll, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: laboratory_procedure
    owner: Biospecimen
    range: string
  parent_sample_id:
    name: parent_sample_id
    definition_uri: include:parent_sample_id
    description: Identifier for the direct parent from which Sample was derived, processed,
      pooled, etc. (if applicable)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: parent_sample_id
    owner: Biospecimen
    range: string
  parent_sample_type:
    name: parent_sample_type
    definition_uri: include:parent_sample_type
    description: Type of biological material comprising the parent sample (e.g. Plasma,
      Serum, White blood cells, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: parent_sample_type
    owner: Biospecimen
    range: string
  sample_availability:
    name: sample_availability
    definition_uri: include:sample_availability
    description: Whether or not the sample is potentially available for sharing through
      the Virtual Biorepository
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sample_availability
    owner: Biospecimen
    range: enum_sample_availability
  sample_id:
    name: sample_id
    definition_uri: include:sample_id
    description: Identifier for sample. A sample is a unique biological material;
      two samples with two different IDs are biologically distinct.
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sample_id
    owner: Biospecimen
    range: string
  sample_type:
    name: sample_type
    definition_uri: include:sample_type
    description: Type of biological material comprising the sample (e.g. Plasma, Serum,
      White blood cells, DNA, RNA, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sample_type
    owner: Biospecimen
    range: string
  volume:
    name: volume
    definition_uri: include:volume
    description: Amount of sample in container
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: volume
    owner: Biospecimen
    range: string
  volume_unit:
    name: volume_unit
    definition_uri: include:volume_unit
    description: Unit of sample volume
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: volume_unit
    owner: Biospecimen
    range: string

```
</details>