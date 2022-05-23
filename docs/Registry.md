# Class: Registry
_Top level data container_





URI: [my_datamodel:Registry](https://w3id.org/my_org/my_datamodelRegistry)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [persons](persons.md) | [Person](Person.md) | 0..* | None  | . |
| [organizations](organizations.md) | [Organization](Organization.md) | 0..* | None  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Registry
description: Top level data container
from_schema: https://w3id.org/my_org/my_datamodel
attributes:
  persons:
    name: persons
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    inlined: true
    inlined_as_list: true
    range: Person
  organizations:
    name: organizations
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    inlined: true
    inlined_as_list: true
    range: Organization
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Registry
description: Top level data container
from_schema: https://w3id.org/my_org/my_datamodel
attributes:
  persons:
    name: persons
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    inlined: true
    inlined_as_list: true
    alias: persons
    owner: Registry
    range: Person
  organizations:
    name: organizations
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    inlined: true
    inlined_as_list: true
    alias: organizations
    owner: Registry
    range: Organization
tree_root: true

```
</details>