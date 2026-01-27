import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nlp.preprocessing import preprocess

print("Loading dataset...")
df = pd.read_csv("data/training/domain_dataset.csv")

X = df["text"].apply(preprocess)
y = df["domain"]

print("Vectorizing...")
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

print("Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

print("Saving model...")
joblib.dump(model, "nlp/domain_model.pkl")
joblib.dump(vectorizer, "nlp/vectorizer.pkl")

print("✅ Training complete")
