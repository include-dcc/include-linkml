


def includify_curie(name):
    return f"include:{name}"

def make_object(curie):
    return {"@id": curie}

def generate_context(prefixes):
    prefix_context = {}
    for k,v in prefixes.items():
        prefix_context[k] = v['prefix_reference']
    return prefix_context

def pascal_to_camel(word):
    words = word.split("_")
    ret_words = [words[0]]
    for wd in words[1:]:
        ret_words.append(wd.replace(wd[0], wd[0].upper(),1))
    return "".join(ret_words)

def display_name(name):
    names = name.split('_')
    capitalized = ' '.join([x.title() for x in names])
    return capitalized

def enum_value_object(value):
    evo = {
        "@id" : includify_curie(pascal_to_camel(value)),
        "@type": "rdfs:Class",
        "rdfs:comment": "TBD",
        "rdfs:label": pascal_to_camel(value),
        "sms:displayName": display_name(value),
        "schema:isPartOf": make_object("https://w3id.org/include"),
        "sms:required": "sms:false"
    }
    return evo

def schema_value_object(value):
    return {
        "@id" : value,
        "@type": "rdfs:Class",
        "rdfs:comment": "TBD",
        "rdfs:label": "include",
        "sms:displayName": "INCLUDE",
        "schema:isPartOf": make_object("https://w3id.org/include"),
        "sms:required": "sms:false"
    }

def set_annotation_required(value):
    return "sms:true" if value == "True" else "sms:false"

def set_slot_required(value):
    return "sms:true" if value else "sms:false"

def process_enum_range(enum_object):
    range_includes = []
    for pv in enum_object.permissible_values:
        range_includes.append(make_object(includify_curie(pascal_to_camel(pv))))
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
