

/*
 ############# PROCEDURE #############
    ####### UPDATE USUARIO ###########

*/



CREATE PROCEDURE [dbo].[sp_update_usuario]
--------------------------------

@nome_usuario VARCHAR(100),
@nome_pessoa VARCHAR(130),
@cep INT,
@cidade VARCHAR(60),
@uf VARCHAR(2),
@endereco VARCHAR(90),
@num_endereco VARCHAR(65),
@telefone VARCHAR(14),
@celular  VARCHAR(15),
@cargo                  VARCHAR(20), 
@senha					VARCHAR(500),
@id_tipo_pessoa         SMALLINT,
@email_usuario	VARCHAR(30)

AS
BEGIN
	UPDATE Usuario
	SET nome_usuario = @nome_usuario, senha_aplicacao = @senha, id_tipopessoa = @id_tipo_pessoa
	WHERE email_usuario = @email_usuario

	UPDATE Pessoa
	SET nome = @nome_pessoa
	WHERE id_pessoa = (select id_pessoa from Usuario where email_usuario = @email_usuario)

	UPDATE Endereco_Pessoa
	SET cep = @cep, cidade =@cidade, uf = @uf, endereco = @endereco, numero_endereco = @num_endereco
	WHERE id_endereco_pessoa = (select id_endereco_pessoa from Usuario where email_usuario = @email_usuario)

	UPDATE Contato_Pessoa
	SET telefone = @telefone, celular = @celular
	WHERE id_contato_pessoa = (select id_contato_pessoa from Usuario where email_usuario = @email_usuario)

	UPDATE Funcionario
	SET cargo = @cargo
	WHERE id_funcionario = (select id_funcionario from Usuario where email_usuario = @email_usuario)
       
END