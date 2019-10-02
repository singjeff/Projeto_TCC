
class Usuario:
    def __init__(self, cod_usuario, id_tipopessoa,  nome_usuario,email_usuario,  dt_cadastro, dt_bloqueio, dt_ultimo_acesso,\
        motivo_bloqueio, qtde_senha_errada, dt_ultima_troca_senha, ind_bloqueado, senha_aplicacao):
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

class Fornecedor:
    def __init__(self, id_fornecedor, id_pessoa):
        self.id_fornecedor = id_fornecedor
        self.id_pessoa = id_pessoa