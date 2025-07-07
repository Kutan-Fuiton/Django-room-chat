# 🗨️ Django Real-Time Chat App

A simple real-time group chat application built using Django. This project allows users to join or create chat rooms and communicate with others in real-time through an intuitive web interface.

---

## 🚀 Features

- 🔹 **Create or Join Rooms**: Users can enter any room name to either join an existing room or create a new one.
- 💬 **Live Messaging**: Messages are sent and retrieved in real-time using AJAX polling.
- 🧠 **Persistent Chat History**: All messages are stored in a database and retrieved when a user joins the room.
- 🎨 **Simple UI**: Clean and minimal HTML templates for the home page and chat interface.
- ⚙️ **Django Backend**: Utilizes Django models for `Room` and `Message`, with views for sending and fetching messages.

---

## 🏗️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (AJAX for real-time updates)
- **Database**: SQLite (default with Django)

---

## 📁 Project Structure

```text
chat_app/
├── chat/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   └── room.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── chat_app/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/django-chat-app.git
cd django-chat-app
```

2. **Create a Virtual Environment & Install Dependencies**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run Migrations**

```bash
python manage.py migrate
```

4. **Start the Development Server**

```bash
python manage.py runserver
```

5. **Visit the App**

Open your browser and go to:  
[http://localhost:8000](http://localhost:8000)
