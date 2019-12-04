
/*
 ############# PROCEDURE #############
    ####### INSERT USUARIO ###########

*/


CREATE PROCEDURE [dbo].[sp_insert_usuario]
---------------------------------------
--funcionario--
---------------------------------------
@cargo VARCHAR(20),

---------------------------------------
--pessoa--
----------------------------------------

@nome_pessoa VARCHAR(130),
@inscricao VARCHAR(18) = NULL,


--------------------------------
@id_tipo_pessoa         SMALLINT,
@nome_usuario           VARCHAR(100),
@email_usuario          VARCHAR(100), 
@dtcadastro             DATE = NULL, 
@senha_usuario			VARCHAR(500),

----------------------------------------------
--contato--
----------------------------------------------
@celular  VARCHAR(15),
@telefone VARCHAR(14),
@email_contato VARCHAR(200),
@nome_contato VARCHAR(50),

-------------------------------------------
--endereco--
-------------------------------------------
@endereco VARCHAR(90),
@complemento VARCHAR(65) = NULL,
@cidade VARCHAR(60),
@uf VARCHAR(2),
@cep INT,
@num_endereco VARCHAR(20)

AS
BEGIN
	DECLARE @id_pessoa smallint 
	DECLARE @id_contato smallint
	DECLARE @id_endereco smallint
	DECLARE @id_funcionario smallint
	SELECT @id_pessoa = (select max(id_pessoa)+1 from Pessoa)
	
	INSERT Pessoa(id_pessoa, id_tipo_pessoa, nome, inscricao)
	VALUES(@id_pessoa, @id_tipo_pessoa, @nome_pessoa, @inscricao)

	INSERT INTO Funcionario(id_pessoa, cargo)
	VALUES(@id_pessoa, @cargo)

	SELECT @id_funcionario = @@IDENTITY

	INSERT INTO Contato_Pessoa(id_pessoa, celular, telefone, email, nome_contato)
	VALUES(@id_pessoa ,@celular, @telefone, @email_contato, @nome_contato)

	SELECT @id_contato = @@IDENTITY
	

	INSERT INTO Endereco_Pessoa(id_pessoa, endereco, complemento, cidade, uf, cep, numero_endereco)
	VALUES(@id_pessoa, @endereco, @complemento, @cidade, @uf, @cep, @num_endereco)

	SELECT @id_endereco = @@IDENTITY

	INSERT INTO Usuario(id_tipopessoa, nome_usuario, email_usuario, dt_cadastro, senha_aplicacao, id_contato_pessoa, id_endereco_pessoa, id_pessoa, id_funcionario)
	VALUES(@id_tipo_pessoa, @nome_usuario, @email_usuario, @dtcadastro, @senha_usuario, @id_contato, @id_endereco,@id_pessoa, @id_funcionario)
         
END

