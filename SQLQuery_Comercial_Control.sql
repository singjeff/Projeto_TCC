
Create table Tipo_Pessoa(
        id_tipo_pessoa CHAR(1),
        descricao VARCHAR(16),
        constraint pkTipoPessoa primary key (id_tipo_pessoa)
    )


Create Table Usuario(
        cod_usuario VARCHAR(30) ,
		id_tipopessoa CHAR(1),
        nome_usuario VARCHAR(40) ,
		email_usuario VARCHAR(40),
        dt_cadastro DATETIME ,
        dt_bloqueio DATETIME ,
        dt_ultimo_acesso DATETIME ,
        motivo_bloqueio VARCHAR(100),
        qtde_senha_errada smallint,
        dt_ultima_troca DATETIME,
        ind_bloqueado VARCHAR(1),
        senha_aplicacao VARCHAR(500),
        constraint pkcod_usuario primary key (cod_usuario),
		constraint fkidtipo foreign key (id_tipopessoa) references Tipo_Pessoa(id_tipo_pessoa)
    )



Create Table Pessoa(
        id_pessoa smallint,
        id_tipo_pessoa CHAR(1),
        nome VARCHAR(130),
        incricao  smallint,
        data_cadastro date,
        ind_cliente VARCHAR (1),
        ind_funcionario VARCHAR(1),
        ind_fornecedor VARCHAR(1),
        constraint pkid_pessoa primary key (id_pessoa),
        constraint fkidtipopessoa foreign key (id_tipo_pessoa) references Tipo_Pessoa(id_tipo_pessoa)
    )

Create table Funcionario(
        id_funcionario smallint identity (1,1),
        id_pessoa smallint ,
        cargo VARCHAR(20),
        constraint pkpessoa primary key (id_funcionario),
        constraint fkid_pessoa foreign key (id_pessoa) references Pessoa(id_pessoa)
    )

Create table Fornecedor(
        id_fornecedor smallint identity (1,1) not null ,
        id_pessoa smallint ,
        constraint pkfornecedor primary key (id_fornecedor),
        constraint fkidpessoa foreign key (id_pessoa) references Pessoa(id_pessoa)
    )

Create table Endereco_Pessoa(
        id_endereco_pessoa smallint identity (1,1) not null ,
        id_pessoa smallint ,
        endereco VARCHAR(90),
        complemento VARCHAR(65),
        cidade VARCHAR(60),
        uf VARCHAR(2),
        cep bigint,

        constraint pkendereco primary key (id_endereco_pessoa),
        constraint fkpessoa foreign key (id_pessoa) references Pessoa(id_pessoa)
    )

Create table Contato_Pessoa(
        id_contato_pessoa smallint identity (1,1) not null ,
        id_pessoa smallint ,
        ddd smallint,
        celular bigint,
        telefone bigint,
        email VARCHAR(200),
        nome_contato VARCHAR(50),
        constraint pkid_contato primary key (id_contato_pessoa),
        constraint fkid_pess foreign key (id_pessoa) references Pessoa(id_pessoa)
    )

Create table Cliente(
        id_cliente smallint identity (1,1) not null,
        id_pessoa smallint ,
        data_nascimento date,
        constraint pkid_cliente primary key (id_cliente),
        constraint fk_pessoa foreign key (id_pessoa) references Pessoa(id_pessoa)
    )

Create table Categoria_Produto(
        id_categoria smallint,
        descricao VARCHAR(20),
        constraint pkid_categoria primary key (id_categoria)
    )

Create table Produto(
        codigo_produto smallint,
        id_categoria smallint,
        descricao VARCHAR(100),
        valor_venda float,
        constraint pkcodigo_produto primary key (codigo_produto),
        constraint fkid_categoria foreign key (id_categoria) references Categoria_Produto(id_categoria)
    )


Create table Item(
        id_item smallint,
        codigo_produto smallint,
        quantidade int,
        constraint pkid_item primary key (id_item),
        constraint fkcodigo_produto foreign key (codigo_produto) references Produto(codigo_produto)
    )


Create table Compra(
        id_compra smallint,
        id_item smallint,
        id_fornecedor smallint,
        id_funcionario smallint,
        data_compra date,
        num_notafiscal smallint,
        constraint pkid_compra primary key (id_compra),
        constraint fkid_item foreign key(id_item) references Item(id_item),
        constraint fkid_fornecedor foreign key(id_fornecedor) references Fornecedor(id_fornecedor),
        constraint fkid_funcionario foreign key(id_funcionario) references Funcionario(id_funcionario)

    )


Create table Estoque(
        id_lote smallint,
        id_item smallint,
        qtde_max int,
        qtde_min int,
        valor_compra float,
        constraint pkid_lote primary key(id_lote),
        constraint fk_item foreign key (id_item) references Item(id_item)
		)


Create table Venda(
        id_venda smallint,
        id_item smallint,
        id_funcionario smallint,
        id_cliente smallint,
        percentual_desconto float,
        valor_desconto float,
        total_venda float,
        data_venda date,
        constraint pkidvenda primary key (id_venda),
        constraint fkiditem foreign key (id_item) references Item(id_item),
        constraint fkidfuncionario foreign key (id_funcionario) references Funcionario(id_funcionario),
        constraint fkidcliente foreign key (id_cliente) references Cliente(id_cliente)
    )


Create table Situacao_pagamento(
        id_situacao_pagamento smallint,
        decricao VARCHAR(30),
        constraint pkid_situacao_pagamento primary key (id_situacao_pagamento)
    )


 Create table Forma_pagamento(
        id_forma_pagamento smallint,
        decricao VARCHAR(30),
        constraint pkid_forma_pagamento primary key (id_forma_pagamento)
    )


Create table Pagamento(
        id_pagamento smallint,
        id_venda smallint,
        id_forma_pagamento smallint,
        id_situacao_pagamento smallint,
        data date,
        constraint pkid_pagamento primary key (id_pagamento),
        constraint fkid_venda foreign key (id_venda) references Venda(id_venda),
        constraint fkid_forma_pagamento foreign key (id_forma_pagamento) references Forma_pagamento(id_forma_pagamento),
        constraint fkid_situacao_pagamento foreign key (id_situacao_pagamento) references Situacao_pagamento(id_situacao_pagamento)
    )
