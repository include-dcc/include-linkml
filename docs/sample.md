
# Class: sample




URI: [include_schema:Sample](https://w3id.org/mixs/include_schema/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject],[Sample]<parent%20sample%200..1-%20[Sample&#124;sample_date:date%20%3F;sample_type:sample_enum%20%3F;id(i):string],[Subject]<subject%201..1-%20[Sample],[NamedThing]^-[Sample],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject],[Sample]<parent%20sample%200..1-%20[Sample&#124;sample_date:date%20%3F;sample_type:sample_enum%20%3F;id(i):string],[Subject]<subject%201..1-%20[Sample],[NamedThing]^-[Sample],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - root class

## Referenced by Class

 *  **None** *[parent sample](parent_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [sample➞subject](sample_subject.md)  <sub>1..1</sub>
     * Description: A person
     * Range: [Subject](Subject.md)
 * [sample date](sample_date.md)  <sub>0..1</sub>
     * Description: Date on which a sample was collected
     * Range: [Date](types/Date.md)
 * [parent sample](parent_sample.md)  <sub>0..1</sub>
     * Description: Sample from which another sample was derived
     * Range: [Sample](Sample.md)
 * [sample type](sample_type.md)  <sub>0..1</sub>
     * Description: Type of sample
     * Range: [sample_enum](sample_enum.md)

### Inherited from named thing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
