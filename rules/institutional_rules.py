def apply_institutional_rules(entities):
    if entities.get("institutional_issue"):
        return ["institutional_rights_violation"]
    return []
