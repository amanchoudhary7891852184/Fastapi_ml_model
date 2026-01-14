from fastapi import FastAPI, HTTPException
from schemas import UrineInput, PredictionOutput
from model_loader import predict_stone

app = FastAPI(title="Kidney Stone Prediction API")

@app.get("/")
def home():
    return {"message": "Kidney Stone Prediction API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: UrineInput):

    try:
        pred = predict_stone(data)
        result = "Kidney Stone Detected" if pred == 1 else "No Kidney Stone"

        return {
            "prediction": pred,
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
