# Auto generated from include_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-11-04T05:49:48
# Schema: include-schema
#
# id: https://w3id.org/include/
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

    uses_biospecimen: Optional[Union[dict, "Biospecimen"]] = None
    has_output: Optional[Union[dict, "DataFile"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uses_biospecimen is not None and not isinstance(self.uses_biospecimen, Biospecimen):
            self.uses_biospecimen = Biospecimen(**as_dict(self.uses_biospecimen))

        if self.has_output is not None and not isinstance(self.has_output, DataFile):
            self.has_output = DataFile(**as_dict(self.has_output))

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

    sample_id: str = None
    sample_type: str = None
    age_at_biospecimen_collection: Optional[str] = None
    biospecimen_storage: Optional[str] = None
    collection_id: Optional[str] = None
    collection_sample_type: Optional[str] = None
    container_id: Optional[str] = None
    has_datafile: Optional[Union[dict, "DataFile"]] = None
    has_participant: Optional[Union[dict, "Participant"]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    laboratory_procedure: Optional[str] = None
    parent_sample_id: Optional[str] = None
    parent_sample_type: Optional[str] = None
    sample_availability: Optional[Union[str, "EnumSampleAvailability"]] = None
    volume: Optional[str] = None
    volume_unit: Optional[str] = None
    has_aliquot: Optional[Union[dict, Aliquot]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.age_at_biospecimen_collection is not None and not isinstance(self.age_at_biospecimen_collection, str):
            self.age_at_biospecimen_collection = str(self.age_at_biospecimen_collection)

        if self.biospecimen_storage is not None and not isinstance(self.biospecimen_storage, str):
            self.biospecimen_storage = str(self.biospecimen_storage)

        if self.collection_id is not None and not isinstance(self.collection_id, str):
            self.collection_id = str(self.collection_id)

        if self.collection_sample_type is not None and not isinstance(self.collection_sample_type, str):
            self.collection_sample_type = str(self.collection_sample_type)

        if self.container_id is not None and not isinstance(self.container_id, str):
            self.container_id = str(self.container_id)

        if self.has_datafile is not None and not isinstance(self.has_datafile, DataFile):
            self.has_datafile = DataFile(**as_dict(self.has_datafile))

        if self.has_participant is not None and not isinstance(self.has_participant, Participant):
            self.has_participant = Participant(**as_dict(self.has_participant))

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

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.volume_unit is not None and not isinstance(self.volume_unit, str):
            self.volume_unit = str(self.volume_unit)

        if self.has_aliquot is not None and not isinstance(self.has_aliquot, Aliquot):
            self.has_aliquot = Aliquot()

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

    data_category: str = None
    file_name: str = None
    format: str = None
    participant_id: str = None
    original_file_name: str = None
    access_url: Optional[str] = None
    collection_id: Optional[str] = None
    data_access: Optional[Union[str, "EnumDataAccess"]] = None
    data_type: Optional[str] = None
    experimental_strategy: Optional[str] = None
    file_id: Optional[str] = None
    has_biospecimen: Optional[Union[dict, Biospecimen]] = None
    has_participant: Optional[Union[dict, "Participant"]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    size: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.data_category):
            self.MissingRequiredField("data_category")
        if not isinstance(self.data_category, str):
            self.data_category = str(self.data_category)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self._is_empty(self.original_file_name):
            self.MissingRequiredField("original_file_name")
        if not isinstance(self.original_file_name, str):
            self.original_file_name = str(self.original_file_name)

        if self.access_url is not None and not isinstance(self.access_url, str):
            self.access_url = str(self.access_url)

        if self.collection_id is not None and not isinstance(self.collection_id, str):
            self.collection_id = str(self.collection_id)

        if self.data_access is not None and not isinstance(self.data_access, EnumDataAccess):
            self.data_access = EnumDataAccess(self.data_access)

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        if self.experimental_strategy is not None and not isinstance(self.experimental_strategy, str):
            self.experimental_strategy = str(self.experimental_strategy)

        if self.file_id is not None and not isinstance(self.file_id, str):
            self.file_id = str(self.file_id)

        if self.has_biospecimen is not None and not isinstance(self.has_biospecimen, Biospecimen):
            self.has_biospecimen = Biospecimen(**as_dict(self.has_biospecimen))

        if self.has_participant is not None and not isinstance(self.has_participant, Participant):
            self.has_participant = Participant(**as_dict(self.has_participant))

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

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

    down_syndrome_status: Union[str, "EnumDownSyndromeStatus"] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    external_id: str = None
    family_type: Union[str, "EnumFamilyType"] = None
    participant_id: str = None
    race: Union[str, "EnumRace"] = None
    sex: Union[str, "EnumSex"] = None
    age_at_last_vital_status: Optional[int] = None
    family_id: Optional[str] = None
    family_relationship: Optional[Union[dict, "Participant"]] = None
    father_id: Optional[str] = None
    has_datafile: Optional[Union[dict, DataFile]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    mother_id: Optional[str] = None
    outcomes_vital_status: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self._is_empty(self.family_type):
            self.MissingRequiredField("family_type")
        if not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, EnumRace):
            self.race = EnumRace(self.race)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        if self.age_at_last_vital_status is not None and not isinstance(self.age_at_last_vital_status, int):
            self.age_at_last_vital_status = int(self.age_at_last_vital_status)

        if self.family_id is not None and not isinstance(self.family_id, str):
            self.family_id = str(self.family_id)

        if self.family_relationship is not None and not isinstance(self.family_relationship, Participant):
            self.family_relationship = Participant(**as_dict(self.family_relationship))

        if self.father_id is not None and not isinstance(self.father_id, str):
            self.father_id = str(self.father_id)

        if self.has_datafile is not None and not isinstance(self.has_datafile, DataFile):
            self.has_datafile = DataFile(**as_dict(self.has_datafile))

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.mother_id is not None and not isinstance(self.mother_id, str):
            self.mother_id = str(self.mother_id)

        if self.outcomes_vital_status is not None and not isinstance(self.outcomes_vital_status, str):
            self.outcomes_vital_status = str(self.outcomes_vital_status)

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

    has_participant: Optional[Union[dict, Participant]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_participant is not None and not isinstance(self.has_participant, Participant):
            self.has_participant = Participant(**as_dict(self.has_participant))

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

    has_participant: Optional[Union[dict, Participant]] = None
    age_at_condition_observation: Optional[int] = None
    mondo_label: Optional[str] = None
    mondo_code: Optional[str] = None
    condition_interpretation: Optional[Union[str, "EnumConditionInterpretation"]] = None
    condition_data_source: Optional[Union[str, "EnumConditionDataSource"]] = None
    hpo_label: Optional[str] = None
    hpo_code: Optional[str] = None
    maxo_label: Optional[str] = None
    maxo_code: Optional[str] = None
    other_label: Optional[str] = None
    other_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_participant is not None and not isinstance(self.has_participant, Participant):
            self.has_participant = Participant(**as_dict(self.has_participant))

        if self.age_at_condition_observation is not None and not isinstance(self.age_at_condition_observation, int):
            self.age_at_condition_observation = int(self.age_at_condition_observation)

        if self.mondo_label is not None and not isinstance(self.mondo_label, str):
            self.mondo_label = str(self.mondo_label)

        if self.mondo_code is not None and not isinstance(self.mondo_code, str):
            self.mondo_code = str(self.mondo_code)

        if self.condition_interpretation is not None and not isinstance(self.condition_interpretation, EnumConditionInterpretation):
            self.condition_interpretation = EnumConditionInterpretation(self.condition_interpretation)

        if self.condition_data_source is not None and not isinstance(self.condition_data_source, EnumConditionDataSource):
            self.condition_data_source = EnumConditionDataSource(self.condition_data_source)

        if self.hpo_label is not None and not isinstance(self.hpo_label, str):
            self.hpo_label = str(self.hpo_label)

        if self.hpo_code is not None and not isinstance(self.hpo_code, str):
            self.hpo_code = str(self.hpo_code)

        if self.maxo_label is not None and not isinstance(self.maxo_label, str):
            self.maxo_label = str(self.maxo_label)

        if self.maxo_code is not None and not isinstance(self.maxo_code, str):
            self.maxo_code = str(self.maxo_code)

        if self.other_label is not None and not isinstance(self.other_label, str):
            self.other_label = str(self.other_label)

        if self.other_code is not None and not isinstance(self.other_code, str):
            self.other_code = str(self.other_code)

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
    more_than_one_race = PermissibleValue(text="more_than_one_race")
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

slots.access_url = Slot(uri=INCLUDE['assay/access_url'], name="access_url", curie=INCLUDE.curie('assay/access_url'),
                   model_uri=INCLUDE.access_url, domain=None, range=Optional[str])

slots.age_at_biospecimen_collection = Slot(uri=INCLUDE['assay/age_at_biospecimen_collection'], name="age_at_biospecimen_collection", curie=INCLUDE.curie('assay/age_at_biospecimen_collection'),
                   model_uri=INCLUDE.age_at_biospecimen_collection, domain=None, range=Optional[str])

slots.biospecimen_storage = Slot(uri=INCLUDE['assay/biospecimen_storage'], name="biospecimen_storage", curie=INCLUDE.curie('assay/biospecimen_storage'),
                   model_uri=INCLUDE.biospecimen_storage, domain=None, range=Optional[str])

slots.collection_id = Slot(uri=INCLUDE['assay/collection_id'], name="collection_id", curie=INCLUDE.curie('assay/collection_id'),
                   model_uri=INCLUDE.collection_id, domain=None, range=Optional[str])

slots.collection_sample_type = Slot(uri=INCLUDE['assay/collection_sample_type'], name="collection_sample_type", curie=INCLUDE.curie('assay/collection_sample_type'),
                   model_uri=INCLUDE.collection_sample_type, domain=None, range=Optional[str])

slots.container_id = Slot(uri=INCLUDE['assay/container_id'], name="container_id", curie=INCLUDE.curie('assay/container_id'),
                   model_uri=INCLUDE.container_id, domain=None, range=Optional[str])

slots.data_access = Slot(uri=INCLUDE['assay/data_access'], name="data_access", curie=INCLUDE.curie('assay/data_access'),
                   model_uri=INCLUDE.data_access, domain=None, range=Optional[Union[str, "EnumDataAccess"]])

slots.data_category = Slot(uri=INCLUDE['assay/data_category'], name="data_category", curie=INCLUDE.curie('assay/data_category'),
                   model_uri=INCLUDE.data_category, domain=None, range=str)

slots.data_type = Slot(uri=INCLUDE['assay/data_type'], name="data_type", curie=INCLUDE.curie('assay/data_type'),
                   model_uri=INCLUDE.data_type, domain=None, range=Optional[str])

slots.experimental_strategy = Slot(uri=INCLUDE['assay/experimental_strategy'], name="experimental_strategy", curie=INCLUDE.curie('assay/experimental_strategy'),
                   model_uri=INCLUDE.experimental_strategy, domain=None, range=Optional[str])

slots.file_id = Slot(uri=INCLUDE['assay/file_id'], name="file_id", curie=INCLUDE.curie('assay/file_id'),
                   model_uri=INCLUDE.file_id, domain=None, range=Optional[str])

slots.file_name = Slot(uri=INCLUDE['assay/file_name'], name="file_name", curie=INCLUDE.curie('assay/file_name'),
                   model_uri=INCLUDE.file_name, domain=None, range=str)

slots.format = Slot(uri=INCLUDE['assay/format'], name="format", curie=INCLUDE.curie('assay/format'),
                   model_uri=INCLUDE.format, domain=None, range=str)

slots.has_aliquot = Slot(uri=INCLUDE['assay/has_aliquot'], name="has_aliquot", curie=INCLUDE.curie('assay/has_aliquot'),
                   model_uri=INCLUDE.has_aliquot, domain=None, range=Optional[Union[dict, Aliquot]])

slots.has_biospecimen = Slot(uri=INCLUDE['assay/has_biospecimen'], name="has_biospecimen", curie=INCLUDE.curie('assay/has_biospecimen'),
                   model_uri=INCLUDE.has_biospecimen, domain=None, range=Optional[Union[dict, Biospecimen]])

slots.has_datafile = Slot(uri=INCLUDE['assay/has_datafile'], name="has_datafile", curie=INCLUDE.curie('assay/has_datafile'),
                   model_uri=INCLUDE.has_datafile, domain=None, range=Optional[Union[dict, DataFile]])

slots.has_output = Slot(uri=INCLUDE['assay/has_output'], name="has_output", curie=INCLUDE.curie('assay/has_output'),
                   model_uri=INCLUDE.has_output, domain=None, range=Optional[Union[dict, DataFile]])

slots.laboratory_procedure = Slot(uri=INCLUDE['assay/laboratory_procedure'], name="laboratory_procedure", curie=INCLUDE.curie('assay/laboratory_procedure'),
                   model_uri=INCLUDE.laboratory_procedure, domain=None, range=Optional[str])

slots.original_file_name = Slot(uri=INCLUDE['assay/original_file_name'], name="original_file_name", curie=INCLUDE.curie('assay/original_file_name'),
                   model_uri=INCLUDE.original_file_name, domain=None, range=str)

slots.parent_sample_id = Slot(uri=INCLUDE['assay/parent_sample_id'], name="parent_sample_id", curie=INCLUDE.curie('assay/parent_sample_id'),
                   model_uri=INCLUDE.parent_sample_id, domain=None, range=Optional[str])

slots.parent_sample_type = Slot(uri=INCLUDE['assay/parent_sample_type'], name="parent_sample_type", curie=INCLUDE.curie('assay/parent_sample_type'),
                   model_uri=INCLUDE.parent_sample_type, domain=None, range=Optional[str])

slots.sample_availability = Slot(uri=INCLUDE['assay/sample_availability'], name="sample_availability", curie=INCLUDE.curie('assay/sample_availability'),
                   model_uri=INCLUDE.sample_availability, domain=None, range=Optional[Union[str, "EnumSampleAvailability"]])

slots.sample_id = Slot(uri=INCLUDE['assay/sample_id'], name="sample_id", curie=INCLUDE.curie('assay/sample_id'),
                   model_uri=INCLUDE.sample_id, domain=None, range=str)

slots.sample_type = Slot(uri=INCLUDE['assay/sample_type'], name="sample_type", curie=INCLUDE.curie('assay/sample_type'),
                   model_uri=INCLUDE.sample_type, domain=None, range=str)

slots.size = Slot(uri=INCLUDE['assay/size'], name="size", curie=INCLUDE.curie('assay/size'),
                   model_uri=INCLUDE.size, domain=None, range=Optional[str])

slots.uses_biospecimen = Slot(uri=INCLUDE['assay/uses_biospecimen'], name="uses_biospecimen", curie=INCLUDE.curie('assay/uses_biospecimen'),
                   model_uri=INCLUDE.uses_biospecimen, domain=None, range=Optional[Union[dict, Biospecimen]])

slots.volume = Slot(uri=INCLUDE['assay/volume'], name="volume", curie=INCLUDE.curie('assay/volume'),
                   model_uri=INCLUDE.volume, domain=None, range=Optional[str])

slots.volume_unit = Slot(uri=INCLUDE['assay/volume_unit'], name="volume_unit", curie=INCLUDE.curie('assay/volume_unit'),
                   model_uri=INCLUDE.volume_unit, domain=None, range=Optional[str])

slots.age_at_condition_observation = Slot(uri=INCLUDE['participant/age_at_condition_observation'], name="age_at_condition_observation", curie=INCLUDE.curie('participant/age_at_condition_observation'),
                   model_uri=INCLUDE.age_at_condition_observation, domain=None, range=Optional[int])

slots.age_at_last_vital_status = Slot(uri=INCLUDE['participant/age_at_last_vital_status'], name="age_at_last_vital_status", curie=INCLUDE.curie('participant/age_at_last_vital_status'),
                   model_uri=INCLUDE.age_at_last_vital_status, domain=None, range=Optional[int])

slots.condition_data_source = Slot(uri=INCLUDE['participant/condition_data_source'], name="condition_data_source", curie=INCLUDE.curie('participant/condition_data_source'),
                   model_uri=INCLUDE.condition_data_source, domain=None, range=Optional[Union[str, "EnumConditionDataSource"]])

slots.condition_interpretation = Slot(uri=INCLUDE['participant/condition_interpretation'], name="condition_interpretation", curie=INCLUDE.curie('participant/condition_interpretation'),
                   model_uri=INCLUDE.condition_interpretation, domain=None, range=Optional[Union[str, "EnumConditionInterpretation"]])

slots.down_syndrome_status = Slot(uri=INCLUDE['participant/down_syndrome_status'], name="down_syndrome_status", curie=INCLUDE.curie('participant/down_syndrome_status'),
                   model_uri=INCLUDE.down_syndrome_status, domain=None, range=Union[str, "EnumDownSyndromeStatus"])

slots.ethnicity = Slot(uri=INCLUDE['participant/ethnicity'], name="ethnicity", curie=INCLUDE.curie('participant/ethnicity'),
                   model_uri=INCLUDE.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.external_id = Slot(uri=INCLUDE['participant/external_id'], name="external_id", curie=INCLUDE.curie('participant/external_id'),
                   model_uri=INCLUDE.external_id, domain=None, range=str)

slots.family_id = Slot(uri=INCLUDE['participant/family_id'], name="family_id", curie=INCLUDE.curie('participant/family_id'),
                   model_uri=INCLUDE.family_id, domain=None, range=Optional[str])

slots.family_relationship = Slot(uri=INCLUDE['participant/family_relationship'], name="family_relationship", curie=INCLUDE.curie('participant/family_relationship'),
                   model_uri=INCLUDE.family_relationship, domain=None, range=Optional[Union[dict, Participant]])

slots.family_type = Slot(uri=INCLUDE['participant/family_type'], name="family_type", curie=INCLUDE.curie('participant/family_type'),
                   model_uri=INCLUDE.family_type, domain=None, range=Union[str, "EnumFamilyType"])

slots.father_id = Slot(uri=INCLUDE['participant/father_id'], name="father_id", curie=INCLUDE.curie('participant/father_id'),
                   model_uri=INCLUDE.father_id, domain=None, range=Optional[str])

slots.has_participant = Slot(uri=INCLUDE['participant/has_participant'], name="has_participant", curie=INCLUDE.curie('participant/has_participant'),
                   model_uri=INCLUDE.has_participant, domain=None, range=Optional[Union[dict, Participant]])

slots.has_study = Slot(uri=INCLUDE['participant/has_study'], name="has_study", curie=INCLUDE.curie('participant/has_study'),
                   model_uri=INCLUDE.has_study, domain=None, range=Optional[Union[dict, Study]])

slots.hpo_code = Slot(uri=INCLUDE['participant/hpo_code'], name="hpo_code", curie=INCLUDE.curie('participant/hpo_code'),
                   model_uri=INCLUDE.hpo_code, domain=None, range=Optional[str])

slots.hpo_label = Slot(uri=INCLUDE['participant/hpo_label'], name="hpo_label", curie=INCLUDE.curie('participant/hpo_label'),
                   model_uri=INCLUDE.hpo_label, domain=None, range=Optional[str])

slots.maxo_code = Slot(uri=INCLUDE['participant/maxo_code'], name="maxo_code", curie=INCLUDE.curie('participant/maxo_code'),
                   model_uri=INCLUDE.maxo_code, domain=None, range=Optional[str])

slots.maxo_label = Slot(uri=INCLUDE['participant/maxo_label'], name="maxo_label", curie=INCLUDE.curie('participant/maxo_label'),
                   model_uri=INCLUDE.maxo_label, domain=None, range=Optional[str])

slots.mondo_code = Slot(uri=INCLUDE['participant/mondo_code'], name="mondo_code", curie=INCLUDE.curie('participant/mondo_code'),
                   model_uri=INCLUDE.mondo_code, domain=None, range=Optional[str])

slots.mondo_label = Slot(uri=INCLUDE['participant/mondo_label'], name="mondo_label", curie=INCLUDE.curie('participant/mondo_label'),
                   model_uri=INCLUDE.mondo_label, domain=None, range=Optional[str])

slots.mother_id = Slot(uri=INCLUDE['participant/mother_id'], name="mother_id", curie=INCLUDE.curie('participant/mother_id'),
                   model_uri=INCLUDE.mother_id, domain=None, range=Optional[str])

slots.other_code = Slot(uri=INCLUDE['participant/other_code'], name="other_code", curie=INCLUDE.curie('participant/other_code'),
                   model_uri=INCLUDE.other_code, domain=None, range=Optional[str])

slots.other_label = Slot(uri=INCLUDE['participant/other_label'], name="other_label", curie=INCLUDE.curie('participant/other_label'),
                   model_uri=INCLUDE.other_label, domain=None, range=Optional[str])

slots.outcomes_vital_status = Slot(uri=INCLUDE['participant/outcomes_vital_status'], name="outcomes_vital_status", curie=INCLUDE.curie('participant/outcomes_vital_status'),
                   model_uri=INCLUDE.outcomes_vital_status, domain=None, range=Optional[str])

slots.participant_id = Slot(uri=INCLUDE['participant/participant_id'], name="participant_id", curie=INCLUDE.curie('participant/participant_id'),
                   model_uri=INCLUDE.participant_id, domain=None, range=str)

slots.race = Slot(uri=INCLUDE['participant/race'], name="race", curie=INCLUDE.curie('participant/race'),
                   model_uri=INCLUDE.race, domain=None, range=Union[str, "EnumRace"])

slots.sex = Slot(uri=INCLUDE['participant/sex'], name="sex", curie=INCLUDE.curie('participant/sex'),
                   model_uri=INCLUDE.sex, domain=None, range=Union[str, "EnumSex"])

slots.dbgap = Slot(uri=INCLUDE['study/dbgap'], name="dbgap", curie=INCLUDE.curie('study/dbgap'),
                   model_uri=INCLUDE.dbgap, domain=None, range=Optional[str])

slots.program = Slot(uri=INCLUDE['study/program'], name="program", curie=INCLUDE.curie('study/program'),
                   model_uri=INCLUDE.program, domain=None, range=Union[str, "EnumProgram"])

slots.study_code = Slot(uri=INCLUDE['study/study_code'], name="study_code", curie=INCLUDE.curie('study/study_code'),
                   model_uri=INCLUDE.study_code, domain=None, range=Union[str, "EnumStudyCode"])

slots.study_name = Slot(uri=INCLUDE['study/study_name'], name="study_name", curie=INCLUDE.curie('study/study_name'),
                   model_uri=INCLUDE.study_name, domain=None, range=str)