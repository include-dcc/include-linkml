from __future__ import annotations 
from datetime import (
    datetime,
    date,
    time
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)
metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'include',
     'id': 'https://w3id.org/include',
     'imports': ['linkml:types',
                 'include_core',
                 'include_assay',
                 'include_participant',
                 'include_study'],
     'name': 'include-schema',
     'prefixes': {'include': {'prefix_prefix': 'include',
                              'prefix_reference': 'https://w3id.org/include/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/linkml/include_schema.yaml'} )

class EnumDataAccess(str, Enum):
    Controlled = "controlled"
    Open = "open"
    Registered = "registered"


class EnumAvailability(str, Enum):
    # Sample or Container is potentially available to be requested through the Virtual Biorepository (see VBR contact info in Study page)
    Available = "available"
    # Sample or Container either was available through Virtual Biorepository but has been used up, or is part of a study that is not participating in the VBR
    Unavailable = "unavailable"


class EnumConditionInterpretation(str, Enum):
    # Condition was observed or reported (this will be the case for most conditions)
    Observed = "observed"
    # Participant was specifically examined or medical record queried for condition and found to be negative
    Not_Observed = "not_observed"


class EnumConditionDataSource(str, Enum):
    # Information about condition was obtained from medical records or reported by investigator
    Clinical = "clinical"
    # Information about condition was reported by participant or family member
    Self_reported = "self_reported"


class EnumConditionStatus(str, Enum):
    # Condition is ongoing
    Current = "current"
    # Condition has been resolved
    Resolved = "resolved"
    # This is a general history of the condition, without known dates
    History_Of = "history_of"


class EnumDownSyndromeStatus(str, Enum):
    # Disomy 21 (euploid)
    D21 = "d21"
    # Trisomy 21 (Down syndrome)
    T21 = "t21"


class EnumEthnicity(str, Enum):
    Hispanic_or_Latino = "hispanic_or_latino"
    Not_Hispanic_or_Latino = "not_hispanic_or_latino"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"


class EnumFamilyRelationship(str, Enum):
    # The first affected family member to join the study
    Proband = "proband"
    Father = "father"
    Mother = "mother"
    Sibling = "sibling"
    Other_relative = "other_relative"
    Unrelated_control = "unrelated_control"


class EnumFamilyType(str, Enum):
    # Unrelated control, no Down syndrome family members
    Control_only = "control_only"
    # Proband + one parent
    Duo = "duo"
    # Other family structure, e.g. one parent + twins
    Other = "other"
    # Proband only, no family members participating in study
    Proband_only = "proband_only"
    # Proband + two parents
    Trio = "trio"
    # Proband + two parents + other relatives
    Trio_Plus = "trio_plus"


class EnumRace(str, Enum):
    American_Indian_or_Alaska_Native = "american_indian_or_alaska_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    More_than_one_race = "more_than_one_race"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_other_pacific_islander"
    Other = "other"
    White = "white"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"
    # UK only; do not use for US data
    East_Asian = "east_asian"
    # UK only; do not use for US data
    Latin_American = "latin_american"
    # UK only; do not use for US data
    Middle_Eastern_or_North_African = "middle_eastern_or_north_african"
    # UK only; do not use for US data
    South_Asian = "south_asian"


class EnumSex(str, Enum):
    Female = "female"
    Male = "male"
    Other = "other"
    Unknown = "unknown"


class EnumVitalStatus(str, Enum):
    Dead = "dead"
    Alive = "alive"
    Unknown_or_not_available = "unknown_or_not_available"


class EnumProgram(str, Enum):
    INCLUDE = "include"
    KF = "kf"
    Other = "other"


class EnumStudyCode(str, Enum):
    AADSC = "aadsc"
    ABC_DS = "abc_ds"
    ADS = "ads"
    AECOM_DS = "aecom_ds"
    BEST21 = "best21"
    BrainPower = "brainpower"
    BRI_DSR = "bri_dsr"
    CHILD_DS = "child_ds"
    CHARGE_DS = "charge_ds"
    DECIDAS = "decidas"
    DS_Brain = "ds_brain"
    DS_COG_ALL = "ds_cog_all"
    DS_COG_AML = "ds_cog_aml"
    DS_DETERMINED = "ds_determined"
    DS_HSAT = "ds_hsat"
    DS_ISP = "ds_isp"
    DS_Nexus = "ds_nexus"
    DS_PALS = "ds_pals"
    DS_PCGC = "ds_pcgc"
    DS_Sleep = "ds_sleep"
    DS_VitE = "ds_vite"
    DS360_CHD = "ds360_chd"
    DSC = "dsc"
    ECODS = "ecods"
    EXcEEDS = "exceeds"
    HTP = "htp"
    OPTimal = "optimal"
    TEAM_DS = "team_ds"
    TRC_DS = "trc_ds"
    X01_deSmith = "x01_desmith"
    X01_Hakonarson = "x01_hakonarson"


class EnumResearchDomain(str, Enum):
    Behavior_and_Behavior_Mechanisms = "behavior_and_behavior_mechanisms"
    Congenital_Heart_Defects = "congenital_heart_defects"
    Immune_System_Diseases = "immune_system_diseases"
    Hematologic_Diseases = "hematologic_diseases"
    Sleep_Wake_Disorders = "sleep_wake_disorders"
    All_Co_occurring_Conditions = "all_co_occurring_conditions"
    Physical_Fitness = "physical_fitness"
    Other = "other"


class EnumParticipantLifespanStage(str, Enum):
    Fetal = "fetal"
    # 0-28 days old
    Neonatal = "neonatal"
    # Birth-17 years old
    Pediatric = "pediatric"
    # 18+ years old
    Adult = "adult"


class EnumStudyDesign(str, Enum):
    Case_Control = "case_control"
    Case_Set = "case_set"
    Control_Set = "control_set"
    Clinical_Trial = "clinical_trial"
    Cross_Sectional = "cross_sectional"
    FamilySOLIDUSTwinsSOLIDUSTrios = "family_twins_trios"
    Interventional = "interventional"
    Longitudinal = "longitudinal"
    Tumor_vs_Matched_Normal = "tumor_vs_matched_normal"


class EnumClinicalDataSourceType(str, Enum):
    # Data obtained directly from medical record
    Medical_Record = "medical_record"
    # Data obtained by examination, interview, etc. with investigator
    Investigator_Assessment = "investigator_assessment"
    # Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    Other = "other"
    Unknown = "unknown"


