
# Class: Condition




URI: [include:Condition](https://w3id.org/include/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Participant],[Participant]<has_participant%200..1-++[Condition&#124;age_at_condition_observation:string%20%3F;mondo_label:string%20%3F;mondo_code:string%20%3F;condition_interpretation:enum_condition_interpretation%20%3F;condition_data_source:enum_condition_data_source%20%3F;hpo_label:string%20%3F;hpo_code:string%20%3F;maxo_label:string%20%3F;maxo_code:string%20%3F;other_label:string%20%3F;other_code:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Participant],[Participant]<has_participant%200..1-++[Condition&#124;age_at_condition_observation:string%20%3F;mondo_label:string%20%3F;mondo_code:string%20%3F;condition_interpretation:enum_condition_interpretation%20%3F;condition_data_source:enum_condition_data_source%20%3F;hpo_label:string%20%3F;hpo_code:string%20%3F;maxo_label:string%20%3F;maxo_code:string%20%3F;other_label:string%20%3F;other_code:string%20%3F])

## Attributes


### Own

 * [has_participant](has_participant.md)  <sub>0..1</sub>
     * Description: Link to a Participant
     * Range: [Participant](Participant.md)
 * [age_at_condition_observation](age_at_condition_observation.md)  <sub>0..1</sub>
     * Description: Age in days at which condition was observed, recorded, or diagnosed
     * Range: [String](types/String.md)
 * [mondo_label](mondo_label.md)  <sub>0..1</sub>
     * Description: Label for condition in the Mondo Disease Ontology (MONDO)
     * Range: [String](types/String.md)
 * [mondo_code](mondo_code.md)  <sub>0..1</sub>
     * Description: Code for condition in the Mondo Disease Ontology (MONDO)
     * Range: [String](types/String.md)
 * [condition_interpretation](condition_interpretation.md)  <sub>0..1</sub>
     * Description: Whether condition was observed or not. "Not Observed" indicates participant was specifically examined for that condition, or health record specifically queried for that condition, and found to be negative. Sept. 2022 release will only include positive assertions.
     * Range: [enum_condition_interpretation](enum_condition_interpretation.md)
 * [condition_data_source](condition_data_source.md)  <sub>0..1</sub>
     * Description: Whether condition information was obtained from medical records (Clinical) or patient survey (Self-Reported)
     * Range: [enum_condition_data_source](enum_condition_data_source.md)
 * [hpo_label](hpo_label.md)  <sub>0..1</sub>
     * Description: Label for condition in the Human Phenotype Ontology (HPO)
     * Range: [String](types/String.md)
 * [hpo_code](hpo_code.md)  <sub>0..1</sub>
     * Description: Code for condition in the Human Phenotype Ontology (HPO)
     * Range: [String](types/String.md)
 * [maxo_label](maxo_label.md)  <sub>0..1</sub>
     * Description: Label for condition in the Medical Action Ontology (MAXO)
     * Range: [String](types/String.md)
 * [maxo_code](maxo_code.md)  <sub>0..1</sub>
     * Description: Code for condition in the Medical Action Ontology (MAXO)
     * Range: [String](types/String.md)
 * [other_label](other_label.md)  <sub>0..1</sub>
     * Description: Label for condition in another ontology (if no match in HPO, MONDO, or MAXO)
     * Range: [String](types/String.md)
 * [other_code](other_code.md)  <sub>0..1</sub>
     * Description: Code for condition in another ontology (if no match in HPO, MONDO, or MAXO)
     * Range: [String](types/String.md)
