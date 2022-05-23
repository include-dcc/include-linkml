# Class: Relationship




URI: [my_datamodel:Relationship](https://w3id.org/my_org/my_datamodelRelationship)




## Inheritance

* **Relationship**
    * [FamilialRelationship](FamilialRelationship.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [started_at_time](started_at_time.md) | [date](date.md) | 0..1 | None  | . |
| [ended_at_time](ended_at_time.md) | [date](date.md) | 0..1 | None  | . |
| [related_to](related_to.md) | [string](string.md) | 0..1 | None  | . |
| [type](type.md) | [string](string.md) | 0..1 | None  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relationship
from_schema: https://w3id.org/my_org/my_datamodel
slots:
- started_at_time
- ended_at_time
- related_to
- type

```
</details>

### Induced

<details>
```yaml
name: Relationship
from_schema: https://w3id.org/my_org/my_datamodel
attributes:
  started_at_time:
    name: started_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: prov:startedAtTime
    alias: started_at_time
    owner: Relationship
    range: date
  ended_at_time:
    name: ended_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: prov:endedAtTime
    alias: ended_at_time
    owner: Relationship
    range: date
  related_to:
    name: related_to
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: related_to
    owner: Relationship
    range: string
  type:
    name: type
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: type
    owner: Relationship
    range: string

```
</details>