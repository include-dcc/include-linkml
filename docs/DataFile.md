# Class: DataFile
_A DataFile Associated with a Participant or Study or Biospecimen_





URI: [include:DataFile](https://w3id.org/include/DataFile)




## Inheritance

* [NamedThing](NamedThing.md)
    * **DataFile**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [access_url](access_url.md) | [string](string.md) | 0..1 | Storage location for this file  | . |
| [collection_id](collection_id.md) | [string](string.md) | 0..1 | Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed).  | . |
| [data_access](data_access.md) | [EnumDataAccess](EnumDataAccess.md) | 0..1 | Type of access control on this file, determined by DCC  | . |
| [data_category](data_category.md) | [string](string.md) | 0..1 | General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune maps, Transcriptomics, etc.)  | . |
| [data_type](data_type.md) | [string](string.md) | 0..1 | Specific type of data contained in file (e.g. Aligned reads, Unaligned reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification, Structural variations, Cytokine profiles, Operation reports, Pathology reports, Histology images, Clinical supplement, Protein expression quantification, etc.)  | . |
| [experimental_strategy](experimental_strategy.md) | [string](string.md) | 0..1 | Experimental method used to obtain data in file (e.g. WGS, RNAseq, WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay, Meso Scale Discovery, etc.)  | . |
| [file_id](file_id.md) | [string](string.md) | 0..1 | File identifier, assigned by DCC  | . |
| [file_name](file_name.md) | [string](string.md) | 0..1 | Synapse ID for file  | . |
| [format](format.md) | [string](string.md) | 0..1 | Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf, dicom, etc.)  | . |
| [has_biospecimen](has_biospecimen.md) | [Biospecimen](Biospecimen.md) | 0..1 | Link to a Biospecimen  | . |
| [has_participant](has_participant.md) | [Participant](Participant.md) | 0..1 | Link to a Participant  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Link to a Study  | . |
| [participant_id](participant_id.md) | [string](string.md) | 0..1 | Unique identifier for the participant, assigned by DCC  | . |
| [size](size.md) | [string](string.md) | 0..1 | Size of file  | . |


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
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
attributes:
  access_url:
    name: access_url
    definition_uri: include:access_url
    description: Storage location for this file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: access_url
    owner: DataFile
    range: string
  collection_id:
    name: collection_id
    definition_uri: include:collection_id
    description: Identifier for the eldest sample in a lineage of processed, pooled,
      or aliquoted samples. This may be the same as Parent Sample ID or Sample ID
      (if no processing was performed).
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: collection_id
    owner: DataFile
    range: string
  data_access:
    name: data_access
    definition_uri: include:data_access
    description: Type of access control on this file, determined by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_access
    owner: DataFile
    range: enum_data_access
  data_category:
    name: data_category
    definition_uri: include:data_category
    description: General category of data in file (e.g. Clinical, Genomics, Proteomics,
      Metabolomics, Immune maps, Transcriptomics, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_category
    owner: DataFile
    range: string
  data_type:
    name: data_type
    definition_uri: include:data_type
    description: Specific type of data contained in file (e.g. Aligned reads, Unaligned
      reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification,
      Structural variations, Cytokine profiles, Operation reports, Pathology reports,
      Histology images, Clinical supplement, Protein expression quantification, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: data_type
    owner: DataFile
    range: string
  experimental_strategy:
    name: experimental_strategy
    definition_uri: include:experimental_strategy
    description: Experimental method used to obtain data in file (e.g. WGS, RNAseq,
      WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay,
      Meso Scale Discovery, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: experimental_strategy
    owner: DataFile
    range: string
  file_id:
    name: file_id
    definition_uri: include:file_id
    description: File identifier, assigned by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: file_id
    owner: DataFile
    range: string
  file_name:
    name: file_name
    definition_uri: include:file_name
    description: Synapse ID for file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: file_name
    owner: DataFile
    range: string
  format:
    name: format
    definition_uri: include:format
    description: Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf,
      dicom, etc.)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: format
    owner: DataFile
    range: string
  has_biospecimen:
    name: has_biospecimen
    definition_uri: include:has_biospecimen
    description: Link to a Biospecimen
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_biospecimen
    owner: DataFile
    range: Biospecimen
  has_participant:
    name: has_participant
    definition_uri: include:has_participant
    description: Link to a Participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_participant
    owner: DataFile
    range: Participant
  has_study:
    name: has_study
    definition_uri: include:has_study
    description: Link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: DataFile
    range: Study
  participant_id:
    name: participant_id
    definition_uri: include:participant_id
    description: Unique identifier for the participant, assigned by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: participant_id
    owner: DataFile
    range: string
  size:
    name: size
    definition_uri: include:size
    description: Size of file
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: size
    owner: DataFile
    range: string

```
</details>