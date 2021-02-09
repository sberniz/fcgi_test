from flask import Flask
import pandas as pd
import logging
# Imports Predict from test.py file
from test import predict
logging.basicConfig(filename='info.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' ,level=logging.INFO)
from category_encoders import OrdinalEncoder
import joblib
app= Flask(__name__)
@app.route('/')
def root():
#    app_pipe = joblib.load('web-app/assets/dating_rf2.joblib')
#    df = pd.read_csv('web-app/dating_csv.csv')
#    df.drop('status',axis=1,inplace=True)
#    test_file = df[df.index==0]
    # Test Predict function from test.py file. 
    result = predict()
    return str(result)
