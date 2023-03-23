from wtforms import Form, SelectField, validators
from models.ResistenciaModel import Resistencia

class ResistenciaForm(Form):
  banda1 = SelectField('banda1', choices=Resistencia.valores(), validators=[validators.DataRequired(message='Selecciona la banda 1.')])
  banda2 = SelectField('banda2', choices=Resistencia.valores(), validators=[validators.DataRequired(message='Selecciona la banda 2.')])
  banda3 = SelectField('banda3', choices=Resistencia.valores(), validators=[validators.DataRequired(message='Selecciona la banda 3.')])
  tolerancia = SelectField('tolerancia', choices=['0', '1'], validators=[validators.DataRequired(message='Selecciona la tolerancia.')])
