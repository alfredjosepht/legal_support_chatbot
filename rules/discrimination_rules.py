def apply_discrimination_rules(entities):
    contexts = []
    if entities.get("caste"):
        contexts.append("caste_discrimination")
    if entities.get("religion"):
        contexts.append("religious_discrimination")
    return contexts
