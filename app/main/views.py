from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Role,Blog,Comment
from .forms import updateProfile,BlogForm,CommentForm

# View function for the landing page
@main.route('/')
    title = 'Dashboard' if current_user.is_authenticated else 'Home'

    Gaming = Blog.query.filter_by(category="Gaming").all()
    Career = Blog.query.filter_by(category="Career").all()
    Finance = Blog.query.filter_by(category="Finance").all()
    Gossip = Blog.query.filter_by(category="Gossip").all()
    Sports = Blog.query.filter_by(category="Sports").all()
    Fitness = Blog.query.filter_by(category="Fitness")

    blogs = Blog.query.filter().all()
    return render_template('index.html',title=title,Gaming=Gaming,Career=Career,Finance=Finance,Gossip=Gossip,Sports=Sports,Fitness=Fitness,blogs=blogs)