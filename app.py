import numpy as np
from flask import Flask, request, render_template
import pickle
import ast  # To safely parse string representations of tuples/lists

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Convert form inputs to float
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]

    # Get prediction from model
    prediction = model.predict(final_features)

    # Parse the stringified list of tuples (e.g., from NumPy array)
    prediction_list_str = prediction[0]  # First string in array
    try:
        parsed_tuples = ast.literal_eval(prediction_list_str)
    except Exception as e:
        parsed_tuples = [("Error parsing prediction", str(e))]

    # Pass parsed data to the template
    return render_template('index.html', prediction_text=parsed_tuples)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
