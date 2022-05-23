# Class: Participant




URI: [include:Participant](https://w3id.org/include/Participant)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Participant**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [age_at_diagnosis__days](age_at_diagnosis__days.md) | [integer](integer.md) | 0..1 | Age in days at which phenotype was assigned (or onset??)  | . |
| [age_at_phenotype_assignment__days](age_at_phenotype_assignment__days.md) | [integer](integer.md) | 0..1 | Age in days at which phenotype was recorded (or onset??)  | . |
| [age_at_the_last_vital_status__days](age_at_the_last_vital_status__days.md) | [integer](integer.md) | 0..1 | Age in days when participant's vital status was last recorded (or actual death date??)  | . |
| [diagnosis__icd](diagnosis__icd.md) | [string](string.md) | 0..1 | ICD-10 code (annotated by data contributor or DCC)  | . |
| [diagnosis__mondo](diagnosis__mondo.md) | [string](string.md) | 0..1 | Mondo disease ontology code (annotated by data contributor or DCC)  | . |
| [diagnosis__ncit](diagnosis__ncit.md) | [string](string.md) | 0..1 | NCI Thesaurus code (annotated by data contributor or DCC)  | . |
| [diagnosis__source_text](diagnosis__source_text.md) | [string](string.md) | 0..1 | Diagnosis as described by data contributor  | . |
| [diagnosis_type](diagnosis_type.md) | [string](string.md) | 0..1 | How diagnosis was assigned ??  | . |
| [down_syndrome_status](down_syndrome_status.md) | [EnumDownSyndromeStatus](EnumDownSyndromeStatus.md) | 1..1 | Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy 21, euploid)  | . |
| [ethnicity](ethnicity.md) | [EnumEthnicity](EnumEthnicity.md) | 1..1 | Ethnicity of participant  | . |
| [external_id](external_id.md) | [string](string.md) | 1..1 | Unique identifier for the participant, assigned by data contributor  | . |
| [family_id](family_id.md) | [string](string.md) | 0..1 | Unique identifer for family to which Participant belongs  | . |
| [family_relationship](family_relationship.md) | [string](string.md) | 0..1 | Relationship of Participant to other family members  | . |
| [family_type](family_type.md) | [EnumFamilyType](EnumFamilyType.md) | 0..1 | Structure of family members participating in the study (proband-only = no family members participating; duo = proband + parent; trio = proband + 2 parents; trio+ = proband + 2 parents + other relatives)  | . |
| [father_id](father_id.md) | [string](string.md) | 0..1 | Participant ID for Participant's father  | . |
| [has_datafile](has_datafile.md) | [DataFile](DataFile.md) | 0..1 | Semantic link to a DataFile  | . |
| [has_study](has_study.md) | [Study](Study.md) | 0..1 | Semantic link to a Study  | . |
| [mother_id](mother_id.md) | [string](string.md) | 0..1 | Participant ID for Participant's mother  | . |
| [outcomes_vital_status](outcomes_vital_status.md) | [string](string.md) | 0..1 | Whether participant is alive or dead [need valid values]  | . |
| [participant_id](participant_id.md) | [string](string.md) | 1..1 | Unique identifier for the participant, assigned by DCC  | . |
| [phenotype__hpo](phenotype__hpo.md) | [string](string.md) | 0..1 | Human Phenotype Ontology code (annotated by data contributor or DCC)  | . |
| [phenotype__source_text](phenotype__source_text.md) | [string](string.md) | 0..1 | Phenotype as described by data contributor  | . |
| [phenotype_interpretation](phenotype_interpretation.md) | [EnumPhenotypeInterpretation](EnumPhenotypeInterpretation.md) | 0..1 | Whether phenotype was observed or not  | . |
| [race](race.md) | [EnumRace](EnumRace.md) | 1..1 | Race of participant  | . |
| [sex](sex.md) | [EnumSex](EnumSex.md) | 1..1 | Sex of participant  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Biospecimen](Biospecimen.md) | [has_participant](has_participant.md) | range | Participant |
| [DataFile](DataFile.md) | [has_participant](has_participant.md) | range | Participant |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Participant
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slots:
- age_at_diagnosis__days
- age_at_phenotype_assignment__days
- age_at_the_last_vital_status__days
- diagnosis__icd
- diagnosis__mondo
- diagnosis__ncit
- diagnosis__source_text
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
- phenotype__hpo
- phenotype__source_text
- phenotype_interpretation
- race
- sex
slot_usage:
  age_at_diagnosis__days:
    name: age_at_diagnosis__days
    description: Age in days at which phenotype was assigned (or onset??)
    range: integer
  age_at_phenotype_assignment__days:
    name: age_at_phenotype_assignment__days
    description: Age in days at which phenotype was recorded (or onset??)
    range: integer
  age_at_the_last_vital_status__days:
    name: age_at_the_last_vital_status__days
    description: Age in days when participant's vital status was last recorded (or
      actual death date??)
    range: integer
  diagnosis__icd:
    name: diagnosis__icd
    description: ICD-10 code (annotated by data contributor or DCC)
  diagnosis__mondo:
    name: diagnosis__mondo
    description: Mondo disease ontology code (annotated by data contributor or DCC)
  diagnosis__ncit:
    name: diagnosis__ncit
    description: NCI Thesaurus code (annotated by data contributor or DCC)
  diagnosis__source_text:
    name: diagnosis__source_text
    description: Diagnosis as described by data contributor
  diagnosis_type:
    name: diagnosis_type
    description: How diagnosis was assigned ??
  down_syndrome_status:
    name: down_syndrome_status
    description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy
      21, euploid)
    range: enum_down_syndrome_status
    required: true
  ethnicity:
    name: ethnicity
    description: Ethnicity of participant
    range: enum_ethnicity
    required: true
  external_id:
    name: external_id
    description: Unique identifier for the participant, assigned by data contributor
    required: true
  family_id:
    name: family_id
    description: Unique identifer for family to which Participant belongs
  family_relationship:
    name: family_relationship
    description: Relationship of Participant to other family members
  family_type:
    name: family_type
    description: Structure of family members participating in the study (proband-only
      = no family members participating; duo = proband + parent; trio = proband +
      2 parents; trio+ = proband + 2 parents + other relatives)
    range: enum_family_type
  father_id:
    name: father_id
    description: Participant ID for Participant's father
  has_datafile:
    name: has_datafile
    range: DataFile
  has_study:
    name: has_study
    range: Study
  mother_id:
    name: mother_id
    description: Participant ID for Participant's mother
  outcomes_vital_status:
    name: outcomes_vital_status
    description: Whether participant is alive or dead [need valid values]
  participant_id:
    name: participant_id
    description: Unique identifier for the participant, assigned by DCC
    identifier: true
    required: true
  phenotype__hpo:
    name: phenotype__hpo
    description: Human Phenotype Ontology code (annotated by data contributor or DCC)
  phenotype__source_text:
    name: phenotype__source_text
    description: Phenotype as described by data contributor
  phenotype_interpretation:
    name: phenotype_interpretation
    description: Whether phenotype was observed or not
    range: enum_phenotype_interpretation
  race:
    name: race
    description: Race of participant
    range: enum_race
    required: true
  sex:
    name: sex
    description: Sex of participant
    range: enum_sex
    required: true