class EnumDataCategory(str, Enum):
    Unharmonized_DemographicSOLIDUSClinical_Data = "unharmonized_demographic_clinical_data"
    Harmonized_DemographicSOLIDUSClinical_Data = "harmonized_demographic_clinical_data"
    Genomics = "genomics"
    Transcriptomics = "transcriptomics"
    Proteomics = "proteomics"
    Metabolomics = "metabolomics"
    CognitiveSOLIDUSBehavioral = "cognitive_behavioral"
    Immune_Maps = "immune_maps"
    Imaging = "imaging"
    Microbiome = "microbiome"
    Fitness = "fitness"
    Physical_Activity = "physical_activity"
    Other = "other"
    Sleep_Study = "sleep_study"


class EnumGuidType(str, Enum):
    # GUID generated by NIMH Data Archive (NDA) GUID tool
    NDAR = "ndar"
    # GUID generated by other system
    Other = "other"
    # No GUIDs used in this study
    No_GUID = "no_guid"



class Thing(ConfiguredBaseModel):
    """
    Highest Level Class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'False'}},
         'definition_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/include/core',
         'title': 'Thing'})

    pass


class Biospecimen(Thing):
    """
    A Biospecimen Collected from A Participant
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'True'},
                         'requires_component': {'tag': 'requires_component',
                                                'value': 'Study,Participant,DataFile'}},
         'definition_uri': 'include:Biospecimen',
         'from_schema': 'https://w3id.org/include/assay',
         'title': 'Biospecimen'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'participantGlobalId',
         'definition_uri': 'include:participantGlobalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""", json_schema_extra = { "linkml_meta": {'alias': 'participantExternalId',
         'definition_uri': 'include:participantExternalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    sampleGlobalId: str = Field(..., title="Sample Global ID", description="""INCLUDE global identifier for sample, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'sampleGlobalId',
         'definition_uri': 'include:sampleGlobalId',
         'domain_of': ['Biospecimen', 'DataFile']} })
    sampleExternalId: str = Field(..., title="Sample External ID", description="""Unique identifier for sample, assigned by data contributor. A sample is a unique biological material; two samples with two different IDs are biologically distinct.""", json_schema_extra = { "linkml_meta": {'alias': 'sampleExternalId',
         'definition_uri': 'include:sampleExternalId',
         'domain_of': ['Biospecimen', 'DataFile']} })
    sampleType: str = Field(..., title="Sample Type", description="""Type of biological material comprising the Sample (e.g. Plasma, White blood cells, Red blood cells, DNA, RNA, Peripheral blood mononuclear cells, CD4+ Tconv cells, NK cells, Monocytes, CD8+ T cells, B cells, Granulocytes, Treg cells)""", json_schema_extra = { "linkml_meta": {'alias': 'sampleType',
         'definition_uri': 'include:sampleType',
         'domain_of': ['Biospecimen']} })
    ageAtBiospecimenCollection: Optional[int] = Field(None, title="Age At Biospecimen Collection", description="""Age in days of participant at time of biospecimen collection""", json_schema_extra = { "linkml_meta": {'alias': 'ageAtBiospecimenCollection',
         'definition_uri': 'include:ageAtBiospecimenCollection',
         'domain_of': ['Biospecimen']} })
    parentSampleGlobalId: Optional[str] = Field(None, title="Parent Sample Global ID", description="""INCLUDE global identifier for the direct parent from which Sample was derived, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'parentSampleGlobalId',
         'definition_uri': 'include:parentSampleGlobalId',
         'domain_of': ['Biospecimen']} })
    parentSampleExternalId: Optional[str] = Field(None, title="Parent Sample External ID", description="""Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable); assigned by data contributor""", json_schema_extra = { "linkml_meta": {'alias': 'parentSampleExternalId',
         'definition_uri': 'include:parentSampleExternalId',
         'domain_of': ['Biospecimen']} })
    parentSampleType: Optional[str] = Field(None, title="Parent Sample Type", description="""Type of biological material comprising the Parent Sample (e.g. Peripheral Whole Blood, Derived Cell Line, Saliva, Whole blood, WBCs)""", json_schema_extra = { "linkml_meta": {'alias': 'parentSampleType',
         'definition_uri': 'include:parentSampleType',
         'domain_of': ['Biospecimen']} })
    collectionGlobalId: Optional[str] = Field(None, title="Collection Global ID", description="""INCLUDE global identifier for the eldest sample in a lineage, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'collectionGlobalId',
         'definition_uri': 'include:collectionGlobalId',
         'domain_of': ['Biospecimen']} })
    collectionExternalId: Optional[str] = Field(None, title="Collection External ID", description="""Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples - typically the material actually collected from the Participant. This may be the same as Parent Sample ID or Sample ID (if no processing was performed). Assigned by data contributor.""", json_schema_extra = { "linkml_meta": {'alias': 'collectionExternalId',
         'definition_uri': 'include:collectionExternalId',
         'domain_of': ['Biospecimen']} })
    collectionSampleType: Optional[str] = Field(None, title="Collection Sample Type", description="""Type of biological material comprising the Collected Sample (e.g. Whole blood, Not reported, Saliva, Derived cell line)""", json_schema_extra = { "linkml_meta": {'alias': 'collectionSampleType',
         'definition_uri': 'include:collectionSampleType',
         'domain_of': ['Biospecimen']} })
    containerGlobalId: Optional[str] = Field(None, title="Container Global ID", description="""INCLUDE global identifier for specific container/aliquot of sample, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'containerGlobalId',
         'definition_uri': 'include:containerGlobalId',
         'domain_of': ['Biospecimen']} })
    containerExternalId: Optional[str] = Field(None, title="Container External ID", description="""Identifier for specific container/aliquot of sample, assigned by data contributor. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.""", json_schema_extra = { "linkml_meta": {'alias': 'containerExternalId',
         'definition_uri': 'include:containerExternalId',
         'domain_of': ['Biospecimen']} })
    volume: Optional[float] = Field(None, title="Volume", description="""Amount of sample in container""", json_schema_extra = { "linkml_meta": {'alias': 'volume',
         'definition_uri': 'include:volume',
         'domain_of': ['Biospecimen']} })
    volumeUnit: Optional[str] = Field(None, title="Volume Unit", description="""Unit of sample volume""", json_schema_extra = { "linkml_meta": {'alias': 'volumeUnit',
         'definition_uri': 'include:volumeUnit',
         'domain_of': ['Biospecimen']} })
    concentration: Optional[float] = Field(None, title="Concentration", description="""Concentration of sample in container""", json_schema_extra = { "linkml_meta": {'alias': 'concentration',
         'definition_uri': 'include:concentration',
         'domain_of': ['Biospecimen']} })
    concentrationUnit: Optional[str] = Field(None, title="Concentration Unit", description="""Unit of sample concentration""", json_schema_extra = { "linkml_meta": {'alias': 'concentrationUnit',
         'definition_uri': 'include:concentrationUnit',
         'domain_of': ['Biospecimen']} })
    laboratoryProcedure: Optional[str] = Field(None, title="Laboratory Procedure", description="""Procedure by which Sample was derived from Parent Sample (e.g. Centrifugation, RBC lysis, Lyse/fix buffer, FACS, PAXgene DNA, PAXgene RNA, Qiagen Allprep, Ficoll)""", json_schema_extra = { "linkml_meta": {'alias': 'laboratoryProcedure',
         'definition_uri': 'include:laboratoryProcedure',
         'domain_of': ['Biospecimen']} })
    biospecimenStorage: Optional[str] = Field(None, title="Biospecimen Storage", description="""Method by which Container is stored (e.g. Minus 80 degrees Celsius, Liquid nitrogen storage)""", json_schema_extra = { "linkml_meta": {'alias': 'biospecimenStorage',
         'definition_uri': 'include:biospecimenStorage',
         'domain_of': ['Biospecimen']} })
    sampleAvailability: EnumAvailability = Field(..., title="Sample Availability", description="""Whether or not the Sample (any Container thereof) is potentially available for sharing through the Virtual Biorepository""", json_schema_extra = { "linkml_meta": {'alias': 'sampleAvailability',
         'definition_uri': 'include:sampleAvailability',
         'domain_of': ['Biospecimen']} })
    containerAvailability: Optional[EnumAvailability] = Field(None, title="Container Availability", description="""Whether or not the specific Container is potentially available for sharing through the Virtual Biorepository""", json_schema_extra = { "linkml_meta": {'alias': 'containerAvailability',
         'definition_uri': 'include:containerAvailability',
         'domain_of': ['Biospecimen']} })


class DataFile(Thing):
    """
    Metadata about Data Files
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'True'},
                         'requires_component': {'tag': 'requires_component',
                                                'value': 'Study,Participant,Biospecimen'}},
         'definition_uri': 'include:DataFile',
         'from_schema': 'https://w3id.org/include/assay',
         'slot_usage': {'dataCategory': {'description': 'General category of data in '
                                                        'file (e.g. Clinical, '
                                                        'Genomics, Proteomics, '
                                                        'Metabolomics, Immune '
                                                        'profiling, Transcriptomics)',
                                         'name': 'dataCategory'},
                        'dataType': {'description': 'Specific type of data contained '
                                                    'in file (e.g. Preprocessed '
                                                    'metabolite relative abundance, '
                                                    'Absolute protein concentration, '
                                                    'Aligned reads, Simple nucleotide '
                                                    'variations, GVCF, Gene expression '
                                                    'quantifications, Gene fusions, '
                                                    'Somatic copy number variations, '
                                                    'Somatic structural variations)',
                                     'name': 'dataType'},
                        'experimentalStrategy': {'description': 'Experimental method '
                                                                'used to obtain data '
                                                                'in file (e.g. Whole '
                                                                'genome sequencing, '
                                                                'RNAseq, Multiplex '
                                                                'immunoassay, Mass '
                                                                'spec metabolomics)',
                                                 'name': 'experimentalStrategy'}},
         'title': 'Data File'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'participantGlobalId',
         'definition_uri': 'include:participantGlobalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""", json_schema_extra = { "linkml_meta": {'alias': 'participantExternalId',
         'definition_uri': 'include:participantExternalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    sampleGlobalId: str = Field(..., title="Sample Global ID", description="""INCLUDE global identifier for sample, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'sampleGlobalId',
         'definition_uri': 'include:sampleGlobalId',
         'domain_of': ['Biospecimen', 'DataFile']} })
    sampleExternalId: str = Field(..., title="Sample External ID", description="""Unique identifier for sample, assigned by data contributor. A sample is a unique biological material; two samples with two different IDs are biologically distinct.""", json_schema_extra = { "linkml_meta": {'alias': 'sampleExternalId',
         'definition_uri': 'include:sampleExternalId',
         'domain_of': ['Biospecimen', 'DataFile']} })
    fileName: str = Field(..., title="File Name", description="""Name of file, assigned by data contributor""", json_schema_extra = { "linkml_meta": {'alias': 'fileName',
         'definition_uri': 'include:fileName',
         'domain_of': ['DataFile', 'DatasetManifest']} })
    fileGlobalId: str = Field(..., title="File Global ID", description="""INCLUDE global file identifier, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'fileGlobalId',
         'definition_uri': 'include:fileGlobalId',
         'domain_of': ['DataFile', 'DatasetManifest']} })
    fileS3Location: str = Field(..., title="File S3 Location", description="""S3 bucket location of file; also serves as dewrangle descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'fileS3Location',
         'definition_uri': 'include:fileS3Location',
         'domain_of': ['DataFile']} })
    fileUploadLocation: Optional[str] = Field(None, title="File Upload Location", description="""Where source file was uploaded, if not directly to an S3 bucket (e.g. Synapse)""", json_schema_extra = { "linkml_meta": {'alias': 'fileUploadLocation',
         'definition_uri': 'include:fileUploadLocation',
         'domain_of': ['DataFile']} })
    drsUri: str = Field(..., title="DRS URI", description="""Data Repository Services API Uniform Resource Identifier""", json_schema_extra = { "linkml_meta": {'alias': 'drsUri',
         'definition_uri': 'include:drsUri',
         'domain_of': ['DataFile']} })
    fileHash: Optional[str] = Field(None, title="File Hash", description="""md5 hash of this file for validation (if known)""", json_schema_extra = { "linkml_meta": {'alias': 'fileHash',
         'definition_uri': 'include:fileHash',
         'domain_of': ['DataFile']} })
    dataAccess: EnumDataAccess = Field(..., title="Data Access", description="""Type of access control on this file, determined by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'dataAccess',
         'definition_uri': 'include:dataAccess',
         'domain_of': ['DataFile']} })
    dataCategory: EnumDataCategory = Field(..., title="Data Category", description="""General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune profiling, Transcriptomics)""", json_schema_extra = { "linkml_meta": {'alias': 'dataCategory',
         'definition_uri': 'include:dataCategory',
         'domain_of': ['DataFile', 'Study', 'Dataset']} })
    dataType: Optional[str] = Field(None, title="Data Type", description="""Specific type of data contained in file (e.g. Preprocessed metabolite relative abundance, Absolute protein concentration, Aligned reads, Simple nucleotide variations, GVCF, Gene expression quantifications, Gene fusions, Somatic copy number variations, Somatic structural variations)""", json_schema_extra = { "linkml_meta": {'alias': 'dataType',
         'definition_uri': 'include:dataType',
         'domain_of': ['DataFile', 'Dataset']} })
    experimentalStrategy: Optional[List[str]] = Field(None, title="Experimental Strategy", description="""Experimental method used to obtain data in file (e.g. Whole genome sequencing, RNAseq, Multiplex immunoassay, Mass spec metabolomics)""", json_schema_extra = { "linkml_meta": {'alias': 'experimentalStrategy',
         'definition_uri': 'include:experimentalStrategy',
         'domain_of': ['DataFile', 'Dataset']} })
    experimentalPlatform: Optional[List[str]] = Field(None, title="Experimental Platform", description="""Specific platform used to perform experiment; pipe-separated if multiple (e.g. SOMAscan, MSD, Luminex, Illumina)""", json_schema_extra = { "linkml_meta": {'alias': 'experimentalPlatform',
         'definition_uri': 'include:experimentalPlatform',
         'domain_of': ['DataFile', 'Dataset']} })
    fileFormat: str = Field(..., title="File Format", description="""Format of file (e.g. tsv, cram, gvcf, vcf, maf, txt, pdf, html, png)""", json_schema_extra = { "linkml_meta": {'alias': 'fileFormat',
         'definition_uri': 'include:fileFormat',
         'domain_of': ['DataFile']} })
    fileSize: Optional[int] = Field(None, title="File Size", description="""Size of file, if known (mainly important if large)""", json_schema_extra = { "linkml_meta": {'alias': 'fileSize',
         'definition_uri': 'include:fileSize',
         'domain_of': ['DataFile']} })
    fileSizeUnit: Optional[str] = Field(None, title="File Size Unit", description="""Unit of file size""", json_schema_extra = { "linkml_meta": {'alias': 'fileSizeUnit',
         'definition_uri': 'include:fileSizeUnit',
         'domain_of': ['DataFile']} })


class Participant(Thing):
    """
    Demographic and clinical information about the participant
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'True'},
                         'requires_component': {'tag': 'requires_component',
                                                'value': 'Study,DataFile'}},
         'definition_uri': 'include:Participant',
         'from_schema': 'https://w3id.org/include/participant',
         'title': 'Participant'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'participantGlobalId',
         'definition_uri': 'include:participantGlobalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""", json_schema_extra = { "linkml_meta": {'alias': 'participantExternalId',
         'definition_uri': 'include:participantExternalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    familyId: Optional[str] = Field(None, title="Family ID", description="""Unique identifer for family to which Participant belongs, assigned by data contributor""", json_schema_extra = { "linkml_meta": {'alias': 'familyId',
         'definition_uri': 'include:familyId',
         'domain_of': ['Participant']} })
    familyType: EnumFamilyType = Field(..., title="Family Type", description="""Structure of family members participating in the study""", json_schema_extra = { "linkml_meta": {'alias': 'familyType',
         'definition_uri': 'include:familyType',
         'domain_of': ['Participant']} })
    fatherId: Optional[str] = Field(None, title="Father ID", description="""Participant External ID for Participant's father (NA if Participant is not the proband)""", json_schema_extra = { "linkml_meta": {'alias': 'fatherId',
         'definition_uri': 'include:fatherId',
         'domain_of': ['Participant']} })
    motherId: Optional[str] = Field(None, title="Mother ID", description="""Participant External ID for Participant's mother (NA if Participant is not the proband)""", json_schema_extra = { "linkml_meta": {'alias': 'motherId',
         'definition_uri': 'include:motherId',
         'domain_of': ['Participant']} })
    siblingId: Optional[str] = Field(None, title="Sibling ID", description="""Participant External ID for Participant's sibling(s) (NA if Participant is not the proband)""", json_schema_extra = { "linkml_meta": {'alias': 'siblingId',
         'definition_uri': 'include:siblingId',
         'domain_of': ['Participant']} })
    otherFamilyMemberId: Optional[str] = Field(None, title="Other Family Member ID", description="""Participant External ID for Participant's other family members (NA if Participant is not the proband)""", json_schema_extra = { "linkml_meta": {'alias': 'otherFamilyMemberId',
         'definition_uri': 'include:otherFamilyMemberId',
         'domain_of': ['Participant']} })
    familyRelationship: EnumFamilyRelationship = Field(..., title="Family Relationship", description="""Relationship of Participant to proband""", json_schema_extra = { "linkml_meta": {'alias': 'familyRelationship',
         'definition_uri': 'include:familyRelationship',
         'domain_of': ['Participant']} })
    sex: EnumSex = Field(..., title="Sex", description="""Sex of Participant""", json_schema_extra = { "linkml_meta": {'alias': 'sex', 'definition_uri': 'include:sex', 'domain_of': ['Participant']} })
    race: EnumRace = Field(..., title="Race", description="""Race of Participant""", json_schema_extra = { "linkml_meta": {'alias': 'race',
         'definition_uri': 'include:race',
         'domain_of': ['Participant']} })
    ethnicity: EnumEthnicity = Field(..., title="Ethnicity", description="""Ethnicity of Participant""", json_schema_extra = { "linkml_meta": {'alias': 'ethnicity',
         'definition_uri': 'include:ethnicity',
         'domain_of': ['Participant']} })
    downSyndromeStatus: EnumDownSyndromeStatus = Field(..., title="Down Syndrome Status", description="""Down Syndrome status of participant""", json_schema_extra = { "linkml_meta": {'alias': 'downSyndromeStatus',
         'definition_uri': 'include:downSyndromeStatus',
         'domain_of': ['Participant']} })
    ageAtFirstPatientEngagement: int = Field(..., title="Age at First Patient Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", ge=0, le=33000, json_schema_extra = { "linkml_meta": {'alias': 'ageAtFirstPatientEngagement',
         'definition_uri': 'include:ageAtFirstPatientEngagement',
         'domain_of': ['Participant']} })
    firstPatientEngagementEvent: str = Field(..., title="First Patient Engagement Event", description="""Event for which Age at First Patient Engagement is given (e.g. enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", json_schema_extra = { "linkml_meta": {'alias': 'firstPatientEngagementEvent',
         'definition_uri': 'include:firstPatientEngagementEvent',
         'domain_of': ['Participant']} })
    outcomesVitalStatus: Optional[EnumVitalStatus] = Field(None, title="Outcomes Vital Status", description="""Whether participant is alive or dead""", json_schema_extra = { "linkml_meta": {'alias': 'outcomesVitalStatus',
         'definition_uri': 'include:outcomesVitalStatus',
         'domain_of': ['Participant']} })
    ageAtLastVitalStatus: Optional[int] = Field(None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""", ge=0, le=33000, json_schema_extra = { "linkml_meta": {'alias': 'ageAtLastVitalStatus',
         'definition_uri': 'include:ageAtLastVitalStatus',
         'domain_of': ['Participant']} })


