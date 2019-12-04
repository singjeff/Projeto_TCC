
function buscar_fornecedor_por_id(e){
    
    var linha = $(e).closest("tr");
    var id_fornecedor = linha.find("td:eq(0)").text().trim();

    $.ajax({
        data: {
            id_fornecedor: id_fornecedor
        },
        type: 'POST',
        url: '/buscar_fornecedor_por_id'
    })
    .done(function(data){
        if(data.error){
            console.log('erro ' + data.error);
        }
        else if(data){
            $("#cnpj").val(data.cnpj);
            $("#razaosocial").val(data.razaosocial);
            $("#cep").val(data.cep);
            $("#endereco").val(data.endereco);
            $("#numero_endereco").val(data.numero_endereco);
            $("#complemento").val(data.complemento);
            $("#cidade").val(data.cidade);
            $("#UF").val(data.uf);
            $("#nome_contato").val(data.nome_contato);
            $("#email").val(data.email);
            $("#telefone").val(data.telefone);
            $("#celular").val(data.celular);
            }
        

    });

    
}



