import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("🔹 Loading dataset...")
df = pd.read_excel("Medical DiseaseAndSymptom dataset.xlsx")

# Combine all symptom columns
symptom_cols = [col for col in df.columns if col.startswith("Symptom_")]
df["Symptoms"] = df[symptom_cols].values.tolist()

# Clean symptoms
df["Symptoms"] = df["Symptoms"].apply(
    lambda x: [sym.strip().lower() for sym in x if isinstance(sym, str)]
)

# Encode symptoms
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["Symptoms"])
y = df["Disease"]

# Train-test split (for accuracy check)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Save model + encoder
joblib.dump(model, "disease_model.pkl")
joblib.dump(mlb, "symptom_encoder.pkl")

print("✅ Model and encoder saved successfully")