class Condition(Thing):
    """
    Co-occurring conditions and other observations for the participant
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'False'}},
         'definition_uri': 'include:Condition',
         'from_schema': 'https://w3id.org/include/participant',
         'title': 'Condition'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'participantGlobalId',
         'definition_uri': 'include:participantGlobalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""", json_schema_extra = { "linkml_meta": {'alias': 'participantExternalId',
         'definition_uri': 'include:participantExternalId',
         'domain_of': ['Biospecimen', 'DataFile', 'Participant', 'Condition']} })
    eventId: Optional[str] = Field(None, title="Event ID", description="""Identifier for event (Visit, Survey completion, Sample collection, etc.) to which the Condition data are linked, if applicable. There may be multiple events linked to a Participant.""", json_schema_extra = { "linkml_meta": {'alias': 'eventId',
         'definition_uri': 'include:eventId',
         'domain_of': ['Condition']} })
    eventType: Optional[str] = Field(None, title="Event Type", description="""Type of event for which Event ID is given (Visit, Survey completion, Sample collection, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'eventType',
         'definition_uri': 'include:eventType',
         'domain_of': ['Condition']} })
    conditionMeasureSourceText: Optional[str] = Field(None, title="Condition or Measure Source Text", description="""Co-occurring Condition (phenotype or diagnosis) or Measure (observation with numeric value), as described by data contributor. The Down Syndrome Genetic Diagnosis will be rolled into this field.""", json_schema_extra = { "linkml_meta": {'alias': 'conditionMeasureSourceText',
         'definition_uri': 'include:conditionMeasureSourceText',
         'domain_of': ['Condition']} })
    ageAtConditionMeasureObservation: Optional[int] = Field(None, title="Age At Condition or Measure Observation", description="""Age in days at which Condition or Measure was observed, recorded, or diagnosed""", ge=0, le=33000, json_schema_extra = { "linkml_meta": {'alias': 'ageAtConditionMeasureObservation',
         'definition_uri': 'include:ageAtConditionMeasureObservation',
         'domain_of': ['Condition']} })
    conditionInterpretation: Optional[EnumConditionInterpretation] = Field(None, title="Condition Interpretation", description="""Whether Condition was observed or not""", json_schema_extra = { "linkml_meta": {'alias': 'conditionInterpretation',
         'definition_uri': 'include:conditionInterpretation',
         'domain_of': ['Condition']} })
    conditionStatus: Optional[EnumConditionStatus] = Field(None, title="Condition Status", description="""Whether the Condition is ongoing, has been resolved, or this is a general history of the condition without known dates""", json_schema_extra = { "linkml_meta": {'alias': 'conditionStatus',
         'definition_uri': 'include:conditionStatus',
         'domain_of': ['Condition']} })
    conditionDataSource: Optional[EnumConditionDataSource] = Field(None, title="Condition Data Source", description="""Whether Condition information was obtained by the investigator or reported by participant/family member""", json_schema_extra = { "linkml_meta": {'alias': 'conditionDataSource',
         'definition_uri': 'include:conditionDataSource',
         'domain_of': ['Condition']} })
    hpoLabel: Optional[str] = Field(None, title="HPO Label", description="""Label for Condition in the Human Phenotype Ontology (HPO)""", json_schema_extra = { "linkml_meta": {'alias': 'hpoLabel',
         'definition_uri': 'include:hpoLabel',
         'domain_of': ['Condition']} })
    hpoCode: Optional[str] = Field(None, title="HPO Code", description="""Code for Condition in the Human Phenotype Ontology (HPO)""", json_schema_extra = { "linkml_meta": {'alias': 'hpoCode',
         'definition_uri': 'include:hpoCode',
         'domain_of': ['Condition']} })
    mondoLabel: Optional[str] = Field(None, title="MONDO Label", description="""Label for Condition in the Mondo Disease Ontology (MONDO)""", json_schema_extra = { "linkml_meta": {'alias': 'mondoLabel',
         'definition_uri': 'include:mondoLabel',
         'domain_of': ['Condition']} })
    mondoCode: Optional[str] = Field(None, title="MONDO Code", description="""Code for Condition in the Mondo Disease Ontology (Mondo)""", json_schema_extra = { "linkml_meta": {'alias': 'mondoCode',
         'definition_uri': 'include:mondoCode',
         'domain_of': ['Condition']} })
    maxoLabel: Optional[str] = Field(None, title="MAXO Label", description="""Label for Condition in the Medical Action Ontology (MAXO)""", json_schema_extra = { "linkml_meta": {'alias': 'maxoLabel',
         'definition_uri': 'include:maxoLabel',
         'domain_of': ['Condition']} })
    maxoCode: Optional[str] = Field(None, title="MAXO Code", description="""Code for condition in the Medical Action Ontology (MAXO)""", json_schema_extra = { "linkml_meta": {'alias': 'maxoCode',
         'definition_uri': 'include:maxoCode',
         'domain_of': ['Condition']} })
    otherLabel: Optional[str] = Field(None, title="Other Label", description="""Label for Condition in another ontology (if no match in HPO, MONDO, or MAXO)""", json_schema_extra = { "linkml_meta": {'alias': 'otherLabel',
         'definition_uri': 'include:otherLabel',
         'domain_of': ['Condition']} })
    otherCode: Optional[str] = Field(None, title="Other Code", description="""Code for Condition in another ontology (if no match in HPO, MONDO, or MAXO)""", json_schema_extra = { "linkml_meta": {'alias': 'otherCode',
         'definition_uri': 'include:otherCode',
         'domain_of': ['Condition']} })
    measureValue: Optional[float] = Field(None, title="Measure Value", description="""Numeric value of Measure""", json_schema_extra = { "linkml_meta": {'alias': 'measureValue',
         'definition_uri': 'include:measureValue',
         'domain_of': ['Condition']} })
    measureUnit: Optional[str] = Field(None, title="Measure Unit", description="""Unit that is associated with Measure Value (e.g. kg, cm, %, x10^9/L, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'measureUnit',
         'definition_uri': 'include:measureUnit',
         'domain_of': ['Condition']} })


