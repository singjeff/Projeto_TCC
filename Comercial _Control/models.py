
class Usuario:
    def __init__(self, id_tipopessoa,  nome_usuario,email_usuario,  dt_cadastro, dt_bloqueio, dt_ultimo_acesso,\
        motivo_bloqueio, qtde_senha_errada, dt_ultima_troca_senha, ind_bloqueado, senha_aplicacao, cod_usuario=None):
        self.cod_usuario = cod_usuario
        self.id_tipopessoa = id_tipopessoa
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.dt_cadastro = dt_cadastro
        self.dt_bloqueio = dt_bloqueio
        self.dt_ultimo_acesso = dt_ultimo_acesso
        self.motivo_bloqueio = motivo_bloqueio
        self.qtde_senha_errada = qtde_senha_errada
        self.dt_ultima_troca_senha = dt_ultima_troca_senha
        self.ind_bloqueado = ind_bloqueado
        self.senha_aplicacao = senha_aplicacao

class Pessoa:
    def __init__(self, id_pessoa, id_tipo_pessoa, nome, inscricao, data_cadastro,\
         ind_cliente, ind_funcionario, ind_fornecedor):
         self.id_pessoa = id_pessoa
         self.id_tipo_pessoa = id_tipo_pessoa
         self.nome = nome
         self.inscricao = inscricao
         self.data_cadastro = data_cadastro
         self.ind_cliente = ind_cliente
         self.ind_funcionario = ind_funcionario
         self.ind_fornecedor = ind_fornecedor

class Endereco_Pessoa:
    def __init__(self, id_pessoa, endereco, complemento, cidade, uf, cep, id_endereco_pessoa=None):
        self.id_endereco_pessoa = id_endereco_pessoa
        self.id_pessoa = id_pessoa
        self.endereco = endereco
        self.complemento = complemento
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

class ContatoPessoa:
    def __init__(self, id_pessoa, ddd, celular, telefone, email, nome_contato, id_contato_pessoa=None):
        self.id_contato_pessoa = id_contato_pessoa
        self.id_pessoa = id_pessoa
        self.ddd = ddd
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.nome_contato = nome_contato

class Funcionario:
    def __init__(self, id_pessoa, cargo, id_funcionario=None):
        self.id_funcionario = id_funcionario
        self.id_pessoa = id_pessoa
        self.cargo = cargo


class exibe_usuario:
    def __init__(self, id_tipopessoa, email_usuario, nome_usuario,  dt_cadastro, cod_usuario=None):
        self.cod_usuario = cod_usuario
        self.email_usuario = email_usuario
        self.nome_usuario = nome_usuario
        self.id_tipopessoa = id_tipopessoa
        self.dt_cadastro = dt_cadastro

class exibe_fornecedor:
    def __init__(self,nome, inscricao, endereco, celular, id_pessoa=None):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.inscricao = inscricao
        self.endereco = endereco
        self.celular = celular

class Fornecedor:
    def __init__(self, id_pessoa, id_fornecedor=None):
        self.id_fornecedor = id_fornecedor
        self.id_pessoa = id_pessoa


class Categoria_Produto:
    def __init__(self, id_categoria, descricao):
        self.id_categoria = id_categoria
        self.descricao = descricao


class Marca_Produto:
    def __init__(self, id_marca, descricao):
        self.id_marca = id_marca
        self.descricao = descricao


class Item:
    def __init__(self, id_item , codigo_produto, quantidade):
        self.id_item = id_item
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade



class Produto:
    def __init__(self, codigo_produto, id_categoria, descricao, id_marca, valor_venda):
        self.codigo_produto = codigo_produto
        self.id_categoria = id_categoria
        self.descricao = descricao
        self.id_marca = id_marca
        self.valor_venda = valor_venda

class Compra:
    def __init__(self, id_item, codigo_produto, id_fornecedor, id_funcionario, data_compra, num_notafiscal, id_compra = None):
        self.id_compra = id_compra
        self.id_item = id_item
        self.codigo_produto = codigo_produto
        self.id_fornecedor = id_fornecedor
        self.id_funcionario = id_funcionario
        self.data_compra = data_compra
        self.num_notafiscal = num_notafiscal



class Exibe_Produto:
    def __init__(self, codigo, produto, marca, categoria, valor_produto, quantidade,   data_cadastro ):
        self.codigo = codigo
        self.produto = produto
        self.marca = marca
        self.categoria = categoria
        self.valor_produto = valor_produto
        self.quantidade = quantidade     
        self.data_cadastro = data_cadastro