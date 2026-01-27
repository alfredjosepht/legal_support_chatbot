import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Extract structured information from user text
    """

    doc = nlp(text.lower())
    entities = {}

    # --------------------------------------------------
    # RAW TEXT (VERY IMPORTANT FOR RULES)
    # --------------------------------------------------
    entities["raw_text"] = text.lower()

    # --------------------------------------------------
    # AGE EXTRACTION
    # --------------------------------------------------
    age_match = re.search(r"\b(\d{1,2})\s*(years?|yr|yrs|yo|y/o)\b", text.lower())
    if age_match:
        try:
            entities["age"] = int(age_match.group(1))
        except ValueError:
            pass

    # --------------------------------------------------
    # CASTE / COMMUNITY MENTION
    # --------------------------------------------------
    caste_keywords = ["sc", "st", "obc", "dalit", "caste"]
    if any(word in text.lower() for word in caste_keywords):
        entities["caste"] = True

    # --------------------------------------------------
    # MEDIUM (ONLINE / OFFLINE)
    # --------------------------------------------------
    if any(word in text.lower() for word in ["online", "instagram", "whatsapp", "facebook"]):
        entities["medium"] = "online"
    else:
        entities["medium"] = "offline"

    return entities
