#################################### APLICAÇÃO FLASK ####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
import pyodbc
from datetime import date
from metodos import metodo_login, metodo_criar_usuario, metodo_att_usuario, metodo_buscar_usuario,\
     metodo_deleta_usuario, metodo_criar_fornecedor, metodo_cadastrar_categoria, metodo_cadastrar_marca, metodo_cadastrar_produto
from models import Usuario,Pessoa,Endereco_Pessoa,ContatoPessoa, exibe_usuario, Fornecedor,\
     Funcionario, Categoria_Produto, Marca_Produto, Produto

app = Flask(__name__)
app.secret_key = 'alura'

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                      'Server=LIRA-PC\SQLEXPRESS;'
                      'Database=Comercial_Control;'
                      'Trusted_Connection=yes;')
    
db = parametro.cursor()
cadastrar_usu = metodo_criar_usuario.cadastrar_usuario(db)
atualiza_usuario = metodo_att_usuario.atualiza_usuario(db)
buscar_id_usuario = metodo_buscar_usuario.busca_usuario(db)
excluir = metodo_deleta_usuario.deletar(db)
cria_fornecedor = metodo_criar_fornecedor.cadastrar_fornecedor(db)
login_usu = metodo_login.UsuarioDao(db)
cadastrar_cate = metodo_cadastrar_categoria.cadastrar_categoria(db)
data_atual = date.today()
cadastrar_marca= metodo_cadastrar_marca.cadastrar_categoria(db)
cadastrar_produto = metodo_cadastrar_produto.cadastrar_produto(db)

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS ADMINISTRADOR       ####################################


@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/gerenciar_Estoque')
def gerenciar_Estoque():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Estoque')))
    listaCategoria = cadastrar_cate.exibe_categoria()
    listaMarca = cadastrar_marca.exibe_marca()
    return render_template('DashBoard/area_adminstrador/gerenciar_Estoque.html',lista_categoria= listaCategoria, lista_marca= listaMarca)


@app.route('/gerenciar_Usuarios')
def gerenciar_Usuarios():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Usuarios')))
    lista = buscar_id_usuario.listar()
    return render_template('DashBoard/area_adminstrador/gerenciar_Usuarios.html',lista_usuario=lista)



@app.route('/gerenciar_Fornecedores')
def gerenciar_Fornecedores():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('gerenciar_Fornededores')))
    lista = cria_fornecedor.exibe_fornecedor()
    return render_template('DashBoard/area_adminstrador/gerenciar_Fornecedores.html',lista_fornecedor= lista)


@app.route('/relatorios')
def relatorios():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('relatorios')))
    return render_template('DashBoard/area_adminstrador/relatorios.html')

@app.route('/contato')
def contato():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('contato')))
    return render_template('DashBoard/area_adminstrador/contato.html')

####################################        VIEWS USUARIO       ####################################

@app.route('/caixa')
def caixa():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('caixa')))
    return render_template('DashBoard/area_usuario/caixa.html')



#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO E CRUD ####################################


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usu.buscar_por_id(request.form['usuario'])
    password = request.form['senha']
    password_app = hashlib.md5(password.encode())
    senha_aplicacao = password_app.hexdigest()
    if usuario:
        if usuario.senha_aplicacao == senha_aplicacao:
                session['usuario_logado'] = usuario.email_usuario
                if usuario.id_tipopessoa == '1':
                    flash('Usuario(a)  ' + usuario.nome_usuario + ' logado!')
                    proxima_pagina = url_for('caixa')
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
    password = request.form['senha_usuario']
    
    password_app = hashlib.md5(password.encode())
    senha_aplicacao = password_app.hexdigest()
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
    att_usuario = Usuario(id_tipopessoa, nome_usuario,email_usuario,dt_cadastro,dt_bloqueio,motivo_bloqueio,\
    dt_ultimo_acesso,qtde_senha_errada,dt_ultima_troca_senha,ind_bloqueado, senha_aplicacao)
    
    id_pessoa = cria_fornecedor.id_fornecedor() + 1
    id_tipo_pessoa = request.form['radio']
    nome = request.form['nome_usuario']
    inscricao = None
    data_cadastro = data_atual.strftime('%d/%m/%y')
    ind_cliente = None
    ind_funcionario = None
    ind_fornecedor = None
    att_pessoa= Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro, ind_cliente, ind_funcionario,ind_fornecedor)
    
   
    cep = request.form['cep']
    cidade = request.form['cidade']
    uf = request.form['uf']
    endereco = request.form['endereco']
    
    complemento = request.form['numero_endereco']
    att_endereco = Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep)

   
    ddd = None
    celular = request.form['celular']
    telefone = request.form['telefone']
    email = request.form['login_usuario']
    nome_contato = request.form['nome_usuario']
    att_contato = ContatoPessoa(id_pessoa, ddd, celular, telefone, email, nome_contato)

    
    cargo = request.form['cargo']
    att_funcionario = Funcionario(id_pessoa, cargo)

    salvar_cadastrausuario= cadastrar_usu.cadastra_usuario(att_usuario,att_pessoa,att_endereco,att_contato,att_funcionario)
    flash('Usuario cadastrado com sucesso!')
    return redirect(url_for('gerenciar_Usuarios'))


