import json
from pprint import pprint
from os.path import dirname
import copy
project_root = dirname(dirname(dirname(__file__)))
from schematic_utils import TRANSFORM_MAP, make_object, set_required, includify_curie
from linkml_runtime.utils.schemaview import SchemaView

OBJECT_TEMPLATE = {'@id': None,
                   '@type': None,
                   'rdfs:comment': None,
                   'rdfs:label': None,
                   'rdfs:subClassOf': [],
                   'schema:isPartOf': None,
                   'sms:displayName': None,
                   'sms:required': None,
                   'sms:requiresDependency': []}

PROPERTY_TEMPLATE = {'@id': None,
                     '@type': None,
                     'rdfs:comment': None,
                     'rdfs:label': None,
                     'schema:isPartOf': None,
                     'sms:displayName': None,
                     'sms:required': None,
                     'sms:domainIncludes': [],
                     'sms:rangeIncludes': []}

# EXAMPLE SCHEMATIC OBJECT
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





class SchematicJSONTransformer(object):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.sv = SchemaView(self.schema_path)
        self.schematic_classes = []
        self.schematic_properties = []

    def class_generator(self):
        sinstance = copy.deepcopy(OBJECT_TEMPLATE)
        for sclass, sdef in self.sv.all_classes().items():
            sinstance['@type'] = 'rdfs:Class'
            sinstance['@id'] = sdef.definition_uri
            sinstance['rdfs:label'] = sdef.name
            sinstance['rdfs:comment'] = sdef.description
            sinstance['sms:displayName'] = sdef.title
            parent = self.sv.get_class(sdef.is_a)
            parent_uri = parent.definition_uri if parent else None
            sinstance['rdfs:subClassOf'] = [make_object(parent_uri)]
            sinstance['schema:isPartOf'] = make_object((self.sv.schema.id))
            if 'required' in sdef['annotations'].keys():
                sinstance['sms:required'] = set_required(sdef['annotations']['required'].value)
            if 'requires_component' in sdef['annotations'].keys():
                    comps = [make_object(includify_curie(x)) for x in
                             sdef['annotations']['requires_component']['value'].split(",")]
                    sinstance['sms:requiresComponent'] = comps
            if len(sdef['slots']):
                sinstance['sms:requiresDependency'] = []
                for slot in sdef['slots']:
                    slot_sv = self.sv.get_slot(slot).definition_uri
                    sinstance['sms:requiresDependency'].append(make_object(slot_sv))
        self.schematic_classes.append(sinstance)

    def property_generator(self):
        sinstance = copy.deepcopy(OBJECT_TEMPLATE)
        for slot, slotdef in self.sv.all_slots().items():
            sinstance['@type'] = 'rdf:Property'
            sinstance['@id'] = slotdef.definition_uri
            sinstance['rdfs:label'] = slotdef.name
            sinstance['rdfs:comment'] = slotdef.description
            sinstance['sms:displayName'] = slotdef.title
            sinstance['schema:isPartOf'] = make_object((self.sv.schema.id))
            print(slotdef.range)
            # if 'sms:rangeIncludes' in :
            #     print(slot)
        self.schematic_properties.append(sinstance)



st = SchematicJSONTransformer(f"{project_root}/src/linkml/include_schema.yaml")
st.class_generator()
st.property_generator()