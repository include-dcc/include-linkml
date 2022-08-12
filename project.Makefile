template_dir = src/data/sheets
output_dir = src/data/output

# ls -1 src/data/sheets/*.tsv
  #src/data/sheets/INCLUDE_Portal_V1_LinkML_Schema_Classes_Slots.tsv
  #src/data/sheets/INCLUDE_Portal_V1_LinkML_Schema_Enums.tsv
  #src/data/sheets/INCLUDE_Portal_V1_LinkML_Schema_Prefixes.tsv
  #src/data/sheets/INCLUDE_Portal_V1_LinkML_Schema_Schema.tsv
  #src/data/sheets/INCLUDE_Portal_V1_LinkML_Schema_Types.tsv

	# ValueError: dict contains fields not in fieldnames: 'desc', 'slot'
	#   when last arg is src/data/sheets/*.tsv
	# but each of the templates complies OK on its own

.PHONY: individually_all linkml2sheets_clean individually

individually_all: linkml2sheets_clean individually

linkml2sheets_clean:
	rm -rf $(output_dir)/*

src/data/output/%.tsv:
	poetry run linkml2sheets \
		--schema src/linkml/include_linkml.yaml \
  		--output-directory $(output_dir) \
  		--overwrite $(subst $(output_dir),$(template_dir),$@)

individually: src/data/output/INCLUDE_Portal_V1_LinkML_Schema_Classes_Slots.tsv \
src/data/output/INCLUDE_Portal_V1_LinkML_Schema_Enums.tsv \
src/data/output/INCLUDE_Portal_V1_LinkML_Schema_Prefixes.tsv \
src/data/output/INCLUDE_Portal_V1_LinkML_Schema_Schema.tsv \
# src/data/output/INCLUDE_Portal_V1_LinkML_Schema_Types.tsv
