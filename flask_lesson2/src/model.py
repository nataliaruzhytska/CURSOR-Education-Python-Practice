import uuid

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField, TextAreaField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):

    id = str(uuid.uuid4())
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    price = IntegerField('price', validators=[DataRequired()])
    submit = SubmitField()
    image = FileField()


class SupermarketForm(FlaskForm):
    id = str(uuid.uuid4())
    name = StringField('name', validators=[DataRequired()])
    location = StringField('location')
    image = FileField()
    submit = SubmitField()
