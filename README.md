# NLP App Features – Google Play Review Feature Mining

A **Flask-based Natural Language Processing (NLP) web application** that identifies **top trending features of mobile apps from Google Play Store reviews**.

The application uses a trained machine learning model to analyze review data and extract **frequently mentioned app features** for a selected app category.

Users can choose a category (e.g., Communication, Social, Productivity), and the system returns the **most commonly discussed features along with the number of reviews mentioning them**.

---

# Example Output

When a user selects the **Communication** category, the application returns trending features such as:

| Rank | Feature Name        | Total Reviews |
| ---- | ------------------- | ------------- |
| 1    | marco polo          | 228           |
| 2    | user friendly       | 189           |
| 3    | stay touch          | 166           |
| 4    | people hyperconnect | 135           |
| 5    | make call           | 126           |
| 6    | video message       | 57            |
| 7    | international call  | 56            |
| 8    | fiber medium        | 39            |
| 9    | location gps        | 36            |
| 10   | time record         | 31            |

Additional features extracted from review data include:

* group chat
* livestream option
* messaging platform
* interface privacy
* battery drain
* desktop version
* open profile

These insights help identify **which product features users talk about most in reviews**.

---

# Application Use Cases

This project can be used for:

* **Product Feature Analysis**
* **Customer Feedback Mining**
* **App Market Research**
* **User Experience Insights**
* **NLP Feature Extraction Experiments**

Companies can use similar approaches to understand:

* What users like most about an app
* What features are most discussed
* What improvements users request

---

# Tech Stack

* Python
* Flask
* NumPy
* Pandas
* Scikit-learn
* Gunicorn
* HTML / CSS

---

# Project Architecture

```
NLP-App-Features
│
├── app.py
├── model.pkl
├── Procfile
├── requirements.txt
├── README.md
│
├── static
│   └── css
│       └── styles.css
│
└── templates
    └── index.html
```

---

# How the Application Works

1. User selects an **app category** from the UI.
2. The selected input is sent to the Flask backend.
3. The backend loads a **pretrained machine learning model (`model.pkl`)**.
4. The model predicts the **top features mentioned in reviews**.
5. The result is returned as **feature names and review counts**.
6. Results are displayed in the web interface.

---

# Local Setup

Clone the repository:

```
git clone https://github.com/herbertmoses/NLP-App-Features.git
cd NLP-App-Features
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open the browser:

```
http://127.0.0.1:5000
```

---

# Production Run

Run using Gunicorn:

```
gunicorn app:app
```

---

# Deployment Options

The application can be deployed on:

* Azure App Service
* AWS Elastic Beanstalk
* Render
* Docker containers
* Kubernetes environments

---

# Example UI Flow

User selects category:

```
Communication
```

System returns:

```
Top Trending App Features
```

Ranked list of features extracted from user reviews.

---

# Future Improvements

Possible enhancements:

* Real-time Google Play review scraping
* Interactive charts for feature frequency
* Sentiment analysis of extracted features
* Support for multiple languages
* REST API version of the feature extractor

---