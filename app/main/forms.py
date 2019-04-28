from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    blog_body = TextAreaField('Write Blog Content',validators=[Required()])
    blog_category = SelectField('Blog Category',choices=[('Sports-Blog','Sports'),('Travel-Blog','Travel'),('Fitness-Blog','Fitness'),('Fashion-Blog','Fashion'),('Food-Blog','Food'),('Political-Blog','Politics')],validators=[Required()])
    submit = SubmitField('Submit Blog')

class CommentForm(FlaskForm):
    name = StringField('Enter Your Name',validators=[Required()])
    comment = TextAreaField('Comments', validators=[Required()])
    submit = SubmitField('Submit Comment')
