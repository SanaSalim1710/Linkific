# House Price Prediction
 Linear Regression
## Model Performance

| Metric | Value        |
|--------|--------------|
| R²     | **0.9925**   | 
| RMSE   | **22031**  | 
| MAE    | **$18422**   | 

The R2 score scale ranges from 0 to 1. The higher the score, the better the model. 
For MAE and RMSE, lower scores are better.
As the model has a very high R2 score, this suggests the model works very well at predicting house prices. 
The RMSE and MAE seem high at first glance, but the values (in dollars) are relatively small in comparison to the actual 
prices of houses.

# Dataset

- **File:** `house_price_regression_dataset.csv`
- **Rows:** 1,000  · **Columns:** 8 · **Missing values:** 0

| Column                | 
|-----------------------|
| `Square_Footage`      | 
| `Num_Bedrooms`        | 
| `Num_Bathrooms`       |
| `Year_Built`          | 
| `Lot_Size`            | 
| `Garage_Size`         | 
| `Neighborhood_Quality`| 
| `House_Price`         | 

I accidentally forgot to include the "Year_Built" column when creating the model.

---
<img width="656" height="559" alt="output2" src="https://github.com/user-attachments/assets/943506c8-0b84-439a-b65c-d9db3b9d1f8f" />

This heatmap shows that house price has a very strong correlation with square footage. It appears to be the strongest predictor.




<img width="691" height="545" alt="output" src="https://github.com/user-attachments/assets/f661dfa8-3750-44b5-9add-ac856785dc7b" />

This plot compares the model's predicted house prices against the actual prices in the test set.
The red line is supposed to represent the perfect prediction. As the predicted values are closely clustered around the red line.
This indicates that the model's predictions are close to the true values.
