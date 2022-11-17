# INCLUDE v2 LinkML Data Model

This repository includes the LinkML model and tooling for the v2 Data Model







# Poetry Environment
This repo requires poetry as a system dependency

https://python-poetry.org/docs/#installation

When poetry is installed run:
`poetry install`




# Workflow to update the model from:
## [INCLUDE Schemasheets Google Sheets Project](https://docs.google.com/spreadsheets/d/1w6zDfz3_yrCjjrqfpXBGNmd0LZL4B03gr1KfzJtk5Cs/edit?usp=sharing)
1. Run the Schematic JSON-LD transformer to generate the JSON-LD that Schematic will use to generate Manifests

`poetry run python src/schematic/schematic_json_transformer.py`

4. Run Schematic configured to point at the generated json-ld at src/schematic/include_schematic_linkml.jsonld

`schematic manifest --config */schematic/config.yml get -s`