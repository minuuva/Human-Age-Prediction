# -*- coding: utf-8 -*-
"""prediction_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NDAAXbPUlfs4j4O41QuTS7p9dz1_Lvlz
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('health.data.csv')
df.head()

df.rename(columns={
    'Height (cm)': 'Height',
    'Weight (kg)': 'Weight',
    'Blood Pressure (s/d)': 'Blood_Pressure',
    'Cholesterol Level (mg/dL)': 'Cholesterol',
    'Blood Glucose Level (mg/dL)': 'Blood_Glucose',
    'Bone Density (g/cm²)': 'Bone_Density',
    'Vision Sharpness': 'Vision',
    'Hearing Ability (dB)': 'Hearing',
    'Physical Activity Level': 'Physical_Activity',
    'Smoking Status': 'Smoking',
    'Alcohol Consumption': 'Alcohol',
    'Chronic Diseases': 'Chronic_Diseases',
    'Medication Use': 'Medication',
    'Family History': 'Family_History',
    'Cognitive Function': 'Cognitive_Function',
    'Mental Health Status': 'Mental_Health',
    'Sleep Patterns': 'Sleep',
    'Stress Levels': 'Stress',
    'Pollution Exposure': 'Pollution',
    'Sun Exposure': 'Sun_Exposure',
    'Education Level': 'Education',
    'Income Level': 'Income',
    'Age (years)': 'Age'
}, inplace=True)

df.info()

df.shape

df.isnull().sum()

for column in df.columns:
  df[column].fillna(df[column].mode()[0], inplace = True)

df.isnull().sum()

df[df.duplicated()]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

le = LabelEncoder()
scaler = StandardScaler()

x = df.drop('Age', axis = 1)
y = df['Age']

numerical_cols = x.select_dtypes(exclude = ['object']).columns
x[numerical_cols] = scaler.fit_transform(x[numerical_cols])
x.head()

for col in x.select_dtypes(include = ['object']):
  x[col] = le.fit_transform(x[col])
  x.head()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
#test_size = 0.2 (20% of data for testing, 80% for training)

x_train.shape, x_test.shape

lr = LinearRegression()
lr.fit(x_train, y_train)

y_predicted= lr.predict(x_test)
y_pred= lr.predict(x_test)

mae = mean_absolute_error(y_test, y_predicted)
mae

mse = mean_squared_error(y_test, y_predicted)
mse

lr.coef_

lr.intercept_

r2_score(y_test, y_pred) * 100

y_test.head()

y_pred[0:5]

import statsmodels.formula.api as smf
df

# based on the correlation above, some attributes that have positive or negative correlation with age have been chosen"
model = smf.ols('Age ~ Gender + Height + Bone_Density + Vision + Hearing + Cognitive_Function + Stress + Physical_Activity', data=df)
results = model.fit()

print(results.summary())

# Check for missing values
df.isnull().sum()

# Convert categorical features to numerical using one-hot encoding or label encoding
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  # Example encoding for Gender
df = pd.get_dummies(df, columns=['Education', 'Income'])  # One-hot encode Education and Income

# Split into features (X) and target (y)
X = df.drop('Age', axis=1)  # All features except Age
y = df['Age']  # Target variable

# Normalize the feature data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Choose and train a regression model (e.g., Random Forest Regressor)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using mean absolute error and R-squared
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")