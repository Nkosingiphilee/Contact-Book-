from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class AddContact(FlaskForm):
    name = StringField('name',
                       validators=[DataRequired('missing'),
                                   Length(min=4, max=20)])
    number = StringField('number',
                         validators=[DataRequired('missing'),
                                     Length(min=10, max=10)])
    email = StringField('email',
                        validators=[Optional(), Email()])
    address = StringField('address',
                          validators=[DataRequired('missing'),
                                      Length(min=2, max=20)])
    submit = SubmitField('Save')


class UpdateContact(FlaskForm):
    name = StringField('name',
                       validators=[DataRequired('missing'),
                                   Length(min=4, max=20)])
    number = StringField('number',
                         validators=[DataRequired('missing'),
                                     Length(min=10, max=10)])
    email = StringField('email',
                        validators=[DataRequired('missing'),
                                    Email()])
    address = StringField('address',
                          validators=[DataRequired('missing'),
                                      Length(min=2, max=20)])
    submit = SubmitField('update')
