import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Create FastAPI application
app = FastAPI(
    title="House Price Prediction API",
    description="California House Price Prediction using Random Forest",
    version="1.0.0"
)

# Load trained model
model = joblib.load("house_price_model.pkl")

# Load feature names
features = joblib.load("features.pkl")


# Input schema
class HouseInput(BaseModel):

    MedInc: float = Field(..., description="Median income")

    HouseAge: float = Field(..., description="Median house age")

    AveRooms: float = Field(..., description="Average number of rooms")

    AveBedrms: float = Field(..., description="Average number of bedrooms")

    Population: float = Field(..., description="Block population")

    AveOccup: float = Field(..., description="Average household occupancy")

    Latitude: float = Field(..., description="Latitude")

    Longitude: float = Field(..., description="Longitude")


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


# Show features
@app.get("/features")
def get_features():
    return {
        "features": features
    }


# Prediction endpoint
@app.post("/predict")
def predict(data: HouseInput):

    try:

        # Convert input to dictionary
        input_data = data.model_dump()

        # Arrange values in the same order as training
        input_df = pd.DataFrame(
            [[input_data[feature] for feature in features]],
            columns=features
        )

        # Predict
        prediction = model.predict(input_df)

        # Get predicted value
        predicted_price = float(prediction[0])

        return {
            "predicted_price": predicted_price,
            "predicted_price_dollars": predicted_price * 100000
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
