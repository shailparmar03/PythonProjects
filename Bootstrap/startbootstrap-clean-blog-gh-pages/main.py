from flask import Flask, render_template
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/10165d721821df2fac59").json()

@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts=posts)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    for post in posts:
        if index == post["id"]:
            requested_post = post
            return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
