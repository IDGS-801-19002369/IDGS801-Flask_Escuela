from flask import Blueprint, render_template, request, redirect, url_for, flash
import forms
from models import Alumnos, db

alumnos = Blueprint('alumnos', __name__)


@alumnos.route('/getalum', methods=['GET'])
def getalum():
    return {'key': 'Alumnos'}


@alumnos.route("/agregar", methods=['GET', 'POST'])
def index():
    create_forms = forms.UserForm(request.form)
    if request.method == 'POST':
        alumn = Alumnos(nombre=create_forms.nombre.data,
                        apellidos=create_forms.apellidos.data,
                        email=create_forms.email.data)
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html', form=create_forms, action = 'agregar')


@alumnos.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    #create_forms = forms.UserForm(request.form)
    modulo = 'Alumnos'
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', alumnos=alumnos, modulo = modulo)


@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        # select * from alumnos where id = id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))

    return render_template('modificar.html', form=create_form)


@alumnos.route("/eliminar", methods=['GET'])
def eliminar():
    id = request.args.get('id')
    # delete from alumnos where id = id
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    db.session.delete(alum1)
    db.session.commit()
    flash("Se ha eliminado el registro con id: {}".format(alum1.id))
    return redirect(url_for('alumnos.ABCompleto'))
