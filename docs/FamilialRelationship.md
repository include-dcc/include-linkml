# Class: FamilialRelationship




URI: [my_datamodel:FamilialRelationship](https://w3id.org/my_org/my_datamodelFamilialRelationship)




## Inheritance

* [Relationship](Relationship.md)
    * **FamilialRelationship**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [started_at_time](started_at_time.md) | [date](date.md) | 0..1 | None  | . |
| [ended_at_time](ended_at_time.md) | [date](date.md) | 0..1 | None  | . |
| [related_to](related_to.md) | [string](string.md) | 0..1 | None  | . |
| [type](type.md) | [FamilialRelationshipType](FamilialRelationshipType.md) | 1..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [has_familial_relationships](has_familial_relationships.md) | range | FamilialRelationship |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FamilialRelationship
from_schema: https://w3id.org/my_org/my_datamodel
is_a: Relationship
slot_usage:
  type:
    name: type
    range: FamilialRelationshipType
    required: true
  related to:
    name: related to
    range: Person
    required: true

```
</details>

### Induced

<details>
```yaml
name: FamilialRelationship
from_schema: https://w3id.org/my_org/my_datamodel
is_a: Relationship
slot_usage:
  type:
    name: type
    range: FamilialRelationshipType
    required: true
  related to:
    name: related to
    range: Person
    required: true
attributes:
  started_at_time:
    name: started_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: prov:startedAtTime
    alias: started_at_time
    owner: FamilialRelationship
    range: date
  ended_at_time:
    name: ended_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: prov:endedAtTime
    alias: ended_at_time
    owner: FamilialRelationship
    range: date
  related_to:
    name: related_to
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: related_to
    owner: FamilialRelationship
    range: string
  type:
    name: type
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: type
    owner: FamilialRelationship
    range: FamilialRelationshipType
    required: true

```
</details>