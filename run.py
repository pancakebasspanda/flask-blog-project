from blog import app

# from blog import db
# db.create_all() in python terminal

# from blog import BlogPost
# BlogPost.query.all()
# BlogPost.query.filter_by(author='Pancake Bass Panda')[0]
# BlogPost.query.get(1)

if __name__ == "__main__":
    app.run(debug=True)
