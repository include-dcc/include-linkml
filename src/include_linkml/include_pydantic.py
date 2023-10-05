from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class EnumProgram(str, Enum):
    
    
    include = "include"
    
    kf = "kf"
    
    

class EnumStudyCode(str, Enum):
    
    
    abcds = "abcds"
    
    ads = "ads"
    
    aecom_ds = "aecom_ds"
    
    brainpower = "brainpower"
    
    bri_dsr = "bri_dsr"
    
    charge_ds = "charge_ds"
    
    ds_brain = "ds_brain"
    
    ds_cog_all = "ds_cog_all"
    
    ds_cog_aml = "ds_cog_aml"
    
    ds_determined = "ds_determined"
    
    ds_hsat = "ds_hsat"
    
    ds_isp = "ds_isp"
    
    ds_nexus = "ds_nexus"
    
    ds_pals = "ds_pals"
    
    ds_pcgc = "ds_pcgc"
    
    ds_sleep = "ds_sleep"
    
    ds360_chd = "ds360_chd"
    
    dsc = "dsc"
    
    ecods = "ecods"
    
    exceeds = "exceeds"
    
    htp = "htp"
    
    trc_ds = "trc_ds"
    
    x01_desmith = "x01_desmith"
    
    x01_hakon = "x01_hakon"
    
    

class EnumConditionInterpretation(str, Enum):
    
    # Condition was observed or reported (this will be the case for most conditions)
    observed = "observed"
    # Participant was specifically examined or medical record queried for condition and found to be negative
    not_observed = "not_observed"
    
    

class EnumConditionDataSource(str, Enum):
    
    # Information about condition was obtained from medical records or reported by investigator
    clinical = "clinical"
    # Information about condition was reported by participant or family member
    self_reported = "self_reported"
    
    

class EnumConditionStatus(str, Enum):
    
    # Condition is ongoing
    current = "current"
    # Condition has been resolved
    resolved = "resolved"
    # This is a general history of the condition, without known dates
    history_of = "history_of"
    
    

class EnumDownSyndromeStatus(str, Enum):
    
    # Disomy 21 (euploid)
    d21 = "d21"
    # Trisomy 21 (Down syndrome)
    t21 = "t21"
    
    

class EnumEthnicity(str, Enum):
    
    
    hispanic_or_latino = "hispanic_or_latino"
    
    not_hispanic_or_latino = "not_hispanic_or_latino"
    
    prefer_not_to_answer = "prefer_not_to_answer"
    
    unknown = "unknown"
    
    

class EnumFamilyRelationship(str, Enum):
    
    # The first affected family member to join the study
    proband = "proband"
    
    father = "father"
    
    mother = "mother"
    
    sibling = "sibling"
    
    other_relative = "other_relative"
    
    unrelated_control = "unrelated_control"
    
    

class EnumFamilyType(str, Enum):
    
    # Unrelated control, no Down syndrome family members
    control_only = "control_only"
    # Proband + one parent
    duo = "duo"
    # Other family structure, e.g. one parent + twins
    other = "other"
    # Proband only, no family members participating in study
    proband_only = "proband_only"
    # Proband + two parents
    trio = "trio"
    # Proband + two parents + other relatives
    trio_plus = "trio_plus"
    
    

class EnumRace(str, Enum):
    
    
    american_indian_or_alaskan_native = "american_indian_or_alaskan_native"
    
    asian = "asian"
    
    black_or_african_american = "black_or_african_american"
    
    more_than_one_race = "more_than_one_race"
    
    native_hawaiian_or_other_pacific_islander = "native_hawaiian_or_other_pacific_islander"
    
    other = "other"
    
    white = "white"
    
    prefer_not_to_answer = "prefer_not_to_answer"
    
    unknown = "unknown"
    # UK only; do not use for US data
    east_asian = "east_asian"
    # UK only; do not use for US data
    latin_american = "latin_american"
    # UK only; do not use for US data
    middle_eastern_or_north_african = "middle_eastern_or_north_african"
    # UK only; do not use for US data
    south_asian = "south_asian"
    
    

class EnumSex(str, Enum):
    
    
    female = "female"
    
    male = "male"
    
    other = "other"
    
    unknown = "unknown"
    
    

