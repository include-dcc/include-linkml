import json
from pprint import pprint
from os.path import dirname
project_root = dirname(dirname(dirname(__file__)))

class SchematicTransformer(object):
    def __init__(self, path_to_schema):
        self.schema_path = path_to_schema
        self.linkml_schema = None
    def load_json_schema(self):
        with open(self.schema_path, 'r') as jschema:
            self.linkml_schema = json.load(jschema)



st = SchematicTransformer(f"{project_root}/project/jsonschema/include_schema.schema.json")
st.load_json_schema()
pprint(st.linkml_schema.keys())
pprint({x:y['type'] for x,y in  st.linkml_schema['$defs'].items()})
