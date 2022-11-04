


def includify_curie(name):
    return f"include:{name}"

def make_object(curie):
    return {"@id": curie}

def generate_context(prefixes):
    prefix_context = {}
    for k,v in prefixes.items():
        prefix_context[k] = v['prefix_reference']
    return prefix_context

def display_name(name):
    names = name.split('_')
    capitalized = ' '.join([x.title() for x in names])
    return capitalized

def enum_value_object(value):
    return {
        "@id" : includify_curie(value.replace(" ", "")),
        "@type": "rdfs:Class",
        "rdfs:comment": "TBD",
        "rdfs:label": value.replace(" ", ""),
        "sms:displayName": display_name(value),
        "schema:isPartOf": "https://w3id.org/include",
        "sms:required": "sms:false"
    }

def set_annotation_required(value):
    return "sms:true" if value == "True" else "sms:false"

def set_slot_required(value):
    return "sms:true" if value else "sms:false"

def process_enum_range(enum_object):
    range_includes = []
    for pv in enum_object.permissible_values:
        range_includes.append(make_object(includify_curie(pv)))
    return range_includes


def gen_domain_list(domain_data):
    data_return = []
    for d in domain_data:
        data_return.append({
            "@id": includify_curie(d)
        })
    return data_return

# In[5]: The easy 1to1 replacements
TRANSFORM_MAP = {
    "definition_uri": "@id",
    "description": "rdfs:comment",
    "name": "rdfs:label",
    "from_schema": "schema:isPartOf",
    "title": "sms:displayName"
}
