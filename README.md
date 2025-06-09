# 🌍 Wanderlust Flask App

**Wanderlust** is a Flask-based web application that recommends top-rated places to visit in a given city using the [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3). The app is deployed on **AWS Elastic Beanstalk**, making it scalable and publicly accessible.


** Use desktop for better UI**
---

## 🚀 Features

- 🔍 Search for attractions in any city
- 📊 Real-time data from Yelp (ratings, images, URLs)
- 📦 Flask backend with REST API endpoint
- 🌐 Deployed on AWS Elastic Beanstalk (Free Tier)

---

## 📦 Technologies Used

- **Backend**: Flask, Gunicorn
- **Frontend**: HTML, CSS, JavaScript
- **API**: [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3)
- **Deployment**: AWS Elastic Beanstalk, Amazon Linux 2 (Python 3.9)

---

## 🧠 How It Works

1. **User Input**: The user enters a city name.
2. **API Request**: The Flask backend makes a request to the Yelp API:

3. **Response Processing**: Top results (name, rating, image, address) are extracted and sent to the frontend.
4. **Dynamic UI**: The frontend dynamically updates the grid of destination cards based on the response.

---

## 🛠️ Project Structure


---

## 🌐 Live Demo

Deployed URL:  
(http://wanderlust-flask-app-env-1.eba-82yvez5t.us-east-2.elasticbeanstalk.com/)
---

## 🔑 Yelp API Key Setup

1. Create a Yelp account and get an API key:  
   [https://www.yelp.com/developers/v3/manage_app](https://www.yelp.com/developers/v3/manage_app)

2. Add the API key as an environment variable in Elastic Beanstalk:
   - AWS Console → Elastic Beanstalk → Configuration → Software
   - Add:  
     ```
     Key: YELP_API_KEY
     Value: <your-key-here>
     ```

3. In `application.py`:
   ```python
   import os
   API_KEY = os.environ.get("YELP_API_KEY")


🧑‍💻 Local Setup

git clone https://github.com/yourusername/wanderlust-flask-app.git
cd wanderlust-flask-app
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python application.py
