from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class BlogForm(FlaskForm):

    blog_title = StringField('Place your blog title here',validators=[Required()])
    blog_description = StringField('Give a brief blog description',validators=[Required()])
    story = TextAreaField('Give the blog content',validators=[Required()])
    category = SelectField('Category', choices=[('Gaming','Gaming'),('Career','Career'),('Finance','Finance'),('Sports','Sports'),('Fitness','Fitness')], validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):

    details = TextAreaField('Your comment',validators=[Required()])

    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# class DeletePost(FlaskForm):
#     comment_id = StringField()
#     delete = SubmitField('Delete')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')