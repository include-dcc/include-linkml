
# Class: subject




URI: [include_schema:Subject](https://w3id.org/mixs/include_schema/Subject)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Visit],[Sample]-%20subject%201..1>[Subject&#124;first_name:string%20%3F;middle_name:string%20%3F;last_name:string%20%3F;dob:date%20%3F;birth_month:integer%20%3F;birth_year:integer%20%3F;birth_city:string%20%3F;birth_country:string%20%3F;sex:gender_enum%20%3F;race:race_enum%20%3F;ethnicity:ethnicity_enum%20%3F;handedness:handedness_enum%20%3F;primary_language:language_enum%20%3F;other_language:language_enum%20%3F;residence:residence_enum%20%3F;age_of_mother_at_birth:integer%20%3F;age_of_father_at_birth:integer%20%3F;id(i):string],[Sample]-%20subject(i)%200..1>[Subject],[Visit]-%20subject(i)%200..1>[Subject],[Visit]-%20subject%201..1>[Subject],[Person]^-[Subject],[Sample],[Person])](https://yuml.me/diagram/nofunky;dir:TB/class/[Visit],[Sample]-%20subject%201..1>[Subject&#124;first_name:string%20%3F;middle_name:string%20%3F;last_name:string%20%3F;dob:date%20%3F;birth_month:integer%20%3F;birth_year:integer%20%3F;birth_city:string%20%3F;birth_country:string%20%3F;sex:gender_enum%20%3F;race:race_enum%20%3F;ethnicity:ethnicity_enum%20%3F;handedness:handedness_enum%20%3F;primary_language:language_enum%20%3F;other_language:language_enum%20%3F;residence:residence_enum%20%3F;age_of_mother_at_birth:integer%20%3F;age_of_father_at_birth:integer%20%3F;id(i):string],[Sample]-%20subject(i)%200..1>[Subject],[Visit]-%20subject(i)%200..1>[Subject],[Visit]-%20subject%201..1>[Subject],[Person]^-[Subject],[Sample],[Person])

## Parents

 *  is_a: [Person](Person.md)

## Children


## Referenced by Class

 *  **[Sample](Sample.md)** *[sample➞subject](sample_subject.md)*  <sub>1..1</sub>  **[Subject](Subject.md)**
 *  **None** *[subject](subject.md)*  <sub>0..1</sub>  **[Subject](Subject.md)**
 *  **[Visit](Visit.md)** *[visit➞subject](visit_subject.md)*  <sub>1..1</sub>  **[Subject](Subject.md)**

## Attributes


### Own

 * [first name](first_name.md)  <sub>0..1</sub>
     * Description: The first name of a person
     * Range: [String](types/String.md)
 * [middle name](middle_name.md)  <sub>0..1</sub>
     * Description: The middle name of a person
     * Range: [String](types/String.md)
 * [last name](last_name.md)  <sub>0..1</sub>
     * Description: The last name of a person
     * Range: [String](types/String.md)
 * [dob](dob.md)  <sub>0..1</sub>
     * Description: The date of a person's birth
     * Range: [Date](types/Date.md)
 * [birth month](birth_month.md)  <sub>0..1</sub>
     * Description: The month of a person's birth
     * Range: [Integer](types/Integer.md)
 * [birth year](birth_year.md)  <sub>0..1</sub>
     * Description: The year of a person's birth
     * Range: [Integer](types/Integer.md)
 * [birth city](birth_city.md)  <sub>0..1</sub>
     * Description: The city in which a person was born
     * Range: [String](types/String.md)
 * [birth country](birth_country.md)  <sub>0..1</sub>
     * Description: The country in which a person was born
     * Range: [String](types/String.md)
 * [sex](sex.md)  <sub>0..1</sub>
     * Description: Person gender
     * Range: [gender_enum](gender_enum.md)
 * [race](race.md)  <sub>0..1</sub>
     * Description: Person race
     * Range: [race_enum](race_enum.md)
 * [ethnicity](ethnicity.md)  <sub>0..1</sub>
     * Description: Person ethnicity
     * Range: [ethnicity_enum](ethnicity_enum.md)
 * [handedness](handedness.md)  <sub>0..1</sub>
     * Description: Side of dominant hand of a person
     * Range: [handedness_enum](handedness_enum.md)
 * [primary language](primary_language.md)  <sub>0..1</sub>
     * Description: A person's first language or the language spoken at home
     * Range: [language_enum](language_enum.md)
 * [other language](other_language.md)  <sub>0..1</sub>
     * Description: Any language a person speaks with fluency
     * Range: [language_enum](language_enum.md)
 * [residence](residence.md)  <sub>0..1</sub>
     * Description: A person's living arrangements
     * Range: [residence_enum](residence_enum.md)
 * [age of mother at birth](age_of_mother_at_birth.md)  <sub>0..1</sub>
     * Description: The age of the mother when the subject was born
     * Range: [Integer](types/Integer.md)
 * [age of father at birth](age_of_father_at_birth.md)  <sub>0..1</sub>
     * Description: The age of the father when the subject was born
     * Range: [Integer](types/Integer.md)

### Inherited from person:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
