function editar(e){

    var linha = $(e).closest("tr");  // Para acrescentar um novo campo para aparecer no modal, só ir adicionado conforme está abaixo
    

    var CNPJ = linha.find("td:eq(7)").text().trim(); // para mudar o conteudo troque o numero do eq(numero)
    var codigoProduto = linha.find("td:eq(0)").text().trim();
    var nomeProduto = linha.find("td:eq(1)").text().trim();
    var valorProduto = linha.find("td:eq(4)").text().trim();
    var qtdProduto = linha.find("td:eq(5)").text().trim();
    var valorTotal = linha.find("td:eq(6)").text().trim();
    //var marcaProduto = linha.find("td:eq(2)").text().trim();
    //var categoriaProduto = linha.find("td:eq(3)").text().trim();
    
    
    $("#cnpj").val(CNPJ);
    $("#codigoProduto").val(codigoProduto);
    $("#nomeProduto").val(nomeProduto);
    //$("#marcaProduto").val(marcaProduto);
    //$("#categoriaProduto").val(categoriaProduto);
    $("#valorProduto").val(valorProduto);
    $("#qtdProduto").val(qtdProduto);
    $("#valorTotal").val(valorTotal);
    
 }


 // Código original (ultimo comentario) = https://pt.stackoverflow.com/questions/358308/passar-dados-para-uma-janela-modal-bootstrap