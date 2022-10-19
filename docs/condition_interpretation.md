# Slot: condition_interpretation
_Whether condition was observed or not. "Not Observed" indicates participant was specifically examined for that condition, or health record specifically queried for that condition, and found to be negative. Sept. 2022 release will only include positive assertions._


URI: [https://w3id.org/include/participant/:condition_interpretation](https://w3id.org/include/participant/:condition_interpretation)



<!-- no inheritance hierarchy -->




## Properties

* Range: [EnumConditionInterpretation](EnumConditionInterpretation.md)
* Multivalued: None







## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/include/participant




## LinkML Specification

<details>
```yaml
name: condition_interpretation
definition_uri: include:condition_interpretation
description: Whether condition was observed or not. "Not Observed" indicates participant
  was specifically examined for that condition, or health record specifically queried
  for that condition, and found to be negative. Sept. 2022 release will only include
  positive assertions.
title: Condition Interpretation
from_schema: https://w3id.org/include/participant
rank: 1000
alias: condition_interpretation
domain_of:
- Condition
range: enum_condition_interpretation

```
</details>