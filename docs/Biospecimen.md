# Class: Biospecimen




URI: [include:Biospecimen](https://w3id.org/include/Biospecimen)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Biospecimen**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [age_at_biospecimen_collection__days](age_at_biospecimen_collection__days.md) | [integer](integer.md) | 0..1 | Age (in days) of participant at time of biospecimen collection  | . |
| [biospecimen_storage](biospecimen_storage.md) | [string](string.md) | 0..1 | Method by which Sample is stored  | . |
| [collection_id](collection_id.md) | [string](string.md) | 0..1 | Identifier for a collection event, during which one or more primary samples are collected, assigned by DCC. Referenced in time with respect to clinical course or to other collection events.  | . |
| [collection_sample_type](collection_sample_type.md) | [string](string.md) | 0..1 | Type of biological material comprising the collected sample  | . |
| [container_id](container_id.md) | [string](string.md) | 0..1 | Unique identifier for specific container of sample, assigned by DCC or contributor??. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.  | . |
| [has_datafile](has_datafile.md) | [DataFile](DataFile.md) | 0..1 | Semantic link to a DataFile  | . |
| [has_participant](has_participant.md) | [Participant](Participant.md) | 0..1 | Semantic link to a Participant  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Semantic link to a Study  | . |
| [laboratory_procedure](laboratory_procedure.md) | [string](string.md) | 0..1 | Procedure by which Sample was derived from Parent Sample  | . |
| [parent_sample_id](parent_sample_id.md) | [string](string.md) | 0..1 | Identifier from Parent Sample from which Sample was derived (if applicable)  | . |
| [parent_sample_type](parent_sample_type.md) | [string](string.md) | 0..1 | Type of Parent Sample  | . |
| [sample_availability](sample_availability.md) | [EnumSampleAvailability](EnumSampleAvailability.md) | 0..1 | Whether or not the container (or sample??) is available for sharing through the Virtual Biorepository  | . |
| [sample_id](sample_id.md) | [string](string.md) | 0..1 | Identifier for sample, assigned (by DCC or contributor??) at time of collection, processing, treatment, or derivation. A sample is a unique biological material; two samples with two different IDs are biologically distinct.  | . |
| [sample_type](sample_type.md) | [string](string.md) | 0..1 | Type of biological material comprising the sample  | . |
| [volume](volume.md) | [string](string.md) | 0..1 | Amount of sample in container  | . |
| [volume_unit](volume_unit.md) | [string](string.md) | 0..1 | Unit of sample volume  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataFile](DataFile.md) | [has_biospecimen](has_biospecimen.md) | range | Biospecimen |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Biospecimen
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- age_at_biospecimen_collection__days
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
slot_usage:
  age_at_biospecimen_collection__days:
    name: age_at_biospecimen_collection__days
    description: Age (in days) of participant at time of biospecimen collection
    range: integer
  biospecimen_storage:
    name: biospecimen_storage
    description: Method by which Sample is stored
  collection_id:
    name: collection_id
    description: Identifier for a collection event, during which one or more primary
      samples are collected, assigned by DCC. Referenced in time with respect to clinical
      course or to other collection events.
  collection_sample_type:
    name: collection_sample_type
    description: Type of biological material comprising the collected sample
  container_id:
    name: container_id
    description: Unique identifier for specific container of sample, assigned by DCC
      or contributor??. For example, distinct aliquots of a sample will have the same
      Sample ID but different Container IDs.
  has_datafile:
    name: has_datafile
    range: DataFile
  has_participant:
    name: has_participant
    range: Participant
  has_study:
    name: has_study
    range: Study
  laboratory_procedure:
    name: laboratory_procedure
    description: Procedure by which Sample was derived from Parent Sample
  parent_sample_id:
    name: parent_sample_id
    description: Identifier from Parent Sample from which Sample was derived (if applicable)
  parent_sample_type:
    name: parent_sample_type
    description: Type of Parent Sample
  sample_availability:
    name: sample_availability
    description: Whether or not the container (or sample??) is available for sharing
      through the Virtual Biorepository
    range: enum_sample_availability
  sample_id:
    name: sample_id
    description: Identifier for sample, assigned (by DCC or contributor??) at time
      of collection, processing, treatment, or derivation. A sample is a unique biological
      material; two samples with two different IDs are biologically distinct.
    identifier: true
  sample_type:
    name: sample_type
    description: Type of biological material comprising the sample
  volume:
    name: volume
    description: Amount of sample in container
  volume_unit:
    name: volume_unit
    description: Unit of sample volume

