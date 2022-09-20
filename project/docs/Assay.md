
# Class: Assay


An assay

URI: [include:Assay](https://w3id.org/include/Assay)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[DataFile],[Biospecimen],[DataFile]<has_output%200..1-++[Assay],[Biospecimen]<uses_biospecimen%200..1-++[Assay],[Thing]^-[Assay])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[DataFile],[Biospecimen],[DataFile]<has_output%200..1-++[Assay],[Biospecimen]<uses_biospecimen%200..1-++[Assay],[Thing]^-[Assay])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [uses_biospecimen](uses_biospecimen.md)  <sub>0..1</sub>
     * Description: The Biospecimen an Assay is performed on
     * Range: [Biospecimen](Biospecimen.md)
 * [has_output](has_output.md)  <sub>0..1</sub>
     * Description: The DataFile Output of an Assay
     * Range: [DataFile](DataFile.md)
