from models import  Usuario, Pessoa, Endereco_Pessoa, ContatoPessoa, Funcionario

SQL_ATUALIZA_USUARIO = 'UPDATE Usuario SET  id_tipopessoa=?, nome_usuario=?, email_usuario=?, senha_aplicacao=?  where email_usuario= ?'
SQL_ATUALIZA_PESSOA ='UPDATE Pessoa SET id_tipo_pessoa=?, nome=? where id_pessoa = ? '
SQL_ATUALIZA_ENDERECO = 'UPDATE Endereco_Pessoa SET endereco=?, complemento=?, cidade=?, uf=?, cep=? where id_pessoa = ? '
SQL_ATUALIZA_CONTATO = 'UPDATE Contato_Pessoa SET celular=?, telefone=?, email=?, nome_contato=? where id_pessoa = ? '
SQL_ATUALIZA_CARGO = 'UPDATE Funcionario SET cargo=? where id_pessoa = ? '

SQL_PROCEDURE_UPDATE_USUARIO = "{CALL sp_update_usuario (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}"

class atualiza_usuario:
    def __init__(self, db):
        self.__db = db

    def att_usuario(self, Usuario, Pessoa, Endereco_Pessoa, ContatoPessoa, Funcionario):
        cursor = self.__db

        values = (
            Usuario.nome_usuario, Pessoa.nome, Endereco_Pessoa.cep, Endereco_Pessoa.cidade,  
            Endereco_Pessoa.uf, Endereco_Pessoa.endereco, Endereco_Pessoa.num_endereco, ContatoPessoa.telefone,
            ContatoPessoa.celular,  Funcionario.cargo, Usuario.senha_aplicacao, Usuario.id_tipopessoa, Usuario.email_usuario,
          
        )

        cursor.execute(SQL_PROCEDURE_UPDATE_USUARIO, values)

        '''
        cursor.execute(SQL_ATUALIZA_USUARIO, (Usuario.id_tipopessoa, Usuario.nome_usuario, Usuario.email_usuario, Usuario.senha_aplicacao, Usuario.email_usuario))
        cursor.execute(SQL_ATUALIZA_PESSOA, (Pessoa.id_tipo_pessoa, Pessoa.nome, Pessoa.id_pessoa))
        cursor.execute(SQL_ATUALIZA_ENDERECO, (Endereco_Pessoa.endereco, Endereco_Pessoa.complemento, Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.cep, Endereco_Pessoa.id_pessoa))
        cursor.execute(SQL_ATUALIZA_CONTATO, (ContatoPessoa.celular, ContatoPessoa.telefone, ContatoPessoa.email, ContatoPessoa.nome_contato, ContatoPessoa.id_pessoa))
        cursor.execute(SQL_ATUALIZA_CARGO, (Funcionario.cargo, Funcionario.id_pessoa))
        '''


        self.__db.connection.commit()
        return Usuario

