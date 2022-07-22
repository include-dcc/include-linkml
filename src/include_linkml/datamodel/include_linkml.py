# Auto generated from include_linkml.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-07-21T12:55:41
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
from linkml_runtime.linkml_model.types import String

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



class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.NamedThing
    class_class_curie: ClassVar[str] = "include:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = INCLUDE.NamedThing


@dataclass
class Biospecimen(NamedThing):
    """
    A Biospecimen Collected from A Participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Biospecimen
    class_class_curie: ClassVar[str] = "include:Biospecimen"
    class_name: ClassVar[str] = "Biospecimen"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Biospecimen

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
    sample_id: Optional[str] = None
    sample_type: Optional[str] = None
    volume: Optional[str] = None
    volume_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.volume_unit is not None and not isinstance(self.volume_unit, str):
            self.volume_unit = str(self.volume_unit)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        super().__post_init__(**kwargs)


@dataclass
class DataFile(NamedThing):
    """
    A DataFile Associated with a Participant or Study or Biospecimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.DataFile
    class_class_curie: ClassVar[str] = "include:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = INCLUDE.DataFile

    access_url: Optional[str] = None
    collection_id: Optional[str] = None
    data_access: Optional[Union[str, "EnumDataAccess"]] = None
    data_category: Optional[str] = None
    data_type: Optional[str] = None
    experimental_strategy: Optional[str] = None
    file_id: Optional[str] = None
    file_name: Optional[str] = None
    format: Optional[str] = None
    has_biospecimen: Optional[Union[dict, Biospecimen]] = None
    has_participant: Optional[Union[dict, "Participant"]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    participant_id: Optional[str] = None
    size: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.file_id is not None and not isinstance(self.file_id, str):
            self.file_id = str(self.file_id)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.has_biospecimen is not None and not isinstance(self.has_biospecimen, Biospecimen):
            self.has_biospecimen = Biospecimen(**as_dict(self.has_biospecimen))

        if self.has_participant is not None and not isinstance(self.has_participant, Participant):
            self.has_participant = Participant(**as_dict(self.has_participant))

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        super().__post_init__(**kwargs)


@dataclass
class Participant(NamedThing):
    """
    A Participant in a Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Participant
    class_class_curie: ClassVar[str] = "include:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Participant

    age_at_diagnosis: Optional[str] = None
    age_at_phenotype_assignment: Optional[str] = None
    age_at_the_last_vital_status: Optional[str] = None
    diagnosis_icd: Optional[str] = None
    diagnosis_mondo: Optional[str] = None
    diagnosis_ncit: Optional[str] = None
    diagnosis_source_text: Optional[str] = None
    diagnosis_type: Optional[str] = None
    down_syndrome_status: Optional[Union[str, "EnumDownSyndromeStatus"]] = None
    ethnicity: Optional[Union[str, "EnumEthnicity"]] = None
    external_id: Optional[str] = None
    family_id: Optional[str] = None
    family_relationship: Optional[str] = None
    family_type: Optional[Union[str, "EnumFamilyType"]] = None
    father_id: Optional[str] = None
    has_datafile: Optional[Union[dict, DataFile]] = None
    has_study: Optional[Union[dict, "Study"]] = None
    mother_id: Optional[str] = None
    outcomes_vital_status: Optional[str] = None
    participant_id: Optional[str] = None
    phenotype_hpo: Optional[str] = None
    phenotype_source_text: Optional[str] = None
    phenotype_interpretation: Optional[Union[str, "EnumPhenotypeInterpretation"]] = None
    race: Optional[Union[str, "EnumRace"]] = None
    sex: Optional[Union[str, "EnumSex"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.age_at_diagnosis is not None and not isinstance(self.age_at_diagnosis, str):
            self.age_at_diagnosis = str(self.age_at_diagnosis)

        if self.age_at_phenotype_assignment is not None and not isinstance(self.age_at_phenotype_assignment, str):
            self.age_at_phenotype_assignment = str(self.age_at_phenotype_assignment)

        if self.age_at_the_last_vital_status is not None and not isinstance(self.age_at_the_last_vital_status, str):
            self.age_at_the_last_vital_status = str(self.age_at_the_last_vital_status)

        if self.diagnosis_icd is not None and not isinstance(self.diagnosis_icd, str):
            self.diagnosis_icd = str(self.diagnosis_icd)

        if self.diagnosis_mondo is not None and not isinstance(self.diagnosis_mondo, str):
            self.diagnosis_mondo = str(self.diagnosis_mondo)

        if self.diagnosis_ncit is not None and not isinstance(self.diagnosis_ncit, str):
            self.diagnosis_ncit = str(self.diagnosis_ncit)

        if self.diagnosis_source_text is not None and not isinstance(self.diagnosis_source_text, str):
            self.diagnosis_source_text = str(self.diagnosis_source_text)

        if self.diagnosis_type is not None and not isinstance(self.diagnosis_type, str):
            self.diagnosis_type = str(self.diagnosis_type)

        if self.down_syndrome_status is not None and not isinstance(self.down_syndrome_status, EnumDownSyndromeStatus):
            self.down_syndrome_status = EnumDownSyndromeStatus(self.down_syndrome_status)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self.external_id is not None and not isinstance(self.external_id, str):
            self.external_id = str(self.external_id)

        if self.family_id is not None and not isinstance(self.family_id, str):
            self.family_id = str(self.family_id)

        if self.family_relationship is not None and not isinstance(self.family_relationship, str):
            self.family_relationship = str(self.family_relationship)

        if self.family_type is not None and not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

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

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.phenotype_hpo is not None and not isinstance(self.phenotype_hpo, str):
            self.phenotype_hpo = str(self.phenotype_hpo)

        if self.phenotype_source_text is not None and not isinstance(self.phenotype_source_text, str):
            self.phenotype_source_text = str(self.phenotype_source_text)

        if self.phenotype_interpretation is not None and not isinstance(self.phenotype_interpretation, EnumPhenotypeInterpretation):
            self.phenotype_interpretation = EnumPhenotypeInterpretation(self.phenotype_interpretation)

        if self.race is not None and not isinstance(self.race, EnumRace):
            self.race = EnumRace(self.race)

        if self.sex is not None and not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    A Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INCLUDE.Study
    class_class_curie: ClassVar[str] = "include:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = INCLUDE.Study

    dbgap: Optional[str] = None
    program: Optional[Union[str, "EnumProgram"]] = None
    study_code: Optional[Union[str, "EnumStudyCode"]] = None
    study_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dbgap is not None and not isinstance(self.dbgap, str):
            self.dbgap = str(self.dbgap)

        if self.program is not None and not isinstance(self.program, EnumProgram):
            self.program = EnumProgram(self.program)

        if self.study_code is not None and not isinstance(self.study_code, EnumStudyCode):
            self.study_code = EnumStudyCode(self.study_code)

        if self.study_name is not None and not isinstance(self.study_name, str):
            self.study_name = str(self.study_name)

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

slots.access_url = Slot(uri=INCLUDE.access_url, name="access_url", curie=INCLUDE.curie('access_url'),
                   model_uri=INCLUDE.access_url, domain=None, range=Optional[str])

slots.age_at_biospecimen_collection = Slot(uri=INCLUDE.age_at_biospecimen_collection, name="age_at_biospecimen_collection", curie=INCLUDE.curie('age_at_biospecimen_collection'),
                   model_uri=INCLUDE.age_at_biospecimen_collection, domain=None, range=Optional[str])

slots.age_at_diagnosis = Slot(uri=INCLUDE.age_at_diagnosis, name="age_at_diagnosis", curie=INCLUDE.curie('age_at_diagnosis'),
                   model_uri=INCLUDE.age_at_diagnosis, domain=None, range=Optional[str])

slots.age_at_phenotype_assignment = Slot(uri=INCLUDE.age_at_phenotype_assignment, name="age_at_phenotype_assignment", curie=INCLUDE.curie('age_at_phenotype_assignment'),
                   model_uri=INCLUDE.age_at_phenotype_assignment, domain=None, range=Optional[str])

slots.age_at_the_last_vital_status = Slot(uri=INCLUDE.age_at_the_last_vital_status, name="age_at_the_last_vital_status", curie=INCLUDE.curie('age_at_the_last_vital_status'),
                   model_uri=INCLUDE.age_at_the_last_vital_status, domain=None, range=Optional[str])

slots.biospecimen_storage = Slot(uri=INCLUDE.biospecimen_storage, name="biospecimen_storage", curie=INCLUDE.curie('biospecimen_storage'),
                   model_uri=INCLUDE.biospecimen_storage, domain=None, range=Optional[str])

slots.collection_id = Slot(uri=INCLUDE.collection_id, name="collection_id", curie=INCLUDE.curie('collection_id'),
                   model_uri=INCLUDE.collection_id, domain=None, range=Optional[str])

slots.collection_sample_type = Slot(uri=INCLUDE.collection_sample_type, name="collection_sample_type", curie=INCLUDE.curie('collection_sample_type'),
                   model_uri=INCLUDE.collection_sample_type, domain=None, range=Optional[str])

slots.container_id = Slot(uri=INCLUDE.container_id, name="container_id", curie=INCLUDE.curie('container_id'),
                   model_uri=INCLUDE.container_id, domain=None, range=Optional[str])

slots.data_access = Slot(uri=INCLUDE.data_access, name="data_access", curie=INCLUDE.curie('data_access'),
                   model_uri=INCLUDE.data_access, domain=None, range=Optional[Union[str, "EnumDataAccess"]])

slots.data_category = Slot(uri=INCLUDE.data_category, name="data_category", curie=INCLUDE.curie('data_category'),
                   model_uri=INCLUDE.data_category, domain=None, range=Optional[str])

slots.data_type = Slot(uri=INCLUDE.data_type, name="data_type", curie=INCLUDE.curie('data_type'),
                   model_uri=INCLUDE.data_type, domain=None, range=Optional[str])

slots.dbgap = Slot(uri=INCLUDE.dbgap, name="dbgap", curie=INCLUDE.curie('dbgap'),
                   model_uri=INCLUDE.dbgap, domain=None, range=Optional[str])

slots.diagnosis_icd = Slot(uri=INCLUDE.diagnosis_icd, name="diagnosis_icd", curie=INCLUDE.curie('diagnosis_icd'),
                   model_uri=INCLUDE.diagnosis_icd, domain=None, range=Optional[str])

slots.diagnosis_mondo = Slot(uri=INCLUDE.diagnosis_mondo, name="diagnosis_mondo", curie=INCLUDE.curie('diagnosis_mondo'),
                   model_uri=INCLUDE.diagnosis_mondo, domain=None, range=Optional[str])

slots.diagnosis_ncit = Slot(uri=INCLUDE.diagnosis_ncit, name="diagnosis_ncit", curie=INCLUDE.curie('diagnosis_ncit'),
                   model_uri=INCLUDE.diagnosis_ncit, domain=None, range=Optional[str])

slots.diagnosis_source_text = Slot(uri=INCLUDE.diagnosis_source_text, name="diagnosis_source_text", curie=INCLUDE.curie('diagnosis_source_text'),
                   model_uri=INCLUDE.diagnosis_source_text, domain=None, range=Optional[str])

slots.diagnosis_type = Slot(uri=INCLUDE.diagnosis_type, name="diagnosis_type", curie=INCLUDE.curie('diagnosis_type'),
                   model_uri=INCLUDE.diagnosis_type, domain=None, range=Optional[str])

slots.down_syndrome_status = Slot(uri=INCLUDE.down_syndrome_status, name="down_syndrome_status", curie=INCLUDE.curie('down_syndrome_status'),
                   model_uri=INCLUDE.down_syndrome_status, domain=None, range=Optional[Union[str, "EnumDownSyndromeStatus"]])

slots.ethnicity = Slot(uri=INCLUDE.ethnicity, name="ethnicity", curie=INCLUDE.curie('ethnicity'),
                   model_uri=INCLUDE.ethnicity, domain=None, range=Optional[Union[str, "EnumEthnicity"]])

slots.experimental_strategy = Slot(uri=INCLUDE.experimental_strategy, name="experimental_strategy", curie=INCLUDE.curie('experimental_strategy'),
                   model_uri=INCLUDE.experimental_strategy, domain=None, range=Optional[str])

slots.external_id = Slot(uri=INCLUDE.external_id, name="external_id", curie=INCLUDE.curie('external_id'),
                   model_uri=INCLUDE.external_id, domain=None, range=Optional[str])

slots.family_id = Slot(uri=INCLUDE.family_id, name="family_id", curie=INCLUDE.curie('family_id'),
                   model_uri=INCLUDE.family_id, domain=None, range=Optional[str])

slots.family_relationship = Slot(uri=INCLUDE.family_relationship, name="family_relationship", curie=INCLUDE.curie('family_relationship'),
                   model_uri=INCLUDE.family_relationship, domain=None, range=Optional[str])

slots.family_type = Slot(uri=INCLUDE.family_type, name="family_type", curie=INCLUDE.curie('family_type'),
                   model_uri=INCLUDE.family_type, domain=None, range=Optional[Union[str, "EnumFamilyType"]])

slots.father_id = Slot(uri=INCLUDE.father_id, name="father_id", curie=INCLUDE.curie('father_id'),
                   model_uri=INCLUDE.father_id, domain=None, range=Optional[str])

slots.file_id = Slot(uri=INCLUDE.file_id, name="file_id", curie=INCLUDE.curie('file_id'),
                   model_uri=INCLUDE.file_id, domain=None, range=Optional[str])

slots.file_name = Slot(uri=INCLUDE.file_name, name="file_name", curie=INCLUDE.curie('file_name'),
                   model_uri=INCLUDE.file_name, domain=None, range=Optional[str])

slots.format = Slot(uri=INCLUDE.format, name="format", curie=INCLUDE.curie('format'),
                   model_uri=INCLUDE.format, domain=None, range=Optional[str])

slots.has_biospecimen = Slot(uri=INCLUDE.has_biospecimen, name="has_biospecimen", curie=INCLUDE.curie('has_biospecimen'),
                   model_uri=INCLUDE.has_biospecimen, domain=None, range=Optional[Union[dict, Biospecimen]])

slots.has_datafile = Slot(uri=INCLUDE.has_datafile, name="has_datafile", curie=INCLUDE.curie('has_datafile'),
                   model_uri=INCLUDE.has_datafile, domain=None, range=Optional[Union[dict, DataFile]])

slots.has_participant = Slot(uri=INCLUDE.has_participant, name="has_participant", curie=INCLUDE.curie('has_participant'),
                   model_uri=INCLUDE.has_participant, domain=None, range=Optional[Union[dict, Participant]])

slots.has_study = Slot(uri=INCLUDE.has_study, name="has_study", curie=INCLUDE.curie('has_study'),
                   model_uri=INCLUDE.has_study, domain=None, range=Optional[Union[dict, Study]])

slots.laboratory_procedure = Slot(uri=INCLUDE.laboratory_procedure, name="laboratory_procedure", curie=INCLUDE.curie('laboratory_procedure'),
                   model_uri=INCLUDE.laboratory_procedure, domain=None, range=Optional[str])

slots.mother_id = Slot(uri=INCLUDE.mother_id, name="mother_id", curie=INCLUDE.curie('mother_id'),
                   model_uri=INCLUDE.mother_id, domain=None, range=Optional[str])

slots.outcomes_vital_status = Slot(uri=INCLUDE.outcomes_vital_status, name="outcomes_vital_status", curie=INCLUDE.curie('outcomes_vital_status'),
                   model_uri=INCLUDE.outcomes_vital_status, domain=None, range=Optional[str])

slots.parent_sample_id = Slot(uri=INCLUDE.parent_sample_id, name="parent_sample_id", curie=INCLUDE.curie('parent_sample_id'),
                   model_uri=INCLUDE.parent_sample_id, domain=None, range=Optional[str])

slots.parent_sample_type = Slot(uri=INCLUDE.parent_sample_type, name="parent_sample_type", curie=INCLUDE.curie('parent_sample_type'),
                   model_uri=INCLUDE.parent_sample_type, domain=None, range=Optional[str])

slots.participant_id = Slot(uri=INCLUDE.participant_id, name="participant_id", curie=INCLUDE.curie('participant_id'),
                   model_uri=INCLUDE.participant_id, domain=None, range=Optional[str])

slots.phenotype_hpo = Slot(uri=INCLUDE.phenotype_hpo, name="phenotype_hpo", curie=INCLUDE.curie('phenotype_hpo'),
                   model_uri=INCLUDE.phenotype_hpo, domain=None, range=Optional[str])

slots.phenotype_interpretation = Slot(uri=INCLUDE.phenotype_interpretation, name="phenotype_interpretation", curie=INCLUDE.curie('phenotype_interpretation'),
                   model_uri=INCLUDE.phenotype_interpretation, domain=None, range=Optional[Union[str, "EnumPhenotypeInterpretation"]])

slots.phenotype_source_text = Slot(uri=INCLUDE.phenotype_source_text, name="phenotype_source_text", curie=INCLUDE.curie('phenotype_source_text'),
                   model_uri=INCLUDE.phenotype_source_text, domain=None, range=Optional[str])

slots.program = Slot(uri=INCLUDE.program, name="program", curie=INCLUDE.curie('program'),
                   model_uri=INCLUDE.program, domain=None, range=Optional[Union[str, "EnumProgram"]])

slots.race = Slot(uri=INCLUDE.race, name="race", curie=INCLUDE.curie('race'),
                   model_uri=INCLUDE.race, domain=None, range=Optional[Union[str, "EnumRace"]])

slots.sample_availability = Slot(uri=INCLUDE.sample_availability, name="sample_availability", curie=INCLUDE.curie('sample_availability'),
                   model_uri=INCLUDE.sample_availability, domain=None, range=Optional[Union[str, "EnumSampleAvailability"]])

slots.sample_id = Slot(uri=INCLUDE.sample_id, name="sample_id", curie=INCLUDE.curie('sample_id'),
                   model_uri=INCLUDE.sample_id, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=INCLUDE.sample_type, name="sample_type", curie=INCLUDE.curie('sample_type'),
                   model_uri=INCLUDE.sample_type, domain=None, range=Optional[str])

slots.sex = Slot(uri=INCLUDE.sex, name="sex", curie=INCLUDE.curie('sex'),
                   model_uri=INCLUDE.sex, domain=None, range=Optional[Union[str, "EnumSex"]])

slots.size = Slot(uri=INCLUDE.size, name="size", curie=INCLUDE.curie('size'),
                   model_uri=INCLUDE.size, domain=None, range=Optional[str])

slots.study_code = Slot(uri=INCLUDE.study_code, name="study_code", curie=INCLUDE.curie('study_code'),
                   model_uri=INCLUDE.study_code, domain=None, range=Optional[Union[str, "EnumStudyCode"]])

slots.study_name = Slot(uri=INCLUDE.study_name, name="study_name", curie=INCLUDE.curie('study_name'),
                   model_uri=INCLUDE.study_name, domain=None, range=Optional[str])

slots.volume = Slot(uri=INCLUDE.volume, name="volume", curie=INCLUDE.curie('volume'),
                   model_uri=INCLUDE.volume, domain=None, range=Optional[str])

slots.volume_unit = Slot(uri=INCLUDE.volume_unit, name="volume_unit", curie=INCLUDE.curie('volume_unit'),
                   model_uri=INCLUDE.volume_unit, domain=None, range=Optional[str])