from __future__ import annotations
from datetime import (
    datetime,
    date
)
from decimal import Decimal
from enum import Enum
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
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
    ABC_DS = "abc_ds"
    ADS = "ads"
    AECOM_DS = "aecom_ds"
    BrainPower = "brainpower"
    BRI_DSR = "bri_dsr"
    CHILD_DS = "child_ds"
    CHARGE_DS = "charge_ds"
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
    DS360_CHD = "ds360_chd"
    DSC = "dsc"
    ECODS = "ecods"
    EXcEEDS = "exceeds"
    HTP = "htp"
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


class EnumClinicalDataSourceType(str, Enum):
    # Data obtained directly from medical record
    Medical_Record = "medical_record"
    # Data obtained by examination, interview, etc. with investigator
    Investigator_Assessment = "investigator_assessment"
    # Data obtained from survey, questionnaire, etc.
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
    pass


class Biospecimen(Thing):
    """
    A Biospecimen Collected from A Participant
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""")
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""")
    sampleGlobalId: str = Field(..., title="Sample Global ID", description="""INCLUDE global identifier for sample, assigned by DCC""")
    sampleExternalId: str = Field(..., title="Sample External ID", description="""Unique identifier for sample, assigned by data contributor. A sample is a unique biological material; two samples with two different IDs are biologically distinct.""")
    sampleType: str = Field(..., title="Sample Type", description="""Type of biological material comprising the Sample (e.g. Plasma, White blood cells, Red blood cells, DNA, RNA, Peripheral blood mononuclear cells, CD4+ Tconv cells, NK cells, Monocytes, CD8+ T cells, B cells, Granulocytes, Treg cells)""")
    ageAtBiospecimenCollection: Optional[int] = Field(None, title="Age At Biospecimen Collection", description="""Age in days of participant at time of biospecimen collection""")
    parentSampleGlobalId: Optional[str] = Field(None, title="Parent Sample Global ID", description="""INCLUDE global identifier for the direct parent from which Sample was derived, assigned by DCC""")
    parentSampleExternalId: Optional[str] = Field(None, title="Parent Sample External ID", description="""Identifier for the direct parent from which Sample was derived, processed, pooled, etc. (if applicable); assigned by data contributor""")
    parentSampleType: Optional[str] = Field(None, title="Parent Sample Type", description="""Type of biological material comprising the Parent Sample (e.g. Peripheral Whole Blood, Derived Cell Line, Saliva, Whole blood, WBCs)""")
    collectionGlobalId: Optional[str] = Field(None, title="Collection Global ID", description="""INCLUDE global identifier for the eldest sample in a lineage, assigned by DCC""")
    collectionExternalId: Optional[str] = Field(None, title="Collection External ID", description="""Identifier for the eldest sample in a lineage of processed, pooled, or aliquoted samples - typically the material actually collected from the Participant. This may be the same as Parent Sample ID or Sample ID (if no processing was performed). Assigned by data contributor.""")
    collectionSampleType: Optional[str] = Field(None, title="Collection Sample Type", description="""Type of biological material comprising the Collected Sample (e.g. Whole blood, Not reported, Saliva, Derived cell line)""")
    containerGlobalId: Optional[str] = Field(None, title="Container Global ID", description="""INCLUDE global identifier for specific container/aliquot of sample, assigned by DCC""")
    containerExternalId: Optional[str] = Field(None, title="Container External ID", description="""Identifier for specific container/aliquot of sample, assigned by data contributor. For example, distinct aliquots of a sample will have the same Sample ID but different Container IDs.""")
    volume: Optional[float] = Field(None, title="Volume", description="""Amount of sample in container""")
    volumeUnit: Optional[str] = Field(None, title="Volume Unit", description="""Unit of sample volume""")
    concentration: Optional[float] = Field(None, title="Concentration", description="""Concentration of sample in container""")
    concentrationUnit: Optional[str] = Field(None, title="Concentration Unit", description="""Unit of sample concentration""")
    laboratoryProcedure: Optional[str] = Field(None, title="Laboratory Procedure", description="""Procedure by which Sample was derived from Parent Sample (e.g. Centrifugation, RBC lysis, Lyse/fix buffer, FACS, PAXgene DNA, PAXgene RNA, Qiagen Allprep, Ficoll)""")
    biospecimenStorage: Optional[str] = Field(None, title="Biospecimen Storage", description="""Method by which Container is stored (e.g. Minus 80 degrees Celsius, Liquid nitrogen storage)""")
    sampleAvailability: EnumAvailability = Field(..., title="Sample Availability", description="""Whether or not the Sample (any Container thereof) is potentially available for sharing through the Virtual Biorepository""")
    containerAvailability: Optional[EnumAvailability] = Field(None, title="Container Availability", description="""Whether or not the specific Container is potentially available for sharing through the Virtual Biorepository""")


class DataFile(Thing):
    """
    Metadata about Data Files
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""")
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""")
    sampleGlobalId: str = Field(..., title="Sample Global ID", description="""INCLUDE global identifier for sample, assigned by DCC""")
    sampleExternalId: str = Field(..., title="Sample External ID", description="""Unique identifier for sample, assigned by data contributor. A sample is a unique biological material; two samples with two different IDs are biologically distinct.""")
    fileName: str = Field(..., title="File Name", description="""Name of file, assigned by data contributor""")
    fileGlobalId: str = Field(..., title="File Global ID", description="""INCLUDE global file identifier, assigned by DCC""")
    fileS3Location: str = Field(..., title="File S3 Location", description="""S3 bucket location of file; also serves as dewrangle descriptor""")
    fileUploadLocation: Optional[str] = Field(None, title="File Upload Location", description="""Where source file was uploaded, if not directly to an S3 bucket (e.g. Synapse)""")
    drsUri: str = Field(..., title="DRS URI", description="""Data Repository Services API Uniform Resource Identifier""")
    fileHash: Optional[str] = Field(None, title="File Hash", description="""md5 hash of this file for validation (if known)""")
    dataAccess: EnumDataAccess = Field(..., title="Data Access", description="""Type of access control on this file, determined by DCC""")
    dataCategory: EnumDataCategory = Field(..., title="Data Category", description="""General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune profiling, Transcriptomics)""")
    dataType: Optional[str] = Field(None, title="Data Type", description="""Specific type of data contained in file (e.g. Preprocessed metabolite relative abundance, Absolute protein concentration, Aligned reads, Simple nucleotide variations, GVCF, Gene expression quantifications, Gene fusions, Somatic copy number variations, Somatic structural variations)""")
    experimentalStrategy: Optional[List[str]] = Field(default_factory=list, title="Experimental Strategy", description="""Experimental method used to obtain data in file (e.g. Whole genome sequencing, RNAseq, Multiplex immunoassay, Mass spec metabolomics)""")
    experimentalPlatform: Optional[List[str]] = Field(default_factory=list, title="Experimental Platform", description="""Specific platform used to perform experiment; pipe-separated if multiple (e.g. SOMAscan, MSD, Luminex, Illumina)""")
    fileFormat: str = Field(..., title="File Format", description="""Format of file (e.g. tsv, cram, gvcf, vcf, maf, txt, pdf, html, png)""")
    fileSize: Optional[int] = Field(None, title="File Size", description="""Size of file, if known (mainly important if large)""")
    fileSizeUnit: Optional[str] = Field(None, title="File Size Unit", description="""Unit of file size""")


