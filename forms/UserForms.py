from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
from wtforms.fields import EmailField, TextAreaField
from wtforms import validators

class UserForm(Form):
  matricula=StringField('matricula', [validators.DataRequired(message='La matricula es obligatoria.')])
  nombre=StringField('nombre', [validators.DataRequired(message='El nombre es obligatorio.')])
  apaterno=StringField('apaterno', [validators.DataRequired(message='El apaterno es obligatorio.')])
  email=EmailField('correo', [validators.DataRequired(message='El correo es obligatorio.'), validators.Email(message='El correo es inválido.')])