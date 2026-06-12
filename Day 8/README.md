# ML Classification and Model Evaluation

## Model Performance 

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | **0.8045** | 0.7931 | **0.6667** | **0.7244** | **0.8519** |
| Decision Tree | 0.7598 | 0.7407 | 0.5797 | 0.6504 | 0.7891 |
| Random Forest | 0.8101 | **0.8571** | 0.6087 | 0.7119 | 0.8502 |
| KNN | 0.6704 | 0.5833 | 0.5072 | 0.5426 | 0.6945 |

Logistic regression had the best performance on the test set. Random forest also performed well.
Logistic regression had the highest F1-Score (0.7244) and ROC-AUC (0.8519). 
Random Forest had slightly better accuracy (0.8101 vs 0.8045) and higher precision (0.8571 vs 0.7931), 
but its recall was lower (0.6087 vs 0.6667). 
Since F1-Score weighs both precision and recall equally, Logistic Regression appears to be the best model based on its perfomance on the test set.


## Cross-Validation F1-Score (Stratified 5-Fold)

| Model | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean |
|-------|--------|--------|--------|--------|--------|------|
| Logistic Regression | 0.7000 | 0.7287 | 0.7040 | 0.7153 | 0.7737 | **0.7243** |
| Decision Tree | 0.7634 | 0.7273 | 0.6833 | 0.7402 | 0.7080 | 0.7244 |
| Random Forest | 0.7903 | 0.7317 | 0.7119 | 0.7642 | 0.7478 | **0.7492** |
| KNN | 0.6508 | 0.6423 | 0.5891 | 0.6094 | 0.5970 | 0.6177 |

Random forest had the best performance using cross validation. Random forest achieved the highest average F1 score (0.7492). 
It consistently achieved high and stable scores compared to the other metrics. 

