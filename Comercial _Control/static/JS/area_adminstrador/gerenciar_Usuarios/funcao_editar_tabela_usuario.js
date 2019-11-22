function editar(e){

    var linha = $(e).closest("tr");  // Para acrescentar um novo campo para aparecer no modal, só ir adicionado conforme está abaixo
    
    var nomeUsuario = linha.find("td:eq(2)").text().trim(); // texto da primeira coluna
    var emailUsuario = linha.find("td:eq(1)").text().trim(); 
 
   
    $("#email_Usuario").val(emailUsuario)
    $("#nome_usuario").val(nomeUsuario);

 }


 // Código original (ultimo comentario) = https://pt.stackoverflow.com/questions/358308/passar-dados-para-uma-janela-modal-bootstrap