Weatherly App ☁️
A sleek and responsive Django-based weather application that provides real-time weather information for cities worldwide. Built with Python and powered by the Weatherstack API, this app features a clean, gradient-based UI to display temperature, humidity, and atmospheric conditions.

✨ Features
Real-time Search: Get instant weather updates by city name.

Detailed Metrics: Displays temperature, "feels like" temperature, humidity, and weather descriptions.

Visual Cues: Dynamic weather icons corresponding to current conditions.

Modern UI: A responsive, mobile-friendly design with a modern aesthetic.

🛠️ Tech Stack
Backend: Python 3.10+, Django 5.x

Frontend: HTML5, CSS3 (Flexbox/Grid)

API: Weatherstack API

Environment: Virtualenv

🚀 Getting Started (Ubuntu/Linux)
1. Clone the repository
Bash
git clone https://github.com/edwardmwinamilaalexander/weatherly
cd weatherly
2. Set up the Virtual Environment
Bash
# Create the environment
python3 -m venv env

# Activate the environment
source env/bin/activate
3. Install Dependencies
Bash
pip install django requests
4. API Key Configuration
To run this app, you need a Weatherstack API key:

Sign up at weatherstack.com.

Open weatherapp/views.py (or your relevant view file).

Replace the api_key variable with your unique key.

5. Run Migrations & Start Server
Bash
python3 manage.py migrate
python3 manage.py runserver
Visit http://127.0.0.1:8000/ in your browser!

📸 Screenshots
Current Weather View for London, United Kingdom.
