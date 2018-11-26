from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User,Role,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm

# View function for the landing page
@main.route('/')
def index():

    Gaming = Blog.query.filter_by(category="Gaming").all()
    Career = Blog.query.filter_by(category="Career").all()
    Finance = Blog.query.filter_by(category="Finance").all()
    Gossip = Blog.query.filter_by(category="Gossip").all()
    Sports = Blog.query.filter_by(category="Sports").all()
    Fitness = Blog.query.filter_by(category="Fitness")

    blogs = Blog.query.filter().all()
    return render_template('index.html',Gaming=Gaming,Career=Career,Finance=Finance,Gossip=Gossip,Sports=Sports,Fitness=Fitness,blogs=blogs)

# View function for profile
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
# Update profile view function
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)