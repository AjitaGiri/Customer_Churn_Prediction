## End to end ML project on Customer Churn Prediction

## Overview
This project predicts whether a telecom customer will churn or stay based on demographic, service usage, and billing information. It demonstrates a complete machine learning workflow, including data preprocessing, feature engineering, model building, evaluation, and business insights.

## Problem Statement
Customer churn leads to revenue loss for businesses. Predicting churn allows the company to proactively retain customers through targeted strategies.
- Goal: Identify customers likely to churn
- Problem type: Binary classification
- Business Impact: Reduce churn rate, improve customer retention, and maximize revenue.

## Dataset
- Source: Kaggle
- Rows: ~7,000 customers
- Key Features: 
    - tenure: Number of months the customer stayed
    - MonthlyCharges: Amount billed monthly
    - TotalCharges: Total amount billed
    - Contract: Type of contract (Month-to-Month, One year, Two year)
    - SeniorCitizen: 0 or 1
    - Other categorical features: PaymentMethod, InternetService etc
- Target: Churn (Yes/No)

## Approach
1. Exploratory Data Analysis (EDA)
  - Checked missing values and data types.
  - Visualized distributions and relationships between numeric and categorical features.
  - Identified multicollinearity between TotalCharges, MonthlyCharges, and tenure.

2. Feature Engineering
  - Created AvgChargesPerMonth = TotalCharges/ tenure to reduce multicollinearity.
  - Scaled numeric features using StandardScaler.
  - Encoded categorical variables:
    - Ordinal: Contract type using OrdinalEncoder
    - Nominal: for output column Churn, used LabelEncoder and OneHotEncoder for remaining nominal features.

3. Pipeline & ColumnTransformer
  - Used ColumnTransformer and Pipeline to streamline preprocessing.
  - Ensured transformations are consistent on train and test sets.

4. Modeling
  - Build and compared multiple models:
     - Logistic Regression
      - Decision Tree
      - Random Forest
  - Evaluated models using Accuracy, Precision, Recall, ROC-AUC.
  - Addressed class imbalance using class_weight='balanced' 

## Model Evaluation Summary
Best Model: Logistic Regression
- ROC-AUC ~0.84
- Good balance between precision and recall
- Preferred due to stability and interpretability

## Tools & Technologies
- Python Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn
- ML Algorithms: LogisticRegression, Decision Tree, Random Forest
- Preprocessing: Pipeline, ColumnTransformer, FunctionTransformer

# Key Insights:
 - Customers with month-to-month contracts are more likely to churn.
 - Higher monthly charges combined with low tenures increase churn probability.
 - Logistic Regression provided the best balance between precision and recall.

 ## Business Recommendations
 1. Target customers with month-to-month contracts for retention campaigns.
 2. Offer incentives or loyalty plans for customers with high monthly charges and short tenure.
 3. Consider hyperparameter tuning for Decision Tree or Random Forest to improve predictive performance.

## Conclusion
This project demonstrates an end-to-end machine learning pipeline including data preprocessing, feature engineering, model building, evaluation, and interpretation. 
Logistic Regression was selected as the final model due to its strong ROC-AUC score and balanced performance across precision and recall. The model can be used to identify customers at risk of churn and support business retention strategies.