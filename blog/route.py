from flask import render_template, request, redirect
from models import blogpost
from blog import app
from blog import db

# list of dictionaries
all_posts = [
    {
        "title": "post 1",
        "content": "content of post 1",
        "author": "Owen",
    },
    {
        "title": "post 2",
        "content": "content of post 2",
    }
]
BlogPost = blogpost.BlogPost

# blog route with usable parameters
@app.route('/home/users/<string:name>/posts/<int:paramid>')
def hello(name, paramid):
    return "Hello World " + name + ", your id is " + str(paramid)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        post_author = request.form["author"]
        new_blogpost = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_blogpost)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template("posts.html", posts=all_posts)


@app.route("/posts/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        post_author = request.form["author"]
        new_blogpost = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_blogpost)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template("new_post.html")


@app.route("/posts/delete/<int:id>")
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/posts")


@app.route("/posts/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect("/posts")
    else:
        return render_template("/edit.html", post=post)

