import json
import yaml
from yaml import FullLoader
from copy import deepcopy
from pprint import pprint


# EXAMPLE SCHEMATIC OBJECT
# {'@id': 'bts:Study',
#  '@type': 'rdfs:Class',
#  'rdfs:comment': 'TBD',
#  'rdfs:label': 'Study',
#  'rdfs:subClassOf': [{'@id': 'schema:Thing'}],
#  'schema:isPartOf': {'@id': 'http://schema.biothings.io'},
#  'sms:displayName': 'Study',
#  'sms:required': 'sms:true',
#  'sms:requiresDependency': [{'@id': 'bts:StudyCode'},
#                             {'@id': 'bts:StudyName'},
#                             {'@id': 'bts:Program'},
#                             {'@id': 'bts:DbGaP'}],
#  'sms:validationRules': []}

# In[3]: Load the linkml yaml spec and the por
with open("../../src/linkml/include_linkml.yaml", 'r') as lmly:
    lml_yaml = yaml.load(lmly, Loader=FullLoader)


# In[4]: Utility methods
def includify_curie(name):
    return f"include:{name}"


def make_object(curie):
    return {"@id": curie}


def generate_context(prefixes):
    context = {}
    for k,v in prefixes.items():
        context[k] = v['prefix_reference']
    return context


def display_name(name):
    names = name.split('_')
    capitalized = ' '.join([x.title() for x in names])
    return capitalized


def process_enum_values(enum):
    range_includes = []
    for k, v in enum['permissible_values'].items():
        range_includes.append(make_object(includify_curie(v['text'])))
    return range_includes


# In[5]: The easy 1to1 replacements
transform_map = {
    "definition_uri": "@id",
    "description": "rdfs:comment",
    "name": "rdfs:label",
    "from_schema": "schema:isPartOf",
    "title": "sms:displayName"
}


# In[7]: Generate context from declared namespaces
context = generate_context(lml_yaml['prefixes'])
context['sms'] = 'www.sms.org'
# Build the schematic json
include_graph = {
    '@context': context,
    "@graph": []
}

for class_key, class_data in lml_yaml['classes'].items():
    inc_class = dict()
    inc_class["@type"] = "rdfs:Class"
    for k, v in class_data.items():
        if k in transform_map.keys():
            inc_class[transform_map[k]] = v
    if 'is_a' in class_data.keys():
        parent = includify_curie(class_data['is_a'])
        inc_class['rdfs:subClassOf'] = [make_object(parent)]
    if "from_schema" in class_data.keys():
        inc_class['schema:isPartOf'] = make_object(class_data['from_schema'])
    if 'annotations' in class_data.keys():
        if 'required' in class_data['annotations'].keys():
            required = class_data['annotations']['required']
            inc_class['sms:required'] = 'sms:true' if required else 'sms:false'
        if 'requires_component' in class_data['annotations'].keys():
            comps = [make_object(includify_curie(x)) for x in
                     class_data['annotations']['requires_component'].split(",")]
            inc_class['sms:requiresComponent'] = comps
    if 'slots' in class_data.keys():
        inc_class['sms:requiresDependency'] = [make_object(includify_curie(x)) for x in class_data['slots']]
    inc_class["sms:validationRules"] = []
    include_graph['@graph'].append(inc_class)

#
for slot_key, slot_data in lml_yaml['slots'].items():
    inc_prop = {}
    inc_prop["@type"] = "rdf:Property"
    inc_prop['sms:displayName'] = display_name(slot_key)
    if slot_data:
        for k, v in slot_data.items():
            if k in transform_map.keys():
                inc_prop[transform_map[k]] = v
        if "from_schema" in slot_data.keys():
            inc_prop['schema:isPartOf'] = make_object(slot_data['from_schema'])
        if "range" in slot_data.keys():
            if "enum" in slot_data['range']:
                pvs = process_enum_values(lml_yaml['enums'][slot_data['range']])
                inc_prop['schema:rangeIncludes'] = pvs
        if "multivalued" in slot_data.keys() and slot_data['multivalued']:
            inc_prop['sms:validationRules'] = ['list']
    include_graph['@graph'].append(inc_prop)

with open("include_schematic_linkml.json", 'w') as islj:
    json.dump(include_graph, islj)
with open("include_schematic_linkml.jsonld", 'w') as isljd:
    json.dump(include_graph, isljd)

