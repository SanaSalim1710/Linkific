from flask import Flask, jsonify, request, render_template
import pickle
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score, mean_absolute_error
import pandas as pd
import joblib
import logging
import os
import re

app = Flask(__name__)

#model = pickle.load(open("House_Price.pkl","rb"))
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route("/")
def home():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    return "Logger Levels"


'''@app.route("/houseprice", methods = ["GET","POST"])
def predict_house_price():
    return render_template("house_price_input.html")'''

'''@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])
        features = [[area, bedrooms, bathrooms]]
        prediction = model.predict(features)[0]
        return {"prediction": float(prediction)}
    except Exception as e:
        return {
            "error": str(e)
        }, 400'''
    

@app.route("/train", methods=["POST"])
def train():
    global model
    global model_metrics 
    housing = pd.read_csv("/Users/sanasalim/Downloads/Linkific/Day 13/house_price_regression_dataset.csv")
    y = housing["House_Price"]
    features = ["Square_Footage","Num_Bedrooms","Num_Bathrooms", "Year_Built","Lot_Size","Garage_Size","Neighborhood_Quality"]
    X = housing[features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42, shuffle=True)
    model = LinearRegression()
    model.fit(X_train,y_train)
    logging.info("Model is training")
    predictions = model.predict(X_test)
    logging.info("Model finished training")
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = root_mean_squared_error(y_test, predictions)
    model_metrics = {
        "r2 score": round(r2, 4),
        "Root Mean Squared Error": rmse.round(0),
        "Mean Absolute Error": mae.round(0)
    }
    model_version = get_next_version()
    joblib.dump(model, f"House Price Version {model_version}.pkl")
    return jsonify({"message": "The model has been trained!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        model_version = get_next_version()-1
        model = joblib.load(f"House Price Version {model_version}.pkl")
        data = request.get_json()
        if not data:
            return jsonify({"error": "Please include JSON data in the request body and try again"}), 400
        features = ["Square_Footage","Num_Bedrooms","Num_Bathrooms", "Year_Built","Lot_Size","Garage_Size","Neighborhood_Quality"]
        for feature in features:
            if feature not in data:
                return jsonify({"error": f"Please input the missing feature '{feature}' and try again"}), 400
        square_foot = int(data["Square_Footage"])
        bedrooms = int(data["Num_Bedrooms"])
        bathrooms = int(data["Num_Bathrooms"])
        year = int(data["Year_Built"])
        lot = float(data["Lot_Size"])
        garage = int(data["Garage_Size"])
        neighbourhood = int(data["Neighborhood_Quality"])
        if neighbourhood < 1 or neighbourhood > 10:
            return jsonify({"error": "Neighborhood_Quality must be between 1 and 10"}), 400
        X_test = [square_foot,bedrooms, bathrooms, year, lot, garage, neighbourhood]
        prediction = model.predict([X_test])[0]
        logging.info(f"Model predicted: {prediction}")
        return jsonify({"predicted_price": float(prediction)})
    except FileNotFoundError:
        return jsonify({"error": "Please train the model before attempting prediction"})
    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 400


@app.route("/model-info",methods=["GET"])
def model_info():
    return jsonify(model_metrics)

def get_next_version():
    files = os.listdir()
    versions = 0
    for file in files:
        version = re.match(r"House Price Version (\d+)\.pkl",file)
        if version:
            versions += 1
    if not versions:
        return 1
    return (versions+1)

if __name__ == "__main__":
    app.run(debug=True)