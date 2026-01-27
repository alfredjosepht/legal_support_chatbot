from nlp.classifier import classify_text
from nlp.entity_extractor import extract_entities
from rules.rule_engine import apply_rules
from response.generator import generate_response

def start_cli():
    print("Student Legal Support Chatbot (type 'exit')")
    while True:
        text = input("\nDescribe your issue: ")
        if text.lower() == "exit":
            break

        domain, confidence = classify_text(text)
        entities = extract_entities(text)
        contexts = apply_rules(domain, entities)

        print("\n" + generate_response(contexts, confidence))
