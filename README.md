# URL Shortener

A simple and efficient **URL Shortener** built with **Django**.  
This project allows users to generate shortened versions of long URLs and easily manage them through a clean, user-friendly interface.

## 🚀 Features

- Create shortened URLs
- Redirect shortened URLs to original links
- Clean and minimal UI
- Django backend for efficient handling
- Unique slug generation for each URL

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (Default Django setup)



## 🧩 Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MeenakshiPramod/URL-Shortener.git
   cd URL-Shortener
2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the server:**
   ```bash
   python manage.py runserver


## How it Works
- Users enter a long URL on the homepage.
- The backend generates a unique short key.
- When the short URL is visited, Django redirects to the original URL.
