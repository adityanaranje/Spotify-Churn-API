import pickle
import pandas as pd

MODEL_VERSION = "1.0.0"

# import ml model
with open("model/model_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

classes = model.classes_.tolist()

def predict_output(user_input : dict):

    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_proba = dict(zip(classes, map(lambda p: round(p, 4), probabilities)))

    resp = {
        "predicted_category": 0,
        "confidence": round(confidence,4),
        "class_probabilities":class_proba
    }
    print(resp)
    return resp