```
</details>

### Induced

<details>
```yaml
name: Participant
from_schema: https://w3id.org/include_portal_v1_schema
is_a: NamedThing
slot_usage:
  age_at_diagnosis__days:
    name: age_at_diagnosis__days
    description: Age in days at which phenotype was assigned (or onset??)
    range: integer
  age_at_phenotype_assignment__days:
    name: age_at_phenotype_assignment__days
    description: Age in days at which phenotype was recorded (or onset??)
    range: integer
  age_at_the_last_vital_status__days:
    name: age_at_the_last_vital_status__days
    description: Age in days when participant's vital status was last recorded (or
      actual death date??)
    range: integer
  diagnosis__icd:
    name: diagnosis__icd
    description: ICD-10 code (annotated by data contributor or DCC)
  diagnosis__mondo:
    name: diagnosis__mondo
    description: Mondo disease ontology code (annotated by data contributor or DCC)
  diagnosis__ncit:
    name: diagnosis__ncit
    description: NCI Thesaurus code (annotated by data contributor or DCC)
  diagnosis__source_text:
    name: diagnosis__source_text
    description: Diagnosis as described by data contributor
  diagnosis_type:
    name: diagnosis_type
    description: How diagnosis was assigned ??
  down_syndrome_status:
    name: down_syndrome_status
    description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy
      21, euploid)
    range: enum_down_syndrome_status
    required: true
  ethnicity:
    name: ethnicity
    description: Ethnicity of participant
    range: enum_ethnicity
    required: true
  external_id:
    name: external_id
    description: Unique identifier for the participant, assigned by data contributor
    required: true
  family_id:
    name: family_id
    description: Unique identifer for family to which Participant belongs
  family_relationship:
    name: family_relationship
    description: Relationship of Participant to other family members
  family_type:
    name: family_type
    description: Structure of family members participating in the study (proband-only
      = no family members participating; duo = proband + parent; trio = proband +
      2 parents; trio+ = proband + 2 parents + other relatives)
    range: enum_family_type
  father_id:
    name: father_id
    description: Participant ID for Participant's father
  has_datafile:
    name: has_datafile
    range: DataFile
  has_study:
    name: has_study
    range: Study
  mother_id:
    name: mother_id
    description: Participant ID for Participant's mother
  outcomes_vital_status:
    name: outcomes_vital_status
    description: Whether participant is alive or dead [need valid values]
  participant_id:
    name: participant_id
    description: Unique identifier for the participant, assigned by DCC
    identifier: true
    required: true
  phenotype__hpo:
    name: phenotype__hpo
    description: Human Phenotype Ontology code (annotated by data contributor or DCC)
  phenotype__source_text:
    name: phenotype__source_text
    description: Phenotype as described by data contributor
  phenotype_interpretation:
    name: phenotype_interpretation
    description: Whether phenotype was observed or not
    range: enum_phenotype_interpretation
  race:
    name: race
    description: Race of participant
    range: enum_race
    required: true
  sex:
    name: sex
    description: Sex of participant
    range: enum_sex
    required: true