```
</details>

### Induced

<details>
```yaml
name: Biospecimen
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slot_usage:
  age_at_biospecimen_collection__days:
    name: age_at_biospecimen_collection__days
    description: Age (in days) of participant at time of biospecimen collection
    range: integer
  biospecimen_storage:
    name: biospecimen_storage
    description: Method by which Sample is stored
  collection_id:
    name: collection_id
    description: Identifier for a collection event, during which one or more primary
      samples are collected, assigned by DCC. Referenced in time with respect to clinical
      course or to other collection events.
  collection_sample_type:
    name: collection_sample_type
    description: Type of biological material comprising the collected sample
  container_id:
    name: container_id
    description: Unique identifier for specific container of sample, assigned by DCC
      or contributor??. For example, distinct aliquots of a sample will have the same
      Sample ID but different Container IDs.
  has_datafile:
    name: has_datafile
    range: DataFile
  has_participant:
    name: has_participant
    range: Participant
  has_study:
    name: has_study
    range: Study
  laboratory_procedure:
    name: laboratory_procedure
    description: Procedure by which Sample was derived from Parent Sample
  parent_sample_id:
    name: parent_sample_id
    description: Identifier from Parent Sample from which Sample was derived (if applicable)
  parent_sample_type:
    name: parent_sample_type
    description: Type of Parent Sample
  sample_availability:
    name: sample_availability
    description: Whether or not the container (or sample??) is available for sharing
      through the Virtual Biorepository
    range: enum_sample_availability
  sample_id:
    name: sample_id
    description: Identifier for sample, assigned (by DCC or contributor??) at time
      of collection, processing, treatment, or derivation. A sample is a unique biological
      material; two samples with two different IDs are biologically distinct.
    identifier: true
  sample_type:
    name: sample_type
    description: Type of biological material comprising the sample
  volume:
    name: volume
    description: Amount of sample in container
  volume_unit:
    name: volume_unit
    description: Unit of sample volume
attributes:
  age_at_biospecimen_collection__days:
    name: age_at_biospecimen_collection__days
    description: Age (in days) of participant at time of biospecimen collection
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_biospecimen_collection__days
    owner: Biospecimen
    range: integer
  biospecimen_storage:
    name: biospecimen_storage
    description: Method by which Sample is stored
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: biospecimen_storage
    owner: Biospecimen
    range: string
  collection_id:
    name: collection_id
    description: Identifier for a collection event, during which one or more primary
      samples are collected, assigned by DCC. Referenced in time with respect to clinical
      course or to other collection events.
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_id
    owner: Biospecimen
    range: string
  collection_sample_type:
    name: collection_sample_type
    description: Type of biological material comprising the collected sample
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_sample_type
    owner: Biospecimen
    range: string
  container_id:
    name: container_id
    description: Unique identifier for specific container of sample, assigned by DCC
      or contributor??. For example, distinct aliquots of a sample will have the same
      Sample ID but different Container IDs.
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: container_id
    owner: Biospecimen
    range: string
  has_datafile:
    name: has_datafile
    description: Semantic link to a DataFile
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_datafile
    owner: Biospecimen
    range: DataFile
  has_participant:
    name: has_participant
    description: Semantic link to a Participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_participant
    owner: Biospecimen
    range: Participant
  has_study:
    name: has_study
    description: Semantic link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: Biospecimen
    range: Study
  laboratory_procedure:
    name: laboratory_procedure
    description: Procedure by which Sample was derived from Parent Sample
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: laboratory_procedure
    owner: Biospecimen
    range: string
  parent_sample_id:
    name: parent_sample_id
    description: Identifier from Parent Sample from which Sample was derived (if applicable)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: parent_sample_id
    owner: Biospecimen
    range: string
  parent_sample_type:
    name: parent_sample_type
    description: Type of Parent Sample
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: parent_sample_type
    owner: Biospecimen
    range: string
  sample_availability:
    name: sample_availability
    description: Whether or not the container (or sample??) is available for sharing
      through the Virtual Biorepository
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sample_availability
    owner: Biospecimen
    range: enum_sample_availability
  sample_id:
    name: sample_id
    description: Identifier for sample, assigned (by DCC or contributor??) at time
      of collection, processing, treatment, or derivation. A sample is a unique biological
      material; two samples with two different IDs are biologically distinct.
    from_schema: https://w3id.org/include_portal_v1_schema
    identifier: true
    alias: sample_id
    owner: Biospecimen
    range: string
  sample_type:
    name: sample_type
    description: Type of biological material comprising the sample
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sample_type
    owner: Biospecimen
    range: string
  volume:
    name: volume
    description: Amount of sample in container
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: volume
    owner: Biospecimen
    range: string
  volume_unit:
    name: volume_unit
    description: Unit of sample volume
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: volume_unit
    owner: Biospecimen
    range: string

```
</details>