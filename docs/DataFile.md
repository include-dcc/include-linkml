# Class: DataFile




URI: [include:DataFile](https://w3id.org/include/DataFile)




## Inheritance

* [NamedThing](NamedThing.md)
    * **DataFile**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [access_url](access_url.md) | [string](string.md) | 0..1 | Storage location for this file ??  | . |
| [collection_id](collection_id.md) | [string](string.md) | 0..1 | List of Collection?? IDs for biospecimens associated with this file  | . |
| [data_access](data_access.md) | [EnumDataAccess](EnumDataAccess.md) | 0..1 | Type of access control on this file  | . |
| [data_category](data_category.md) | [string](string.md) | 0..1 | General category of data in file, e.g. Clinical; Genomic; Proteomic; Metabolomic  | . |
| [data_type](data_type.md) | [string](string.md) | 0..1 | Specific type of data contained in file, e.g. Simple nucleotide variations; aligned reads; gVCF  | . |
| [experimental_strategy](experimental_strategy.md) | [string](string.md) | 0..1 | Specific experimental method used to obtain data in file, e.g. Whole-genome sequencing; LCMS metabolomics  | . |
| [file_id](file_id.md) | [string](string.md) | 0..1 | File identifier, assigned by DCC??  | . |
| [file_name](file_name.md) | [string](string.md) | 0..1 | Name of file, assigned by data contributor??  | . |
| [format](format.md) | [string](string.md) | 0..1 | Format of file  | . |
| [has_biospecimen](has_biospecimen.md) | [Biospecimen](Biospecimen.md) | 0..1 | Semantic link to a Biospecimen  | . |
| [has_participant](has_participant.md) | [Participant](Participant.md) | 0..1 | Semantic link to a Participant  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Semantic link to a Study  | . |
| [participant_id](participant_id.md) | [string](string.md) | 0..1 | List of Participant IDs for participants associated with this file  | . |
| [size](size.md) | [string](string.md) | 0..1 | Size of file  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_datafile](has_datafile.md) | range | DataFile |
| [Participant](Participant.md) | [has_datafile](has_datafile.md) | range | DataFile |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataFile
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- access_url
- collection_id
- data_access
- data_category
- data_type
- experimental_strategy
- file_id
- file_name
- format
- has_biospecimen
- has_participant
- has_study
- participant_id
- size
slot_usage:
  access_url:
    name: access_url
    description: Storage location for this file ??
  collection_id:
    name: collection_id
    description: List of Collection?? IDs for biospecimens associated with this file
  data_access:
    name: data_access
    description: Type of access control on this file
    range: enum_data_access
  data_category:
    name: data_category
    description: General category of data in file, e.g. Clinical; Genomic; Proteomic;
      Metabolomic
  data_type:
    name: data_type
    description: Specific type of data contained in file, e.g. Simple nucleotide variations;
      aligned reads; gVCF
  experimental_strategy:
    name: experimental_strategy
    description: Specific experimental method used to obtain data in file, e.g. Whole-genome
      sequencing; LCMS metabolomics
  file_id:
    name: file_id
    description: File identifier, assigned by DCC??
    identifier: true
  file_name:
    name: file_name
    description: Name of file, assigned by data contributor??
  format:
    name: format
    description: Format of file
  has_biospecimen:
    name: has_biospecimen
    range: Biospecimen
  has_participant:
    name: has_participant
    range: Participant
  has_study:
    name: has_study
    range: Study
  participant_id:
    name: participant_id
    description: List of Participant IDs for participants associated with this file
  size:
    name: size
    description: Size of file

```
</details>

### Induced

<details>
```yaml
name: DataFile
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slot_usage:
  access_url:
    name: access_url
    description: Storage location for this file ??
  collection_id:
    name: collection_id
    description: List of Collection?? IDs for biospecimens associated with this file
  data_access:
    name: data_access
    description: Type of access control on this file
    range: enum_data_access
  data_category:
    name: data_category
    description: General category of data in file, e.g. Clinical; Genomic; Proteomic;
      Metabolomic
  data_type:
    name: data_type
    description: Specific type of data contained in file, e.g. Simple nucleotide variations;
      aligned reads; gVCF
  experimental_strategy:
    name: experimental_strategy
    description: Specific experimental method used to obtain data in file, e.g. Whole-genome
      sequencing; LCMS metabolomics
  file_id:
    name: file_id
    description: File identifier, assigned by DCC??
    identifier: true
  file_name:
    name: file_name
    description: Name of file, assigned by data contributor??
  format:
    name: format
    description: Format of file
  has_biospecimen:
    name: has_biospecimen
    range: Biospecimen
  has_participant:
    name: has_participant
    range: Participant
  has_study:
    name: has_study
    range: Study
  participant_id:
    name: participant_id
    description: List of Participant IDs for participants associated with this file
  size:
    name: size
    description: Size of file
attributes:
  access_url:
    name: access_url
    description: Storage location for this file ??
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: access_url
    owner: DataFile
    range: string
  collection_id:
    name: collection_id
    description: List of Collection?? IDs for biospecimens associated with this file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_id
    owner: DataFile
    range: string
  data_access:
    name: data_access
    description: Type of access control on this file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_access
    owner: DataFile
    range: enum_data_access
  data_category:
    name: data_category
    description: General category of data in file, e.g. Clinical; Genomic; Proteomic;
      Metabolomic
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_category
    owner: DataFile
    range: string
  data_type:
    name: data_type
    description: Specific type of data contained in file, e.g. Simple nucleotide variations;
      aligned reads; gVCF
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_type
    owner: DataFile
    range: string
  experimental_strategy:
    name: experimental_strategy
    description: Specific experimental method used to obtain data in file, e.g. Whole-genome
      sequencing; LCMS metabolomics
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: experimental_strategy
    owner: DataFile
    range: string
  file_id:
    name: file_id
    description: File identifier, assigned by DCC??
    from_schema: https://w3id.org/include_portal_v1_schema
    identifier: true
    alias: file_id
    owner: DataFile
    range: string
  file_name:
    name: file_name
    description: Name of file, assigned by data contributor??
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: file_name
    owner: DataFile
    range: string
  format:
    name: format
    description: Format of file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: format
    owner: DataFile
    range: string
  has_biospecimen:
    name: has_biospecimen
    description: Semantic link to a Biospecimen
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_biospecimen
    owner: DataFile
    range: Biospecimen
  has_participant:
    name: has_participant
    description: Semantic link to a Participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_participant
    owner: DataFile
    range: Participant
  has_study:
    name: has_study
    description: Semantic link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: DataFile
    range: Study
  participant_id:
    name: participant_id
    description: List of Participant IDs for participants associated with this file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: participant_id
    owner: DataFile
    range: string
  size:
    name: size
    description: Size of file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: size
    owner: DataFile
    range: string

```
</details>