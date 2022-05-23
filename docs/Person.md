# Class: Person
_A person (alive, dead, undead, or fictional)._





URI: [schema:Person](http://schema.org/Person)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Person** [ HasAliases]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [primary_email](primary_email.md) | [string](string.md) | 0..1 | None  | . |
| [birth_date](birth_date.md) | [string](string.md) | 0..1 | None  | . |
| [age_in_years](age_in_years.md) | [integer](integer.md) | 0..1 | None  | . |
| [current_address](current_address.md) | [Address](Address.md) | 0..1 | The address at which a person currently lives  | . |
| [has_familial_relationships](has_familial_relationships.md) | [FamilialRelationship](FamilialRelationship.md) | 0..* | None  | . |
| [aliases](aliases.md) | [string](string.md) | 0..* | None  | . |
| [id](id.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [string](string.md) | 0..1 | None  | . |
| [description](description.md) | [string](string.md) | 0..1 | None  | . |
| [image](image.md) | [string](string.md) | 0..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Registry](Registry.md) | [persons](persons.md) | range | Person |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
description: A person (alive, dead, undead, or fictional).
from_schema: https://w3id.org/my_org/my_datamodel
is_a: NamedThing
mixins:
- HasAliases
slots:
- primary_email
- birth_date
- age_in_years
- current_address
- has_familial_relationships
slot_usage:
  primary_email:
    name: primary_email
    pattern: ^\S+@[\S+\.]+\S+
class_uri: schema:Person

```
</details>

### Induced

<details>
```yaml
name: Person
description: A person (alive, dead, undead, or fictional).
from_schema: https://w3id.org/my_org/my_datamodel
is_a: NamedThing
mixins:
- HasAliases
slot_usage:
  primary_email:
    name: primary_email
    pattern: ^\S+@[\S+\.]+\S+
attributes:
  primary_email:
    name: primary_email
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:email
    alias: primary_email
    owner: Person
    range: string
    pattern: ^\S+@[\S+\.]+\S+
  birth_date:
    name: birth_date
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:birthDate
    alias: birth_date
    owner: Person
    range: string
  age_in_years:
    name: age_in_years
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: age_in_years
    owner: Person
    range: integer
    minimum_value: 0
    maximum_value: 999
  current_address:
    name: current_address
    description: The address at which a person currently lives
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: current_address
    owner: Person
    range: Address
  has_familial_relationships:
    name: has_familial_relationships
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    inlined: true
    inlined_as_list: true
    alias: has_familial_relationships
    owner: Person
    range: FamilialRelationship
  aliases:
    name: aliases
    exact_mappings:
    - schema:alternateName
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    alias: aliases
    owner: Person
    range: string
  id:
    name: id
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Person
    range: string
  name:
    name: name
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:name
    alias: name
    owner: Person
    range: string
  description:
    name: description
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:description
    alias: description
    owner: Person
    range: string
  image:
    name: image
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:image
    alias: image
    owner: Person
    range: string
class_uri: schema:Person

```
</details>