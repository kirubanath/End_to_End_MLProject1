#required libraries:
import pickle
from flask import Flask, request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

#loading the model using pickle:
regmodel = pickle.load(open('regmodel.pkl','rb'))
scaler   = pickle.load(open('scale.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    output = regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text =f"The house price prediction is: {output}" )

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
  
    



