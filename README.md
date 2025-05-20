# 🎬 Movie Collection App (Django Project)

This is a simple Django web application that allows users to **add**, **view**, and **search** movies. It demonstrates the use of Django's models, forms, views, templates, and static files
## 🚀 Features

- ✅ Add new movies (with poster upload)
- ✅ View list of all movies
- ✅ Search movies by hero name
- ✅ Admin panel support
- ✅ Responsive layout with background styling


## 🛠 Tech Stack

- **Backend**: Python 3, Django 5.2
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django DB)
- **Other**: Django Admin, Static & Media handling



## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/movie-collection-app.git
cd movie-collection-app
2. Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Start the development server
python manage.py runserver
Visit: http://127.0.0.1:8000/
       http://127.0.0.1:8000/
       http://127.0.0.1:8000/index/
       http://127.0.0.1:8000/add/
       http://127.0.0.1:8000/list/
🧾 Project Structure
movie/
├── movie/
│   └── settings.py, urls.py, wsgi.py...
├── movieapp/
│   ├── migrations/
│   ├── static/movieapp/
│   │   └── style.css, background.jpg
│   ├── templates/movieapp/
│   │   └── index.html, addmovie.html, listmovie.html
│   ├── admin.py, models.py, views.py, forms.py
├── manage.py
📋 Sample Movies in App
Inception

Interstellar

The Dark Knight

Hi Nanna

Sita Ramam

Aa Naluguru

Taare Zameen Par

M.S. Dhoni

Super 30

✨ To Do
✅ Add poster preview

🔲 Add edit/delete functionality

🔲 Deploy to cloud (e.g., PythonAnywhere, Render)

🧑 Author
POKALA PRATYUSHA
LinkedIn:www.linkedin.com/in/pokala-pratyusha-a6695a222
GitHub:https://github.com/PRATYU124

📃 License
This project is licensed under the MIT License.

