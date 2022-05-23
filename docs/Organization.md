# Class: Organization
_An organization such as a company or university_





URI: [schema:Organization](http://schema.org/Organization)




## Inheritance

* [NamedThing](NamedThing.md)
    * **Organization** [ HasAliases]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [mission_statement](mission_statement.md) | [string](string.md) | 0..1 | None  | . |
| [founding_date](founding_date.md) | [string](string.md) | 0..1 | None  | . |
| [aliases](aliases.md) | [string](string.md) | 0..* | None  | . |
| [id](id.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [string](string.md) | 0..1 | None  | . |
| [description](description.md) | [string](string.md) | 0..1 | None  | . |
| [image](image.md) | [string](string.md) | 0..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Registry](Registry.md) | [organizations](organizations.md) | range | Organization |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organization
description: An organization such as a company or university
from_schema: https://w3id.org/my_org/my_datamodel
is_a: NamedThing
mixins:
- HasAliases
slots:
- mission_statement
- founding_date
class_uri: schema:Organization

```
</details>

### Induced

<details>
```yaml
name: Organization
description: An organization such as a company or university
from_schema: https://w3id.org/my_org/my_datamodel
is_a: NamedThing
mixins:
- HasAliases
attributes:
  mission_statement:
    name: mission_statement
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: mission_statement
    owner: Organization
    range: string
  founding_date:
    name: founding_date
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: founding_date
    owner: Organization
    range: string
  aliases:
    name: aliases
    exact_mappings:
    - schema:alternateName
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    alias: aliases
    owner: Organization
    range: string
  id:
    name: id
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Organization
    range: string
  name:
    name: name
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:name
    alias: name
    owner: Organization
    range: string
  description:
    name: description
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:description
    alias: description
    owner: Organization
    range: string
  image:
    name: image
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:image
    alias: image
    owner: Organization
    range: string
class_uri: schema:Organization

```
</details>