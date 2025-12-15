import csv
import json
from pathlib import Path
import yaml
import re

SCHEMA_PATH = Path("src/linkml/include_schema.yaml").resolve()
INPUT_CSV = Path("../validation_logs/hakon_participants_v7_2025-12-12.csv").resolve()
OUTPUT_JSON = Path("../validation_logs/hakon_participants_js.json").resolve()


def get_multivalued_slots(schema_path):
    """Return list of slots that are multivalued in the schema."""
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    return [name for name, slot in schema.get("slots", {}).items() if slot.get("multivalued")]


def get_enum_slots(schema_path):
    """
    Return dict of slots constrained by enums.
    Keys = slot names, Values = set of normalized permissible values.
    """
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    enum_slots = {}
    enums = schema.get("enums", {})

    for name, slot in schema.get("slots", {}).items():
        enum_name = None

        if "enum" in slot:
            enum_name = slot["enum"]
        elif "values" in slot:
            enum_slots[name] = {normalize_value(v) for v in slot["values"]}
            continue
        elif slot.get("range") and str(slot["range"]).startswith("enum_"):
            enum_name = slot["range"]

        if enum_name and enum_name in enums:
            permissible = enums[enum_name].get("permissible_values", {})
            enum_slots[name] = {normalize_value(v) for v in permissible.keys()}

    return enum_slots


def get_slot_types(schema_path):
    """Return dict of slot → range (datatype or enum)."""
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    return {name: slot.get("range", "string") for name, slot in schema.get("slots", {}).items()}


def normalize_value(value: str) -> str:
    """Normalize values to snake_case (lowercase with underscores)."""
    if not value:
        return value
    value = value.strip().lower()
    value = re.sub(r"[ \-/]+", "_", value)  # replace spaces, slashes, hyphens
    value = re.sub(r"_+", "_", value)       # collapse multiple underscores
    return value


def cast_value(value, datatype):
    """Cast CSV string value to correct datatype based on schema range."""
    if value is None or value == "":
        return None

    if datatype == "integer":
        try:
            return int(value)
        except ValueError:
            print(f"⚠️ Warning: Cannot cast '{value}' to integer, leaving as string")
            return value
    elif datatype in {"float", "double", "number"}:
        try:
            return float(value)
        except ValueError:
            print(f"⚠️ Warning: Cannot cast '{value}' to float, leaving as string")
            return value
    elif datatype == "boolean":
        val = value.strip().lower()
        if val in {"true", "1", "yes"}:
            return True
        elif val in {"false", "0", "no"}:
            return False
        else:
            print(f"⚠️ Warning: Cannot cast '{value}' to boolean, leaving as string")
            return value
    else:
        return value  # default: keep as string


def validate_enum(slot, value, enum_slots):
    """Check if value is valid for the slot's enum. Warn if not."""
    permissible = enum_slots.get(slot, set())
    if permissible and value not in permissible:
        print(f"⚠️ Warning: Value '{value}' not in permissible values for slot '{slot}'")
    return value


def preprocess_csv_to_json(input_csv, array_slots, enum_slots, slot_types, delimiter="|"):
    """Convert CSV to JSON with type casting, enum normalization, and array handling."""
    records = []
    with input_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for slot in row:
                datatype = slot_types.get(slot, "string")
                value = row[slot].strip() if row[slot] is not None else ""

                if slot in array_slots:
                    if value == "":
                        row[slot] = []  # empty string → empty list
                    else:
                        values = value.split(delimiter)
                        if slot in enum_slots:
                            row[slot] = [validate_enum(slot, normalize_value(v), enum_slots) for v in values]
                        else:
                            row[slot] = [cast_value(v.strip(), datatype) for v in values]
                else:
                    if value == "":
                        row[slot] = None  # empty string → null
                    elif slot in enum_slots:
                        row[slot] = validate_enum(slot, normalize_value(value), enum_slots)
                    else:
                        row[slot] = cast_value(value, datatype)
            records.append(row)
    return records


def main():
    multivalued_slots = get_multivalued_slots(SCHEMA_PATH)
    enum_slots = get_enum_slots(SCHEMA_PATH)
    slot_types = get_slot_types(SCHEMA_PATH)

    # Add known array slots that might not have multivalued: true in schema
    extra_array_slots = ["publication", "acknowledgments", "citationStatement"]
    array_slots = list(set(multivalued_slots + extra_array_slots))

    print(f"Array slots detected: {array_slots}")
    print(f"Enum slots detected: {list(enum_slots.keys())}")
    print(f"Slot types detected: {slot_types}")

    data = preprocess_csv_to_json(INPUT_CSV, array_slots, enum_slots, slot_types)

    with OUTPUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Preprocessed JSON written to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
