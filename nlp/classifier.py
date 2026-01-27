import joblib
from nlp.preprocessing import preprocess

model = joblib.load("nlp/domain_model.pkl")
vectorizer = joblib.load("nlp/vectorizer.pkl")

def classify_text(text: str):
    cleaned = preprocess(text)
    vec = vectorizer.transform([cleaned])
    probs = model.predict_proba(vec)[0]

    domain = model.classes_[probs.argmax()]
    confidence = probs.max()

    return domain, confidence
