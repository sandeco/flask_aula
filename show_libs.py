from flask import Flask, request
import pandas as pd
import numpy as np
import tensorflow.keras as keras
import tensorflow as tf
import json

app = Flask(__name__)

@app.route("/bibs/version/json/")
def bibs_version_json():

	json_resposta = json.dumps({
      "numpy": np.__version__,
      "pandas": pd.__version__,
      "tensorflow": tf.__version__,
	  "keras": keras.__version__}, ensure_ascii=False).encode('utf8')

	return json_resposta

@app.route("/jsonmsg/<json_msg>")
def add_message(json_msg):
    return json_msg




@app.route("/tensorflow/version/")
def versao_tensorflow():
	return tf.__version__


@app.route("/keras/version/")
def versao_keras():
	return keras.__version__


@app.route("/pandas/version/")
def versao_pandas():
	return pd.__version__


@app.route("/numpy/version/")
def versao_numpy():
	return np.__version__



app.run(port=5000, host="0.0.0.0")
