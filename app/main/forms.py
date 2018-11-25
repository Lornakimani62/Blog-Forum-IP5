from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class BlogForm(FlaskForm):

    title = StringField('Place your blog title here',validators=[Required()])

    Description = StringField('Give a brief blog description',validators=[Required()])

    story = TextAreaField('Give the blog content',validators=[Required()])

    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    comment = TextAreaField('Your comment',validators=[Required()])

    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# class DeletePost(FlaskForm):
#     comment_id = StringField()
#     delete = SubmitField('Delete')