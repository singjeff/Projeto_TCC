#################################### APLICAÇÃO FLASK ####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import pyodbc
from metodos import cadas_att, UsuarioDao
from models import Usuario,login

app = Flask(__name__)
app.secret_key = 'alura'

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-6181A8Q\SQLEXPRESS;'
                      'Database=Comercial_Controll;'
                      'Trusted_Connection=yes;')
    
db = parametro.cursor()
input_att = cadas_att(db)
login_usu = UsuarioDao(db)


#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS       ####################################


@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/gerenciar_Estoque')
def gerenciar_Estoque():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Estoque')))
    return render_template('DashBoard/area_adminstrador/gerenciar_Estoque.html')












#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO E CRUD ####################################

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usu.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id_usuario
            flash(usuario.nome_usuario + ' está logado!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Senha invalida, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Usuario não encontrado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('login'))

#################################### ^^^^^^^^^^^^^^^^^^ ####################################


app.run(debug=True)
