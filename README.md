📝 Simple Flask Blog App

A lightweight Flask application that demonstrates full CRUD functionality using a JSON file as persistent storage.
Users can create, read, update, and delete blog posts — each stored as a dictionary inside storage.json.

This project is ideal for learning:

Basic Flask routing

Working with templates

Handling GET/POST requests

Managing JSON-based storage

Implementing CRUD functionality

📁 Project Structure
your-project-folder/
├── app.py
├── data/
│   └── storage.json
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
├── static/              # (Optional, for CSS/JS/images)
└── README.md

🚀 Features
✔ View all blog posts

The homepage (/) loads all posts from storage.json and displays them.

✔ Add new posts

The /add route displays a form and saves new posts with a unique ID.

✔ Update existing posts

The /update/<post_id> route pre-fills a form with existing data and updates the selected post.

✔ Delete posts

The /delete/<post_id> route removes a post from the JSON storage.

✔ JSON-based storage

No database required — all posts are stored in and loaded from data/storage.json.

🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # macOS/Linux

venv\Scripts\activate      # Windows

3. Install dependencies
pip install flask

4. Ensure the JSON storage file exists

Inside data/storage.json:

[]


(An empty list to start with.)

5. Run the app
python app.py


Then open in your browser:

http://localhost:5001

🧠 How It Works
Loading posts
def load_blog_posts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

Saving posts
def save_blog_posts(posts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)

CRUD Routes
Route	Method	Description
/	GET	Show all blog posts
/add	GET/POST	Add new post
/update/<id>	GET/POST	Update existing post
/delete/<id>	GET	Delete post
🧪 Example JSON Entry
{
    "id": 1,
    "author": "Alice",
    "title": "My First Post",
    "content": "Hello world!"
}

📌 Notes

This project is for learning and small personal usage — not for production.

JSON storage is simple but not suitable for concurrent writes.

You can style the templates using the optional /static folder.