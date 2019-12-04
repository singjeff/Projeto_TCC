
document.getElementById('cnpj').addEventListener('focusout', function(event){

    $.ajax({
        data: {
            cnpj: document.getElementById("cnpj").value
        },
        type: 'POST',
        url: '/consultar_fornecedor'
    })
    .done(function(data){
        if(data.error){
            console.log('erro ' + data.error);
        }
        else if(data.mensagem){
            let nome_fornecedor = document.getElementById("nomeFornecedor");

            nome_fornecedor.value = data.mensagem;
        }
        else{
            alert("Fornecedor não encontrado");
            document.getElementById("cnpj").value = ""
            //document.getElementById("cnpj").focus();
        }

    });

    event.preventDefault();
    

 
});