class Study(Thing):
    """
    General information about the study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'True'}},
         'definition_uri': 'include:Study',
         'from_schema': 'https://w3id.org/include/study',
         'slot_usage': {'dataCategory': {'description': 'Categories of data expected '
                                                        'to be collected in this study',
                                         'multivalued': True,
                                         'name': 'dataCategory'},
                        'dbgap': {'description': 'dbGaP "phs" accession code(s) '
                                                 'associated with this Study, either '
                                                 'for access or informational purposes '
                                                 '(pipe-separated if multiple)',
                                  'name': 'dbgap'},
                        'expectedNumberOfParticipants': {'description': 'Expected '
                                                                        'number of '
                                                                        'participants '
                                                                        'in this study '
                                                                        '(or actual '
                                                                        'number, if '
                                                                        'data has been '
                                                                        'submitted to '
                                                                        'INCLUDE DCC). '
                                                                        'If additional '
                                                                        'explanation '
                                                                        'is needed, '
                                                                        'please add to '
                                                                        'Study '
                                                                        'Description '
                                                                        'field.',
                                                         'name': 'expectedNumberOfParticipants'},
                        'publication': {'description': 'URL for publication(s) '
                                                       "describing the study's "
                                                       'rationale and methodology '
                                                       '(PubMed Central preferred but '
                                                       'not required; pipe-separated '
                                                       'if multiple)',
                                        'name': 'publication'}},
         'title': 'Study'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    studyTitle: str = Field(..., title="Study Title", description="""Full title of the study""", json_schema_extra = { "linkml_meta": {'alias': 'studyTitle',
         'definition_uri': 'include:studyTitle',
         'domain_of': ['Study']} })
    program: List[EnumProgram] = Field(..., title="Program", description="""Funding source(s) for the study (pipe-separated if multiple)""", json_schema_extra = { "linkml_meta": {'alias': 'program',
         'definition_uri': 'include:program',
         'domain_of': ['Study']} })
    studyDescription: str = Field(..., title="Study Description", description="""Brief description of the study (2-4 sentences)""", json_schema_extra = { "linkml_meta": {'alias': 'studyDescription',
         'definition_uri': 'include:studyDescription',
         'domain_of': ['Study']} })
    principalInvestigatorName: List[str] = Field(..., title="Principal Investigator Name", description="""Name(s) of Principal Investigator(s) of this study; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'principalInvestigatorName',
         'definition_uri': 'include:principalInvestigatorName',
         'domain_of': ['Study']} })
    studyContactName: List[str] = Field(..., title="Study Contact Name", description="""Name of contact person for this study; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'studyContactName',
         'definition_uri': 'include:studyContactName',
         'domain_of': ['Study']} })
    studyContactInstitution: List[str] = Field(..., title="Study Contact Institution", description="""Institution of contact person for this study; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'studyContactInstitution',
         'definition_uri': 'include:studyContactInstitution',
         'domain_of': ['Study']} })
    studyContactEmail: List[str] = Field(..., title="Study Contact Email", description="""Email address of contact person for this study; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'studyContactEmail',
         'definition_uri': 'include:studyContactEmail',
         'domain_of': ['Study']} })
    vbrEmail: Optional[str] = Field(None, title="VBR Email", description="""Email address for Virtual Biorepository requests/inquiries, if participating""", json_schema_extra = { "linkml_meta": {'alias': 'vbrEmail',
         'definition_uri': 'include:vbrEmail',
         'domain_of': ['Study']} })
    vbrUrl: Optional[str] = Field(None, title="VBR URL", description="""Link to Virtual Biorepository request form, if participating""", json_schema_extra = { "linkml_meta": {'alias': 'vbrUrl', 'definition_uri': 'include:vbrUrl', 'domain_of': ['Study']} })
    vbrReadme: Optional[str] = Field(None, title="VBR Readme", description="""Instructions for contacting or requesting samples from Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'alias': 'vbrReadme',
         'definition_uri': 'include:vbrReadme',
         'domain_of': ['Study']} })
    researchDomain: List[EnumResearchDomain] = Field(..., title="Research Domain", description="""Main research domain(s) of the study, other than Down syndrome; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'researchDomain',
         'definition_uri': 'include:researchDomain',
         'domain_of': ['Study']} })
    participantLifespanStage: List[EnumParticipantLifespanStage] = Field(..., title="Participant Lifespan Stage", description="""Focus age group(s) of the study population; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'participantLifespanStage',
         'definition_uri': 'include:participantLifespanStage',
         'domain_of': ['Study']} })
    selectionCriteria: Optional[str] = Field(None, title="Selection Criteria", description="""Brief description of inclusion and/or exclusion criteria for the study""", json_schema_extra = { "linkml_meta": {'alias': 'selectionCriteria',
         'definition_uri': 'include:selectionCriteria',
         'domain_of': ['Study']} })
    studyDesign: EnumStudyDesign = Field(..., title="Study Design", description="""Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled""", json_schema_extra = { "linkml_meta": {'alias': 'studyDesign',
         'definition_uri': 'include:studyDesign',
         'domain_of': ['Study']} })
    clinicalDataSourceType: List[EnumClinicalDataSourceType] = Field(..., title="Clinical Data Source Type", description="""Source(s) of data collected from study participants; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalDataSourceType',
         'definition_uri': 'include:clinicalDataSourceType',
         'domain_of': ['Study']} })
    dataCategory: List[EnumDataCategory] = Field(..., title="Data Category", description="""Categories of data expected to be collected in this study""", json_schema_extra = { "linkml_meta": {'alias': 'dataCategory',
         'definition_uri': 'include:dataCategory',
         'domain_of': ['DataFile', 'Study', 'Dataset']} })
    studyWebsite: Optional[str] = Field(None, title="Study Website", description="""Website for the study""", json_schema_extra = { "linkml_meta": {'alias': 'studyWebsite',
         'definition_uri': 'include:studyWebsite',
         'domain_of': ['Study']} })
    dbgap: Optional[List[str]] = Field(None, title="dbGaP", description="""dbGaP \"phs\" accession code(s) associated with this Study, either for access or informational purposes (pipe-separated if multiple)""", json_schema_extra = { "linkml_meta": {'alias': 'dbgap',
         'definition_uri': 'include:dbgap',
         'domain_of': ['Study', 'Dataset']} })
    publication: Optional[List[str]] = Field(None, title="Publication", description="""URL for publication(s) describing the study's rationale and methodology (PubMed Central preferred but not required; pipe-separated if multiple)""", json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'definition_uri': 'include:publication',
         'domain_of': ['Study', 'Dataset']} })
    expectedNumberOfParticipants: int = Field(..., title="Expected Number of Participants", description="""Expected number of participants in this study (or actual number, if data has been submitted to INCLUDE DCC). If additional explanation is needed, please add to Study Description field.""", json_schema_extra = { "linkml_meta": {'alias': 'expectedNumberOfParticipants',
         'definition_uri': 'include:expectedNumberOfParticipants',
         'domain_of': ['Study', 'Dataset']} })
    guidType: EnumGuidType = Field(..., title="GUID Type", description="""System used to generate globally unique identifiers (GUIDs)""", json_schema_extra = { "linkml_meta": {'alias': 'guidType',
         'definition_uri': 'include:guidType',
         'domain_of': ['Study']} })
    guidMapped: Optional[bool] = Field(None, title="GUIDs Mapped?", description="""For studies using NDAR GUIDs, have the GUIDs been added to the INCLUDE GUID Mapping File?""", json_schema_extra = { "linkml_meta": {'alias': 'guidMapped',
         'definition_uri': 'include:guidMapped',
         'domain_of': ['Study']} })
    acknowledgments: Optional[List[str]] = Field(None, title="Acknowledgments", description="""Funding statement and acknowledgments for this study""", json_schema_extra = { "linkml_meta": {'alias': 'acknowledgments',
         'definition_uri': 'include:acknowledgments',
         'domain_of': ['Study']} })
    citationStatement: Optional[List[str]] = Field(None, title="Citation Statement", description="""Statement that secondary data users should use to acknowledge use of this dataset. E.g., \"The results analyzed and <published or shown> here are based in whole or in part upon data generated by the INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE) Project <insert accession number(s) and/or study DOI(s)>, and were accessed from the INCLUDE Data Hub and <insert other database(s)>.\"""", json_schema_extra = { "linkml_meta": {'alias': 'citationStatement',
         'definition_uri': 'include:citationStatement',
         'domain_of': ['Study']} })


