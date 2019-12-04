
function buscar_usuario_por_id(e){
    
    var linha = $(e).closest("tr");
    var id_usuario = linha.find("td:eq(0)").text().trim();

    $.ajax({
        data: {
            id_usuario: id_usuario
        },
        type: 'POST',
        url: '/buscar_usuario_por_id'
    })
    .done(function(data){
        if(data.error){
            console.log('erro ' + data.error);
        }
        else if(data){
            $("#nome_usuario").val(data.nome_usuario);
            $("#cep").val(data.cep);
            $("#cidade").val(data.cidade);
            $("#UF").val(data.uf);
            $("#endereco").val(data.endereco);
            $("#numero_endereco").val(data.numero_endereco);
            $("#telefone").val(data.telefone);
            $("#celular").val(data.celular);
            $("#cargo").val(data.cargo);
            $("#email_Usuario").val(data.email_usuario);
            
            if(data.id_tipo_pessoa == 1){
                $("#tipo_Usuario").prop('checked', true)
                $("#tipo_adminstrador").prop('checked', false)
            }
            else if(data.id_tipo_pessoa == 2){
                
                $("#tipo_adminstrador").prop('checked', true)
                $("#tipo_Usuario").prop('checked', false)

                
            }


        }
        

    });

    
}
