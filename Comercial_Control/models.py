
class login:
    def __init__(self,id_usuario,nome_usuario,senha):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.senha = senha
        

class Usuario:
    def __init__(self, cod_usuario, email_usuario, nome_usuario, dt_cadastro,usuario_bloqueado, dt_bloqueio, dt_ultimo_acesso,motivo_bloqueio, qtde_senha_errada, dt_ultima_troca_senha, ind_bloqueado, senha_aplicacao):
        self.cod_usuario = cod_usuario
        self.email_usuario = email_usuario
        self.nome_usuario = nome_usuario
        self.dt_cadastro = dt_cadastro
        self.usuario_bloqueado = usuario_bloqueado
        self.dt_bloqueio = dt_bloqueio
        self.dt_ultimo_acesso = dt_ultimo_acesso
        self.motivo_bloqueio = motivo_bloqueio
        self.qtde_senha_errada = qtde_senha_errada
        self.dt_ultima_troca_senha = dt_ultima_troca_senha
        self.ind_bloqueado = ind_bloqueado
        self.senha_aplicacao = senha_aplicacao