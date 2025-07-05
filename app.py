from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('diabetes_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [float(x) for x in request.form.values()]
        prediction = model.predict([inputs])[0]
        result = 'Diabetic' if prediction == 1 else 'Not Diabetic'
        return render_template('index.html', prediction_text=f'Result: {result}')
    except:
        return render_template('index.html', prediction_text='Invalid input. Please enter all fields correctly.')

if __name__ == '__main__':
    app.run(debug=True)
