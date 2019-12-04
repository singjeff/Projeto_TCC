
function buscar_produto_por_id(e){
    
    var linha = $(e).closest("tr");
    var id_produto = linha.find("td:eq(0)").text().trim();

    $.ajax({
        data: {
            id_produto: id_produto
        },
        type: 'POST',
        url: '/buscar_produto_por_id'
    })
    .done(function(data){
        if(data.error){
            console.log('erro ' + data.error);
        }
        else if(data){
            $("#cnpj").val(data.cnpj);
            $("#data_nota").val(data.data_nota);
            $("#numeroNotaFiscal").val(data.numeroNotaFiscal);
            $("#codigoProduto").val(data.codigoProduto);
            $("#nomeProduto").val(data.nomeProduto);
            $("#valorProduto").val(data.valorProduto);
            $("#qtdProduto").val(data.qtdProduto);
            $("#marca").val(data.marca);
            $("#categoriaproduto").val(data.categoriaproduto);
           
            
        
        }
        



    });

    
}