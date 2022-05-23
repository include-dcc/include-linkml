# Auto generated from include_linkml.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-23T07:56:47
# Schema: IncludePortalV1
#
# id: https://w3id.org/include_portal_v1_schema
# description: Initial Include Portal Schema
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
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
INCLUDE = CurieNamespace('include', 'https://w3id.org/include/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = INCLUDE


# Types

# Class references
class BiospecimenSampleId(extended_str):
    pass


class DataFileFileId(extended_str):
    pass


class ParticipantParticipantId(extended_str):
    pass


class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.NamedThing
    class_class_curie: ClassVar[str] = "include:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = INCLUDE.NamedThing


@dataclass
class Biospecimen(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Biospecimen
    class_class_curie: ClassVar[str] = "include:Biospecimen"
    class_name: ClassVar[str] = "Biospecimen"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Biospecimen

    sample_id: Union[str, BiospecimenSampleId] = None
    age_at_biospecimen_collection__days: Optional[int] = None
    biospecimen_storage: Optional[str] = None
    collection_id: Optional[str] = None
    collection_sample_type: Optional[str] = None
    container_id: Optional[str] = None
    has_datafile: Optional[Union[str, DataFileFileId]] = None
    has_participant: Optional[Union[str, ParticipantParticipantId]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    laboratory_procedure: Optional[str] = None
    parent_sample_id: Optional[str] = None
    parent_sample_type: Optional[str] = None
    sample_availability: Optional[Union[str, "EnumSampleAvailability"]] = None
    sample_type: Optional[str] = None
    volume: Optional[str] = None
    volume_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, BiospecimenSampleId):
            self.sample_id = BiospecimenSampleId(self.sample_id)

        if self.age_at_biospecimen_collection__days is not None and not isinstance(self.age_at_biospecimen_collection__days, int):
            self.age_at_biospecimen_collection__days = int(self.age_at_biospecimen_collection__days)

        if self.biospecimen_storage is not None and not isinstance(self.biospecimen_storage, str):
            self.biospecimen_storage = str(self.biospecimen_storage)

        if self.collection_id is not None and not isinstance(self.collection_id, str):
            self.collection_id = str(self.collection_id)

        if self.collection_sample_type is not None and not isinstance(self.collection_sample_type, str):
            self.collection_sample_type = str(self.collection_sample_type)

        if self.container_id is not None and not isinstance(self.container_id, str):
            self.container_id = str(self.container_id)

        if self.has_datafile is not None and not isinstance(self.has_datafile, DataFileFileId):
            self.has_datafile = DataFileFileId(self.has_datafile)

        if self.has_participant is not None and not isinstance(self.has_participant, ParticipantParticipantId):
            self.has_participant = ParticipantParticipantId(self.has_participant)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.laboratory_procedure is not None and not isinstance(self.laboratory_procedure, str):
            self.laboratory_procedure = str(self.laboratory_procedure)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, str):
            self.parent_sample_id = str(self.parent_sample_id)

        if self.parent_sample_type is not None and not isinstance(self.parent_sample_type, str):
            self.parent_sample_type = str(self.parent_sample_type)

        if self.sample_availability is not None and not isinstance(self.sample_availability, EnumSampleAvailability):
            self.sample_availability = EnumSampleAvailability(self.sample_availability)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.volume_unit is not None and not isinstance(self.volume_unit, str):
            self.volume_unit = str(self.volume_unit)

        super().__post_init__(**kwargs)


@dataclass
class DataFile(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.DataFile
    class_class_curie: ClassVar[str] = "include:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = INCLUDE.DataFile

    file_id: Union[str, DataFileFileId] = None
    access_url: Optional[str] = None
    collection_id: Optional[str] = None
    data_access: Optional[Union[str, "EnumDataAccess"]] = None
    data_category: Optional[str] = None
    data_type: Optional[str] = None
    experimental_strategy: Optional[str] = None
    file_name: Optional[str] = None
    format: Optional[str] = None
    has_biospecimen: Optional[Union[str, BiospecimenSampleId]] = None
    has_participant: Optional[Union[str, ParticipantParticipantId]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    participant_id: Optional[str] = None
    size: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, DataFileFileId):
            self.file_id = DataFileFileId(self.file_id)

        if self.access_url is not None and not isinstance(self.access_url, str):
            self.access_url = str(self.access_url)

        if self.collection_id is not None and not isinstance(self.collection_id, str):
            self.collection_id = str(self.collection_id)

        if self.data_access is not None and not isinstance(self.data_access, EnumDataAccess):
            self.data_access = EnumDataAccess(self.data_access)

        if self.data_category is not None and not isinstance(self.data_category, str):
            self.data_category = str(self.data_category)

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        if self.experimental_strategy is not None and not isinstance(self.experimental_strategy, str):
            self.experimental_strategy = str(self.experimental_strategy)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.has_biospecimen is not None and not isinstance(self.has_biospecimen, BiospecimenSampleId):
            self.has_biospecimen = BiospecimenSampleId(self.has_biospecimen)

        if self.has_participant is not None and not isinstance(self.has_participant, ParticipantParticipantId):
            self.has_participant = ParticipantParticipantId(self.has_participant)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        super().__post_init__(**kwargs)


@dataclass
class Participant(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Participant
    class_class_curie: ClassVar[str] = "include:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Participant

    participant_id: Union[str, ParticipantParticipantId] = None
    down_syndrome_status: Union[str, "EnumDownSyndromeStatus"] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    external_id: str = None
    race: Union[str, "EnumRace"] = None
    sex: Union[str, "EnumSex"] = None
    age_at_diagnosis__days: Optional[int] = None
    age_at_phenotype_assignment__days: Optional[int] = None
    age_at_the_last_vital_status__days: Optional[int] = None
    diagnosis__icd: Optional[str] = None
    diagnosis__mondo: Optional[str] = None
    diagnosis__ncit: Optional[str] = None
    diagnosis__source_text: Optional[str] = None
    diagnosis_type: Optional[str] = None
    family_id: Optional[str] = None
    family_relationship: Optional[str] = None
    family_type: Optional[Union[str, "EnumFamilyType"]] = None
    father_id: Optional[str] = None
    has_datafile: Optional[Union[str, DataFileFileId]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    mother_id: Optional[str] = None
    outcomes_vital_status: Optional[str] = None
    phenotype__hpo: Optional[str] = None
    phenotype__source_text: Optional[str] = None
    phenotype_interpretation: Optional[Union[str, "EnumPhenotypeInterpretation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.down_syndrome_status):
            self.MissingRequiredField("down_syndrome_status")
        if not isinstance(self.down_syndrome_status, EnumDownSyndromeStatus):
            self.down_syndrome_status = EnumDownSyndromeStatus(self.down_syndrome_status)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self._is_empty(self.external_id):
            self.MissingRequiredField("external_id")
        if not isinstance(self.external_id, str):
            self.external_id = str(self.external_id)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, EnumRace):
            self.race = EnumRace(self.race)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        if self.age_at_diagnosis__days is not None and not isinstance(self.age_at_diagnosis__days, int):
            self.age_at_diagnosis__days = int(self.age_at_diagnosis__days)

        if self.age_at_phenotype_assignment__days is not None and not isinstance(self.age_at_phenotype_assignment__days, int):
            self.age_at_phenotype_assignment__days = int(self.age_at_phenotype_assignment__days)

        if self.age_at_the_last_vital_status__days is not None and not isinstance(self.age_at_the_last_vital_status__days, int):
            self.age_at_the_last_vital_status__days = int(self.age_at_the_last_vital_status__days)

        if self.diagnosis__icd is not None and not isinstance(self.diagnosis__icd, str):
            self.diagnosis__icd = str(self.diagnosis__icd)

        if self.diagnosis__mondo is not None and not isinstance(self.diagnosis__mondo, str):
            self.diagnosis__mondo = str(self.diagnosis__mondo)

        if self.diagnosis__ncit is not None and not isinstance(self.diagnosis__ncit, str):
            self.diagnosis__ncit = str(self.diagnosis__ncit)

        if self.diagnosis__source_text is not None and not isinstance(self.diagnosis__source_text, str):
            self.diagnosis__source_text = str(self.diagnosis__source_text)

        if self.diagnosis_type is not None and not isinstance(self.diagnosis_type, str):
            self.diagnosis_type = str(self.diagnosis_type)

        if self.family_id is not None and not isinstance(self.family_id, str):
            self.family_id = str(self.family_id)

        if self.family_relationship is not None and not isinstance(self.family_relationship, str):
            self.family_relationship = str(self.family_relationship)

        if self.family_type is not None and not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

        if self.father_id is not None and not isinstance(self.father_id, str):
            self.father_id = str(self.father_id)

        if self.has_datafile is not None and not isinstance(self.has_datafile, DataFileFileId):
            self.has_datafile = DataFileFileId(self.has_datafile)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.mother_id is not None and not isinstance(self.mother_id, str):
            self.mother_id = str(self.mother_id)

        if self.outcomes_vital_status is not None and not isinstance(self.outcomes_vital_status, str):
            self.outcomes_vital_status = str(self.outcomes_vital_status)

        if self.phenotype__hpo is not None and not isinstance(self.phenotype__hpo, str):
            self.phenotype__hpo = str(self.phenotype__hpo)

        if self.phenotype__source_text is not None and not isinstance(self.phenotype__source_text, str):
            self.phenotype__source_text = str(self.phenotype__source_text)

        if self.phenotype_interpretation is not None and not isinstance(self.phenotype_interpretation, EnumPhenotypeInterpretation):
            self.phenotype_interpretation = EnumPhenotypeInterpretation(self.phenotype_interpretation)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Study
    class_class_curie: ClassVar[str] = "include:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Study

    program: Union[str, "EnumProgram"] = None
    study_code: Union[str, "EnumStudyCode"] = None
    study_name: str = None
    dbgap: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.program):
            self.MissingRequiredField("program")
        if not isinstance(self.program, EnumProgram):
            self.program = EnumProgram(self.program)

        if self._is_empty(self.study_code):
            self.MissingRequiredField("study_code")
        if not isinstance(self.study_code, EnumStudyCode):
            self.study_code = EnumStudyCode(self.study_code)

        if self._is_empty(self.study_name):
            self.MissingRequiredField("study_name")
        if not isinstance(self.study_name, str):
            self.study_name = str(self.study_name)

        if self.dbgap is not None and not isinstance(self.dbgap, str):
            self.dbgap = str(self.dbgap)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataAccess(EnumDefinitionImpl):

    Controlled = PermissibleValue(text="Controlled")
    Open = PermissibleValue(text="Open")
    Registered = PermissibleValue(text="Registered")

    _defn = EnumDefinition(
        name="EnumDataAccess",
    )

class EnumDownSyndromeStatus(EnumDefinitionImpl):

    D21 = PermissibleValue(text="D21")
    T21 = PermissibleValue(text="T21")

    _defn = EnumDefinition(
        name="EnumDownSyndromeStatus",
    )

class EnumEthnicity(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumEthnicity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Asked but unknown",
                PermissibleValue(text="Asked but unknown") )
        setattr(cls, "Hispanic or Latino",
                PermissibleValue(text="Hispanic or Latino") )
        setattr(cls, "Not Hispanic or Latino",
                PermissibleValue(text="Not Hispanic or Latino") )

class EnumFamilyType(EnumDefinitionImpl):

    Duo = PermissibleValue(text="Duo")
    Other = PermissibleValue(text="Other")
    Trio = PermissibleValue(text="Trio")

    _defn = EnumDefinition(
        name="EnumFamilyType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Proband-only",
                PermissibleValue(text="Proband-only") )

class EnumPhenotypeInterpretation(EnumDefinitionImpl):

    Observed = PermissibleValue(text="Observed")

    _defn = EnumDefinition(
        name="EnumPhenotypeInterpretation",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Observed",
                PermissibleValue(text="Not Observed") )

class EnumProgram(EnumDefinitionImpl):

    INCLUDE = PermissibleValue(text="INCLUDE")
    KF = PermissibleValue(text="KF")

    _defn = EnumDefinition(
        name="EnumProgram",
    )

class EnumRace(EnumDefinitionImpl):

    Asian = PermissibleValue(text="Asian")
    Other = PermissibleValue(text="Other")
    White = PermissibleValue(text="White")

    _defn = EnumDefinition(
        name="EnumRace",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Indian or Alaska Native",
                PermissibleValue(text="American Indian or Alaska Native") )
        setattr(cls, "Black or African American",
                PermissibleValue(text="Black or African American") )
        setattr(cls, "More than one race",
                PermissibleValue(text="More than one race") )
        setattr(cls, "Native Hawaiian or Other Pacific Islander",
                PermissibleValue(text="Native Hawaiian or Other Pacific Islander") )

class EnumSampleAvailability(EnumDefinitionImpl):

    Available = PermissibleValue(text="Available")
    Unavailable = PermissibleValue(text="Unavailable")

    _defn = EnumDefinition(
        name="EnumSampleAvailability",
    )

class EnumSex(EnumDefinitionImpl):

    Female = PermissibleValue(text="Female")
    Male = PermissibleValue(text="Male")
    Other = PermissibleValue(text="Other")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="EnumSex",
    )

class EnumStudyCode(EnumDefinitionImpl):

    DSC = PermissibleValue(text="DSC")
    HTP = PermissibleValue(text="HTP")

    _defn = EnumDefinition(
        name="EnumStudyCode",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DS-COG-ALL",
                PermissibleValue(text="DS-COG-ALL") )
        setattr(cls, "DS-PCGC",
                PermissibleValue(text="DS-PCGC") )
        setattr(cls, "DS360-CHD",
                PermissibleValue(text="DS360-CHD") )

# Slots
class slots:
    pass

slots.age_at_biospecimen_collection__days = Slot(uri=INCLUDE.age_at_biospecimen_collection__days, name="age_at_biospecimen_collection__days", curie=INCLUDE.curie('age_at_biospecimen_collection__days'),
                   model_uri=INCLUDE.age_at_biospecimen_collection__days, domain=None, range=Optional[str])

slots.biospecimen_storage = Slot(uri=INCLUDE.biospecimen_storage, name="biospecimen_storage", curie=INCLUDE.curie('biospecimen_storage'),
                   model_uri=INCLUDE.biospecimen_storage, domain=None, range=Optional[str])

slots.collection_id = Slot(uri=INCLUDE.collection_id, name="collection_id", curie=INCLUDE.curie('collection_id'),
                   model_uri=INCLUDE.collection_id, domain=None, range=Optional[str])

slots.collection_sample_type = Slot(uri=INCLUDE.collection_sample_type, name="collection_sample_type", curie=INCLUDE.curie('collection_sample_type'),
                   model_uri=INCLUDE.collection_sample_type, domain=None, range=Optional[str])

slots.container_id = Slot(uri=INCLUDE.container_id, name="container_id", curie=INCLUDE.curie('container_id'),
                   model_uri=INCLUDE.container_id, domain=None, range=Optional[str])

slots.has_datafile = Slot(uri=INCLUDE.has_datafile, name="has_datafile", curie=INCLUDE.curie('has_datafile'),
                   model_uri=INCLUDE.has_datafile, domain=None, range=Optional[Union[str, DataFileFileId]])

slots.has_participant = Slot(uri=INCLUDE.has_participant, name="has_participant", curie=INCLUDE.curie('has_participant'),
                   model_uri=INCLUDE.has_participant, domain=None, range=Optional[Union[str, ParticipantParticipantId]])

slots.has_study = Slot(uri=INCLUDE.has_study, name="has_study", curie=INCLUDE.curie('has_study'),
                   model_uri=INCLUDE.has_study, domain=None, range=Optional[Union[dict, Study]])

slots.laboratory_procedure = Slot(uri=INCLUDE.laboratory_procedure, name="laboratory_procedure", curie=INCLUDE.curie('laboratory_procedure'),
                   model_uri=INCLUDE.laboratory_procedure, domain=None, range=Optional[str])

slots.parent_sample_id = Slot(uri=INCLUDE.parent_sample_id, name="parent_sample_id", curie=INCLUDE.curie('parent_sample_id'),
                   model_uri=INCLUDE.parent_sample_id, domain=None, range=Optional[str])

slots.parent_sample_type = Slot(uri=INCLUDE.parent_sample_type, name="parent_sample_type", curie=INCLUDE.curie('parent_sample_type'),
                   model_uri=INCLUDE.parent_sample_type, domain=None, range=Optional[str])

slots.sample_availability = Slot(uri=INCLUDE.sample_availability, name="sample_availability", curie=INCLUDE.curie('sample_availability'),
                   model_uri=INCLUDE.sample_availability, domain=None, range=Optional[str])

slots.sample_id = Slot(uri=INCLUDE.sample_id, name="sample_id", curie=INCLUDE.curie('sample_id'),
                   model_uri=INCLUDE.sample_id, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=INCLUDE.sample_type, name="sample_type", curie=INCLUDE.curie('sample_type'),
                   model_uri=INCLUDE.sample_type, domain=None, range=Optional[str])

slots.volume = Slot(uri=INCLUDE.volume, name="volume", curie=INCLUDE.curie('volume'),
                   model_uri=INCLUDE.volume, domain=None, range=Optional[str])

slots.volume_unit = Slot(uri=INCLUDE.volume_unit, name="volume_unit", curie=INCLUDE.curie('volume_unit'),
                   model_uri=INCLUDE.volume_unit, domain=None, range=Optional[str])

slots.access_url = Slot(uri=INCLUDE.access_url, name="access_url", curie=INCLUDE.curie('access_url'),
                   model_uri=INCLUDE.access_url, domain=None, range=Optional[str])

slots.data_access = Slot(uri=INCLUDE.data_access, name="data_access", curie=INCLUDE.curie('data_access'),
                   model_uri=INCLUDE.data_access, domain=None, range=Optional[str])

slots.data_category = Slot(uri=INCLUDE.data_category, name="data_category", curie=INCLUDE.curie('data_category'),
                   model_uri=INCLUDE.data_category, domain=None, range=Optional[str])

slots.data_type = Slot(uri=INCLUDE.data_type, name="data_type", curie=INCLUDE.curie('data_type'),
                   model_uri=INCLUDE.data_type, domain=None, range=Optional[str])

slots.experimental_strategy = Slot(uri=INCLUDE.experimental_strategy, name="experimental_strategy", curie=INCLUDE.curie('experimental_strategy'),
                   model_uri=INCLUDE.experimental_strategy, domain=None, range=Optional[str])

slots.file_id = Slot(uri=INCLUDE.file_id, name="file_id", curie=INCLUDE.curie('file_id'),
                   model_uri=INCLUDE.file_id, domain=None, range=Optional[str])

slots.file_name = Slot(uri=INCLUDE.file_name, name="file_name", curie=INCLUDE.curie('file_name'),
                   model_uri=INCLUDE.file_name, domain=None, range=Optional[str])

slots.format = Slot(uri=INCLUDE.format, name="format", curie=INCLUDE.curie('format'),
                   model_uri=INCLUDE.format, domain=None, range=Optional[str])

slots.has_biospecimen = Slot(uri=INCLUDE.has_biospecimen, name="has_biospecimen", curie=INCLUDE.curie('has_biospecimen'),
                   model_uri=INCLUDE.has_biospecimen, domain=None, range=Optional[Union[str, BiospecimenSampleId]])

slots.participant_id = Slot(uri=INCLUDE.participant_id, name="participant_id", curie=INCLUDE.curie('participant_id'),
                   model_uri=INCLUDE.participant_id, domain=None, range=Optional[str])

slots.size = Slot(uri=INCLUDE.size, name="size", curie=INCLUDE.curie('size'),
                   model_uri=INCLUDE.size, domain=None, range=Optional[str])

slots.age_at_diagnosis__days = Slot(uri=INCLUDE.age_at_diagnosis__days, name="age_at_diagnosis__days", curie=INCLUDE.curie('age_at_diagnosis__days'),
                   model_uri=INCLUDE.age_at_diagnosis__days, domain=None, range=Optional[str])

slots.age_at_phenotype_assignment__days = Slot(uri=INCLUDE.age_at_phenotype_assignment__days, name="age_at_phenotype_assignment__days", curie=INCLUDE.curie('age_at_phenotype_assignment__days'),
                   model_uri=INCLUDE.age_at_phenotype_assignment__days, domain=None, range=Optional[str])

slots.age_at_the_last_vital_status__days = Slot(uri=INCLUDE.age_at_the_last_vital_status__days, name="age_at_the_last_vital_status__days", curie=INCLUDE.curie('age_at_the_last_vital_status__days'),
                   model_uri=INCLUDE.age_at_the_last_vital_status__days, domain=None, range=Optional[str])

slots.diagnosis__icd = Slot(uri=INCLUDE.diagnosis__icd, name="diagnosis__icd", curie=INCLUDE.curie('diagnosis__icd'),
                   model_uri=INCLUDE.diagnosis__icd, domain=None, range=Optional[str])

slots.diagnosis__mondo = Slot(uri=INCLUDE.diagnosis__mondo, name="diagnosis__mondo", curie=INCLUDE.curie('diagnosis__mondo'),
                   model_uri=INCLUDE.diagnosis__mondo, domain=None, range=Optional[str])

slots.diagnosis__ncit = Slot(uri=INCLUDE.diagnosis__ncit, name="diagnosis__ncit", curie=INCLUDE.curie('diagnosis__ncit'),
                   model_uri=INCLUDE.diagnosis__ncit, domain=None, range=Optional[str])

slots.diagnosis__source_text = Slot(uri=INCLUDE.diagnosis__source_text, name="diagnosis__source_text", curie=INCLUDE.curie('diagnosis__source_text'),
                   model_uri=INCLUDE.diagnosis__source_text, domain=None, range=Optional[str])

slots.diagnosis_type = Slot(uri=INCLUDE.diagnosis_type, name="diagnosis_type", curie=INCLUDE.curie('diagnosis_type'),
                   model_uri=INCLUDE.diagnosis_type, domain=None, range=Optional[str])

slots.down_syndrome_status = Slot(uri=INCLUDE.down_syndrome_status, name="down_syndrome_status", curie=INCLUDE.curie('down_syndrome_status'),
                   model_uri=INCLUDE.down_syndrome_status, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=INCLUDE.ethnicity, name="ethnicity", curie=INCLUDE.curie('ethnicity'),
                   model_uri=INCLUDE.ethnicity, domain=None, range=Optional[str])

slots.external_id = Slot(uri=INCLUDE.external_id, name="external_id", curie=INCLUDE.curie('external_id'),
                   model_uri=INCLUDE.external_id, domain=None, range=Optional[str])

slots.family_id = Slot(uri=INCLUDE.family_id, name="family_id", curie=INCLUDE.curie('family_id'),
                   model_uri=INCLUDE.family_id, domain=None, range=Optional[str])

slots.family_relationship = Slot(uri=INCLUDE.family_relationship, name="family_relationship", curie=INCLUDE.curie('family_relationship'),
                   model_uri=INCLUDE.family_relationship, domain=None, range=Optional[str])

slots.family_type = Slot(uri=INCLUDE.family_type, name="family_type", curie=INCLUDE.curie('family_type'),
                   model_uri=INCLUDE.family_type, domain=None, range=Optional[str])

slots.father_id = Slot(uri=INCLUDE.father_id, name="father_id", curie=INCLUDE.curie('father_id'),
                   model_uri=INCLUDE.father_id, domain=None, range=Optional[str])

slots.mother_id = Slot(uri=INCLUDE.mother_id, name="mother_id", curie=INCLUDE.curie('mother_id'),
                   model_uri=INCLUDE.mother_id, domain=None, range=Optional[str])

slots.outcomes_vital_status = Slot(uri=INCLUDE.outcomes_vital_status, name="outcomes_vital_status", curie=INCLUDE.curie('outcomes_vital_status'),
                   model_uri=INCLUDE.outcomes_vital_status, domain=None, range=Optional[str])

slots.phenotype__hpo = Slot(uri=INCLUDE.phenotype__hpo, name="phenotype__hpo", curie=INCLUDE.curie('phenotype__hpo'),
                   model_uri=INCLUDE.phenotype__hpo, domain=None, range=Optional[str])

slots.phenotype__source_text = Slot(uri=INCLUDE.phenotype__source_text, name="phenotype__source_text", curie=INCLUDE.curie('phenotype__source_text'),
                   model_uri=INCLUDE.phenotype__source_text, domain=None, range=Optional[str])

slots.phenotype_interpretation = Slot(uri=INCLUDE.phenotype_interpretation, name="phenotype_interpretation", curie=INCLUDE.curie('phenotype_interpretation'),
                   model_uri=INCLUDE.phenotype_interpretation, domain=None, range=Optional[str])

slots.race = Slot(uri=INCLUDE.race, name="race", curie=INCLUDE.curie('race'),
                   model_uri=INCLUDE.race, domain=None, range=Optional[str])

slots.sex = Slot(uri=INCLUDE.sex, name="sex", curie=INCLUDE.curie('sex'),
                   model_uri=INCLUDE.sex, domain=None, range=Optional[str])

slots.dbgap = Slot(uri=INCLUDE.dbgap, name="dbgap", curie=INCLUDE.curie('dbgap'),
                   model_uri=INCLUDE.dbgap, domain=None, range=Optional[str])

slots.program = Slot(uri=INCLUDE.program, name="program", curie=INCLUDE.curie('program'),
                   model_uri=INCLUDE.program, domain=None, range=Optional[str])

slots.study_code = Slot(uri=INCLUDE.study_code, name="study_code", curie=INCLUDE.curie('study_code'),
                   model_uri=INCLUDE.study_code, domain=None, range=Optional[str])

slots.study_name = Slot(uri=INCLUDE.study_name, name="study_name", curie=INCLUDE.curie('study_name'),
                   model_uri=INCLUDE.study_name, domain=None, range=Optional[str])

slots.Biospecimen_age_at_biospecimen_collection__days = Slot(uri=INCLUDE.age_at_biospecimen_collection__days, name="Biospecimen_age_at_biospecimen_collection__days", curie=INCLUDE.curie('age_at_biospecimen_collection__days'),
                   model_uri=INCLUDE.Biospecimen_age_at_biospecimen_collection__days, domain=Biospecimen, range=Optional[int])

slots.Biospecimen_biospecimen_storage = Slot(uri=INCLUDE.biospecimen_storage, name="Biospecimen_biospecimen_storage", curie=INCLUDE.curie('biospecimen_storage'),
                   model_uri=INCLUDE.Biospecimen_biospecimen_storage, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_collection_id = Slot(uri=INCLUDE.collection_id, name="Biospecimen_collection_id", curie=INCLUDE.curie('collection_id'),
                   model_uri=INCLUDE.Biospecimen_collection_id, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_collection_sample_type = Slot(uri=INCLUDE.collection_sample_type, name="Biospecimen_collection_sample_type", curie=INCLUDE.curie('collection_sample_type'),
                   model_uri=INCLUDE.Biospecimen_collection_sample_type, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_container_id = Slot(uri=INCLUDE.container_id, name="Biospecimen_container_id", curie=INCLUDE.curie('container_id'),
                   model_uri=INCLUDE.Biospecimen_container_id, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_has_datafile = Slot(uri=INCLUDE.has_datafile, name="Biospecimen_has_datafile", curie=INCLUDE.curie('has_datafile'),
                   model_uri=INCLUDE.Biospecimen_has_datafile, domain=Biospecimen, range=Optional[Union[str, DataFileFileId]])

slots.Biospecimen_has_participant = Slot(uri=INCLUDE.has_participant, name="Biospecimen_has_participant", curie=INCLUDE.curie('has_participant'),
                   model_uri=INCLUDE.Biospecimen_has_participant, domain=Biospecimen, range=Optional[Union[str, ParticipantParticipantId]])

slots.Biospecimen_has_study = Slot(uri=INCLUDE.has_study, name="Biospecimen_has_study", curie=INCLUDE.curie('has_study'),
                   model_uri=INCLUDE.Biospecimen_has_study, domain=Biospecimen, range=Optional[Union[dict, "Study"]])

slots.Biospecimen_laboratory_procedure = Slot(uri=INCLUDE.laboratory_procedure, name="Biospecimen_laboratory_procedure", curie=INCLUDE.curie('laboratory_procedure'),
                   model_uri=INCLUDE.Biospecimen_laboratory_procedure, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_parent_sample_id = Slot(uri=INCLUDE.parent_sample_id, name="Biospecimen_parent_sample_id", curie=INCLUDE.curie('parent_sample_id'),
                   model_uri=INCLUDE.Biospecimen_parent_sample_id, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_parent_sample_type = Slot(uri=INCLUDE.parent_sample_type, name="Biospecimen_parent_sample_type", curie=INCLUDE.curie('parent_sample_type'),
                   model_uri=INCLUDE.Biospecimen_parent_sample_type, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_sample_availability = Slot(uri=INCLUDE.sample_availability, name="Biospecimen_sample_availability", curie=INCLUDE.curie('sample_availability'),
                   model_uri=INCLUDE.Biospecimen_sample_availability, domain=Biospecimen, range=Optional[Union[str, "EnumSampleAvailability"]])

slots.Biospecimen_sample_id = Slot(uri=INCLUDE.sample_id, name="Biospecimen_sample_id", curie=INCLUDE.curie('sample_id'),
                   model_uri=INCLUDE.Biospecimen_sample_id, domain=Biospecimen, range=Union[str, BiospecimenSampleId])

slots.Biospecimen_sample_type = Slot(uri=INCLUDE.sample_type, name="Biospecimen_sample_type", curie=INCLUDE.curie('sample_type'),
                   model_uri=INCLUDE.Biospecimen_sample_type, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_volume = Slot(uri=INCLUDE.volume, name="Biospecimen_volume", curie=INCLUDE.curie('volume'),
                   model_uri=INCLUDE.Biospecimen_volume, domain=Biospecimen, range=Optional[str])

slots.Biospecimen_volume_unit = Slot(uri=INCLUDE.volume_unit, name="Biospecimen_volume_unit", curie=INCLUDE.curie('volume_unit'),
                   model_uri=INCLUDE.Biospecimen_volume_unit, domain=Biospecimen, range=Optional[str])

slots.DataFile_access_url = Slot(uri=INCLUDE.access_url, name="DataFile_access_url", curie=INCLUDE.curie('access_url'),
                   model_uri=INCLUDE.DataFile_access_url, domain=DataFile, range=Optional[str])

slots.DataFile_collection_id = Slot(uri=INCLUDE.collection_id, name="DataFile_collection_id", curie=INCLUDE.curie('collection_id'),
                   model_uri=INCLUDE.DataFile_collection_id, domain=DataFile, range=Optional[str])

slots.DataFile_data_access = Slot(uri=INCLUDE.data_access, name="DataFile_data_access", curie=INCLUDE.curie('data_access'),
                   model_uri=INCLUDE.DataFile_data_access, domain=DataFile, range=Optional[Union[str, "EnumDataAccess"]])

slots.DataFile_data_category = Slot(uri=INCLUDE.data_category, name="DataFile_data_category", curie=INCLUDE.curie('data_category'),
                   model_uri=INCLUDE.DataFile_data_category, domain=DataFile, range=Optional[str])

slots.DataFile_data_type = Slot(uri=INCLUDE.data_type, name="DataFile_data_type", curie=INCLUDE.curie('data_type'),
                   model_uri=INCLUDE.DataFile_data_type, domain=DataFile, range=Optional[str])

slots.DataFile_experimental_strategy = Slot(uri=INCLUDE.experimental_strategy, name="DataFile_experimental_strategy", curie=INCLUDE.curie('experimental_strategy'),
                   model_uri=INCLUDE.DataFile_experimental_strategy, domain=DataFile, range=Optional[str])

slots.DataFile_file_id = Slot(uri=INCLUDE.file_id, name="DataFile_file_id", curie=INCLUDE.curie('file_id'),
                   model_uri=INCLUDE.DataFile_file_id, domain=DataFile, range=Union[str, DataFileFileId])

slots.DataFile_file_name = Slot(uri=INCLUDE.file_name, name="DataFile_file_name", curie=INCLUDE.curie('file_name'),
                   model_uri=INCLUDE.DataFile_file_name, domain=DataFile, range=Optional[str])

slots.DataFile_format = Slot(uri=INCLUDE.format, name="DataFile_format", curie=INCLUDE.curie('format'),
                   model_uri=INCLUDE.DataFile_format, domain=DataFile, range=Optional[str])

slots.DataFile_has_biospecimen = Slot(uri=INCLUDE.has_biospecimen, name="DataFile_has_biospecimen", curie=INCLUDE.curie('has_biospecimen'),
                   model_uri=INCLUDE.DataFile_has_biospecimen, domain=DataFile, range=Optional[Union[str, BiospecimenSampleId]])

slots.DataFile_has_participant = Slot(uri=INCLUDE.has_participant, name="DataFile_has_participant", curie=INCLUDE.curie('has_participant'),
                   model_uri=INCLUDE.DataFile_has_participant, domain=DataFile, range=Optional[Union[str, ParticipantParticipantId]])

slots.DataFile_has_study = Slot(uri=INCLUDE.has_study, name="DataFile_has_study", curie=INCLUDE.curie('has_study'),
                   model_uri=INCLUDE.DataFile_has_study, domain=DataFile, range=Optional[Union[dict, "Study"]])

slots.DataFile_participant_id = Slot(uri=INCLUDE.participant_id, name="DataFile_participant_id", curie=INCLUDE.curie('participant_id'),
                   model_uri=INCLUDE.DataFile_participant_id, domain=DataFile, range=Optional[str])

slots.DataFile_size = Slot(uri=INCLUDE.size, name="DataFile_size", curie=INCLUDE.curie('size'),
                   model_uri=INCLUDE.DataFile_size, domain=DataFile, range=Optional[str])

slots.Participant_age_at_diagnosis__days = Slot(uri=INCLUDE.age_at_diagnosis__days, name="Participant_age_at_diagnosis__days", curie=INCLUDE.curie('age_at_diagnosis__days'),
                   model_uri=INCLUDE.Participant_age_at_diagnosis__days, domain=Participant, range=Optional[int])

slots.Participant_age_at_phenotype_assignment__days = Slot(uri=INCLUDE.age_at_phenotype_assignment__days, name="Participant_age_at_phenotype_assignment__days", curie=INCLUDE.curie('age_at_phenotype_assignment__days'),
                   model_uri=INCLUDE.Participant_age_at_phenotype_assignment__days, domain=Participant, range=Optional[int])

slots.Participant_age_at_the_last_vital_status__days = Slot(uri=INCLUDE.age_at_the_last_vital_status__days, name="Participant_age_at_the_last_vital_status__days", curie=INCLUDE.curie('age_at_the_last_vital_status__days'),
                   model_uri=INCLUDE.Participant_age_at_the_last_vital_status__days, domain=Participant, range=Optional[int])

slots.Participant_diagnosis__icd = Slot(uri=INCLUDE.diagnosis__icd, name="Participant_diagnosis__icd", curie=INCLUDE.curie('diagnosis__icd'),
                   model_uri=INCLUDE.Participant_diagnosis__icd, domain=Participant, range=Optional[str])

slots.Participant_diagnosis__mondo = Slot(uri=INCLUDE.diagnosis__mondo, name="Participant_diagnosis__mondo", curie=INCLUDE.curie('diagnosis__mondo'),
                   model_uri=INCLUDE.Participant_diagnosis__mondo, domain=Participant, range=Optional[str])

slots.Participant_diagnosis__ncit = Slot(uri=INCLUDE.diagnosis__ncit, name="Participant_diagnosis__ncit", curie=INCLUDE.curie('diagnosis__ncit'),
                   model_uri=INCLUDE.Participant_diagnosis__ncit, domain=Participant, range=Optional[str])

slots.Participant_diagnosis__source_text = Slot(uri=INCLUDE.diagnosis__source_text, name="Participant_diagnosis__source_text", curie=INCLUDE.curie('diagnosis__source_text'),
                   model_uri=INCLUDE.Participant_diagnosis__source_text, domain=Participant, range=Optional[str])

slots.Participant_diagnosis_type = Slot(uri=INCLUDE.diagnosis_type, name="Participant_diagnosis_type", curie=INCLUDE.curie('diagnosis_type'),
                   model_uri=INCLUDE.Participant_diagnosis_type, domain=Participant, range=Optional[str])

slots.Participant_down_syndrome_status = Slot(uri=INCLUDE.down_syndrome_status, name="Participant_down_syndrome_status", curie=INCLUDE.curie('down_syndrome_status'),
                   model_uri=INCLUDE.Participant_down_syndrome_status, domain=Participant, range=Union[str, "EnumDownSyndromeStatus"])

slots.Participant_ethnicity = Slot(uri=INCLUDE.ethnicity, name="Participant_ethnicity", curie=INCLUDE.curie('ethnicity'),
                   model_uri=INCLUDE.Participant_ethnicity, domain=Participant, range=Union[str, "EnumEthnicity"])

slots.Participant_external_id = Slot(uri=INCLUDE.external_id, name="Participant_external_id", curie=INCLUDE.curie('external_id'),
                   model_uri=INCLUDE.Participant_external_id, domain=Participant, range=str)

slots.Participant_family_id = Slot(uri=INCLUDE.family_id, name="Participant_family_id", curie=INCLUDE.curie('family_id'),
                   model_uri=INCLUDE.Participant_family_id, domain=Participant, range=Optional[str])

slots.Participant_family_relationship = Slot(uri=INCLUDE.family_relationship, name="Participant_family_relationship", curie=INCLUDE.curie('family_relationship'),
                   model_uri=INCLUDE.Participant_family_relationship, domain=Participant, range=Optional[str])

slots.Participant_family_type = Slot(uri=INCLUDE.family_type, name="Participant_family_type", curie=INCLUDE.curie('family_type'),
                   model_uri=INCLUDE.Participant_family_type, domain=Participant, range=Optional[Union[str, "EnumFamilyType"]])

slots.Participant_father_id = Slot(uri=INCLUDE.father_id, name="Participant_father_id", curie=INCLUDE.curie('father_id'),
                   model_uri=INCLUDE.Participant_father_id, domain=Participant, range=Optional[str])

slots.Participant_has_datafile = Slot(uri=INCLUDE.has_datafile, name="Participant_has_datafile", curie=INCLUDE.curie('has_datafile'),
                   model_uri=INCLUDE.Participant_has_datafile, domain=Participant, range=Optional[Union[str, DataFileFileId]])

slots.Participant_has_study = Slot(uri=INCLUDE.has_study, name="Participant_has_study", curie=INCLUDE.curie('has_study'),
                   model_uri=INCLUDE.Participant_has_study, domain=Participant, range=Optional[Union[dict, "Study"]])

slots.Participant_mother_id = Slot(uri=INCLUDE.mother_id, name="Participant_mother_id", curie=INCLUDE.curie('mother_id'),
                   model_uri=INCLUDE.Participant_mother_id, domain=Participant, range=Optional[str])

slots.Participant_outcomes_vital_status = Slot(uri=INCLUDE.outcomes_vital_status, name="Participant_outcomes_vital_status", curie=INCLUDE.curie('outcomes_vital_status'),
                   model_uri=INCLUDE.Participant_outcomes_vital_status, domain=Participant, range=Optional[str])

slots.Participant_participant_id = Slot(uri=INCLUDE.participant_id, name="Participant_participant_id", curie=INCLUDE.curie('participant_id'),
                   model_uri=INCLUDE.Participant_participant_id, domain=Participant, range=Union[str, ParticipantParticipantId])

slots.Participant_phenotype__hpo = Slot(uri=INCLUDE.phenotype__hpo, name="Participant_phenotype__hpo", curie=INCLUDE.curie('phenotype__hpo'),
                   model_uri=INCLUDE.Participant_phenotype__hpo, domain=Participant, range=Optional[str])

slots.Participant_phenotype__source_text = Slot(uri=INCLUDE.phenotype__source_text, name="Participant_phenotype__source_text", curie=INCLUDE.curie('phenotype__source_text'),
                   model_uri=INCLUDE.Participant_phenotype__source_text, domain=Participant, range=Optional[str])

slots.Participant_phenotype_interpretation = Slot(uri=INCLUDE.phenotype_interpretation, name="Participant_phenotype_interpretation", curie=INCLUDE.curie('phenotype_interpretation'),
                   model_uri=INCLUDE.Participant_phenotype_interpretation, domain=Participant, range=Optional[Union[str, "EnumPhenotypeInterpretation"]])

slots.Participant_race = Slot(uri=INCLUDE.race, name="Participant_race", curie=INCLUDE.curie('race'),
                   model_uri=INCLUDE.Participant_race, domain=Participant, range=Union[str, "EnumRace"])

slots.Participant_sex = Slot(uri=INCLUDE.sex, name="Participant_sex", curie=INCLUDE.curie('sex'),
                   model_uri=INCLUDE.Participant_sex, domain=Participant, range=Union[str, "EnumSex"])

slots.Study_dbgap = Slot(uri=INCLUDE.dbgap, name="Study_dbgap", curie=INCLUDE.curie('dbgap'),
                   model_uri=INCLUDE.Study_dbgap, domain=Study, range=Optional[str])

slots.Study_program = Slot(uri=INCLUDE.program, name="Study_program", curie=INCLUDE.curie('program'),
                   model_uri=INCLUDE.Study_program, domain=Study, range=Union[str, "EnumProgram"])

slots.Study_study_code = Slot(uri=INCLUDE.study_code, name="Study_study_code", curie=INCLUDE.curie('study_code'),
                   model_uri=INCLUDE.Study_study_code, domain=Study, range=Union[str, "EnumStudyCode"])

slots.Study_study_name = Slot(uri=INCLUDE.study_name, name="Study_study_name", curie=INCLUDE.curie('study_name'),
                   model_uri=INCLUDE.Study_study_name, domain=Study, range=str)