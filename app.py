from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)  # no need for template_folder now

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'house.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        yr_build = int(request.form['yr_build'])
        features = np.array([[yr_build]])
        prediction = model.predict(features)[0]
        return render_template(
            'result.html',
            yr_build=yr_build,
            price=f"Rs.{prediction:,.2f}"
        )
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
