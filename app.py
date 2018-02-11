from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from database import db_session
from models import User, Post
from config import Config
from models import LoginForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def upload():

    all_users = User.query.all()
    all_posts = Post.query.all()

    context = {
    'all_users': all_users,
    'all_posts': all_posts,
    }
    return render_template('landing.html', context = context)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()