from flask import Flask
from sklearn.externals import joblib
import json

import pandas as pd

app = Flask(__name__)

@app.route("/iris/")
def iris():
    df = pd.read_csv('iris.csv')
    df = df.to_json(orient='records')
    return df


@app.route("/iris/predict/<sepal_length>/<sepal_width>/<petal_length>/<petal_width>/")
def predict(sepal_length, sepal_width, petal_length, petal_width):

    sepal_length = float(sepal_length)
    sepal_width  = float(sepal_width)
    petal_length = float(petal_length)
    petal_width  = float(petal_width)

    ## carregando o modelo
    knn = joblib.load('iris_modelo.pkl')

    classe = knn.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    proba  = knn.predict_proba([[sepal_length, sepal_width, petal_length, petal_width]])

    proba = proba[0].tolist()

    classes = knn.classes_.tolist()

    json_resposta = json.dumps({
      "classe": classe[0],
      "probabilidade": proba,
      "targets":classes}  , ensure_ascii=False).encode('utf8')

    return json_resposta

app.run(port=5000, host="0.0.0.0")