class EnumVitalStatus(str, Enum):
    
    
    dead = "dead"
    
    alive = "alive"
    
    unknown_or_not_available = "unknown_or_not_available"
    
    

class EnumDataAccess(str, Enum):
    
    
    controlled = "controlled"
    
    open = "open"
    
    registered = "registered"
    
    

class EnumSampleAvailability(str, Enum):
    
    # Sample is potentially available to be requested through the Virtual Biorepository (see VBR contact info in Study page)
    available = "available"
    # Sample either was available through Virtual Biorepository but has been used up, or is part of a study that is not participating in the VBR
    unavailable = "unavailable"
    
    

class Thing(ConfiguredBaseModel):
    """
    Highest Level Class
    """
    None
    


class Study(Thing):
    """
    General information about the study
    """
    studyCode: EnumStudyCode = Field(..., title="Study Code", description="""Unique identifer for the study, assigned by DCC""")
    studyName: str = Field(..., title="Study Name", description="""Full name of the study, chosen by data contributor""")
    program: EnumProgram = Field(..., title="Program", description="""Funding source for the study""")
    dbgap: Optional[str] = Field(None, title="dbGaP", description="""dbGaP study accession code""")
    vbrContact: Optional[str] = Field(None, title="Virtual Biorepository Contact", description="""Contact information for Virtual Biorepository inquiries to this Study (email or form)""")
    


