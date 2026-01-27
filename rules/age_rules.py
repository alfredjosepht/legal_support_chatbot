def apply_age_rules(domain, entities):
    if domain == "sexual_offence":
        if entities.get("age") and entities["age"] < 18:
            return ["child_protection"]
        return ["adult_sexual_offence"]
    return []
