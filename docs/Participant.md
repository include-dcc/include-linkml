# Class: Participant
_A Participant in a Study_





URI: [include:Participant](https://w3id.org/include/Participant)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Participant**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [age_at_diagnosis](age_at_diagnosis.md) | [string](string.md) | 0..1 | Age in days at which phenotype was assigned  | . |
| [age_at_phenotype_assignment](age_at_phenotype_assignment.md) | [string](string.md) | 0..1 | Age in days at which phenotype was recorded  | . |
| [age_at_the_last_vital_status](age_at_the_last_vital_status.md) | [string](string.md) | 0..1 | None  | . |
| [diagnosis_icd](diagnosis_icd.md) | [string](string.md) | 0..1 | ICD-10 code (annotated by data contributor or DCC)  | . |
| [diagnosis_mondo](diagnosis_mondo.md) | [string](string.md) | 0..1 | Mondo disease ontology code (annotated by data contributor or DCC)  | . |
| [diagnosis_ncit](diagnosis_ncit.md) | [string](string.md) | 0..1 | NCI Thesaurus code (annotated by data contributor or DCC)  | . |
| [diagnosis_source_text](diagnosis_source_text.md) | [string](string.md) | 0..1 | Diagnosis as described by data contributor  | . |
| [diagnosis_type](diagnosis_type.md) | [string](string.md) | 0..1 | How diagnosis was assigned  | . |
| [down_syndrome_status](down_syndrome_status.md) | [EnumDownSyndromeStatus](EnumDownSyndromeStatus.md) | 0..1 | Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)  | . |
| [ethnicity](ethnicity.md) | [EnumEthnicity](EnumEthnicity.md) | 0..1 | Ethnicity of participant  | . |
| [external_id](external_id.md) | [string](string.md) | 0..1 | Unique identifier for the participant, assigned by data contributor  | . |
| [family_id](family_id.md) | [string](string.md) | 0..1 | Unique identifer for family to which Participant belongs  | . |
| [family_relationship](family_relationship.md) | [string](string.md) | 0..1 | Relationship of Participant to other family members  | . |
| [family_type](family_type.md) | [EnumFamilyType](EnumFamilyType.md) | 0..1 | Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)   | . |
| [father_id](father_id.md) | [string](string.md) | 0..1 | Participant ID for Participant's father  | . |
| [has_datafile](has_datafile.md) | [DataFile](DataFile.md) | 0..1 | Link to a DataFile  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Link to a Study  | . |
| [mother_id](mother_id.md) | [string](string.md) | 0..1 | Participant ID for Participant's mother  | . |
| [outcomes_vital_status](outcomes_vital_status.md) | [string](string.md) | 0..1 | Whether participant is alive or dead  | . |
| [participant_id](participant_id.md) | [string](string.md) | 0..1 | Unique identifier for the participant, assigned by DCC  | . |
| [phenotype_hpo](phenotype_hpo.md) | [string](string.md) | 0..1 | Human Phenotype Ontology code (annotated by data contributor or DCC)  | . |
| [phenotype_source_text](phenotype_source_text.md) | [string](string.md) | 0..1 | Phenotype as described by data contributor  | . |
| [phenotype_interpretation](phenotype_interpretation.md) | [EnumPhenotypeInterpretation](EnumPhenotypeInterpretation.md) | 0..1 | Whether phenotype was observed or not  | . |
| [race](race.md) | [EnumRace](EnumRace.md) | 0..1 | Race of participant  | . |
| [sex](sex.md) | [EnumSex](EnumSex.md) | 0..1 | Sex of participant  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_participant](has_participant.md) | range | Participant |
| [DataFile](DataFile.md) | [has_participant](has_participant.md) | range | Participant |



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| requires_component | Study,DataFile |
| required | False |






## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Participant
definition_uri: include:Participant
annotations:
  requires_component:
    tag: requires_component
    value: Study,DataFile
  required:
    tag: required
    value: 'False'
description: A Participant in a Study
title: Participant
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- age_at_diagnosis
- age_at_phenotype_assignment
- age_at_the_last_vital_status
- diagnosis_icd
- diagnosis_mondo
- diagnosis_ncit
- diagnosis_source_text
- diagnosis_type
- down_syndrome_status
- ethnicity
- external_id
- family_id
- family_relationship
- family_type
- father_id
- has_datafile
- has_study
- mother_id
- outcomes_vital_status
- participant_id
- phenotype_hpo
- phenotype_source_text
- phenotype_interpretation
- race
- sex

```
</details>

### Induced

<details>
```yaml
name: Participant
definition_uri: include:Participant
annotations:
  requires_component:
    tag: requires_component
    value: Study,DataFile
  required:
    tag: required
    value: 'False'
