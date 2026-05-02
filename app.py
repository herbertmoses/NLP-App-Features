import logging
from flask import Flask, request, render_template

from config import Config
from utils import parse_prediction, chunk_list
from services.model_service import ModelService
from data.categories import CATEGORIES

# deployment_message = "Azure DevOps CI/CD Deployment Successful!"

app = Flask(__name__)
app.config.from_object(Config)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize service
model_service = ModelService(Config.MODEL_PATH)


@app.route('/')
def home():
    logger.info("Rendering home page")
    return render_template(
        'index.html',
        categories=CATEGORIES,
        deployment_message=deployment_message
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input processing
        float_features = [float(x) for x in request.form.values()]
        logger.info(f"Received input: {float_features}")

        # Model prediction
        prediction = model_service.predict(float_features)
        logger.info(f"Raw prediction: {prediction}")

        # Parsing
        parsed_tuples = parse_prediction(prediction)

        # Chunking
        chunked_results = chunk_list(parsed_tuples, chunk_size=Config.CHUNK_SIZE)

        return render_template(
            'index.html',
            categories=CATEGORIES,
            results=chunked_results,
            deployment_message=deployment_message
        )

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")

        return render_template(
            'index.html',
            categories=CATEGORIES,
            results=[[("Error", str(e))]],
            deployment_message="Something went wrong"
        )


if __name__ == "__main__":
    app.run(debug=Config.DEBUG, use_reloader=False)

# Azure entry point
application = app
