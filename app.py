from flask import Flask, jinja2, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data/storage.json')


def load_blog_posts():
    """Load blog posts from JSON storage file."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
