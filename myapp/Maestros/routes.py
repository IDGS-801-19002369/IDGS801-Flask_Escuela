from flask import Blueprint, render_template, request, redirect, url_for, flash
import forms
from models import Maestros
from db import get_connection

maestros = Blueprint('maestros', __name__)


@maestros.route('/getmaes', methods=['GET'])
def getmaes():
    return {'key': 'Maestros'}


@maestros.route('/agregarMaestro', methods=['GET','POST'])
def index():
    create_forms = forms.UserForm(request.form)
    if request.method == 'POST':
        try:
            maest = Maestros(nombre=create_forms.nombre.data,
                            apellidos=create_forms.apellidos.data,
                            email=create_forms.email.data)
            con = get_connection()
            with con.cursor() as cursor:
                cursor.execute('call maestroUPD(%s,%s,%s,%s)',(0,maest.nombre,maest.nombre,maest.email))             
            con.commit()
            con.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('index.html', form=create_forms, action = 'agregarMaestro')


@maestros.route('/ABCompletoMaestro', methods=['GET','POST'])
def ABCompleto():
    modulo = 'Maestros'
    maestro = {}
    try:
        con = get_connection()
        with con.cursor() as cursor:
            cursor.execute('call maestroLST(%s)',(None,))
            maestro = cursor.fetchall()
        con.close()
    except Exception as ex:
        print(ex)
    return render_template('ABCompleto.html', maestross = maestro, modulo = modulo)


@maestros.route('/modificarMaestro', methods=['GET','POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = ()
        try:
            con = get_connection()
            with con.cursor() as cursor:
                cursor.execute('call maestroLST(%s)',(id,))
                maestro = cursor.fetchone()
            con.close()
            create_form.id.data = maestro[0]
            create_form.nombre.data = maestro[1]
            create_form.apellidos.data = maestro[2]
            create_form.email.data = maestro[3]
        except Exception as ex:
            print(ex)
    if request.method == 'POST':
        id = create_form.id.data
        try:
            con = get_connection()
            with con.cursor() as cursor:
                cursor.execute('call maestroLST(%s)',(id,))
                maestro = cursor.fetchone()
            con.close()
            maest = Maestros(id = maestro[0],
                            nombre=create_form.nombre.data,
                            apellidos=create_form.apellidos.data,
                            email=create_form.email.data)
            con = get_connection()
            with con.cursor() as cursor:
                cursor.execute('call maestroUPD(%s,%s,%s,%s)',(maest.id,maest.nombre,maest.apellidos,maest.email))
            con.commit()
            con.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('modificar.html', form=create_form)


@maestros.route('/eliminarMaestro', methods=['GET','POST'])
def eliminar():
    id = request.args.get('id')
    try:
        con = get_connection()
        with con.cursor() as cursor:
            cursor.execute('call maestroDEL(%s)',(id,))
        con.commit()
        con.close()
    except Exception as ex:
        print(ex)
    return redirect(url_for('maestros.ABCompleto'))