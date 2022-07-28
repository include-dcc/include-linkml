# Class: DataFile
_A DataFile Associated with a Participant or Study or Biospecimen_





URI: [include:DataFile](https://w3id.org/include/DataFile)




```mermaid
 classDiagram
      Thing <|-- DataFile
      
      DataFile : access_url
      DataFile : collection_id
      DataFile : data_access
      DataFile : data_category
      DataFile : data_type
      DataFile : experimental_strategy
      DataFile : file_id
      DataFile : file_name
      DataFile : format
      DataFile : has_biospecimen
      DataFile : has_participant
      DataFile : has_study
      DataFile : participant_id
      DataFile : size
      

```





## Inheritance
* [Thing](Thing.md)
    * **DataFile**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [access_url](access_url.md) | 0..1 <br/> [xsd:string](xsd:string)  | Storage location for this file  |
| [collection_id](collection_id.md) | 0..1 <br/> [xsd:string](xsd:string)  | Identifier for the eldest sample in a lineage of processed, pooled, or aliquo...  |
| [data_access](data_access.md) | 0..1 <br/> [EnumDataAccess](EnumDataAccess.md)  | Type of access control on this file, determined by DCC  |
| [data_category](data_category.md) | 1..1 <br/> [xsd:string](xsd:string)  | General category of data in file (e  |
| [data_type](data_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | Specific type of data contained in file (e  |
| [experimental_strategy](experimental_strategy.md) | 0..1 <br/> [xsd:string](xsd:string)  | Experimental method used to obtain data in file (e  |
| [file_id](file_id.md) | 0..1 <br/> [xsd:string](xsd:string)  | File identifier, assigned by DCC  |
| [file_name](file_name.md) | 0..1 <br/> [xsd:string](xsd:string)  | Synapse ID for file  |
| [format](format.md) | 1..1 <br/> [xsd:string](xsd:string)  | Format of file (e  |
| [has_biospecimen](has_biospecimen.md) | 0..1 <br/> [Biospecimen](Biospecimen.md)  | Link to a Biospecimen  |
| [has_participant](has_participant.md) | 0..1 <br/> [Participant](Participant.md)  | Link to a Participant  |
| [has_study](has_study.md) | 0..1 <br/> [Study](Study.md)  | Link to a Study  |
| [participant_id](participant_id.md) | 1..1 <br/> [xsd:string](xsd:string)  | Unique identifier for the participant, assigned by DCC  |
| [size](size.md) | 0..1 <br/> [xsd:string](xsd:string)  | Size of file  |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_datafile](has_datafile.md) | range | DataFile |
| [Participant](Participant.md) | [has_datafile](has_datafile.md) | range | DataFile |



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| requires_component | Study,Participant,Biospecimen |
| required | False |




### Schema Source


* from schema: https://w3id.org/include







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['include:DataFile'] |
| native | ['include:DataFile'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataFile
definition_uri: include:DataFile
annotations:
  requires_component:
    tag: requires_component
    value: Study,Participant,Biospecimen
  required:
    tag: required
    value: 'False'
description: A DataFile Associated with a Participant or Study or Biospecimen
title: DataFile
from_schema: https://w3id.org/include
rank: 1000
is_a: Thing
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

```
</details>

### Induced

<details>
```yaml
name: DataFile
definition_uri: include:DataFile
annotations:
  requires_component:
    tag: requires_component
    value: Study,Participant,Biospecimen
  required:
    tag: required
    value: 'False'
description: A DataFile Associated with a Participant or Study or Biospecimen
title: DataFile
from_schema: https://w3id.org/include
rank: 1000
is_a: Thing
attributes:
  access_url:
    name: access_url
    definition_uri: include:access_url
    description: Storage location for this file
    from_schema: https://w3id.org/include
    rank: 1000
    alias: access_url
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false
  collection_id:
    name: collection_id
    definition_uri: include:collection_id
    description: Identifier for the eldest sample in a lineage of processed, pooled,
      or aliquoted samples. This may be the same as Parent Sample ID or Sample ID
      (if no processing was performed).
    from_schema: https://w3id.org/include
    rank: 1000
    alias: collection_id
    owner: DataFile
    domain_of:
    - Biospecimen
    - DataFile
    - Biospecimen
    - DataFile
    range: string
    required: false
  data_access:
    name: data_access
    definition_uri: include:data_access
    description: Type of access control on this file, determined by DCC
    from_schema: https://w3id.org/include
    rank: 1000
    alias: data_access
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: enum_data_access
    required: false
  data_category:
    name: data_category
    definition_uri: include:data_category
    description: General category of data in file (e.g. Clinical, Genomics, Proteomics,
      Metabolomics, Immune maps, Transcriptomics, etc.)
    from_schema: https://w3id.org/include
    rank: 1000
    alias: data_category
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: true
  data_type:
    name: data_type
    definition_uri: include:data_type
    description: Specific type of data contained in file (e.g. Aligned reads, Unaligned
      reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification,
      Structural variations, Cytokine profiles, Operation reports, Pathology reports,
      Histology images, Clinical supplement, Protein expression quantification, etc.)
    from_schema: https://w3id.org/include
    rank: 1000
    alias: data_type
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false
  experimental_strategy:
    name: experimental_strategy
    definition_uri: include:experimental_strategy
    description: Experimental method used to obtain data in file (e.g. WGS, RNAseq,
      WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay,
      Meso Scale Discovery, etc.)
    from_schema: https://w3id.org/include
    rank: 1000
    alias: experimental_strategy
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false
  file_id:
    name: file_id
    definition_uri: include:file_id
    description: File identifier, assigned by DCC
    from_schema: https://w3id.org/include
    rank: 1000
    alias: file_id
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false
  file_name:
    name: file_name
    definition_uri: include:file_name
    description: Synapse ID for file
    from_schema: https://w3id.org/include
    rank: 1000
    alias: file_name
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false
  format:
    name: format
    definition_uri: include:format
    description: Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf,
      dicom, etc.)
    from_schema: https://w3id.org/include
    rank: 1000
    alias: format
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: true
  has_biospecimen:
    name: has_biospecimen
    definition_uri: include:has_biospecimen
    description: Link to a Biospecimen
    from_schema: https://w3id.org/include
    rank: 1000
    alias: has_biospecimen
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: Biospecimen
    required: false
  has_participant:
    name: has_participant
    definition_uri: include:has_participant
    description: Link to a Participant
    from_schema: https://w3id.org/include
    rank: 1000
    alias: has_participant
    owner: DataFile
    domain_of:
    - Biospecimen
    - DataFile
    - Biospecimen
    - DataFile
    range: Participant
    required: false
  has_study:
    name: has_study
    definition_uri: include:has_study
    description: Link to a Study
    from_schema: https://w3id.org/include
    rank: 1000
    alias: has_study
    owner: DataFile
    domain_of:
    - Biospecimen
    - Biospecimen
    - DataFile
    - Participant
    - Biospecimen
    - DataFile
    - Participant
    range: Study
    required: false
  participant_id:
    name: participant_id
    definition_uri: include:participant_id
    description: Unique identifier for the participant, assigned by DCC
    from_schema: https://w3id.org/include
    rank: 1000
    alias: participant_id
    owner: DataFile
    domain_of:
    - DataFile
    - Participant
    - DataFile
    - Participant
    range: string
    required: true
  size:
    name: size
    definition_uri: include:size
    description: Size of file
    from_schema: https://w3id.org/include
    rank: 1000
    alias: size
    owner: DataFile
    domain_of:
    - DataFile
    - DataFile
    range: string
    required: false

```
</details>