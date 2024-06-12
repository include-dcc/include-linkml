<img src="src/docs/images/include-dcc_logo.png" width="75%">

# INCLUDE LinkML Data Model

## Overview

This repository hosts the Include LinkML Model, a specialized data model crafted to empower collaboration and streamline data integration within Down syndrome research. By harnessing advanced [LinkML](https://linkml.io/) features, it provides a versatile framework for harmonizing data representation, articulating metadata, and delineating intricate relationships between entities. This structured approach not only promotes seamless data exchange but also facilitates interoperability and scalability across diverse research initiatives.

## Getting Started

To work with the Include Model, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Poetry**: If not already installed, install Poetry as a system dependency. Refer to [Poetry Documentation](https://python-poetry.org/docs/#installation) for installation instructions.

3. **Install Dependencies**: Run the following command to install project dependencies using Poetry:

```bash
poetry install
```

After running `poetry install`, you can proceed with further setup or usage instructions specific to your project.

## Repository Structure

The repository structure is organized as follows:

- `src/linkml`: Contains the YAML files defining the Include Model.
- `src/data/schematic`: Includes the JSON-LD schema for the Include Model.

## Updates Since Previous Release (v2.2.0)

### Model Enhancements:

- Updated Assay component to include latest Virtual Biorepository model.
- Updated Study component and added new Dataset and DatasetManifest components to support new Study/Dataset pages in Data Hub.
- Inclusion of over 25 new slots.
- 5 new enumerations: EnumClinicalDataSourceType, EnumDataCategory, EnumGuidType, EnumParticipantLifespanStage, EnumResearchDomain.

### CLI Enhancements:

- **Validation**: Streamlines data cleaning and validation via the command line (CLI), allowing users to specify the data type and file path. The CLI reads, cleans, and validates data using LinkML-defined models for robust validation. For more details, use:

```bash
validate-data --help
```

## Setting Up INCLUDE Schemasheets with Schematic

1. **Generate JSON-LD using Schematic Transformer:**

```bash
poetry run python src/main.py schematic_transform
```
This command triggers the Schematic JSON-LD transformer to generate the JSON-LD required for creating Manifests.

2. **Run Schematic with Generated JSON-LD:**

Configure Schematic to use the generated JSON-LD located at `src/schematic/include_schematic_linkml.jsonld`:

```bash
schematic manifest --config */schematic/config.yml get -s
```

