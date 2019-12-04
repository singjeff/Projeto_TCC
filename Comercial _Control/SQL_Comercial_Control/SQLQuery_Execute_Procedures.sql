

exec sp_insert_usuario 'gerente', 'ADMIN', null, '2', 'ADMIN','admin@admin.com', '2019-11-30', '21232f297a57a5a743894a0e4a801fc3','(11) 1111-111', '(11) 1111-111', 'admin@admin.com','admin','Av Admin', 'casa 157', 'São Paulo', 'SP', '08285060', '5784'



exec sp_insert_usuario 'Caixa', 'Usuario', null, '1', 'Usuario','usuarion@usuario.com', '2019-11-30', 'f8032d5cae3de20fcec887f395ec9a6a','(11) 1111-111', '(11) 1111-111', 'usuario@usuario.com','Usuario','Av Admin', 'casa 157', 'São Paulo', 'SP', '08285060', '5784'



delete from Pessoa where id_pessoa = '3'

select * from Usuario
select * from Fornecedor
select * from Pessoa
select * from Endereco_Pessoa

select * from Contato_Pessoa



select * from Pessoa where inscricao = '01.026.219/0001-22'

SELECT a.cnpj, a.data_compra, a.num_notafiscal, b.codigo_produto, b.descricao, b.valor_venda, c.quantidade, b.id_marca, b.id_categoria, a.valor_total 
      FROM Produto B INNER JOIN Compra A ON A.codigo_produto= B.codigo_produto
          INNER JOIN  Item C ON C.codigo_produto = B.codigo_produto 

select * from Compra
select * from Item
select * from Produto