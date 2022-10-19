# Slot: family_type
_Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)_


URI: [https://w3id.org/include/participant/:family_type](https://w3id.org/include/participant/:family_type)



<!-- no inheritance hierarchy -->




## Properties

* Range: [EnumFamilyType](EnumFamilyType.md)
* Multivalued: None



* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/include/participant




## LinkML Specification

<details>
```yaml
name: family_type
definition_uri: include:family_type
description: Structure of family members participating in the study (proband-only
  = no family members participating; duo = proband + parent; trio = proband + 2 parents;
  trio+ = proband + 2 parents + other relatives)
title: Family Type
from_schema: https://w3id.org/include/participant
rank: 1000
alias: family_type
domain_of:
- Participant
range: enum_family_type
required: true

```
</details>