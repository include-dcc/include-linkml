# Class: Address




URI: [schema:PostalAddress](http://schema.org/PostalAddress)



<!-- no inheritance hierarchy -->



## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [street](street.md) | [string](string.md) | 0..1 | None  | . |
| [city](city.md) | [string](string.md) | 0..1 | None  | . |
| [postal_code](postal_code.md) | [string](string.md) | 0..1 | None  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [current_address](current_address.md) | range | Address |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Address
from_schema: https://w3id.org/my_org/my_datamodel
slots:
- street
- city
- postal_code
class_uri: schema:PostalAddress

```
</details>

### Induced

<details>
```yaml
name: Address
from_schema: https://w3id.org/my_org/my_datamodel
attributes:
  street:
    name: street
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: street
    owner: Address
    range: string
  city:
    name: city
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: city
    owner: Address
    range: string
  postal_code:
    name: postal_code
    from_schema: https://w3id.org/my_org/my_datamodel
    alias: postal_code
    owner: Address
    range: string
class_uri: schema:PostalAddress

```
</details>