from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputForm(FlaskForm):

    field1 = StringField('Bedroom(in number)')
    field2 = StringField('Bathroom(in number)')
    field3 = StringField('Area(Sqft)')
    field4 = StringField('Furnish Type(Furnished=0,Semi-Furnished=1,Unfurnished=2)')
    field5 = StringField('Seller Type(Agent=0,Builder=1,Owner=2)')
    submit = SubmitField('Submit')
