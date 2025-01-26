
from flask import Flask, request, render_template 
from app import app
from .forms import InputForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


@app.route('/', methods=['GET', 'POST'])
def index():
    data=pd.read_csv("D:/shub/app/Pune rent2.csv")
    data=data.dropna()
    categorical_columns = ['bedroom', 'bathroom', 'area', 'furnish_type', 'seller_type']
    label_encoder = LabelEncoder()
    for column in categorical_columns:
        data[column] = label_encoder.fit_transform(data[column])
        print(data.head())
    X=data[["bedroom","bathroom","area","furnish_type","seller_type"]]
    y=data["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    sc = StandardScaler()
    X_train_sc = sc.fit_transform(X_train)
    X_test_sc = sc.transform(X_test)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train_sc, y_train)
    rf_predictions = rf_model.predict(X_test_sc)
    form = InputForm()
    if form.validate_on_submit():
        field1 = request.form.get("1")
        field2 = request.form.get("2")
        field3 = request.form.get("3")
        field4 = request.form.get("4")
        field5 = request.form.get("5")
        total = rf_model.predict([[field1,field2,field3,field4,field5]])
        for i in total:
            result = round(i,2)
            print(result)
        return render_template('result.html', result=result)
    return render_template('index.html', form=form)
