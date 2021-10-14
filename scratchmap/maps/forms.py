from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from scratchmap import db
from scratchmap.models import Scratched_Map

#Create a Scratch Map from the possible Map Types
class MapForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    #Map Type Select Field should have all possible map_type choices
    map_type = SelectField('Select Map', choices= [()])
    submit = SubmitField('Create')

#Edit the Scratch Map (Add/Remove countries from the visited and wish_list lists)
class ScratchedMapForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    visited = SelectMultipleField('Visted', choices=[()])
    wish_list = SelectMultipleField('Wish List', choices=[()])
    submit = SubmitField('Scratch')
