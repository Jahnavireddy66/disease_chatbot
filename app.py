from flask import Flask, render_template, request, jsonify
import joblib
import difflib

app = Flask(__name__)

# ======================
# LOAD MODEL & ENCODER
# ======================
model = joblib.load("disease_model.pkl")
mlb = joblib.load("symptom_encoder.pkl")

# Map readable symptoms (for text matching)
symptom_name_map = {
    sym.lower().replace("_", " "): sym for sym in mlb.classes_
}

KNOWN_SYMPTOMS = list(symptom_name_map.keys())

# ======================
# HELPER FUNCTIONS
# ======================
def get_closest_symptom(symptom):
    match = difflib.get_close_matches(
        symptom.lower(), KNOWN_SYMPTOMS, n=1, cutoff=0.8
    )
    return symptom_name_map[match[0]] if match else None


def extract_symptoms_from_text(text):
    """
    Extract known symptoms from a free-text sentence
    """
    text = text.lower()
    found = set()

    # Direct substring match
    for readable_symptom in KNOWN_SYMPTOMS:
        if readable_symptom in text:
            found.add(readable_symptom)

    # Fuzzy match individual words
    for word in text.replace(",", " ").split():
        matched = get_closest_symptom(word)
        if matched:
            found.add(matched.lower().replace("_", " "))

    return list(found)


def predict_disease(extracted_symptoms):
    cleaned = []

    for sym in extracted_symptoms:
        key = sym.strip().lower()
        matched = symptom_name_map.get(key) or get_closest_symptom(key)
        if matched:
            cleaned.append(matched)

    if not cleaned:
        return None

    encoded = mlb.transform([cleaned])
    prediction = model.predict(encoded)
    return prediction[0]


# ======================
# ROUTES
# ======================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "")

    # 🔹 Extract symptoms from free-text input
    extracted = extract_symptoms_from_text(message)

    if not extracted:
        return jsonify({
            "reply": (
                "❌ <b>No known symptoms detected.</b><br><br>"
                "Please try using common symptoms like:<br>"
                "<i>fever, cough, headache, rash, eye itching</i>."
            )
        })

    result = predict_disease(extracted)

    if not result:
        return jsonify({
            "reply": (
                "⚠️ I couldn’t confidently match your symptoms. "
                "Please add more details."
            )
        })

    response = (
        f"🩺 <b>Predicted Disease:</b><br>"
        f"<b>{result}</b><br><br>"
        "⚠️ <b>Medical Advisory:</b> "
        "This prediction is for informational purposes only. "
        "Please consult a qualified doctor."
    )

    return jsonify({"reply": response})


# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    app.run(debug=True)
