#################################### APLICAÇÃO FLASK ####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import pyodbc
from datetime import date
from metodos import metodo_login, metodo_criar_usuario, metodo_att_usuario, metodo_criar_fornecedor
from models import Usuario,Pessoa,Endereco_Pessoa,ContatoPessoa, Fornecedor

app = Flask(__name__)
app.secret_key = 'alura'

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0KG5KKS\SQLEXPRESS;'
                      'Database=Comercial_Control;'
                      'Trusted_Connection=yes;')    
db = parametro.cursor()
cadastrar_usu = metodo_criar_usuario.cadastrar_usuario(db)
atualiza_usuario = metodo_att_usuario.atualiza_usuario(db)
login_usu = metodo_login.UsuarioDao(db)
data_atual = date.today()

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
                if usuario.id_tipopessoa == '1':
                    flash('Funcionário(a)  ' + usuario.nome_usuario + ' logado!')
                    proxima_pagina = url_for('gerenciar_Usuarios')
                    return redirect(proxima_pagina)
                else:
                    flash('Administrador(a)  ' + usuario.nome_usuario + ' logado!')
                    proxima_pagina = url_for('gerenciar_Estoque')
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
    cod_usuario = request.form['login_usuario']
    senha_aplicacao = request.form['senha_usuario']
    id_tipopessoa = request.form['radio']
    nome_usuario = request.form['nome_usuario']
    email_usuario = request.form['login_usuario']
    dt_cadastro = data_atual.strftime('%d/%m/%y')
    dt_bloqueio = None
    motivo_bloqueio = None
    dt_ultimo_acesso = None
    qtde_senha_errada = None
    dt_ultima_troca_senha = None
    ind_bloqueado = None
    usuario = login_usu.buscar_por_id(request.form['login_usuario'])
    att_usuario = Usuario(cod_usuario,id_tipopessoa,nome_usuario,email_usuario,dt_cadastro,dt_bloqueio,motivo_bloqueio,\
        dt_ultimo_acesso,qtde_senha_errada,dt_ultima_troca_senha,ind_bloqueado, senha_aplicacao)
    
    id_pessoa = request.form['numero_endereco']
    id_tipo_pessoa = request.form['radio']
    nome = request.form['nome_usuario']
    inscricao = None
    data_cadastro = None
    ind_cliente = None
    ind_funcionario = None
    ind_fornecedor = None
    att_pessoa= Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro, ind_cliente, ind_funcionario,ind_fornecedor)
    
    id_pessoa = request.form['numero_endereco']
    cep = request.form['cep']
    cidade = request.form['cidade']
    uf = request.form['uf']
    endereco = request.form['endereco']
    complemento = request.form['numero_endereco']
    att_endereco = Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep)

    id_pessoa = request.form['numero_endereco']
    ddd = None
    celular = request.form['celular']
    telefone = request.form['telefone']
    email = request.form['login_usuario']
    nome_contato = request.form['nome_usuario']
    att_contato = ContatoPessoa(id_pessoa, ddd, celular, telefone, email, nome_contato)

    


    if usuario:
        if usuario.cod_usuario == cod_usuario:
            salvar_attusuario = atualiza_usuario.atualiza(att_usuario)
    else:
        salvar_cadastrausuario= cadastrar_usu.cadastra_usuario(att_usuario,att_pessoa,att_endereco,att_contato)



    return redirect(url_for('gerenciar_Usuarios'))



@app.route('/cadastrar_fornecedor',methods=['POST',])
def cadastrar_fornecedor():  
    inscricao = request.form['cnpj']
    ind_fornecedor = request.form['razaosocial']
    att_pessoa= Pessoa(inscricao,ind_fornecedor)
    
    id_pessoa = request.form['numero_endereco']
    cep = request.form['cep']
    cidade = request.form['cidade']
    uf = request.form['uf']
    endereco = request.form['endereco']
    complemento = request.form['numero_endereco']
    att_endereco = Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep)

    id_pessoa = request.form['numero_endereco']
    ddd = None
    celular = request.form['celular']
    telefone = request.form['telefone']
    email = request.form['login_usuario']
    nome_contato = request.form['nome_usuario']
    att_contato = ContatoPessoa(id_pessoa, ddd, celular, telefone, email, nome_contato)

    if fornecedor:
        if fornecedor.cod_fornecedor == cod_fornecedor:
            salvar_attfornecedor = atualiza_fornecedor.atualiza(att_fornecedor)
    else:
        salvar_cadastrafornecedor= cadastrar_for.cadastra_fornecedor(att_fornecedor,att_pessoa,att_endereco,att_contato)



    return redirect(url_for('gerenciar_fornecedor'))

#################################### ^^^^^^^^^^^^^^^^^^ ####################################


app.run(debug=True)


