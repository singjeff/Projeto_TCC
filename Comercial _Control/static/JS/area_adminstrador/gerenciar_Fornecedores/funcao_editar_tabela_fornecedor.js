function editar(e){

    var linha = $(e).closest("tr");  // Para acrescentar um novo campo para aparecer no modal, só ir adicionado conforme está abaixo
    
    var numeroEndereco = linha.find("td:eq(1)").text().trim(); // para mudar o conteudo troque o numero do eq(numero)
    var razaSocial = linha.find("td:eq(2)").text().trim(); 
    var CNPJ = linha.find("td:eq(3)").text().trim(); 
    var celularFornecedor =  linha.find("td:eq(5)").text().trim(); 
 
   
    $("#numero_endereco").val(numeroEndereco) // Ascrente o ID do input e o nome da varivavel 
    $("#razaosocial").val(razaSocial);
    $("#cnpj").val(CNPJ);
    $("#celular").val(celularFornecedor);



 }


 // Código original (ultimo comentario) = https://pt.stackoverflow.com/questions/358308/passar-dados-para-uma-janela-modal-bootstrap