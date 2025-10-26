from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schema.user_input import UserInputs
from schema.result import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION




app = FastAPI()

countries = ["AU","US","DE","IN","PK","FR","UK","CA"]

sub_type = ["Premium","Free","Student","Family" ]

device_type = ["Desktop","Web","Mobile"]
# pydantic model to validate incomig data



@app.get("/")
def home():
    return {
        "message":"Spotify Churn Prediction API"
        }

@app.get('/health')
def health_check():
    return {
        "status": "OK",
        "version": MODEL_VERSION,
        "model_loaded": True if model else False
    }


@app.post('/predict', response_model=PredictionResponse)
def predict_churn(data : UserInputs):

    user_input = {
            'gender': data.gender, 
            'age':data.age, 
            'country':data.country, 
            'subscription_type':data.subscription_type, 
            'listening_time':data.listening_time,
            'songs_played_per_day':data.songs_played_per_day, 
            'skip_rate':data.skip_rate, 
            'device_type':data.device_type,
            'ads_listened_per_week':data.ads_listened_per_week, 
            'offline_listening':data.offline_listening
        }

    try:
        prediction = predict_output(user_input=user_input)

        #pred = "Not Churn" if (prediction == 0) else "Churn"

        return JSONResponse(status_code=200, content={'prediction':jsonable_encoder(prediction)})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

