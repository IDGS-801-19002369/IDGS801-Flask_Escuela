from flask import Flask, request, redirect, make_response, render_template as view, flash, url_for
from forms.ResistenciaForm import ResistenciaForm
from models.ResistenciaModel import Resistencia

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
  form = ResistenciaForm(request.form)
  if request.method == 'POST' and form.validate():
    banda1 = form.banda1.data
    banda2 = form.banda2.data
    banda3 = form.banda3.data
    tolerancia = form.tolerancia.data
    color_banda1 = Resistencia.colores()[int(banda1)]
    color_banda2 = Resistencia.colores()[int(banda2)]
    color_banda3 = Resistencia.colores()[int(banda3)]
    color_tolerancia = Resistencia.colorTolerancias()[int(tolerancia)]
    clase_banda1 = Resistencia.clases()[int(banda1)]
    clase_banda2 = Resistencia.clases()[int(banda2)]
    clase_banda3 = Resistencia.clases()[int(banda3)]
    clase_tolerancia = Resistencia.clasesTolerancia()[int(tolerancia)]
    banda1 = '' if banda1 == '0' else banda1
    banda3 = Resistencia.multiplicadores()[int(banda3)]
    resultado = f'{banda1}{banda2}{banda3}'
    tolerancia = Resistencia.tolerancias[int(tolerancia)].get('valor')
    maximo = float(resultado) * float(tolerancia)
    minimo = round(float(resultado) / float(tolerancia), 2)
    # print(f'resultado: {resultado}, maximo: {maximo}, minimo: {minimo}')
    resp = make_response(redirect(url_for('root')))
    resp.set_cookie('color_banda1', color_banda1)
    resp.set_cookie('color_banda2', color_banda2)
    resp.set_cookie('color_banda3', color_banda3)
    resp.set_cookie('color_tolerancia', color_tolerancia)
    resp.set_cookie('clase_banda1', clase_banda1)
    resp.set_cookie('clase_banda2', clase_banda2)
    resp.set_cookie('clase_banda3', clase_banda3)
    resp.set_cookie('clase_tolerancia', clase_tolerancia)
    resp.set_cookie('resultado', resultado)
    resp.set_cookie('minimo', str(minimo))
    resp.set_cookie('maximo', str(maximo))
    return resp
  return view('resistencias.j2',
              form=form,
              colores = Resistencia.colores(),
              valores = Resistencia.valores(),
              tolerancias = Resistencia.colorTolerancias()
              )

app.run(debug=True)