class Participant(Thing):
    """
    Demographic and clinical information about the participant
    """
    hasStudy: Optional[Study] = Field(None, title="Has Study", description="""Link to a Study""")
    participantGlobalId: Optional[str] = Field(None, title="Participant Global ID", description="""Unique INCLUDE global identifier for the participant, assigned by DCC""")
    participantExternalId: str = Field(..., title="Participant External ID", description="""Unique, de-identified identifier for the participant, assigned by data contributor. External IDs must be two steps removed from personal information in the study records.""")
    familyId: Optional[str] = Field(None, title="Family ID", description="""Unique identifer for family to which Participant belongs, assigned by data contributor""")
    familyType: EnumFamilyType = Field(..., title="Family Type", description="""Structure of family members participating in the study""")
    fatherId: Optional[str] = Field(None, title="Father ID", description="""Participant External ID for Participant's father (NA if Participant is not the proband)""")
    motherId: Optional[str] = Field(None, title="Mother ID", description="""Participant External ID for Participant's mother (NA if Participant is not the proband)""")
    siblingId: Optional[str] = Field(None, title="Sibling ID", description="""Participant External ID for Participant's sibling(s) (NA if Participant is not the proband)""")
    otherFamilyMemberId: Optional[str] = Field(None, title="Other Family Member ID", description="""Participant External ID for Participant's other family members (NA if Participant is not the proband)""")
    familyRelationship: Optional[EnumFamilyRelationship] = Field(None, title="Family Relationship", description="""Relationship of Participant to proband""")
    sex: EnumSex = Field(..., title="Sex", description="""Sex of Participant""")
    race: List[EnumRace] = Field(default_factory=list, title="Race", description="""Race of Participant""")
    ethnicity: EnumEthnicity = Field(..., title="Ethnicity", description="""Ethnicity of Participant""")
    downSyndromeStatus: EnumDownSyndromeStatus = Field(..., title="Down Syndrome Status", description="""Down Syndrome status of participant""")
    ageAtFirstPatientEngagement: int = Field(..., title="Age at First Patient Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""")
    firstPatientEngagementEvent: str = Field(..., title="First Patient Engagement Event", description="""Event for which Age at First Patient Engagement is given (e.g. enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""")
    outcomesVitalStatus: Optional[EnumVitalStatus] = Field(None, title="Outcomes Vital Status", description="""Whether participant is alive or dead""")
    ageAtLastVitalStatus: Optional[int] = Field(None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""")
    


class Condition(Thing):
    """
    Co-occurring conditions and other observations for the participant
    """
    hasStudy: Optional[Study] = Field(None, title="Has Study", description="""Link to a Study""")
    hasParticipant: Optional[Participant] = Field(None, title="Has Participant", description="""Link to a Participant""")
    eventId: Optional[str] = Field(None, title="Event ID", description="""Identifier for event (Visit, Survey completion, Sample collection, etc.) to which the Condition data are linked, if applicable. There may be multiple events linked to a Participant.""")
    eventType: Optional[str] = Field(None, title="Event Type", description="""Type of event for which Event ID is given (Visit, Survey completion, Sample collection, etc.)""")
    conditionMeasureSourceText: Optional[str] = Field(None, title="Condition or Measure Source Text", description="""Co-occurring Condition (phenotype or diagnosis) or Measure (observation with numeric value), as described by data contributor. The Down Syndrome Genetic Diagnosis will be rolled into this field.""")
    ageAtConditionMeasureObservation: Optional[int] = Field(None, title="Age At Condition or Measure Observation", description="""Age in days at which Condition or Measure was observed, recorded, or diagnosed""")
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
    


class Biospecimen(Thing):
    """
    A Biospecimen Collected from A Participant
    """
    hasStudy: Optional[Study] = Field(None, title="Has Study", description="""Link to a Study""")
    hasParticipant: Optional[Participant] = Field(None, title="Has Participant", description="""Link to a Participant""")
    sampleGlobalId: Optional[str] = Field(None, title="Sample Global ID", description="""INCLUDE global identifier for sample, assigned by DCC""")
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
    sampleAvailability: Optional[EnumSampleAvailability] = Field(None, title="Sample Availability", description="""Whether or not the sample is potentially available for sharing through the Virtual Biorepository""")
    


class DataFile(Thing):
    """
    A DataFile Associated with a Participant or Study or Biospecimen
    """
    hasStudy: Optional[Study] = Field(None, title="Has Study", description="""Link to a Study""")
    hasParticipant: Optional[Participant] = Field(None, title="Has Participant", description="""Link to a Participant""")
    hasBiospecimen: Optional[Biospecimen] = Field(None, title="Has Biospecimen", description="""Link to a Biospecimen""")
    fileGlobalId: Optional[str] = Field(None, title="File Global ID", description="""INCLUDE global file identifier, assigned by DCC""")
    fileExternalId: str = Field(..., title="File External ID", description="""Unique identifier for data file, assigned by data contributor""")
    fileName: str = Field(..., title="File Name", description="""Name of file, assigned by data contributor""")
    fileHash: Optional[str] = Field(None, title="File Hash", description="""md5 hash of this file for validation (if known)""")
    dataAccess: Optional[EnumDataAccess] = Field(None, title="Data Access", description="""Type of access control on this file, determined by DCC""")
    dataCategory: str = Field(..., title="Data Category", description="""General category of data in file (e.g. Clinical, Genomics, Proteomics, Metabolomics, Immune profiling, Transcriptomics)""")
    dataType: Optional[str] = Field(None, title="Data Type", description="""Specific type of data contained in file (e.g. Preprocessed metabolite relative abundance, Absolute protein concentration, Aligned reads, Simple nucleotide variations, GVCF, Gene expression quantifications, Gene fusions, Somatic copy number variations, Somatic structural variations)""")
    experimentalStrategy: Optional[str] = Field(None, title="Experimental Strategy", description="""Experimental method used to obtain data in file (e.g. Whole genome sequencing, RNAseq, Multiplex immunoassay, Mass spec metabolomics)""")
    experimentalPlatform: Optional[str] = Field(None, title="Experimental Platform", description="""Specific platform used to perform experiment (e.g. SOMAscan, MSD, Luminex, Illumina)""")
    fileFormat: str = Field(..., title="File Format", description="""Format of file (e.g. tsv, cram, gvcf, vcf, maf, txt, pdf, html, png)""")
    fileSize: Optional[int] = Field(None, title="File Size", description="""Size of file, if known (mainly important if large)""")
    fileSizeUnit: Optional[str] = Field(None, title="File Size Unit", description="""Unit of file size""")
    accessUrl: Optional[str] = Field(None, title="Access URL", description="""URL/URI to file repository location""")
    publicationDoi: Optional[str] = Field(None, title="Publication DOI", description="""DOI of publication associated with this file, if published""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Thing.update_forward_refs()
Study.update_forward_refs()
Participant.update_forward_refs()
Condition.update_forward_refs()
Biospecimen.update_forward_refs()
DataFile.update_forward_refs()

