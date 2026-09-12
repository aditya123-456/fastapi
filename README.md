# 🏠 House Price Prediction API

A FastAPI application for predicting California house prices using a Random Forest Regression model.

> 📚 **Learning Purpose:** This project was created for learning and practice purposes, to understand how a machine learning model can be trained and used through a FastAPI application.

## 🛠️ Technologies Used

* 🐍 Python
* ⚡ FastAPI
* 🐼 Pandas
* 🤖 Scikit-learn
* 💾 Joblib
* ✅ Pydantic

## 📂 Project Structure

```text
fastapi-main/
│
├── main.py
├── train.py
├── explore.py
└── .gitignore
```

## 🤖 Machine Learning Model

The project uses the **California Housing dataset** from Scikit-learn.

A `RandomForestRegressor` is used for prediction with:

```text
n_estimators = 100
random_state = 42
```

The dataset is divided into training and testing data using an 80/20 split.

## 🏠 Features

The model uses the following features:

* `MedInc` - Median income
* `HouseAge` - Median house age
* `AveRooms` - Average number of rooms
* `AveBedrms` - Average number of bedrooms
* `Population` - Block population
* `AveOccup` - Average household occupancy
* `Latitude` - Latitude
* `Longitude` - Longitude

## 🧠 Model Training

The model is trained using `train.py`.

Run:

```bash
python train.py
```

The training process:

1. Loads the California Housing dataset.
2. Creates a Pandas DataFrame from the dataset.
3. Saves the feature names in `features.pkl`.
4. Splits the data into training and testing sets.
5. Trains the Random Forest Regressor.
6. Predicts values for the test data.
7. Calculates Mean Absolute Error (MAE).
8. Calculates the R² score.
9. Saves the trained model in `house_price_model.pkl`.

The training script prints the average error and R² score.

## ⚡ FastAPI Application

The API is implemented in `main.py`.

The application loads:

```text
house_price_model.pkl
features.pkl
```

The FastAPI application has the title:

```text
House Price Prediction API
```

and the description:

```text
California House Price Prediction using Random Forest
```

## 🔌 API Endpoints

### 🏠 `GET /`

Returns a message indicating that the API is running.

Response:

```json
{
    "message": "House Price Prediction API is running"
}
```

### 📋 `GET /features`

Returns the feature names used by the model.

### 🔮 `POST /predict`

Accepts the following values:

```text
MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude
```

The API uses these values to create a DataFrame and passes it to the trained Random Forest model.

The response contains:

```json
{
    "predicted_price": "...",
    "predicted_price_dollars": "..."
}
```

The dollar value is calculated by multiplying the predicted value by `100000`.

## ▶️ Running the API

Start the FastAPI application using:

```bash
uvicorn main:app --reload
```

The application uses the FastAPI interactive documentation available through the application's `/docs` route.

## 📁 Generated Files

Running `train.py` generates:

```text
house_price_model.pkl
features.pkl
```

These files are listed in `.gitignore`.

The `.gitignore` also excludes:

```text
__pycache__/
venv/
```

## 📊 Evaluation

The model is evaluated using:

* 📏 Mean Absolute Error (MAE)
* 📈 R² Score
