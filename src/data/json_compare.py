import json
from pprint import pprint

docs = []
with open('old_json_transform/old.json', 'r') as oj:
    ojson = json.load(oj)
    ojsongraph = ojson['@graph']
    ojsoncontext = ojson['@context']
    docs.append(ojson)
# with open('old_schematic_model/original.json', 'r') as mj:
#     originaljson = json.load(mj)['@graph']
#     originaljsoncontext = json.load(mj)['@context']
#     docs.append(originaljson)
with open('schematic/include_schematic_linkml.json', 'r') as ij:
    newjson = json.load(ij)
    newjsongraph = newjson['@graph']
    newjsoncontext = newjson['@context']
    docs.append(newjson)


def get_object(key, value, objlist):
    return [x for x in objlist if x[key] == value]
new_keys = sorted([x['@id'] for x in ojsongraph])
old_keys = sorted([x['@id'] for x in ojsongraph])
new_json_sorted = []
for nk in new_keys:
    new_json_sorted += get_object('@id', nk, newjsongraph)
old_json_sorted = []
for ok in old_keys:
    old_json_sorted += get_object('@id', ok, ojsongraph)


njsongraph = {
    '@context': newjsoncontext,
    '@graph': new_json_sorted
}
with open("sorted_new.jsonld", 'w') as snjld:
    json.dump(njsongraph, snjld, sort_keys=True)
with open("sorted_new.json", 'w') as snj:
    json.dump(njsongraph, snj, sort_keys=True)

oldjsongraph = {
    '@context': ojsoncontext,
    '@graph': old_json_sorted
}

with open("sorted_old.jsonld", 'w') as sojld:
    json.dump(oldjsongraph, sojld, sort_keys=True)
with open("sorted_old.json", 'w') as soj:
    json.dump(oldjsongraph, soj, sort_keys=True)