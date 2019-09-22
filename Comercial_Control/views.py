#################################### APLICAÇÃO FLASK ####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import pyodbc
from metodos import cadas_att, UsuarioDao
from models import Usuario

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


@app.route('/gerenciar_Usuarios')
def gerenciar_Usuarios():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Usuarios')))
    return render_template('DashBoard/area_adminstrador/gerenciar_Usuarios.html')



@app.route('/gerenciar_Fornecedores')
def gerenciar_Fornecedores():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Fornededores')))
    return render_template('DashBoard/area_adminstrador/gerenciar_Fornecedores.html')







#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO E CRUD ####################################


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usu.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha_aplicacao == request.form['senha']:
            session['usuario_logado'] = usuario.cod_usuario
            flash('Funcionário(a)  ' + usuario.nome_usuario + ' logado!')
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
    flash('Deslogado com sucesso!')
    return redirect(url_for('login'))


@app.route('/cadastrar_usuario',methods=['POST',])
def cadastrar_usuario():
    cod_usuario = request.form['nome']
    senha_aplicacao = request.form['senha']
    nome_usuario='teste'
    email_usuario = 'teste@gmail.com'
    dt_cadastro = None
    dt_bloqueio = None
    motivo_bloqueio = None
    dt_ultimo_acesso = None
    qtde_senha_errada = None
    tipo_usuario = request.form['radio']
    dt_ultima_troca_senha= None
    dt_ultimo_acesso = None
    ind_bloqueado = None
    usuario = login_usu.buscar_por_id(request.form['nome'])
    att_usuario = Usuario(cod_usuario,nome_usuario,email_usuario,dt_cadastro,dt_bloqueio,motivo_bloqueio,\
        dt_ultimo_acesso,qtde_senha_errada,dt_ultima_troca_senha,ind_bloqueado,tipo_usuario,senha_aplicacao)
    if usuario:
        if usuario.cod_usuario == cod_usuario:
            salvar_attusuario = input_att.atualiza(att_usuario)
    else:
        salvar_cadastrausuario= input_att.cadastrausuario(att_usuario)
    return redirect(url_for('gerenciar_Usuarios'))

#################################### ^^^^^^^^^^^^^^^^^^ ####################################


app.run(debug=True)