description: A Participant in a Study
title: Participant
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
attributes:
  age_at_diagnosis:
    name: age_at_diagnosis
    definition_uri: include:age_at_diagnosis
    description: Age in days at which phenotype was assigned
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_diagnosis
    owner: Participant
    range: string
  age_at_phenotype_assignment:
    name: age_at_phenotype_assignment
    definition_uri: include:age_at_phenotype_assignment
    description: Age in days at which phenotype was recorded
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_phenotype_assignment
    owner: Participant
    range: string
  age_at_the_last_vital_status:
    name: age_at_the_last_vital_status
    definition_uri: include:age_at_the_last_vital_status
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_the_last_vital_status
    owner: Participant
    range: string
  diagnosis_icd:
    name: diagnosis_icd
    definition_uri: include:diagnosis_icd
    description: ICD-10 code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_icd
    owner: Participant
    range: string
  diagnosis_mondo:
    name: diagnosis_mondo
    definition_uri: include:diagnosis_mondo
    description: Mondo disease ontology code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_mondo
    owner: Participant
    range: string
  diagnosis_ncit:
    name: diagnosis_ncit
    definition_uri: include:diagnosis_ncit
    description: NCI Thesaurus code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_ncit
    owner: Participant
    range: string
  diagnosis_source_text:
    name: diagnosis_source_text
    definition_uri: include:diagnosis_source_text
    description: Diagnosis as described by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_source_text
    owner: Participant
    range: string
  diagnosis_type:
    name: diagnosis_type
    definition_uri: include:diagnosis_type
    description: How diagnosis was assigned
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_type
    owner: Participant
    range: string
  down_syndrome_status:
    name: down_syndrome_status
    definition_uri: include:down_syndrome_status
    description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy
      21, euploid)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: down_syndrome_status
    owner: Participant
    range: enum_down_syndrome_status
  ethnicity:
    name: ethnicity
    definition_uri: include:ethnicity
    description: Ethnicity of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: ethnicity
    owner: Participant
    range: enum_ethnicity
  external_id:
    name: external_id
    definition_uri: include:external_id
    description: Unique identifier for the participant, assigned by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: external_id
    owner: Participant
    range: string
  family_id:
    name: family_id
    definition_uri: include:family_id
    description: Unique identifer for family to which Participant belongs
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_id
    owner: Participant
    range: string
  family_relationship:
    name: family_relationship
    definition_uri: include:family_relationship
    description: Relationship of Participant to other family members
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_relationship
    owner: Participant
    range: string
  family_type:
    name: family_type
    definition_uri: include:family_type
    description: 'Structure of family members participating in the study (proband-only
      = no family members participating; duo = proband + parent; trio = proband +
      2 parents; trio+ = proband + 2 parents + other relatives) '
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_type
    owner: Participant
    range: enum_family_type
  father_id:
    name: father_id
    definition_uri: include:father_id
    description: Participant ID for Participant's father
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: father_id
    owner: Participant
    range: string
  has_datafile:
    name: has_datafile
    definition_uri: include:has_datafile
    description: Link to a DataFile
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_datafile
    owner: Participant
    range: DataFile
  has_study:
    name: has_study
    definition_uri: include:has_study
    description: Link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: Participant
    range: Study
  mother_id:
    name: mother_id
    definition_uri: include:mother_id
    description: Participant ID for Participant's mother
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: mother_id
    owner: Participant
    range: string
  outcomes_vital_status:
    name: outcomes_vital_status
    definition_uri: include:outcomes_vital_status
    description: Whether participant is alive or dead
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: outcomes_vital_status
    owner: Participant
    range: string
  participant_id:
    name: participant_id
    definition_uri: include:participant_id
    description: Unique identifier for the participant, assigned by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: participant_id
    owner: Participant
    range: string
  phenotype_hpo:
    name: phenotype_hpo
    definition_uri: include:phenotype_hpo
    description: Human Phenotype Ontology code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype_hpo
    owner: Participant
    range: string
  phenotype_source_text:
    name: phenotype_source_text
    definition_uri: include:phenotype_source_text
    description: Phenotype as described by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype_source_text
    owner: Participant
    range: string
  phenotype_interpretation:
    name: phenotype_interpretation
    definition_uri: include:phenotype_interpretation
    description: Whether phenotype was observed or not
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype_interpretation
    owner: Participant
    range: enum_phenotype_interpretation
  race:
    name: race
    definition_uri: include:race
    description: Race of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: race
    owner: Participant
    range: enum_race
  sex:
    name: sex
    definition_uri: include:sex
    description: Sex of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sex
    owner: Participant
    range: enum_sex

```
</details>