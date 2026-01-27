from rules.age_rules import apply_age_rules
from rules.discrimination_rules import apply_discrimination_rules
from rules.institutional_rules import apply_institutional_rules


def apply_rules(domain, entities):
    """
    Central legal rule engine.
    ML gives a domain suggestion.
    Rules enforce legal correctness and priority.
    """

    contexts = []

    # --------------------------------------------------
    # 🔴 HARD OVERRIDE 1: RACISM / CASTEISM / DISCRIMINATION
    # --------------------------------------------------
    text = entities.get("raw_text", "")

    racism_keywords = [
        "black", "dark", "colour", "color",
        "caste", "sc", "st", "obc",
        "untouchable", "lower caste",
        "racial", "racist"
    ]

    if any(word in text for word in racism_keywords):
        return ["discrimination_hate"]

    # --------------------------------------------------
    # 🔴 HARD OVERRIDE 2: POCSO (CHILD SEXUAL OFFENCE)
    # --------------------------------------------------
    if domain == "sexual_offence":
        age = entities.get("age")
        if age is not None and age < 18:
            return ["child_sexual_offence"]

    # --------------------------------------------------
    # APPLY EXISTING RULE MODULES
    # --------------------------------------------------
    contexts += apply_age_rules(domain, entities)
    contexts += apply_discrimination_rules(entities)
    contexts += apply_institutional_rules(entities)

    # --------------------------------------------------
    # FALLBACK TO ML DOMAIN
    # --------------------------------------------------
    if not contexts:
        contexts.append(domain)

    # Remove duplicates
    return list(set(contexts))
