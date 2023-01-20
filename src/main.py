from schematic.schematic_json_transformer import SchematicJSONTransformer
import typer

from os.path import dirname
PROJECT_ROOT = dirname(dirname(dirname(__file__)))

app = typer.Typer(help='INCLUDE LinkML.')


@app.command(name="schematic_transform")
def schematic_transform():
    st = SchematicJSONTransformer(f"{PROJECT_ROOT}/include-linkml/src/linkml/include_schema.yaml",
                                  f"{PROJECT_ROOT}/include-linkml/src/data/schematic")
    st.class_generator()
    st.property_generator()
    st.write_output()

@app.callback()
def callback():
    pass

if __name__ == "__main__":
    app()