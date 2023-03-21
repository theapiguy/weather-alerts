from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, validators


class WeatherSearchForm(FlaskForm):
    """
    Build the form that will request user input
    """
    state_field = SelectField('State:', choices=[('AL', 'Alabama'),
                                                 ('AK', 'Alaska'), ('AZ', 'Arizona'),
                                                 ('AR', 'Arkansas'), ('AS', 'American Samoa'),
                                                 ('CA', 'California'), ('CO', 'Colorado'),
                                                 ('CT', 'Connecticut'), ('DE', 'Delaware'),
                                                 ('DC', 'District of Columbia'), ('FL', 'Florida'),
                                                 ('GA', 'Georgia'), ('GU', 'Guam'),
                                                 ('HI', 'Hawaii'), ('ID', 'Idaho'),
                                                 ('IL', 'Illinois'), ('IN', 'Indiana'),
                                                 ('IA', 'Iowa'), ('KS', 'Kansas'),
                                                 ('KY', 'Kentucky'), ('LA', 'Louisiana'),
                                                 ('ME', 'Maine'), ('MD', 'Maryland'),
                                                 ('MA', 'Massachusetts'), ('MI', 'Michigan'),
                                                 ('MN', 'Minnesota'), ('MS', 'Mississippi'),
                                                 ('MO', 'Missouri'), ('MT', 'Montana'),
                                                 ('NE', 'Nebraska'), ('NV', 'Nevada'),
                                                 ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
                                                 ('NM', 'New Mexico'), ('NY', 'New York'),
                                                 ('NC', 'North Carolina'), ('ND', 'North Dakota'),
                                                 ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'),
                                                 ('OK', 'Oklahoma'), ('OR', 'Oregon'),
                                                 ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'),
                                                 ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
                                                 ('SD', 'South Dakota'), ('TN', 'Tennessee'),
                                                 ('TX', 'Texas'), ('TT', 'Trust Territories'),
                                                 ('UT', 'Utah'), ('VT', 'Vermont'),
                                                 ('VA', 'Virginia'), ('VI', 'Virgin Islands'),
                                                 ('WA', 'Washington'), ('WV', 'West Virginia'),
                                                 ('WI', 'Wisconsin'), ('WY', 'Wyoming')
                                                 ])
    urgency_field = SelectField('Urgency:',
                                choices=[('Immediate', 'Immediate'), ('Expected', 'Expected'), ('Future', 'Future'),
                                         ('Unknown', 'Unknown')])
    severity_field = SelectField('Severity:',
                                 choices=[('Extreme', 'Extreme'), ('Severe', 'Severe'), ('Moderate', 'Moderate'),
                                          ('Minor', 'Minor'), ('Unknown', 'Unknown')])

    certainty_field = SelectField('Certainty:',
                                  choices=[('Observed', 'Observed'), ('Likely', 'Likely'), ('Possible', 'Possible'),
                                           ('Unlikely', 'Unlikely'), ('Unknown', 'Unknown')])

    max_results_field = IntegerField('Max Results:',
                                     validators=[validators.NumberRange(min=1,
                                                                        message='Please enter an integer greater than 1.')])
    submit = SubmitField('Submit')
