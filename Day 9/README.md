# IMDB Sentiment Analysis


This project uses Natural Language Processing (NLP) techniques to classify movie reviews from the IMDB dataset as either **Positive** or **Negative**. Logistic Regression was used in this instance.


## Dataset

- **Dataset:** IMDB Movie Reviews Dataset
- **Total Reviews:** 50,000
- **Classes:**
  - Positive: 25,000
  - Negative: 25,000

---


###  Model Training
- Logistic Regression

---

###  Model Evaluation
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- 5-Fold Cross Validation

---

## Model Performance

### Test Set Metrics

| Metric | Score |
|----------|----------|
| Accuracy | **88.72%** |
| Precision | **87.75%** |
| Recall | **90.00%** |
| F1 Score | **88.86%** |

---

### Cross-Validation Results

5-Fold Cross Validation Scores:

| Fold | Accuracy |
|------|----------|
| 1 | 88.55% |
| 2 | 88.33% |
| 3 | 88.17% |
| 4 | 88.14% |
| 5 | 88.20% |

**Average Cross-Validation Accuracy:** **88.28%**

---

### Classification Report

| Class | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| Negative | 0.90 | 0.87 | 0.89 |
| Positive | 0.88 | 0.90 | 0.89 |

---

### Confusion Matrix

| Actual / Predicted | Negative | Positive |
|-------------------|----------|----------|
| True | 4372 | 4500 |
| False | 500 | 628|

Where:

- **True Positives (TP):** 4500
- **True Negatives (TN):** 4372
- **False Positives (FP):** 628
- **False Negatives (FN):** 500

---


## Example Predictions on New Data

| Review | Prediction|
|----------|----------|
| "This was a great movie!" | Positive |
| "I hated this movie and thought it was awful" | Negative |
| "I am not really eager to see the next movie in the franchise" | Negative |
| "It was a thrilling addition to the series" | Positive |

---