class Dataset(Thing):
    """
    Information about a specific grouping of data files
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'False'}},
         'definition_uri': 'include:Dataset',
         'from_schema': 'https://w3id.org/include/study',
         'slot_usage': {'dataCategory': {'description': 'General category of data in '
                                                        'Dataset; pipe-separated if '
                                                        'multiple',
                                         'multivalued': True,
                                         'name': 'dataCategory'},
                        'dataType': {'description': 'Specific type of data contained '
                                                    'in Dataset; pipe-separated if '
                                                    'multiple (e.g. Preprocessed '
                                                    'metabolite relative abundance, '
                                                    'Absolute protein concentration, '
                                                    'Aligned reads, Simple nucleotide '
                                                    'variations, GVCF, Gene expression '
                                                    'quantifications, Gene fusions, '
                                                    'Somatic copy number variations, '
                                                    'Somatic structural variations)',
                                     'multivalued': True,
                                     'name': 'dataType'},
                        'dbgap': {'description': 'dbGaP "phs" accession code(s) '
                                                 'required to access the files in this '
                                                 'Dataset, if applicable '
                                                 '(pipe-separated if multiple)',
                                  'name': 'dbgap'},
                        'expectedNumberOfParticipants': {'description': 'Expected '
                                                                        'number of '
                                                                        'participants '
                                                                        'in this '
                                                                        'Dataset (or '
                                                                        'actual '
                                                                        'number, if '
                                                                        'data has been '
                                                                        'submitted to '
                                                                        'INCLUDE DCC). '
                                                                        'If additional '
                                                                        'explanation '
                                                                        'is needed, '
                                                                        'please add to '
                                                                        'Dataset '
                                                                        'Description '
                                                                        'field.',
                                                         'name': 'expectedNumberOfParticipants'},
                        'experimentalStrategy': {'description': 'Experimental method '
                                                                'used to obtain data '
                                                                'in Dataset; '
                                                                'pipe-separated if '
                                                                'multiple (e.g. Whole '
                                                                'genome sequencing, '
                                                                'RNAseq, Multiplex '
                                                                'immunoassay, Mass '
                                                                'spec metabolomics)',
                                                 'multivalued': True,
                                                 'name': 'experimentalStrategy'},
                        'publication': {'description': 'URL for publication(s) '
                                                       "describing the Dataset's "
                                                       'rationale and methodology '
                                                       '(PubMed Central preferred but '
                                                       'not required; pipe-separated '
                                                       'if multiple)',
                                        'name': 'publication'}},
         'title': 'Dataset'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    datasetName: str = Field(..., title="Dataset Name", description="""Full name of the dataset, provided by contributor""", json_schema_extra = { "linkml_meta": {'alias': 'datasetName',
         'definition_uri': 'include:datasetName',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    datasetDescription: Optional[str] = Field(None, title="Dataset Description", description="""Brief additional notes about the dataset (1-3 sentences) that are not already captured in the other fields""", json_schema_extra = { "linkml_meta": {'alias': 'datasetDescription',
         'definition_uri': 'include:datasetDescription',
         'domain_of': ['Dataset']} })
    datasetGlobalId: Optional[str] = Field(None, title="Dataset Global ID", description="""Unique Global ID for dataset, generated by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'datasetGlobalId',
         'definition_uri': 'include:datasetGlobalId',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    datasetExternalId: Optional[str] = Field(None, title="Dataset External ID", description="""Unique identifier or code for dataset, if provided by contributor""", json_schema_extra = { "linkml_meta": {'alias': 'datasetExternalId',
         'definition_uri': 'include:datasetExternalId',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    expectedNumberOfParticipants: int = Field(..., title="Expected Number of Participants", description="""Expected number of participants in this Dataset (or actual number, if data has been submitted to INCLUDE DCC). If additional explanation is needed, please add to Dataset Description field.""", json_schema_extra = { "linkml_meta": {'alias': 'expectedNumberOfParticipants',
         'definition_uri': 'include:expectedNumberOfParticipants',
         'domain_of': ['Study', 'Dataset']} })
    expectedNumberOfFiles: Optional[int] = Field(None, title="Expected Number of Files", description="""Expected number of files associated with this dataset, including dictionaries. If additional explanation is needed, please add to Dataset Description field.""", json_schema_extra = { "linkml_meta": {'alias': 'expectedNumberOfFiles',
         'definition_uri': 'include:expectedNumberOfFiles',
         'domain_of': ['Dataset']} })
    dataCollectionStartYear: Optional[str] = Field(None, title="Data Collection Start Year", description="""Year that data collection started""", json_schema_extra = { "linkml_meta": {'alias': 'dataCollectionStartYear',
         'definition_uri': 'include:dataCollectionStartYear',
         'domain_of': ['Dataset']} })
    dataCollectionEndYear: Optional[str] = Field(None, title="Data Collection End Year", description="""Year that data collection ended""", json_schema_extra = { "linkml_meta": {'alias': 'dataCollectionEndYear',
         'definition_uri': 'include:dataCollectionEndYear',
         'domain_of': ['Dataset']} })
    dataCategory: List[EnumDataCategory] = Field(..., title="Data Category", description="""General category of data in Dataset; pipe-separated if multiple""", json_schema_extra = { "linkml_meta": {'alias': 'dataCategory',
         'definition_uri': 'include:dataCategory',
         'domain_of': ['DataFile', 'Study', 'Dataset']} })
    dataType: Optional[List[str]] = Field(None, title="Data Type", description="""Specific type of data contained in Dataset; pipe-separated if multiple (e.g. Preprocessed metabolite relative abundance, Absolute protein concentration, Aligned reads, Simple nucleotide variations, GVCF, Gene expression quantifications, Gene fusions, Somatic copy number variations, Somatic structural variations)""", json_schema_extra = { "linkml_meta": {'alias': 'dataType',
         'definition_uri': 'include:dataType',
         'domain_of': ['DataFile', 'Dataset']} })
    experimentalStrategy: Optional[List[str]] = Field(None, title="Experimental Strategy", description="""Experimental method used to obtain data in Dataset; pipe-separated if multiple (e.g. Whole genome sequencing, RNAseq, Multiplex immunoassay, Mass spec metabolomics)""", json_schema_extra = { "linkml_meta": {'alias': 'experimentalStrategy',
         'definition_uri': 'include:experimentalStrategy',
         'domain_of': ['DataFile', 'Dataset']} })
    experimentalPlatform: Optional[List[str]] = Field(None, title="Experimental Platform", description="""Specific platform used to perform experiment; pipe-separated if multiple (e.g. SOMAscan, MSD, Luminex, Illumina)""", json_schema_extra = { "linkml_meta": {'alias': 'experimentalPlatform',
         'definition_uri': 'include:experimentalPlatform',
         'domain_of': ['DataFile', 'Dataset']} })
    publication: Optional[List[str]] = Field(None, title="Publication", description="""URL for publication(s) describing the Dataset's rationale and methodology (PubMed Central preferred but not required; pipe-separated if multiple)""", json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'definition_uri': 'include:publication',
         'domain_of': ['Study', 'Dataset']} })
    accessLimitations: Optional[str] = Field(None, title="Access Limitations", description="""Data access limitations, as defined in the GA4GH Data Use Ontology (DUO; can list more than one, pipe separated)""", json_schema_extra = { "linkml_meta": {'alias': 'accessLimitations',
         'definition_uri': 'include:accessLimitations',
         'domain_of': ['Dataset']} })
    accessRequirements: Optional[str] = Field(None, title="Access Requirements", description="""Data access requirements, as defined in the GA4GH Data Use Ontology (DUO; can list more than one, pipe separated)""", json_schema_extra = { "linkml_meta": {'alias': 'accessRequirements',
         'definition_uri': 'include:accessRequirements',
         'domain_of': ['Dataset']} })
    dbgap: Optional[List[str]] = Field(None, title="dbGaP", description="""dbGaP \"phs\" accession code(s) required to access the files in this Dataset, if applicable (pipe-separated if multiple)""", json_schema_extra = { "linkml_meta": {'alias': 'dbgap',
         'definition_uri': 'include:dbgap',
         'domain_of': ['Study', 'Dataset']} })
    otherRepository: Optional[str] = Field(None, title="Other Repository", description="""URL if dataset is already deposited in a public repository other than dbGaP (e.g. LONI, Metabolomics Workbench, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'otherRepository',
         'definition_uri': 'include:otherRepository',
         'domain_of': ['Dataset']} })
    otherAccessAuthority: Optional[str] = Field(None, title="Other Access Authority", description="""Email or URL for dataset's Access Authority, if not dbGaP""", json_schema_extra = { "linkml_meta": {'alias': 'otherAccessAuthority',
         'definition_uri': 'include:otherAccessAuthority',
         'domain_of': ['Dataset']} })
    isHarmonized: Optional[bool] = Field(None, title="Is Harmonized?", description="""For omics datasets, is this Dataset already harmonized and available in the INCLUDE Data Hub?""", json_schema_extra = { "linkml_meta": {'alias': 'isHarmonized',
         'definition_uri': 'include:isHarmonized',
         'domain_of': ['Dataset']} })


