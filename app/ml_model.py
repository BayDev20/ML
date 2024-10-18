import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np

def preprocess_data(df):
    """
    Preprocess the data by encoding categorical variables.
    
    :param df: DataFrame containing the data to preprocess.
    :return: Preprocessed DataFrame.
    """
    le = LabelEncoder()
    df['sex'] = le.fit_transform(df['sex'])
    df['smoker'] = le.fit_transform(df['smoker'])
    df['region'] = le.fit_transform(df['region'])
    return df

def train_and_save_model():
    """
    Train a Random Forest model on the insurance data and save it to a file.
    """
    # Load the full dataset
    df = pd.read_csv('data/insurance.csv')
    print(f"Loaded {len(df)} records from insurance.csv")
    
    df = preprocess_data(df)
    
    # Prepare features (X) and target variable (y)
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared Score: {r2:.2f}")
    
    # Calculate and print feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Save the trained model
    joblib.dump(model, 'insurance_predictor.joblib')
    print("\nModel trained and saved as insurance_predictor.joblib")

def predict_charges(age, sex, bmi, children, smoker, region):
    """
    Predict insurance charges using the trained model.
    
    :param age: Age of the person
    :param sex: Sex of the person
    :param bmi: BMI of the person
    :param children: Number of children
    :param smoker: Smoking status
    :param region: Region of residence
    :return: Predicted insurance charge
    """
    model = joblib.load('insurance_predictor.joblib')
    df = pd.DataFrame([[age, sex, bmi, children, smoker, region]], 
                      columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
    df = preprocess_data(df)
    prediction = model.predict(df)[0]
    return np.round(prediction, 2)

if __name__ == "__main__":
    train_and_save_model()