attributes:
  age_at_diagnosis__days:
    name: age_at_diagnosis__days
    description: Age in days at which phenotype was assigned (or onset??)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_diagnosis__days
    owner: Participant
    range: integer
  age_at_phenotype_assignment__days:
    name: age_at_phenotype_assignment__days
    description: Age in days at which phenotype was recorded (or onset??)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_phenotype_assignment__days
    owner: Participant
    range: integer
  age_at_the_last_vital_status__days:
    name: age_at_the_last_vital_status__days
    description: Age in days when participant's vital status was last recorded (or
      actual death date??)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: age_at_the_last_vital_status__days
    owner: Participant
    range: integer
  diagnosis__icd:
    name: diagnosis__icd
    description: ICD-10 code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis__icd
    owner: Participant
    range: string
  diagnosis__mondo:
    name: diagnosis__mondo
    description: Mondo disease ontology code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis__mondo
    owner: Participant
    range: string
  diagnosis__ncit:
    name: diagnosis__ncit
    description: NCI Thesaurus code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis__ncit
    owner: Participant
    range: string
  diagnosis__source_text:
    name: diagnosis__source_text
    description: Diagnosis as described by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis__source_text
    owner: Participant
    range: string
  diagnosis_type:
    name: diagnosis_type
    description: How diagnosis was assigned ??
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: diagnosis_type
    owner: Participant
    range: string
  down_syndrome_status:
    name: down_syndrome_status
    description: Down Syndrome status of participant (T21 = Trisomy 21; D21 = Disomy
      21, euploid)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: down_syndrome_status
    owner: Participant
    range: enum_down_syndrome_status
    required: true
  ethnicity:
    name: ethnicity
    description: Ethnicity of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: ethnicity
    owner: Participant
    range: enum_ethnicity
    required: true
  external_id:
    name: external_id
    description: Unique identifier for the participant, assigned by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: external_id
    owner: Participant
    range: string
    required: true
  family_id:
    name: family_id
    description: Unique identifer for family to which Participant belongs
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_id
    owner: Participant
    range: string
  family_relationship:
    name: family_relationship
    description: Relationship of Participant to other family members
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_relationship
    owner: Participant
    range: string
  family_type:
    name: family_type
    description: Structure of family members participating in the study (proband-only
      = no family members participating; duo = proband + parent; trio = proband +
      2 parents; trio+ = proband + 2 parents + other relatives)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: family_type
    owner: Participant
    range: enum_family_type
  father_id:
    name: father_id
    description: Participant ID for Participant's father
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: father_id
    owner: Participant
    range: string
  has_datafile:
    name: has_datafile
    description: Semantic link to a DataFile
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_datafile
    owner: Participant
    range: DataFile
  has_study:
    name: has_study
    description: Semantic link to a Study
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: has_study
    owner: Participant
    range: Study
  mother_id:
    name: mother_id
    description: Participant ID for Participant's mother
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: mother_id
    owner: Participant
    range: string
  outcomes_vital_status:
    name: outcomes_vital_status
    description: Whether participant is alive or dead [need valid values]
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: outcomes_vital_status
    owner: Participant
    range: string
  participant_id:
    name: participant_id
    description: Unique identifier for the participant, assigned by DCC
    from_schema: https://w3id.org/include_portal_v1_schema
    identifier: true
    alias: participant_id
    owner: Participant
    range: string
    required: true
  phenotype__hpo:
    name: phenotype__hpo
    description: Human Phenotype Ontology code (annotated by data contributor or DCC)
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype__hpo
    owner: Participant
    range: string
  phenotype__source_text:
    name: phenotype__source_text
    description: Phenotype as described by data contributor
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype__source_text
    owner: Participant
    range: string
  phenotype_interpretation:
    name: phenotype_interpretation
    description: Whether phenotype was observed or not
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: phenotype_interpretation
    owner: Participant
    range: enum_phenotype_interpretation
  race:
    name: race
    description: Race of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: race
    owner: Participant
    range: enum_race
    required: true
  sex:
    name: sex
    description: Sex of participant
    from_schema: https://w3id.org/include_portal_v1_schema
    alias: sex
    owner: Participant
    range: enum_sex
    required: true

```
</details>