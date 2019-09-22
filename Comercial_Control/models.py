'''
#Classe de Teste para login 

class login:
    def __init__(self,id_usuario,nome_usuario,senha):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.senha = senha
'''      

class Usuario:
    def __init__(self, cod_usuario, nome_usuario,email_usuario,  dt_cadastro, dt_bloqueio, dt_ultimo_acesso,motivo_bloqueio, qtde_senha_errada, dt_ultima_troca_senha, ind_bloqueado,tipo_usuario, senha_aplicacao):
        self.cod_usuario = cod_usuario
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.dt_cadastro = dt_cadastro
        self.dt_bloqueio = dt_bloqueio
        self.dt_ultimo_acesso = dt_ultimo_acesso
        self.motivo_bloqueio = motivo_bloqueio
        self.qtde_senha_errada = qtde_senha_errada
        self.dt_ultima_troca_senha = dt_ultima_troca_senha
        self.ind_bloqueado = ind_bloqueado
        self.tipo_usuario = tipo_usuario
        self.senha_aplicacao = senha_aplicacao