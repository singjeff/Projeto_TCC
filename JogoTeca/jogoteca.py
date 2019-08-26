from flask import Flask, render_template, request, redirect, session, flash, url_for
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dao import JogoDao
from models import jogo, Usuario

app = Flask(__name__)
app.secret_key = 'alura'



conn=('Driver={SQL Server};'
    'Server=DESKTOP-6181A8Q\SQLEXPRESS;'
    'Database=JogoTeca;'
    'Trusted_Connection=yes;')

url_db = quote_plus(conn)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=%s' % url_db

db=SQLAlchemy(app)
jogo_dao = JogoDao(db)


usuario1 = Usuario('lira', 'Henrique Lira', 'he2010')
usuario2 = Usuario('nico', 'nico stepapt', '7a1')
usuario3 = Usuario('flavio', 'flavio', 'javascript')

usuarios= {usuario1.id: usuario1,
           usuario2.id: usuario2,
           usuario3.id: usuario3}

jogo1 = jogo('Super Mario', 'Ação', 'SNES')
jogo2 = jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login', proxima= url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome= request.form['nome']
    categoria= request.form['categoria']
    console= request.form['console']
    Jogo = jogo(nome, categoria,console)
    jogo_dao.salvar(Jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if  request.form['usuario'] in usuarios:
        usuario=usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
             session['usuario_logado']= usuario.id
             flash(usuario.nome + ' logou com sucesso !')
             proxima_pagina = request.form['proxima']
             return redirect(proxima_pagina)
        else:
            flash('Senha errada, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Usuario não existe!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('index'))







app.run(debug=True) 