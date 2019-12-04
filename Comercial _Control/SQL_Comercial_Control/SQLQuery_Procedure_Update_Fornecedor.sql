/*
 ############# PROCEDURE #############
    ####### UPDATE FORNECEDOR ###########

*/



CREATE PROCEDURE [dbo].[sp_update_fornecedor]
--------------------------------
@razao_social VARCHAR(130),
@cep int,
@cidade VARCHAR(60),
@uf VARCHAR(2),
@endereco VARCHAR(90),
@num_endereco VARCHAR(65),
@complemento VARCHAR(65),
@telefone VARCHAR(14),
@celular  VARCHAR(15),
@email VARCHAR(200),
@nome_contato VARCHAR(50),
@inscricao  VARCHAR(18)
AS
BEGIN
	UPDATE Pessoa
	SET nome = @razao_social
	WHERE inscricao = @inscricao

	UPDATE Endereco_Pessoa
	SET cep = @cep, endereco = @endereco, numero_endereco = @num_endereco,complemento = @complemento, cidade = @cidade, uf = @uf
	WHERE id_pessoa = (select id_pessoa from Pessoa where inscricao = @inscricao)

	UPDATE Contato_Pessoa
	SET telefone = @telefone, celular = @celular, email = @email, nome_contato=@nome_contato
	WHERE id_pessoa = (select id_pessoa from Pessoa where inscricao= @inscricao)

       
END
