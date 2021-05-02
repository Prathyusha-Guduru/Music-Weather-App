from flask_wtf import FlaskForm
from wtforms import SubmitField

class checkWeatherForm(FlaskForm):
	submit = SubmitField('Check Weather')

	