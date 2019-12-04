

/*
 ############# PROCEDURE #############
    ####### UPDATE PRODUTO ###########

*/



CREATE PROCEDURE [dbo].[sp_update_produto]
--------------------------------

@data_compra date,
@num_notafiscal bigint,

@descricao_produto VARCHAR(100),
@valor_venda float,
@quantidade int,
@id_marca smallint,
@id_categoria smallint,
@valor_total float,
@codigo_produto smallint

AS
BEGIN
	
	UPDATE Produto
	SET descricao = @descricao_produto, valor_venda = @valor_venda, id_marca = @id_marca , id_categoria = @id_categoria
	WHERE codigo_produto = @codigo_produto


	UPDATE Compra
	SET data_compra = @data_compra, num_notafiscal= @num_notafiscal, valor_total = @valor_total
	WHERE codigo_produto = (select codigo_produto from Produto where codigo_produto = @codigo_produto)

	UPDATE Item
	SET quantidade = @quantidade
	WHERE codigo_produto = (select codigo_produto from Produto where codigo_produto = @codigo_produto)

	
       
END