class Participant(Thing):
    """
    Demographic and clinical information about the participant
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""")
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""")
    familyId: Optional[str] = Field(None, title="Family ID", description="""Unique identifer for family to which Participant belongs, assigned by data contributor""")
    familyType: EnumFamilyType = Field(..., title="Family Type", description="""Structure of family members participating in the study""")
    fatherId: Optional[str] = Field(None, title="Father ID", description="""Participant External ID for Participant's father (NA if Participant is not the proband)""")
    motherId: Optional[str] = Field(None, title="Mother ID", description="""Participant External ID for Participant's mother (NA if Participant is not the proband)""")
    siblingId: Optional[str] = Field(None, title="Sibling ID", description="""Participant External ID for Participant's sibling(s) (NA if Participant is not the proband)""")
    otherFamilyMemberId: Optional[str] = Field(None, title="Other Family Member ID", description="""Participant External ID for Participant's other family members (NA if Participant is not the proband)""")
    familyRelationship: EnumFamilyRelationship = Field(..., title="Family Relationship", description="""Relationship of Participant to proband""")
    sex: EnumSex = Field(..., title="Sex", description="""Sex of Participant""")
    race: EnumRace = Field(..., title="Race", description="""Race of Participant""")
    ethnicity: EnumEthnicity = Field(..., title="Ethnicity", description="""Ethnicity of Participant""")
    downSyndromeStatus: EnumDownSyndromeStatus = Field(..., title="Down Syndrome Status", description="""Down Syndrome status of participant""")
    ageAtFirstPatientEngagement: int = Field(..., title="Age at First Patient Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", ge=0, le=33000)
    firstPatientEngagementEvent: str = Field(..., title="First Patient Engagement Event", description="""Event for which Age at First Patient Engagement is given (e.g. enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""")
    outcomesVitalStatus: Optional[EnumVitalStatus] = Field(None, title="Outcomes Vital Status", description="""Whether participant is alive or dead""")
    ageAtLastVitalStatus: Optional[int] = Field(None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""", ge=0, le=33000)


class Condition(Thing):
    """
    Co-occurring conditions and other observations for the participant
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    participantGlobalId: str = Field(..., title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""")
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""")
    eventId: Optional[str] = Field(None, title="Event ID", description="""Identifier for event (Visit, Survey completion, Sample collection, etc.) to which the Condition data are linked, if applicable. There may be multiple events linked to a Participant.""")
    eventType: Optional[str] = Field(None, title="Event Type", description="""Type of event for which Event ID is given (Visit, Survey completion, Sample collection, etc.)""")
    conditionMeasureSourceText: Optional[str] = Field(None, title="Condition or Measure Source Text", description="""Co-occurring Condition (phenotype or diagnosis) or Measure (observation with numeric value), as described by data contributor. The Down Syndrome Genetic Diagnosis will be rolled into this field.""")
    ageAtConditionMeasureObservation: Optional[int] = Field(None, title="Age At Condition or Measure Observation", description="""Age in days at which Condition or Measure was observed, recorded, or diagnosed""", ge=0, le=33000)
    conditionInterpretation: Optional[EnumConditionInterpretation] = Field(None, title="Condition Interpretation", description="""Whether Condition was observed or not""")
    conditionStatus: Optional[EnumConditionStatus] = Field(None, title="Condition Status", description="""Whether the Condition is ongoing, has been resolved, or this is a general history of the condition without known dates""")
    conditionDataSource: Optional[EnumConditionDataSource] = Field(None, title="Condition Data Source", description="""Whether Condition information was obtained by the investigator or reported by participant/family member""")
    hpoLabel: Optional[str] = Field(None, title="HPO Label", description="""Label for Condition in the Human Phenotype Ontology (HPO)""")
    hpoCode: Optional[str] = Field(None, title="HPO Code", description="""Code for Condition in the Human Phenotype Ontology (HPO)""")
    mondoLabel: Optional[str] = Field(None, title="MONDO Label", description="""Label for Condition in the Mondo Disease Ontology (MONDO)""")
    mondoCode: Optional[str] = Field(None, title="MONDO Code", description="""Code for Condition in the Mondo Disease Ontology (Mondo)""")
    maxoLabel: Optional[str] = Field(None, title="MAXO Label", description="""Label for Condition in the Medical Action Ontology (MAXO)""")
    maxoCode: Optional[str] = Field(None, title="MAXO Code", description="""Code for condition in the Medical Action Ontology (MAXO)""")
    otherLabel: Optional[str] = Field(None, title="Other Label", description="""Label for Condition in another ontology (if no match in HPO, MONDO, or MAXO)""")
    otherCode: Optional[str] = Field(None, title="Other Code", description="""Code for Condition in another ontology (if no match in HPO, MONDO, or MAXO)""")
    measureValue: Optional[int] = Field(None, title="Measure Value", description="""Numeric value of Measure""")
    measureUnit: Optional[str] = Field(None, title="Measure Unit", description="""Unit that is associated with Measure Value (e.g. kg, cm, %, x10^9/L, etc.)""")


class Study(Thing):
    """
    General information about the study
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    studyTitle: str = Field(..., title="Study Title", description="""Full title of the study""")
    program: List[EnumProgram] = Field(default_factory=list, title="Program", description="""Funding source(s) for the study (pipe-separated if multiple)""")
    studyDescription: str = Field(..., title="Study Description", description="""Brief description of the study (2-4 sentences)""")
    principalInvestigatorName: List[str] = Field(default_factory=list, title="Principal Investigator Name", description="""Name(s) of Principal Investigator(s) of this study; pipe-separated if multiple""")
    studyContactName: List[str] = Field(default_factory=list, title="Study Contact Name", description="""Name of contact person for this study; pipe-separated if multiple""")
    studyContactInstitution: List[str] = Field(default_factory=list, title="Study Contact Institution", description="""Institution of contact person for this study; pipe-separated if multiple""")
    studyContactEmail: List[str] = Field(default_factory=list, title="Study Contact Email", description="""Email address of contact person for this study; pipe-separated if multiple""")
    vbrEmail: Optional[str] = Field(None, title="VBR Email", description="""Email address for Virtual Biorepository requests/inquiries""")
    vbrUrl: Optional[str] = Field(None, title="VBR URL", description="""Link to Virtual Biorepository request form""")
    vbrReadme: Optional[str] = Field(None, title="VBR Readme", description="""Instructions for contacting or requesting samples from Virtual Biorepository""")
    researchDomain: List[EnumResearchDomain] = Field(default_factory=list, title="Research Domain", description="""Main research domain(s) of the study, other than Down syndrome; pipe-separated if multiple""")
    participantLifespanStage: List[EnumParticipantLifespanStage] = Field(default_factory=list, title="Participant Lifespan Stage", description="""Focus age group(s) of the study population; pipe-separated if multiple""")
    selectionCriteria: Optional[str] = Field(None, title="Selection Criteria", description="""Brief description of inclusion and/or exclusion criteria for the study""")
    studyDesign: str = Field(..., title="Study Design", description="""Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled""")
    clinicalDataSourceType: List[EnumClinicalDataSourceType] = Field(default_factory=list, title="Clinical Data Source Type", description="""Source(s) of data collected from study participants; pipe-separated if multiple""")
    dataCategory: EnumDataCategory = Field(..., title="Data Category", description="""Categories of data expected to be collected in this study""")
    studyWebsite: Optional[str] = Field(None, title="Study Website", description="""Website for the study""")
    dbgap: Optional[List[str]] = Field(default_factory=list, title="dbGaP", description="""dbGaP \"phs\" accession code(s) associated with this Study, either for access or informational purposes (pipe-separated if multiple)""")
    publication: Optional[List[str]] = Field(default_factory=list, title="Publication", description="""URL for publication(s) describing the study's rationale and methodology (PubMed Central preferred but not required; pipe-separated if multiple)""")
    expectedNumberOfParticipants: int = Field(..., title="Expected Number of Participants", description="""Expected number of participants in this study. If additional explanation is needed, please add to Study Description field.""")
    guidType: EnumGuidType = Field(..., title="GUID Type", description="""System used to generate globally unique identifiers (GUIDs)""")
    acknowledgments: Optional[List[str]] = Field(default_factory=list, title="Acknowledgments", description="""Funding statement and acknowledgments for this study""")
    citationStatement: Optional[List[str]] = Field(default_factory=list, title="Citation Statement", description="""Statement that secondary data users should use to acknowledge use of this dataset. E.g., \"The results analyzed and <published or shown> here are based in whole or in part upon data generated by the INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE) Project <insert accession number(s) and/or study DOI(s)>, and were accessed from the INCLUDE Data Hub and <insert other database(s)>.\"""")


