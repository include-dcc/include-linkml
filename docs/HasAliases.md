# Class: HasAliases
_A mixin applied to any class that can have aliases/alternateNames_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [my_datamodel:HasAliases](https://w3id.org/my_org/my_datamodelHasAliases)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [aliases](aliases.md) | [string](string.md) | 0..* | None  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasAliases
description: A mixin applied to any class that can have aliases/alternateNames
from_schema: https://w3id.org/my_org/my_datamodel
mixin: true
attributes:
  aliases:
    name: aliases
    exact_mappings:
    - schema:alternateName
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: HasAliases
description: A mixin applied to any class that can have aliases/alternateNames
from_schema: https://w3id.org/my_org/my_datamodel
mixin: true
attributes:
  aliases:
    name: aliases
    exact_mappings:
    - schema:alternateName
    from_schema: https://w3id.org/my_org/my_datamodel
    multivalued: true
    alias: aliases
    owner: HasAliases
    range: string

```
</details>