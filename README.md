[![INCLUDE DCC Logo](src/docs/images/include-dcc_logo.png)](https://includedcc.org/)

# INCLUDE LinkML Data Model

## Overview

This repository hosts the INCLUDE LinkML Model, a specialized data model crafted to empower collaboration and streamline data integration within Down syndrome research. By harnessing advanced [LinkML](https://linkml.io/) features, it provides a versatile framework for harmonizing data representation, articulating metadata, and delineating intricate relationships between entities. This structured approach not only promotes seamless data exchange but also facilitates interoperability and scalability across diverse research initiatives.

## Getting Started

To work with the INCLUDE Model, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Poetry**: If not already installed, install Poetry as a system dependency. Refer to [Poetry Documentation](https://python-poetry.org/docs/#installation) for installation instructions.

3. **Install Dependencies**: Run the following command to install project dependencies using Poetry:

```bash
poetry install
```

After running `poetry install`, you can proceed with further setup or usage instructions specific to your project.

## Repository Structure

The repository structure is organized as follows:

- `src/linkml`: Contains the YAML files defining the INCLUDE Model.

## Updates Since Previous Release (v2.2.0)

### Model Enhancements:

- Updated Assay component to include latest Virtual Biorepository model.
- Updated Study component and added new Dataset and DatasetManifest components to support new Study/Dataset pages in Data Hub.
- Inclusion of over 25 new slots.
- 5 new enumerations: EnumClinicalDataSourceType, EnumDataCategory, EnumGuidType, EnumParticipantLifespanStage, EnumResearchDomain.



