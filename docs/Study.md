# Class: Study
_A Study_





URI: [include:Study](https://w3id.org/include/Study)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Study**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [dbgap](dbgap.md) | [string](string.md) | 0..1 | dbGaP study accession code  | . |
| [program](program.md) | [EnumProgram](EnumProgram.md) | 0..1 | Funding source for the study  | . |
| [study_code](study_code.md) | [EnumStudyCode](EnumStudyCode.md) | 0..1 | Unique identifer for the study, assigned by DCC  | . |
| [study_name](study_name.md) | [string](string.md) | 0..1 | Name of the study, chosen by data contributor  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_study](has_study.md) | range | Study |
| [DataFile](DataFile.md) | [has_study](has_study.md) | range | Study |
| [Participant](Participant.md) | [has_study](has_study.md) | range | Study |



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| required | True |






## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Study
definition_uri: include:Study
annotations:
  required:
    tag: required
    value: 'True'
description: A Study
title: Study
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- dbgap
- program
- study_code
- study_name

```
</details>

### Induced

<details>
```yaml
name: Study
definition_uri: include:Study
annotations:
  required:
    tag: required
    value: 'True'
description: A Study
title: Study
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
attributes:
  dbgap:
    name: dbgap
    definition_uri: include:dbgap
    description: dbGaP study accession code
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: dbgap
    owner: Study
    range: string
  program:
    name: program
    definition_uri: include:program
    description: Funding source for the study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: program
    owner: Study
    range: enum_program
  study_code:
    name: study_code
    definition_uri: include:study_code
    description: Unique identifer for the study, assigned by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: study_code
    owner: Study
    range: enum_study_code
  study_name:
    name: study_name
    definition_uri: include:study_name
    description: Name of the study, chosen by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: study_name
    owner: Study
    range: string

```
</details>