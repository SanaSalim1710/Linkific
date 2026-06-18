# House Price Prediction API

## Setup Instructions

### Install Flask
```bash
pip install flask
```

### Virtual Environment
```bash
mkdir ml-api-deployment
cd ml-api-deployment
python3 -m venv venv
source venv/bin/activate
```

### Run Application
```bash
python app.py
```
### View in Browser
```
http://127.0.0.1:5000
```




---
### `POST /train`

Trains a Linear Regression model on the house price regression dataset. It computes metrics for the
performance of the model. It uses the get_next_version method to determine what version it is on. It then saves the model as House Price Version {version number}.pkl. It returns the following message when training has successfully been completed:
```JSON
{
    "message": "The model has been trained!"
}
```

### `POST /predict`

It predicts a house price from property features. It uses the model saved after visiting the 
/train endpoint. The user provides the details of the house they want to predict using the following features.


| Features | Type | Description |
|---|---|---|
| `Square_Footage` | int | The size of the house in square feet |
| `Num_Bedrooms` | int | The number of bedrooms in the house |
| `Num_Bathrooms` | int | The number of bathrooms in the house |
| `Year_Built` | int | The year the house was built |
| `Lot_Size` | float | The size of the lot the house is built on, measured in acres |
| `Garage_Size` | int | The number of cars that can fit in the garage|
| `Neighborhood_Quality` | int | A rating of the neighborhood’s quality on a scale of 1(low) - 10 (high)|

Example input in JSON:
```JSON
{
    "Square_Footage": 2000,
    "Num_Bedrooms": 3,
    "Num_Bathrooms": 2,
    "Year_Built": 2015,
    "Lot_Size": 0.25,
    "Garage_Size": 2,
    "Neighborhood_Quality": 7
}
```

Example output:
```JSON
{
    "predicted_price": 452348.07548226416
}
```

### `GET /model-info`

Returns  metrics for the model. The metrics included are R2 score, RMSE and MAE.

Example output:
```JSON
{
    "Mean Absolute Error": 8175.0,
    "Root Mean Squared Error": 10071.0,
    "r2 score": 0.9984
}
```
