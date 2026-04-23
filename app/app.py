from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open(r"D:\Crop_prediction_app\model\xgb_model (1).pkl", 'rb'))
le = pickle.load(open(r"D:\Crop_prediction_app\model\label_encoder (1).pkl", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ndvi = float(request.form['ndvi'])
        evi = float(request.form['evi'])
        ndwi = float(request.form['ndwi'])
        rainfall = float(request.form['rainfall'])
        temp = float(request.form['temp'])

        features = np.array([[ndvi, evi, ndwi, rainfall, temp]])
        prediction = model.predict(features)
        result = le.inverse_transform(prediction)[0]

        return render_template('result.html', prediction=result)

    except:
        return "Error in input"

if __name__ == "__main__":
    app.run(debug=True)