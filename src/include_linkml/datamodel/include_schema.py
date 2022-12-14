# Auto generated from include_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-14T09:10:11
# Schema: include-schema
#
# id: https://w3id.org/include
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
INCLUDE = CurieNamespace('include', 'https://w3id.org/include/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = INCLUDE


# Types

# Class references



class Thing(YAMLRoot):
    """
    Highest Level Class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["core/Thing"]
    class_class_curie: ClassVar[str] = "include:core/Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Thing


class Aliquot(Thing):
    """
    An aliquot of a sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["assay/Aliquot"]
    class_class_curie: ClassVar[str] = "include:assay/Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Aliquot


@dataclass
class Assay(Thing):
    """
    An assay
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["assay/Assay"]
    class_class_curie: ClassVar[str] = "include:assay/Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Assay

    UsesBiospecimen: Optional[Union[dict, "Biospecimen"]] = None
    HasOutput: Optional[Union[dict, "DataFile"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.UsesBiospecimen is not None and not isinstance(self.UsesBiospecimen, Biospecimen):
            self.UsesBiospecimen = Biospecimen(**as_dict(self.UsesBiospecimen))

        if self.HasOutput is not None and not isinstance(self.HasOutput, DataFile):
            self.HasOutput = DataFile(**as_dict(self.HasOutput))

        super().__post_init__(**kwargs)


@dataclass
class Biospecimen(Thing):
    """
    A Biospecimen Collected from A Participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["assay/Biospecimen"]
    class_class_curie: ClassVar[str] = "include:assay/Biospecimen"
    class_name: ClassVar[str] = "Biospecimen"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Biospecimen

    SampleID: str = None
    SampleType: str = None
    AgeAtBiospecimenCollection: Optional[int] = None
    BiospecimenStorage: Optional[str] = None
    CollectionID: Optional[str] = None
    CollectionSampleType: Optional[str] = None
    ContainerID: Optional[str] = None
    HasDatafile: Optional[Union[dict, "DataFile"]] = None
    HasParticipant: Optional[Union[dict, "Participant"]] = None
    HasStudy: Optional[Union[dict, "Study"]] = None
    LaboratoryProcedure: Optional[str] = None
    ParentSampleID: Optional[str] = None
    ParentSampleType: Optional[str] = None
    SampleAvailability: Optional[Union[str, "EnumSampleAvailability"]] = None
    Volume: Optional[float] = None
    VolumeUnit: Optional[str] = None
    HasAliquot: Optional[Union[dict, Aliquot]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SampleID):
            self.MissingRequiredField("SampleID")
        if not isinstance(self.SampleID, str):
            self.SampleID = str(self.SampleID)

        if self._is_empty(self.SampleType):
            self.MissingRequiredField("SampleType")
        if not isinstance(self.SampleType, str):
            self.SampleType = str(self.SampleType)

        if self.AgeAtBiospecimenCollection is not None and not isinstance(self.AgeAtBiospecimenCollection, int):
            self.AgeAtBiospecimenCollection = int(self.AgeAtBiospecimenCollection)

        if self.BiospecimenStorage is not None and not isinstance(self.BiospecimenStorage, str):
            self.BiospecimenStorage = str(self.BiospecimenStorage)

        if self.CollectionID is not None and not isinstance(self.CollectionID, str):
            self.CollectionID = str(self.CollectionID)

        if self.CollectionSampleType is not None and not isinstance(self.CollectionSampleType, str):
            self.CollectionSampleType = str(self.CollectionSampleType)

        if self.ContainerID is not None and not isinstance(self.ContainerID, str):
            self.ContainerID = str(self.ContainerID)

        if self.HasDatafile is not None and not isinstance(self.HasDatafile, DataFile):
            self.HasDatafile = DataFile(**as_dict(self.HasDatafile))

        if self.HasParticipant is not None and not isinstance(self.HasParticipant, Participant):
            self.HasParticipant = Participant(**as_dict(self.HasParticipant))

        if self.HasStudy is not None and not isinstance(self.HasStudy, Study):
            self.HasStudy = Study(**as_dict(self.HasStudy))

        if self.LaboratoryProcedure is not None and not isinstance(self.LaboratoryProcedure, str):
            self.LaboratoryProcedure = str(self.LaboratoryProcedure)

        if self.ParentSampleID is not None and not isinstance(self.ParentSampleID, str):
            self.ParentSampleID = str(self.ParentSampleID)

        if self.ParentSampleType is not None and not isinstance(self.ParentSampleType, str):
            self.ParentSampleType = str(self.ParentSampleType)

        if self.SampleAvailability is not None and not isinstance(self.SampleAvailability, EnumSampleAvailability):
            self.SampleAvailability = EnumSampleAvailability(self.SampleAvailability)

        if self.Volume is not None and not isinstance(self.Volume, float):
            self.Volume = float(self.Volume)

        if self.VolumeUnit is not None and not isinstance(self.VolumeUnit, str):
            self.VolumeUnit = str(self.VolumeUnit)

        if self.HasAliquot is not None and not isinstance(self.HasAliquot, Aliquot):
            self.HasAliquot = Aliquot()

        super().__post_init__(**kwargs)


@dataclass
class DataFile(Thing):
    """
    A DataFile Associated with a Participant or Study or Biospecimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["assay/DataFile"]
    class_class_curie: ClassVar[str] = "include:assay/DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = INCLUDE.DataFile

    DataCategory: str = None
    FileName: str = None
    Format: str = None
    ParticipantID: str = None
    OriginalFileName: str = None
    AccessURL: Optional[Union[str, URIorCURIE]] = None
    CollectionID: Optional[str] = None
    DataAccess: Optional[Union[str, "EnumDataAccess"]] = None
    DataType: Optional[str] = None
    ExperimentalStrategy: Optional[str] = None
    FileID: Optional[str] = None
    HasBiospecimen: Optional[Union[dict, Biospecimen]] = None
    HasParticipant: Optional[Union[dict, "Participant"]] = None
    HasStudy: Optional[Union[dict, "Study"]] = None
    Size: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.DataCategory):
            self.MissingRequiredField("DataCategory")
        if not isinstance(self.DataCategory, str):
            self.DataCategory = str(self.DataCategory)

        if self._is_empty(self.FileName):
            self.MissingRequiredField("FileName")
        if not isinstance(self.FileName, str):
            self.FileName = str(self.FileName)

        if self._is_empty(self.Format):
            self.MissingRequiredField("Format")
        if not isinstance(self.Format, str):
            self.Format = str(self.Format)

        if self._is_empty(self.ParticipantID):
            self.MissingRequiredField("ParticipantID")
        if not isinstance(self.ParticipantID, str):
            self.ParticipantID = str(self.ParticipantID)

        if self._is_empty(self.OriginalFileName):
            self.MissingRequiredField("OriginalFileName")
        if not isinstance(self.OriginalFileName, str):
            self.OriginalFileName = str(self.OriginalFileName)

        if self.AccessURL is not None and not isinstance(self.AccessURL, URIorCURIE):
            self.AccessURL = URIorCURIE(self.AccessURL)

        if self.CollectionID is not None and not isinstance(self.CollectionID, str):
            self.CollectionID = str(self.CollectionID)

        if self.DataAccess is not None and not isinstance(self.DataAccess, EnumDataAccess):
            self.DataAccess = EnumDataAccess(self.DataAccess)

        if self.DataType is not None and not isinstance(self.DataType, str):
            self.DataType = str(self.DataType)

        if self.ExperimentalStrategy is not None and not isinstance(self.ExperimentalStrategy, str):
            self.ExperimentalStrategy = str(self.ExperimentalStrategy)

        if self.FileID is not None and not isinstance(self.FileID, str):
            self.FileID = str(self.FileID)

        if self.HasBiospecimen is not None and not isinstance(self.HasBiospecimen, Biospecimen):
            self.HasBiospecimen = Biospecimen(**as_dict(self.HasBiospecimen))

        if self.HasParticipant is not None and not isinstance(self.HasParticipant, Participant):
            self.HasParticipant = Participant(**as_dict(self.HasParticipant))

        if self.HasStudy is not None and not isinstance(self.HasStudy, Study):
            self.HasStudy = Study(**as_dict(self.HasStudy))

        if self.Size is not None and not isinstance(self.Size, str):
            self.Size = str(self.Size)

        super().__post_init__(**kwargs)


@dataclass
class Participant(Thing):
    """
    A Participant in a Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["participant/Participant"]
    class_class_curie: ClassVar[str] = "include:participant/Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Participant

    DownSyndromeStatus: Union[str, "EnumDownSyndromeStatus"] = None
    Ethnicity: Union[str, "EnumEthnicity"] = None
    ExternalID: str = None
    FamilyType: Union[str, "EnumFamilyType"] = None
    ParticipantID: str = None
    Race: Union[str, "EnumRace"] = None
    Sex: Union[str, "EnumSex"] = None
    AgeAtLastVitalStatus: Optional[int] = None
    FamilyID: Optional[str] = None
    FamilyRelationship: Optional[Union[dict, "Participant"]] = None
    FatherID: Optional[str] = None
    HasDatafile: Optional[Union[dict, DataFile]] = None
    HasStudy: Optional[Union[dict, "Study"]] = None
    MotherID: Optional[str] = None
    OutcomesVitalStatus: Optional[Union[str, "EnumVitalStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.DownSyndromeStatus):
            self.MissingRequiredField("DownSyndromeStatus")
        if not isinstance(self.DownSyndromeStatus, EnumDownSyndromeStatus):
            self.DownSyndromeStatus = EnumDownSyndromeStatus(self.DownSyndromeStatus)

        if self._is_empty(self.Ethnicity):
            self.MissingRequiredField("Ethnicity")
        if not isinstance(self.Ethnicity, EnumEthnicity):
            self.Ethnicity = EnumEthnicity(self.Ethnicity)

        if self._is_empty(self.ExternalID):
            self.MissingRequiredField("ExternalID")
        if not isinstance(self.ExternalID, str):
            self.ExternalID = str(self.ExternalID)

        if self._is_empty(self.FamilyType):
            self.MissingRequiredField("FamilyType")
        if not isinstance(self.FamilyType, EnumFamilyType):
            self.FamilyType = EnumFamilyType(self.FamilyType)

        if self._is_empty(self.ParticipantID):
            self.MissingRequiredField("ParticipantID")
        if not isinstance(self.ParticipantID, str):
            self.ParticipantID = str(self.ParticipantID)

        if self._is_empty(self.Race):
            self.MissingRequiredField("Race")
        if not isinstance(self.Race, EnumRace):
            self.Race = EnumRace(self.Race)

        if self._is_empty(self.Sex):
            self.MissingRequiredField("Sex")
        if not isinstance(self.Sex, EnumSex):
            self.Sex = EnumSex(self.Sex)

        if self.AgeAtLastVitalStatus is not None and not isinstance(self.AgeAtLastVitalStatus, int):
            self.AgeAtLastVitalStatus = int(self.AgeAtLastVitalStatus)

        if self.FamilyID is not None and not isinstance(self.FamilyID, str):
            self.FamilyID = str(self.FamilyID)

        if self.FamilyRelationship is not None and not isinstance(self.FamilyRelationship, Participant):
            self.FamilyRelationship = Participant(**as_dict(self.FamilyRelationship))

        if self.FatherID is not None and not isinstance(self.FatherID, str):
            self.FatherID = str(self.FatherID)

        if self.HasDatafile is not None and not isinstance(self.HasDatafile, DataFile):
            self.HasDatafile = DataFile(**as_dict(self.HasDatafile))

        if self.HasStudy is not None and not isinstance(self.HasStudy, Study):
            self.HasStudy = Study(**as_dict(self.HasStudy))

        if self.MotherID is not None and not isinstance(self.MotherID, str):
            self.MotherID = str(self.MotherID)

        if self.OutcomesVitalStatus is not None and not isinstance(self.OutcomesVitalStatus, EnumVitalStatus):
            self.OutcomesVitalStatus = EnumVitalStatus(self.OutcomesVitalStatus)

        super().__post_init__(**kwargs)


@dataclass
class FamilyGroup(Thing):
    """
    A group of Participants in the same Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["participant/FamilyGroup"]
    class_class_curie: ClassVar[str] = "include:participant/FamilyGroup"
    class_name: ClassVar[str] = "FamilyGroup"
    class_model_uri: ClassVar[URIRef] = INCLUDE.FamilyGroup

    HasParticipant: Optional[Union[dict, Participant]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.HasParticipant is not None and not isinstance(self.HasParticipant, Participant):
            self.HasParticipant = Participant(**as_dict(self.HasParticipant))

        super().__post_init__(**kwargs)


@dataclass
class Condition(Thing):
    """
    A Condition of a Participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["participant/Condition"]
    class_class_curie: ClassVar[str] = "include:participant/Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Condition

    HasParticipant: Optional[Union[dict, Participant]] = None
    AgeAtConditionObservation: Optional[int] = None
    MONDOLabel: Optional[str] = None
    MONDOCode: Optional[str] = None
    ConditionInterpretation: Optional[Union[str, "EnumConditionInterpretation"]] = None
    ConditionDataSource: Optional[Union[str, "EnumConditionDataSource"]] = None
    HPOLabel: Optional[str] = None
    HPOCode: Optional[str] = None
    MAXOLabel: Optional[str] = None
    MAXOCode: Optional[str] = None
    OtherLabel: Optional[str] = None
    OtherCode: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.HasParticipant is not None and not isinstance(self.HasParticipant, Participant):
            self.HasParticipant = Participant(**as_dict(self.HasParticipant))

        if self.AgeAtConditionObservation is not None and not isinstance(self.AgeAtConditionObservation, int):
            self.AgeAtConditionObservation = int(self.AgeAtConditionObservation)

        if self.MONDOLabel is not None and not isinstance(self.MONDOLabel, str):
            self.MONDOLabel = str(self.MONDOLabel)

        if self.MONDOCode is not None and not isinstance(self.MONDOCode, str):
            self.MONDOCode = str(self.MONDOCode)

        if self.ConditionInterpretation is not None and not isinstance(self.ConditionInterpretation, EnumConditionInterpretation):
            self.ConditionInterpretation = EnumConditionInterpretation(self.ConditionInterpretation)

        if self.ConditionDataSource is not None and not isinstance(self.ConditionDataSource, EnumConditionDataSource):
            self.ConditionDataSource = EnumConditionDataSource(self.ConditionDataSource)

        if self.HPOLabel is not None and not isinstance(self.HPOLabel, str):
            self.HPOLabel = str(self.HPOLabel)

        if self.HPOCode is not None and not isinstance(self.HPOCode, str):
            self.HPOCode = str(self.HPOCode)

        if self.MAXOLabel is not None and not isinstance(self.MAXOLabel, str):
            self.MAXOLabel = str(self.MAXOLabel)

        if self.MAXOCode is not None and not isinstance(self.MAXOCode, str):
            self.MAXOCode = str(self.MAXOCode)

        if self.OtherLabel is not None and not isinstance(self.OtherLabel, str):
            self.OtherLabel = str(self.OtherLabel)

        if self.OtherCode is not None and not isinstance(self.OtherCode, str):
            self.OtherCode = str(self.OtherCode)

        super().__post_init__(**kwargs)


@dataclass
class Study(Thing):
    """
    A Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE["study/Study"]
    class_class_curie: ClassVar[str] = "include:study/Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Study

    Program: Union[str, "EnumProgram"] = None
    StudyCode: Union[str, "EnumStudyCode"] = None
    StudyName: str = None
    dbGap: Optional[str] = None
    HasParticipant: Optional[Union[dict, Participant]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Program):
            self.MissingRequiredField("Program")
        if not isinstance(self.Program, EnumProgram):
            self.Program = EnumProgram(self.Program)

        if self._is_empty(self.StudyCode):
            self.MissingRequiredField("StudyCode")
        if not isinstance(self.StudyCode, EnumStudyCode):
            self.StudyCode = EnumStudyCode(self.StudyCode)

        if self._is_empty(self.StudyName):
            self.MissingRequiredField("StudyName")
        if not isinstance(self.StudyName, str):
            self.StudyName = str(self.StudyName)

        if self.dbGap is not None and not isinstance(self.dbGap, str):
            self.dbGap = str(self.dbGap)

        if self.HasParticipant is not None and not isinstance(self.HasParticipant, Participant):
            self.HasParticipant = Participant(**as_dict(self.HasParticipant))

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataAccess(EnumDefinitionImpl):

    controlled = PermissibleValue(text="controlled")
    open = PermissibleValue(text="open")
    registered = PermissibleValue(text="registered")

    _defn = EnumDefinition(
        name="EnumDataAccess",
    )

class EnumSampleAvailability(EnumDefinitionImpl):

    available = PermissibleValue(text="available")
    unavailable = PermissibleValue(text="unavailable")

    _defn = EnumDefinition(
        name="EnumSampleAvailability",
    )

class EnumConditionInterpretation(EnumDefinitionImpl):

    observed = PermissibleValue(text="observed")
    not_observed = PermissibleValue(text="not_observed")

    _defn = EnumDefinition(
        name="EnumConditionInterpretation",
    )

class EnumConditionDataSource(EnumDefinitionImpl):

    clinical = PermissibleValue(text="clinical")
    self_reported = PermissibleValue(text="self_reported")

    _defn = EnumDefinition(
        name="EnumConditionDataSource",
    )

class EnumDownSyndromeStatus(EnumDefinitionImpl):

    d21 = PermissibleValue(text="d21")
    t21 = PermissibleValue(text="t21",
                             meaning=MONDO["0008608"])

    _defn = EnumDefinition(
        name="EnumDownSyndromeStatus",
    )

class EnumEthnicity(EnumDefinitionImpl):

    asked_but_unknown = PermissibleValue(text="asked_but_unknown")
    hispanic_or_latino = PermissibleValue(text="hispanic_or_latino")
    not_hispanic_or_latino = PermissibleValue(text="not_hispanic_or_latino")
    prefer_not_to_answer = PermissibleValue(text="prefer_not_to_answer")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="EnumEthnicity",
    )

class EnumFamilyType(EnumDefinitionImpl):

    duo = PermissibleValue(text="duo")
    other = PermissibleValue(text="other")
    proband_only = PermissibleValue(text="proband_only")
    trio = PermissibleValue(text="trio")
    trio_plus = PermissibleValue(text="trio_plus")

    _defn = EnumDefinition(
        name="EnumFamilyType",
    )

class EnumRace(EnumDefinitionImpl):

    american_indian_or_alaskan_native = PermissibleValue(text="american_indian_or_alaskan_native")
    asian = PermissibleValue(text="asian")
    black_or_african_american = PermissibleValue(text="black_or_african_american")
    more_than_one_Race = PermissibleValue(text="more_than_one_Race")
    native_hawaiian_or_other_pacific_islander = PermissibleValue(text="native_hawaiian_or_other_pacific_islander")
    other = PermissibleValue(text="other")
    white = PermissibleValue(text="white")
    prefer_not_to_answer = PermissibleValue(text="prefer_not_to_answer")

    _defn = EnumDefinition(
        name="EnumRace",
    )

class EnumSex(EnumDefinitionImpl):

    female = PermissibleValue(text="female")
    male = PermissibleValue(text="male")
    other = PermissibleValue(text="other")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="EnumSex",
    )

class EnumVitalStatus(EnumDefinitionImpl):

    dead = PermissibleValue(text="dead")
    alive = PermissibleValue(text="alive")

    _defn = EnumDefinition(
        name="EnumVitalStatus",
    )

class EnumProgram(EnumDefinitionImpl):

    include = PermissibleValue(text="include")
    kf = PermissibleValue(text="kf")

    _defn = EnumDefinition(
        name="EnumProgram",
    )

class EnumStudyCode(EnumDefinitionImpl):

    ds_cog_all = PermissibleValue(text="ds_cog_all")
    ds_pcgc = PermissibleValue(text="ds_pcgc")
    ds360_chd = PermissibleValue(text="ds360_chd")
    dsc = PermissibleValue(text="dsc")
    htp = PermissibleValue(text="htp")
    abcds = PermissibleValue(text="abcds")
    ads = PermissibleValue(text="ads")
    ds_brain = PermissibleValue(text="ds_brain")
    ds_cog_aml = PermissibleValue(text="ds_cog_aml")
    bri_dsr = PermissibleValue(text="bri_dsr")
    ds_isp = PermissibleValue(text="ds_isp")
    ds_nexus = PermissibleValue(text="ds_nexus")
    ds_pals = PermissibleValue(text="ds_pals")
    ds_sleep = PermissibleValue(text="ds_sleep")
    ecods = PermissibleValue(text="ecods")
    exceeds = PermissibleValue(text="exceeds")
    trc_ds = PermissibleValue(text="trc_ds")
    x01_desmith = PermissibleValue(text="x01_desmith")
    x01_hakon = PermissibleValue(text="x01_hakon")

    _defn = EnumDefinition(
        name="EnumStudyCode",
    )

# Slots
class slots:
    pass

slots.AccessURL = Slot(uri=INCLUDE['assay/AccessURL'], name="AccessURL", curie=INCLUDE.curie('assay/AccessURL'),
                   model_uri=INCLUDE.AccessURL, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.AgeAtBiospecimenCollection = Slot(uri=INCLUDE['assay/AgeAtBiospecimenCollection'], name="AgeAtBiospecimenCollection", curie=INCLUDE.curie('assay/AgeAtBiospecimenCollection'),
                   model_uri=INCLUDE.AgeAtBiospecimenCollection, domain=None, range=Optional[int])

slots.BiospecimenStorage = Slot(uri=INCLUDE['assay/BiospecimenStorage'], name="BiospecimenStorage", curie=INCLUDE.curie('assay/BiospecimenStorage'),
                   model_uri=INCLUDE.BiospecimenStorage, domain=None, range=Optional[str])

slots.CollectionID = Slot(uri=INCLUDE['assay/CollectionID'], name="CollectionID", curie=INCLUDE.curie('assay/CollectionID'),
                   model_uri=INCLUDE.CollectionID, domain=None, range=Optional[str])

slots.CollectionSampleType = Slot(uri=INCLUDE['assay/CollectionSampleType'], name="CollectionSampleType", curie=INCLUDE.curie('assay/CollectionSampleType'),
                   model_uri=INCLUDE.CollectionSampleType, domain=None, range=Optional[str])

slots.ContainerID = Slot(uri=INCLUDE['assay/ContainerID'], name="ContainerID", curie=INCLUDE.curie('assay/ContainerID'),
                   model_uri=INCLUDE.ContainerID, domain=None, range=Optional[str])

slots.DataAccess = Slot(uri=INCLUDE['assay/DataAccess'], name="DataAccess", curie=INCLUDE.curie('assay/DataAccess'),
                   model_uri=INCLUDE.DataAccess, domain=None, range=Optional[Union[str, "EnumDataAccess"]])

slots.DataCategory = Slot(uri=INCLUDE['assay/DataCategory'], name="DataCategory", curie=INCLUDE.curie('assay/DataCategory'),
                   model_uri=INCLUDE.DataCategory, domain=None, range=str)

slots.DataType = Slot(uri=INCLUDE['assay/DataType'], name="DataType", curie=INCLUDE.curie('assay/DataType'),
                   model_uri=INCLUDE.DataType, domain=None, range=Optional[str])

slots.ExperimentalStrategy = Slot(uri=INCLUDE['assay/ExperimentalStrategy'], name="ExperimentalStrategy", curie=INCLUDE.curie('assay/ExperimentalStrategy'),
                   model_uri=INCLUDE.ExperimentalStrategy, domain=None, range=Optional[str])

slots.FileID = Slot(uri=INCLUDE['assay/FileID'], name="FileID", curie=INCLUDE.curie('assay/FileID'),
                   model_uri=INCLUDE.FileID, domain=None, range=Optional[str])

slots.FileName = Slot(uri=INCLUDE['assay/FileName'], name="FileName", curie=INCLUDE.curie('assay/FileName'),
                   model_uri=INCLUDE.FileName, domain=None, range=str)

slots.Format = Slot(uri=INCLUDE['assay/Format'], name="Format", curie=INCLUDE.curie('assay/Format'),
                   model_uri=INCLUDE.Format, domain=None, range=str)

slots.HasAliquot = Slot(uri=INCLUDE['assay/HasAliquot'], name="HasAliquot", curie=INCLUDE.curie('assay/HasAliquot'),
                   model_uri=INCLUDE.HasAliquot, domain=None, range=Optional[Union[dict, Aliquot]])

slots.HasBiospecimen = Slot(uri=INCLUDE['assay/HasBiospecimen'], name="HasBiospecimen", curie=INCLUDE.curie('assay/HasBiospecimen'),
                   model_uri=INCLUDE.HasBiospecimen, domain=None, range=Optional[Union[dict, Biospecimen]])

slots.HasDatafile = Slot(uri=INCLUDE['assay/HasDatafile'], name="HasDatafile", curie=INCLUDE.curie('assay/HasDatafile'),
                   model_uri=INCLUDE.HasDatafile, domain=None, range=Optional[Union[dict, DataFile]])

slots.HasOutput = Slot(uri=INCLUDE['assay/HasOutput'], name="HasOutput", curie=INCLUDE.curie('assay/HasOutput'),
                   model_uri=INCLUDE.HasOutput, domain=None, range=Optional[Union[dict, DataFile]])

slots.LaboratoryProcedure = Slot(uri=INCLUDE['assay/LaboratoryProcedure'], name="LaboratoryProcedure", curie=INCLUDE.curie('assay/LaboratoryProcedure'),
                   model_uri=INCLUDE.LaboratoryProcedure, domain=None, range=Optional[str])

slots.OriginalFileName = Slot(uri=INCLUDE['assay/OriginalFileName'], name="OriginalFileName", curie=INCLUDE.curie('assay/OriginalFileName'),
                   model_uri=INCLUDE.OriginalFileName, domain=None, range=str)

slots.ParentSampleID = Slot(uri=INCLUDE['assay/ParentSampleID'], name="ParentSampleID", curie=INCLUDE.curie('assay/ParentSampleID'),
                   model_uri=INCLUDE.ParentSampleID, domain=None, range=Optional[str])

slots.ParentSampleType = Slot(uri=INCLUDE['assay/ParentSampleType'], name="ParentSampleType", curie=INCLUDE.curie('assay/ParentSampleType'),
                   model_uri=INCLUDE.ParentSampleType, domain=None, range=Optional[str])

slots.SampleAvailability = Slot(uri=INCLUDE['assay/SampleAvailability'], name="SampleAvailability", curie=INCLUDE.curie('assay/SampleAvailability'),
                   model_uri=INCLUDE.SampleAvailability, domain=None, range=Optional[Union[str, "EnumSampleAvailability"]])

slots.SampleID = Slot(uri=INCLUDE['assay/SampleID'], name="SampleID", curie=INCLUDE.curie('assay/SampleID'),
                   model_uri=INCLUDE.SampleID, domain=None, range=str)

slots.SampleType = Slot(uri=INCLUDE['assay/SampleType'], name="SampleType", curie=INCLUDE.curie('assay/SampleType'),
                   model_uri=INCLUDE.SampleType, domain=None, range=str)

slots.Size = Slot(uri=INCLUDE['assay/Size'], name="Size", curie=INCLUDE.curie('assay/Size'),
                   model_uri=INCLUDE.Size, domain=None, range=Optional[str])

slots.UsesBiospecimen = Slot(uri=INCLUDE['assay/UsesBiospecimen'], name="UsesBiospecimen", curie=INCLUDE.curie('assay/UsesBiospecimen'),
                   model_uri=INCLUDE.UsesBiospecimen, domain=None, range=Optional[Union[dict, Biospecimen]])

slots.Volume = Slot(uri=INCLUDE['assay/Volume'], name="Volume", curie=INCLUDE.curie('assay/Volume'),
                   model_uri=INCLUDE.Volume, domain=None, range=Optional[float])

slots.VolumeUnit = Slot(uri=INCLUDE['assay/VolumeUnit'], name="VolumeUnit", curie=INCLUDE.curie('assay/VolumeUnit'),
                   model_uri=INCLUDE.VolumeUnit, domain=None, range=Optional[str])

slots.AgeAtConditionObservation = Slot(uri=INCLUDE['participant/AgeAtConditionObservation'], name="AgeAtConditionObservation", curie=INCLUDE.curie('participant/AgeAtConditionObservation'),
                   model_uri=INCLUDE.AgeAtConditionObservation, domain=None, range=Optional[int])

slots.AgeAtLastVitalStatus = Slot(uri=INCLUDE['participant/AgeAtLastVitalStatus'], name="AgeAtLastVitalStatus", curie=INCLUDE.curie('participant/AgeAtLastVitalStatus'),
                   model_uri=INCLUDE.AgeAtLastVitalStatus, domain=None, range=Optional[int])

slots.ConditionDataSource = Slot(uri=INCLUDE['participant/ConditionDataSource'], name="ConditionDataSource", curie=INCLUDE.curie('participant/ConditionDataSource'),
                   model_uri=INCLUDE.ConditionDataSource, domain=None, range=Optional[Union[str, "EnumConditionDataSource"]])

slots.ConditionInterpretation = Slot(uri=INCLUDE['participant/ConditionInterpretation'], name="ConditionInterpretation", curie=INCLUDE.curie('participant/ConditionInterpretation'),
                   model_uri=INCLUDE.ConditionInterpretation, domain=None, range=Optional[Union[str, "EnumConditionInterpretation"]])

slots.DownSyndromeStatus = Slot(uri=INCLUDE['participant/DownSyndromeStatus'], name="DownSyndromeStatus", curie=INCLUDE.curie('participant/DownSyndromeStatus'),
                   model_uri=INCLUDE.DownSyndromeStatus, domain=None, range=Union[str, "EnumDownSyndromeStatus"])

slots.Ethnicity = Slot(uri=INCLUDE['participant/Ethnicity'], name="Ethnicity", curie=INCLUDE.curie('participant/Ethnicity'),
                   model_uri=INCLUDE.Ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.ExternalID = Slot(uri=INCLUDE['participant/ExternalID'], name="ExternalID", curie=INCLUDE.curie('participant/ExternalID'),
                   model_uri=INCLUDE.ExternalID, domain=None, range=str)

slots.FamilyID = Slot(uri=INCLUDE['participant/FamilyID'], name="FamilyID", curie=INCLUDE.curie('participant/FamilyID'),
                   model_uri=INCLUDE.FamilyID, domain=None, range=Optional[str])

slots.FamilyRelationship = Slot(uri=INCLUDE['participant/FamilyRelationship'], name="FamilyRelationship", curie=INCLUDE.curie('participant/FamilyRelationship'),
                   model_uri=INCLUDE.FamilyRelationship, domain=None, range=Optional[Union[dict, Participant]])

slots.FamilyType = Slot(uri=INCLUDE['participant/FamilyType'], name="FamilyType", curie=INCLUDE.curie('participant/FamilyType'),
                   model_uri=INCLUDE.FamilyType, domain=None, range=Union[str, "EnumFamilyType"])

slots.FatherID = Slot(uri=INCLUDE['participant/FatherID'], name="FatherID", curie=INCLUDE.curie('participant/FatherID'),
                   model_uri=INCLUDE.FatherID, domain=None, range=Optional[str])

slots.HasParticipant = Slot(uri=INCLUDE['participant/HasParticipant'], name="HasParticipant", curie=INCLUDE.curie('participant/HasParticipant'),
                   model_uri=INCLUDE.HasParticipant, domain=None, range=Optional[Union[dict, Participant]])

slots.HasStudy = Slot(uri=INCLUDE['participant/HasStudy'], name="HasStudy", curie=INCLUDE.curie('participant/HasStudy'),
                   model_uri=INCLUDE.HasStudy, domain=None, range=Optional[Union[dict, Study]])

slots.HPOCode = Slot(uri=INCLUDE['participant/HPOCode'], name="HPOCode", curie=INCLUDE.curie('participant/HPOCode'),
                   model_uri=INCLUDE.HPOCode, domain=None, range=Optional[str])

slots.HPOLabel = Slot(uri=INCLUDE['participant/HPOLabel'], name="HPOLabel", curie=INCLUDE.curie('participant/HPOLabel'),
                   model_uri=INCLUDE.HPOLabel, domain=None, range=Optional[str])

slots.MAXOCode = Slot(uri=INCLUDE['participant/MAXOCode'], name="MAXOCode", curie=INCLUDE.curie('participant/MAXOCode'),
                   model_uri=INCLUDE.MAXOCode, domain=None, range=Optional[str])

slots.MAXOLabel = Slot(uri=INCLUDE['participant/MAXOLabel'], name="MAXOLabel", curie=INCLUDE.curie('participant/MAXOLabel'),
                   model_uri=INCLUDE.MAXOLabel, domain=None, range=Optional[str])

slots.MONDOCode = Slot(uri=INCLUDE['participant/MONDOCode'], name="MONDOCode", curie=INCLUDE.curie('participant/MONDOCode'),
                   model_uri=INCLUDE.MONDOCode, domain=None, range=Optional[str])

slots.MONDOLabel = Slot(uri=INCLUDE['participant/MONDOLabel'], name="MONDOLabel", curie=INCLUDE.curie('participant/MONDOLabel'),
                   model_uri=INCLUDE.MONDOLabel, domain=None, range=Optional[str])

slots.MotherID = Slot(uri=INCLUDE['participant/MotherID'], name="MotherID", curie=INCLUDE.curie('participant/MotherID'),
                   model_uri=INCLUDE.MotherID, domain=None, range=Optional[str])

slots.OtherCode = Slot(uri=INCLUDE['participant/OtherCode'], name="OtherCode", curie=INCLUDE.curie('participant/OtherCode'),
                   model_uri=INCLUDE.OtherCode, domain=None, range=Optional[str])

slots.OtherLabel = Slot(uri=INCLUDE['participant/OtherLabel'], name="OtherLabel", curie=INCLUDE.curie('participant/OtherLabel'),
                   model_uri=INCLUDE.OtherLabel, domain=None, range=Optional[str])

slots.OutcomesVitalStatus = Slot(uri=INCLUDE['participant/OutcomesVitalStatus'], name="OutcomesVitalStatus", curie=INCLUDE.curie('participant/OutcomesVitalStatus'),
                   model_uri=INCLUDE.OutcomesVitalStatus, domain=None, range=Optional[Union[str, "EnumVitalStatus"]])

slots.ParticipantID = Slot(uri=INCLUDE['participant/ParticipantID'], name="ParticipantID", curie=INCLUDE.curie('participant/ParticipantID'),
                   model_uri=INCLUDE.ParticipantID, domain=None, range=str)

slots.Race = Slot(uri=INCLUDE['participant/Race'], name="Race", curie=INCLUDE.curie('participant/Race'),
                   model_uri=INCLUDE.Race, domain=None, range=Union[str, "EnumRace"])

slots.Sex = Slot(uri=INCLUDE['participant/Sex'], name="Sex", curie=INCLUDE.curie('participant/Sex'),
                   model_uri=INCLUDE.Sex, domain=None, range=Union[str, "EnumSex"])

slots.dbGap = Slot(uri=INCLUDE['study/dbGap'], name="dbGap", curie=INCLUDE.curie('study/dbGap'),
                   model_uri=INCLUDE.dbGap, domain=None, range=Optional[str])

slots.Program = Slot(uri=INCLUDE['study/Program'], name="Program", curie=INCLUDE.curie('study/Program'),
                   model_uri=INCLUDE.Program, domain=None, range=Union[str, "EnumProgram"])

slots.StudyCode = Slot(uri=INCLUDE['study/StudyCode'], name="StudyCode", curie=INCLUDE.curie('study/StudyCode'),
                   model_uri=INCLUDE.StudyCode, domain=None, range=Union[str, "EnumStudyCode"])

slots.StudyName = Slot(uri=INCLUDE['study/StudyName'], name="StudyName", curie=INCLUDE.curie('study/StudyName'),
                   model_uri=INCLUDE.StudyName, domain=None, range=str)