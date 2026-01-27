def map_to_indian_laws(crime, entities):
    laws = []

    # Sexual offences
    if crime == "sexual_offence":
        if entities.get("age") and entities["age"] < 18:
            laws.append({
                "law": "POCSO Act, 2012",
                "sections": ["Section 7", "Section 8", "Section 11"]
            })
        else:
            laws.append({
                "law": "Indian Penal Code",
                "sections": ["Section 354", "Section 354A"]
            })

    # Physical violence
    if crime == "physical_violence":
        laws.append({
            "law": "Indian Penal Code",
            "sections": ["Section 323", "Section 325"]
        })

    # Threats
    if crime == "threat_intimidation":
        laws.append({
            "law": "Indian Penal Code",
            "sections": ["Section 506"]
        })

    # Cyber crimes
    if crime == "cyber_crime":
        laws.append({
            "law": "IT Act, 2000",
            "sections": ["Section 66C", "Section 67"]
        })
        laws.append({
            "law": "Indian Penal Code",
            "sections": ["Section 507"]
        })

    # Caste discrimination
    if crime == "discrimination_hate" and entities.get("caste"):
        laws.append({
            "law": "SC/ST (Prevention of Atrocities) Act",
            "sections": ["Section 3"]
        })

    return laws
