import category_encoders
from category_encoders import OneHotEncoder,OrdinalEncoder
import pandas as pd 
import joblib
def predict():
    app_pipe = joblib.load('web-app/assets/dating_rf2.joblib')
    df = pd.read_csv('web-app/dating_csv.csv')
    df.drop('status',axis=1,inplace=True)
    test_file = df[df.index==0]
    print(test_file)
    y_pred = app_pipe.predict(test_file)
    print(y_pred[0])
    return y_pred[0]
if __name__ == "__main__":
    tester = predict()
    print(tester)