@app.route('/cadastrar_fornecedor',methods=['POST',])
def cadastrar_fornecedor():

    id_pessoa = cria_fornecedor.id_fornecedor() + 1
    #id_pessoa = table_pessoa + 1
    id_tipo_pessoa = '3'
    nome = request.form['razaosocial']
    inscricao = request.form['cnpj']
    data_cadastro = data_atual.strftime('%d/%m/%y')
    ind_fornecedor = None
    ind_cliente = None
    ind_funcionario = None
    att_pessoa= Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro, ind_cliente, ind_funcionario,ind_fornecedor )
    

  
    
    cep = request.form['cep']
    cidade = request.form['cidade']
    uf = request.form['UF']
    endereco = request.form['endereco']
    complemento = request.form['numero_endereco']
    att_endereco = Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep)

    
    ddd = None
    celular = request.form['celular']
    telefone = request.form['telefone']
    email = request.form['email']
    dt_cadastro = data_atual.strftime('%d/%m/%y')
    nome_contato = request.form['nome_contato']
    att_contato = ContatoPessoa(id_pessoa, ddd, celular, telefone, email, nome_contato)
    salvar_fornecedor = cria_fornecedor.cadastra_fornecedor(att_pessoa, att_endereco, att_contato)


    flash('Fornecedor cadastrado com sucesso!')
    return redirect(url_for('gerenciar_Fornecedores'))


@app.route('/cadastrar_Categoria', methods=['POST' ,])
def cadastrar_Categoria():
   
    id_categoria = request.form['idCategoria']
    descricao = request.form['descricaoCategoria']
    att_categoria = Categoria_Produto(id_categoria, descricao)
    Cadastrar_Categoria_Produto = cadastrar_cate.salvar_categoria(att_categoria)
    flash('Categoria cadastrado com sucesso!')
    return redirect(url_for('gerenciar_Estoque'))
  

@app.route('/cadastrar_Marca', methods=['POST' ,])
def cadastrar_Marca():
   
    id_marca = request.form['id_marca']
    descricao = request.form['descricaomarca']
    att_marca = Marca_Produto(id_marca,descricao)
    cadastrar_marca_produto = cadastrar_marca.salvar_marca(att_marca)
    flash('Marca cadastrada com sucesso!')
    return redirect(url_for('gerenciar_Estoque'))


@app.route('/cadastrar_Produto', methods = ['POST', ])
def cadastrar_Produto():
    print('a',request.form['categoriaProduto'])
    codigo_produto = request.form['codigoProduto']
    #id_categoria = cadastrar_produto.id_categoria(request.form['categoriaProduto'])
    #descricao = request.form['nomeProduto']
    #id_marca =  cadastrar_produto.id_marca(request.args.get('marca'))
    #valor_venda = request.form['valorProduto']
    #att_produto = Produto(codigo_produto, id_categoria, descricao, id_marca, valor_venda)
        


    #cadastrar = cadastrar_produto.salvar_produto(att_produto)
    flash('Produto cadastrado com sucesso!')
    return redirect(url_for('gerenciar_Estoque'))





@app.route('/excluir_usuario/<string:id>')
def excluir_usuario(id):
    excluir.deletar_usuario(id)
    flash('Usuario removido com sucesso!')
    return redirect(url_for('gerenciar_Usuarios'))

@app.route('/excluir_fornecedor/<string:id>')
def excluir_fornecedor(id):
    excluir.deletar_fornecedor(id)
    flash('Fornecedor removido com sucesso!')
    return redirect(url_for('gerenciar_Fornecedores'))
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


app.run(debug=True)


