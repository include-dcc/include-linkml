
# Class: DataFile


A DataFile Associated with a Participant or Study or Biospecimen

URI: [include:DataFile](https://w3id.org/include/DataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Participant],[Study]<has_study%200..1-++[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:enum_data_access%20%3F;data_category:string;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string%20%3F;file_name:string;format:string;participant_id:string;size:string%20%3F;original_file_name:string],[Participant]<has_participant%200..1-++[DataFile],[Biospecimen]<has_biospecimen%200..1-++[DataFile],[Biospecimen]++-%20has_datafile%200..1>[DataFile],[Participant]++-%20has_datafile%200..1>[DataFile],[Assay]++-%20has_output%200..1>[DataFile],[Thing]^-[DataFile],[Biospecimen],[Assay])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study],[Participant],[Study]<has_study%200..1-++[DataFile&#124;access_url:string%20%3F;collection_id:string%20%3F;data_access:enum_data_access%20%3F;data_category:string;data_type:string%20%3F;experimental_strategy:string%20%3F;file_id:string%20%3F;file_name:string;format:string;participant_id:string;size:string%20%3F;original_file_name:string],[Participant]<has_participant%200..1-++[DataFile],[Biospecimen]<has_biospecimen%200..1-++[DataFile],[Biospecimen]++-%20has_datafile%200..1>[DataFile],[Participant]++-%20has_datafile%200..1>[DataFile],[Assay]++-%20has_output%200..1>[DataFile],[Thing]^-[DataFile],[Biospecimen],[Assay])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[has_datafile](has_datafile.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**
 *  **None** *[has_output](has_output.md)*  <sub>0..1</sub>  **[DataFile](DataFile.md)**

## Attributes


### Own

 * [access_url](access_url.md)  <sub>0..1</sub>
     * Description: Storage location for this file
     * Range: [String](types/String.md)
 * [collection_id](collection_id.md)  <sub>0..1</sub>
     * Description: Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples. This may be the same as Parent Sample ID or Sample ID (if no processing was performed).
     * Range: [String](types/String.md)
 * [data_access](data_access.md)  <sub>0..1</sub>
     * Description: Type of access control on this file, determined by DCC
     * Range: [enum_data_access](enum_data_access.md)
 * [data_category](data_category.md)  <sub>1..1</sub>
     * Description: General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune maps, Transcriptomics, etc.)
     * Range: [String](types/String.md)
 * [data_type](data_type.md)  <sub>0..1</sub>
     * Description: Specific type of data contained in file (e.g. Aligned reads, Unaligned reads, SNV, CNV, Gene fusions, Isoform expression, Gene expression quantification, Structural variations, Cytokine profiles, Operation reports, Pathology reports, Histology images, Clinical supplement, Protein expression quantification, etc.)
     * Range: [String](types/String.md)
 * [experimental_strategy](experimental_strategy.md)  <sub>0..1</sub>
     * Description: Experimental method used to obtain data in file (e.g. WGS, RNAseq, WXS, SOMAscan, Mass spec proteomics, LCMS metabolomics, Multiplex immunoassay, Meso Scale Discovery, etc.)
     * Range: [String](types/String.md)
 * [file_id](file_id.md)  <sub>0..1</sub>
     * Description: File identifier, assigned by DCC
     * Range: [String](types/String.md)
 * [file_name](file_name.md)  <sub>1..1</sub>
     * Description: Synapse ID for file
     * Range: [String](types/String.md)
 * [format](format.md)  <sub>1..1</sub>
     * Description: Format of file (e.g. bam, cram, vcf, csv, html, png, fastq, pdf, dicom, etc.)
     * Range: [String](types/String.md)
 * [has_biospecimen](has_biospecimen.md)  <sub>0..1</sub>
     * Description: Link to a Biospecimen
     * Range: [Biospecimen](Biospecimen.md)
 * [has_participant](has_participant.md)  <sub>0..1</sub>
     * Description: Link to a Participant
     * Range: [Participant](Participant.md)
 * [has_study](has_study.md)  <sub>0..1</sub>
     * Description: Link to a Study
     * Range: [Study](Study.md)
 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for the participant, assigned by DCC
     * Range: [String](types/String.md)
 * [size](size.md)  <sub>0..1</sub>
     * Description: Size of file
     * Range: [String](types/String.md)
 * [original_file_name](original_file_name.md)  <sub>1..1</sub>
     * Description: Name of file, assigned by data contributor
     * Range: [String](types/String.md)
