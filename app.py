from flask import Flask, redirect, render_template, request, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data/storage.json')


def load_blog_posts():
    """Load blog posts from JSON storage file."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_blog_posts(posts):
    """Save blog posts to JSON storage file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)

@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST': #This is the post request that is executed when the user sends the filled out form
        if request.method == 'POST':
            author = request.form.get("author")
            title = request.form.get("title")
            content = request.form.get("content")

            posts = load_blog_posts()

            if posts:
                unique_id = max(post["id"] for post in posts) + 1
            else:
                unique_id = 1

            new_post = {
                "author": author,
                "title": title,
                "content": content,
                "id": unique_id
            }
            posts.append(new_post)
            save_blog_posts(posts)

            return redirect(url_for('index')) #This is executed after the dict is updated and shows all posts

    return render_template('add.html') #This is the get requests that shows the form to the user

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_blog_posts()

    # Keep all posts except the one with the matching ID
    posts = [post for post in posts if post["id"] != post_id]

    save_blog_posts(posts)
    # Redirect back to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
