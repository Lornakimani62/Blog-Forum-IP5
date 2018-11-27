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
    Fitness = Blog.query.filter_by(category="Fitness").all()

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

# update photos view function
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
# Blog view function
@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()


    if blog_form.validate_on_submit():

        blog_title= blog_form.blog_title.data
        blog_description= blog_form.blog_description.data
        story= blog_form.story.data
        category= blog_form.category.data

        # Updated  instance
        new_blog = Blog(blog_title=blog_title,blog_description=blog_description,story=story,category=category,user=current_user)
        blogs = Blog.query.filter().all()
        # save  method
        new_blog.save_blog()

        return redirect(url_for('main.blog'))

    title = 'New Blog'
    return render_template('new_blog.html',title = title, blog_form=blog_form)

# View function to display blog articles
@main.route('/blog', methods = ['GET','POST'])
@login_required
def blog():
    Gaming = Blog.query.filter_by(category="Gaming").all()
    Career = Blog.query.filter_by(category="Career").all()
    Finance = Blog.query.filter_by(category="Finance").all()
    Gossip = Blog.query.filter_by(category="Gossip").all()
    Sports = Blog.query.filter_by(category="Sports").all()
    Fitness = Blog.query.filter_by(category="Fitness").all()

    blogs = Blog.query.filter().all()

    return render_template('blogs.html',Gaming=Gaming,Career=Career,Finance=Finance,Gossip=Gossip,Sports=Sports,Fitness=Fitness,blogs=blogs)

# The view function for comments
@main.route('/comment/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    comment = Comment.query.filter_by(blog_id=id)

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        comment = form_comment.details.data

        new_comment = Comment(comment= comment,blog_id=id,user=current_user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html',form_comment = form_comment,comment=comment)