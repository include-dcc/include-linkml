.PHONY: all clean temp

all: clean temp

clean:

temp:
	poetry run linkml2sheets \
		-s src/linkml/include_linkml.yaml \
  		-d src/data/sheets --overwrite src/data/sheets/*.tsv