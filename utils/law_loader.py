
import json

LAW_MAPPING_PATH = "knowledge_base/law_mapping.json"

def get_laws_for_crime(crime_key):
    with open(LAW_MAPPING_PATH, "r") as f:
        law_map = json.load(f)

    return law_map.get(crime_key, [])
