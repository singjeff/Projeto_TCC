from models import  Fornecedor, Pessoa, Endereco_Pessoa, ContatoPessoa

SQL_CADASTRAR_FORNECEDOR = 'insert into Fornecedor(id_fornecedor, id_pessoa) values (?, ?)'
SQL_CADASTRAR_PESSOA = 'insert into Pessoa(id_pessoa, id_tipo_pessoa, nome) values (?, ?, ?)'
SQL_CADASTRAR_ENDERECO = 'insert into Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf ,cep) values (?, ?, ?, ?, ?, ?)'
SQL_CADASTRAR_CONTATO = 'insert into Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato) values (?, ?, ?, ?, ?)'


class cadastrar_fornecedor:
    def __init__(self, db):
        self.__db = db
    

    def cadastra_fornecedor(self, fornecedor,Pessoa,Endereco_Pessoa,ContatoPessoa):
        cursor= self.__db

        cursor.execute(SQL_CADASTRAR_PESSOA, (Pessoa.id_pessoa, Pessoa.id_tipo_pessoa, Pessoa.nome))
        cursor.execute(SQL_CADASTRAR_FORNECEDOR, (fornecedor.cod_fornecedor, fornecedor.id_tipopessoa, fornecedor.email_fornecedor, fornecedor.dt_cadastro))
        cursor.execute(SQL_CADASTRAR_ENDERECO, (Endereco_Pessoa.id_pessoa, Endereco_Pessoa.endereco, Endereco_Pessoa.complemento, Endereco_Pessoa.cidade, Endereco_Pessoa.uf, Endereco_Pessoa.cep))
        cursor.execute(SQL_CADASTRAR_CONTATO, (ContatoPessoa.id_pessoa, ContatoPessoa.celular, ContatoPessoa.telefone, ContatoPessoa.email, ContatoPessoa.nome_contato))
        fornecedor.cod_fornecedor = cursor.execute('SELECT @@IDENTITY AS cod_fornecedor;')
        
        self.__db.connection.commit()
        return fornecedor