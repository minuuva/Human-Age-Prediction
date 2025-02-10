# Human Age Predictor
🧑‍⚕️ Age Prediction Using Health and Lifestyle Factors

📄 Project Overview
This project aims to predict a person's age based on various health and lifestyle factors using Ordinary Least Squares (OLS) regression. The model was developed on a dataset containing attributes such as height, bone density, vision, hearing, cognitive function, stress levels, and physical activity. The goal is to create a tool for accurately predicting age, which can have applications in personalized healthcare and wellness programs.

📊 Dataset
The dataset used for this project is a synthetic dataset designed to simulate real-world scenarios. It includes the following features:

Gender: Categorical (Male/Female)
Height: Numeric (in cm)
Bone Density: Numeric (bone density score)
Vision: Numeric (vision score)
Hearing: Numeric (hearing score)
Cognitive Function: Numeric (cognitive function score)
Stress: Numeric (stress score)
Physical Activity: Categorical (Low, Moderate, High)

🔍 Exploratory Data Analysis (EDA)
Several exploratory data analysis (EDA) steps were conducted to understand the data better and prepare it for modeling:
Data Cleaning: Managed missing values and transformed categorical variables into numeric format.
Correlation Analysis: Investigated relationships between age and other variables to identify significant predictors.
Visualization: Used visual tools to explore the distribution of each feature and their correlations with age.

🧠 Model Building
An Ordinary Least Squares (OLS) Regression Model was developed to predict age based on the selected features:

Feature Selection: Chose features with significant correlations with age (e.g., Height, Bone Density, Vision, Hearing).
Data Preparation: Applied one-hot encoding for categorical variables and standardized numeric features.
Model Training: The OLS model was trained using the prepared dataset to predict age.

📊 Model Interpretation
Model Overview:
R-squared: 0.927 – The model explains approximately 92.7% of the variance in age, indicating high explanatory power.
Adjusted R-squared: 0.927 – Very close to the R-squared value, showing that adding predictors did not overfit the model.
F-statistic: 4215 – A large value, with a Prob(F-statistic) of 0.00, indicating that the model as a whole is statistically significant.

Coefficients and Interpretation:
Intercept (89.8644) – Represents the predicted age when all other variables are at their baseline levels.
Gender[T.Male] (0.0610) – Positive coefficient but not statistically significant (p-value = 0.835), indicating gender does not significantly influence age in this model.
Physical_Activity[T.Low] (0.2872) – Positive coefficient but not significant (p-value = 0.308), indicating no strong evidence that low physical activity impacts age.
Physical_Activity[T.Moderate] (0.4596) – Close to significance (p-value = 0.076), suggesting moderate physical activity might affect age positively, but this is not definitive.
Height (0.0065) – Not significant (p-value = 0.678), indicating that height does not have a substantial effect on predicting age.
Bone_Density (-26.0485) – Highly significant (p-value = 0.000), suggesting that lower bone density is strongly associated with younger age.
Vision (-33.0361) – Highly significant (p-value = 0.000), showing that poorer vision strongly correlates with younger age.
Hearing (0.1512) – Significant (p-value = 0.000), indicating that better hearing is associated with older age.
Cognitive_Function (-0.0760) – Significant (p-value = 0.000), suggesting better cognitive function predicts a younger age.
Stress (-0.0211) – Not significant (p-value = 0.593), indicating no substantial impact of stress on age.

Model Diagnostics:
Durbin-Watson (2.038) – This value is close to 2, suggesting there is no strong autocorrelation in the residuals.
Omnibus, Jarque-Bera, Prob(Omnibus), Prob(JB) – Non-significant p-values indicate that the residuals are normally distributed.
Condition Number (4.98e+03) – A large value that suggests potential multicollinearity among the independent variables.

Summary:
Significant predictors of age include Bone Density, Vision, Hearing, and Cognitive Function.
Factors such as Gender, Height, Stress, and Physical Activity do not significantly impact age.
The model is overall significant and explains a large proportion of the variance in age, although there may be some concerns about multicollinearity.

💻 How to Use the Model
The trained model can predict age based on new input data (e.g., height, bone density, vision, etc.).

Input Data: Provide details such as gender, height, bone density, vision, hearing, cognitive function, stress level, and physical activity.

Output: The model returns a numerical age prediction.

EXAMPLE:
`#Create a DataFrame with the input data
input_data = pd.DataFrame({
    'Gender': ['Male'],
    'Height': [170],
    'Bone_Density': [0.5],
    'Vision': [-1.0],
    'Hearing': [0.2],
    'Cognitive_Function': [0.1],
    'Stress': [0.3],
    'Physical_Activity': ['Moderate']
})`

#Predict age using the fitted model
`predicted_age = results.predict(input_data)
print('Predicted Age:', predicted_age.values)`

📈 Results
The model achieved an R-squared of 92.7%, indicating a high level of accuracy in predicting age based on health and lifestyle factors.

🤝 Contributing
Feel free to submit issues or pull requests for enhancements, bug fixes, or additional features. All contributions are welcome!

📧 Contact
For questions or suggestions, please reach out to mminu0814@gmail.com
