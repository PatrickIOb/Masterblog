📝 Simple Flask Blog App

A lightweight Flask application demonstrating full CRUD functionality using a JSON file as persistent storage.
Users can create, read, update, and delete blog posts, each stored as an entry inside storage.json.

This project is ideal for learning:

Flask routing

GET/POST form handling

Template rendering with Jinja2

JSON file storage

Basic front-end styling

## 📁 Project Structure

```
your-project-folder/
├── app.py
├── data/
│   └── storage.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
├── static/
│   └── style.css
└── README.md
```


🎨 Styling

A basic stylesheet exists at:

static/style.css


To use it in your templates, include this line inside the <head> of each HTML file:

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


You can expand this file to adjust layout, spacing, colors, or responsiveness.

🚀 Features
✔ View all posts

Homepage loads all posts from JSON and displays them.

✔ Add new posts

/add shows a form and stores a new post with a unique ID.

✔ Update existing posts

/update/<id> loads a form with existing data and saves changes.

✔ Delete posts

/delete/<id> removes a post from storage.

✔ JSON-based persistence

All application data lives in data/storage.json.

🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3. Install Flask
pip install flask

4. Ensure the JSON storage file exists
data/storage.json


with contents:

[]

5. Run the application
python app.py


Then open in your browser:

http://localhost:5001

🧠 How It Works
Load posts
def load_blog_posts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

Save posts
def save_blog_posts(posts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)

CRUD Routes
Route	Method	Description
/	GET	Display all posts
/add	GET/POST	Create new post
/update/<id>	GET/POST	Edit existing post
/delete/<id>	GET	Remove a post

📜 License

This project is free for learning and personal use.