class Dataset(Thing):
    """
    Information about a specific grouping of data files
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    datasetName: str = Field(..., title="Dataset Name", description="""Full name of the dataset, provided by contributor""")
    datasetDescription: Optional[str] = Field(None, title="Dataset Description", description="""Brief additional notes about the dataset (1-3 sentences) that are not already captured in the other fields""")
    datasetGlobalId: Optional[str] = Field(None, title="Dataset Global ID", description="""Unique Global ID for dataset, generated by DCC""")
    datasetExternalId: Optional[str] = Field(None, title="Dataset External ID", description="""Unique identifier or code for dataset, if provided by contributor""")
    expectedNumberOfParticipants: int = Field(..., title="Expected Number of Participants", description="""Expected number of participants in this Dataset. If additional explanation is needed, please add to Dataset Description field.""")
    expectedNumberOfFiles: Optional[int] = Field(None, title="Expected Number of Files", description="""Expected number of files associated with this dataset, including dictionaries. If additional explanation is needed, please add to Dataset Description field.""")
    dataCollectionStartYear: Optional[str] = Field(None, title="Data Collection Start Year", description="""Year that data collection started""")
    dataCollectionEndYear: Optional[str] = Field(None, title="Data Collection End Year", description="""Year that data collection ended""")
    dataCategory: EnumDataCategory = Field(..., title="Data Category", description="""General category of data in Dataset; pipe-separated if multiple""")
    dataType: Optional[str] = Field(None, title="Data Type", description="""Specific type of data contained in Dataset; pipe-separated if multiple (e.g. Preprocessed metabolite relative abundance, Absolute protein concentration, Aligned reads, Simple nucleotide variations, GVCF, Gene expression quantifications, Gene fusions, Somatic copy number variations, Somatic structural variations)""")
    experimentalStrategy: Optional[List[str]] = Field(default_factory=list, title="Experimental Strategy", description="""Experimental method used to obtain data in Dataset; pipe-separated if multiple (e.g. Whole genome sequencing, RNAseq, Multiplex immunoassay, Mass spec metabolomics)""")
    experimentalPlatform: Optional[List[str]] = Field(default_factory=list, title="Experimental Platform", description="""Specific platform used to perform experiment; pipe-separated if multiple (e.g. SOMAscan, MSD, Luminex, Illumina)""")
    publication: Optional[List[str]] = Field(default_factory=list, title="Publication", description="""URL for publication(s) describing the Dataset's rationale and methodology (PubMed Central preferred but not required; pipe-separated if multiple)""")
    accessLimitations: Optional[str] = Field(None, title="Access Limitations", description="""Data access limitations, as defined in the GA4GH Data Use Ontology (DUO; can list more than one, pipe separated)""")
    accessRequirements: Optional[str] = Field(None, title="Access Requirements", description="""Data access requirements, as defined in the GA4GH Data Use Ontology (DUO; can list more than one, pipe separated)""")
    dbgap: Optional[List[str]] = Field(default_factory=list, title="dbGaP", description="""dbGaP \"phs\" accession code(s) required to access the files in this Dataset, if applicable (pipe-separated if multiple)""")
    otherRepository: Optional[str] = Field(None, title="Other Repository", description="""URL if dataset is already deposited in a public repository other than dbGaP (e.g. LONI, Metabolomics Workbench, etc.)""")
    otherAccessAuthority: Optional[str] = Field(None, title="Other Access Authority", description="""Email or URL for dataset's Access Authority, if not dbGaP""")
    isHarmonized: Optional[bool] = Field(None, title="Is Harmonized?", description="""For omics datasets, is this Dataset already harmonized and available in the INCLUDE Data Hub?""")


class DatasetManifest(Thing):
    """
    Mapping information for files in Dataset
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study (generally a short acronym)""")
    datasetName: str = Field(..., title="Dataset Name", description="""Full name of the dataset, provided by contributor""")
    datasetGlobalId: Optional[str] = Field(None, title="Dataset Global ID", description="""Unique Global ID for dataset, generated by DCC""")
    datasetExternalId: Optional[str] = Field(None, title="Dataset External ID", description="""Unique identifier or code for dataset, if provided by contributor""")
    fileName: str = Field(..., title="File Name", description="""Name of file, assigned by data contributor""")
    fileGlobalId: str = Field(..., title="File Global ID", description="""INCLUDE global file identifier, assigned by DCC""")


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