class DatasetManifest(Thing):
    """
    Mapping information for files in Dataset
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'required': {'tag': 'required', 'value': 'False'}},
         'definition_uri': 'include:DatasetManifest',
         'from_schema': 'https://w3id.org/include/study',
         'title': 'Dataset Manifest'})

    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'alias': 'studyCode',
         'definition_uri': 'include:studyCode',
         'domain_of': ['Biospecimen',
                       'DataFile',
                       'Participant',
                       'Condition',
                       'Study',
                       'Dataset',
                       'DatasetManifest']} })
    datasetName: str = Field(..., title="Dataset Name", description="""Full name of the dataset, provided by contributor""", json_schema_extra = { "linkml_meta": {'alias': 'datasetName',
         'definition_uri': 'include:datasetName',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    datasetGlobalId: Optional[str] = Field(None, title="Dataset Global ID", description="""Unique Global ID for dataset, generated by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'datasetGlobalId',
         'definition_uri': 'include:datasetGlobalId',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    datasetExternalId: Optional[str] = Field(None, title="Dataset External ID", description="""Unique identifier or code for dataset, if provided by contributor""", json_schema_extra = { "linkml_meta": {'alias': 'datasetExternalId',
         'definition_uri': 'include:datasetExternalId',
         'domain_of': ['Dataset', 'DatasetManifest']} })
    fileName: str = Field(..., title="File Name", description="""Name of file, assigned by data contributor""", json_schema_extra = { "linkml_meta": {'alias': 'fileName',
         'definition_uri': 'include:fileName',
         'domain_of': ['DataFile', 'DatasetManifest']} })
    fileGlobalId: str = Field(..., title="File Global ID", description="""INCLUDE global file identifier, assigned by DCC""", json_schema_extra = { "linkml_meta": {'alias': 'fileGlobalId',
         'definition_uri': 'include:fileGlobalId',
         'domain_of': ['DataFile', 'DatasetManifest']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
Biospecimen.model_rebuild()
DataFile.model_rebuild()
Participant.model_rebuild()
Condition.model_rebuild()
Study.model_rebuild()
Dataset.model_rebuild()
DatasetManifest.model_rebuild()

