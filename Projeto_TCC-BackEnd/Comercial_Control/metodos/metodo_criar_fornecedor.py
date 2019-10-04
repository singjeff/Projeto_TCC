from models import  Fornecedor, Pessoa, Endereco_Pessoa, ContatoPessoa

SQL_CADASTRAR_FORNECEDOR = 'insert into Fornecedor(id_fornecedor, id_pessoa) values (?, ?)'
SQL_CADASTRAR_PESSOA = 'insert into Pessoa(id_pessoa, id_tipo_pessoa, nome, incricao, data_cadastro, ind_funcionario, ind_fornecedor) values (?, ?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_ENDERECO = 'insert into Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf ,cep) values (?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_CONTATO = 'insert into Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) values (?, ?, ?, ?, ?)'


class cadastrar_fornecedor:
    def __init__(self, db):
        self.__db = db
    

    def cadastra_fornecedor(self, Pessoa,Endereco_Pessoa,ContatoPessoa):
        cursor= self.__db

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.id_tipo_pessoa, Pessoa.nome, Pessoa.incricao, Pessoa.data_cadastro, Pessoa.ind_funcionario, Pessoa.ind_fornecedor))
        cursor.execute(SQL_CADASTRAR_ENDERECO, (Endereco_Pessoa.id_pessoa, Endereco_Pessoa.endereco, Endereco_Pessoa.complemento, Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.cep))
        cursor.execute(SQL_CADASTRAR_CONTATO, (ContatoPessoa.id_pessoa, ContatoPessoa.celular, ContatoPessoa.telefone, ContatoPessoa.email, ContatoPessoa.nome_contato))
        
        self.__db.connection.commit()