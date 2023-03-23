from wtforms import Form, StringField, IntegerField, validators, EmailField


class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Email')