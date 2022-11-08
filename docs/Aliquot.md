# Class: Aliquot
_An aliquot of a sample_





URI: [https://w3id.org/include/assay/:Aliquot](https://w3id.org/include/assay/:Aliquot)




```mermaid
 classDiagram
    class Aliquot
      Thing <|-- Aliquot
      
      
```





## Inheritance
* [Thing](Thing.md)
    * **Aliquot**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_aliquot](has_aliquot.md) | range | Aliquot |



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| required | True |
| requires_component | Biospecimen |




### Schema Source


* from schema: https://w3id.org/include/assay







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['https://w3id.org/include/assay/:Aliquot'] |
| native | ['https://w3id.org/include/assay/:Aliquot'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Aliquot
definition_uri: include:Aliquot
annotations:
  required:
    tag: required
    value: 'True'
  requires_component:
    tag: requires_component
    value: Biospecimen
description: An aliquot of a sample
title: Aliquot
from_schema: https://w3id.org/include/assay
rank: 1000
is_a: Thing

```
</details>

### Induced

<details>
```yaml
name: Aliquot
definition_uri: include:Aliquot
annotations:
  required:
    tag: required
    value: 'True'
  requires_component:
    tag: requires_component
    value: Biospecimen
description: An aliquot of a sample
title: Aliquot
from_schema: https://w3id.org/include/assay
rank: 1000
is_a: Thing

```
</details>