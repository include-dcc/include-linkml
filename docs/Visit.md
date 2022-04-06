
# Class: visit




URI: [include_schema:Visit](https://w3id.org/mixs/include_schema/Visit)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subject%201..1-%20[Visit&#124;sample:string%20*;visit_date:date%20%3F;id(i):string],[NamedThing]^-[Visit],[Subject],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]<subject%201..1-%20[Visit&#124;sample:string%20*;visit_date:date%20%3F;id(i):string],[NamedThing]^-[Visit],[Subject],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - root class

## Referenced by Class


## Attributes


### Own

 * [visit➞subject](visit_subject.md)  <sub>1..1</sub>
     * Description: A person
     * Range: [Subject](Subject.md)
 * [sample](sample.md)  <sub>0..\*</sub>
     * Description: Material collected from the subject
     * Range: [String](types/String.md)
 * [visit date](visit_date.md)  <sub>0..1</sub>
     * Description: Date on which a visit occurred
     * Range: [Date](types/Date.md)

### Inherited from named thing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
