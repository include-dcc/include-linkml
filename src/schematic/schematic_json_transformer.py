import json
from pprint import pprint

import copy
import logging
from os.path import dirname
PROJECT_ROOT = dirname(dirname(dirname(__file__)))


from .schematic_utils import make_object, \
    set_annotation_required, \
    set_slot_required, \
    includify_curie, \
    process_enum_range,\
    enum_value_object, \
    schema_value_object, \
    pascal_to_camel

from linkml_runtime.utils.schemaview import SchemaView

logging.info("running transformer")

# EXAMPLE Target SCHEMATIC OBJECT
# {'@id': 'bts:Study',
#  '@type': 'rdfs:Class',
#  'rdfs:comment': 'TBD',
#  'rdfs:label': 'Study',
#  'rdfs:subClassOf': [{'@id': 'schema:Thing'}],
#  'schema:isPartOf': {'@id': 'http://schema.biothings.io'},
#  'sms:displayName': 'Study',
#  'sms:required': 'sms:true',
#   "sms:requiresComponent": [
#     {
#         "@id": "bts:Study"
#     },
#     {
#         "@id": "bts:DataFile"
#     }
# ],
#  'sms:requiresDependency': [{'@id': 'bts:StudyCode'},
#                             {'@id': 'bts:StudyName'},
#                             {'@id': 'bts:Program'},
#                             {'@id': 'bts:DbGaP'}],
#  'sms:validationRules': []}


OBJECT_RANGE_MAP = {
    "hasParticipant": "participantId",
    "hasBiospecimen": "sampleId",
    "hasStudy": "studyCode",
    "hasDatafile": "fileId"
}

class SchematicJSONTransformer(object):
    def __init__(self, schema_path, output_path):
        self.schema_path = schema_path
        self.output_path = output_path
        self.sv = SchemaView(self.schema_path)
        self.context = self.generate_context()

        # Build the schematic json
        self.schematic_classes = []
        self.class_keys = []
        self.schematic_properties = []
        self.prop_keys = []
        self.generate_schema_object()

    def class_generator(self):
        for sclass, sdef in self.sv.all_classes().items():
            class_object = dict()
            class_object['@type'] = 'rdfs:Class'
            class_object['@id'] = sdef.definition_uri
            class_object['rdfs:label'] = sdef.name
            class_object['rdfs:comment'] = sdef.description
            class_object['sms:displayName'] = sdef.title
            class_object['sms:validationRules'] = []
            class_object['schema:isPartOf'] = make_object(self.sv.schema.id)

            parent = self.sv.get_class(sdef.is_a)
            parent_uri = parent.definition_uri if parent else None
            if parent_uri:
                class_object['rdfs:subClassOf'] = [make_object(parent_uri)]

            if 'required' in sdef['annotations'].keys():
                class_object['sms:required'] = set_annotation_required(sdef['annotations']['required'].value)
            if 'requires_component' in sdef['annotations'].keys():
                    comps = [make_object(includify_curie(x)) for x in
                             sdef['annotations']['requires_component']['value'].split(",")]
                    class_object['sms:requiresComponent'] = comps
            if len(sdef['slots']):
                class_object['sms:requiresDependency'] = []
                for slot in sdef['slots']:
                    slotdef = self.sv.get_slot(slot)
                    slot_range = slotdef.range
                    slot_sv = slotdef.definition_uri
                    if slot in OBJECT_RANGE_MAP.keys():
                        slot_sv = includify_curie(OBJECT_RANGE_MAP[slot])

                    class_object['sms:requiresDependency'].append(make_object(slot_sv))
            self.schematic_classes.append(class_object)

    def property_generator(self):
        for slot, slotdef in self.sv.all_slots().items():
            slot_object = dict()
            slot_object['@type'] = 'rdf:Property'
            slot_object['@id'] = slotdef.definition_uri
            slot_object['rdfs:label'] = slotdef.name
            slot_object['rdfs:comment'] = slotdef.description
            slot_object['sms:displayName'] = slotdef.title
            slot_object['schema:isPartOf'] = make_object(self.sv.schema.id)
            slot_object['sms:required'] = set_slot_required(slotdef.required)
            slot_object['sms:validationRules'] = []
            domain_list = self.sv.get_classes_by_slot(slotdef)
            slot_object['schema:domainIncludes'] = [make_object(includify_curie(x)) for x in domain_list]
            type_string = str(type(self.sv.get_element(slotdef.range)))
            if "ClassDefinition" in type_string:
                slot_object['schema:rangeIncludes'] = [make_object(includify_curie(slotdef.range))]
            if "EnumDefinition" in type_string:
                slot_object['schema:rangeIncludes'] = process_enum_range(self.sv.get_enum(slotdef.range))
                enum = self.sv.get_enum(slotdef.range)
                for enum_value in enum.permissible_values:
                    if enum_value not in self.class_keys:
                        self.schematic_classes.append(enum_value_object(enum.permissible_values[enum_value], slotdef.definition_uri))
                        self.class_keys.append(enum_value)
                    else:
                        pass
            self.schematic_properties.append(slot_object)

    def generate_schema_object(self):
        self.schematic_classes.append(schema_value_object(self.sv.schema.id))

    def generate_context(self):
        context = self.sv.namespaces()
        context['sms'] = 'www.sms.org'
        return {x:str(y) for x, y in context.items()}

    def write_output(self):
        include_graph = {
            '@context': self.context ,
            "@graph": self.schematic_classes + self.schematic_properties
        }
        with open(f"{self.output_path}/include_schematic_linkml.jsonld", 'w') as isljd:
            logging.info(f"writing to {self.output_path}/include_schematic_linkml.jsonld")
            json.dump(include_graph, isljd, sort_keys=True, indent=4)


st = SchematicJSONTransformer(f"{PROJECT_ROOT}/src/linkml/include_schema.yaml", f"{PROJECT_ROOT}/src/data/schematic")
st.class_generator()
st.property_generator()
st.write_output()

