/* ################ MASCARA DE NOME E SOBRENOME (Gerenciar Usuario)  ################# */

function formatanomeUsuario(nome_usuario){

    var nome = document.getElementById("nome_usuario").value;
  
    nome = nome.toLowerCase().replace(/(?:^|\s)\S/g, function(capitalize) { return capitalize.toUpperCase(); });
  
    document.getElementById("nome_usuario").value=nome;
  
  }


/* ################# FIM MASCARA DE NOME E SOBRENOME(Gerenciar Usuario) ################# */

/* ###################################################################################### */
/* ###################################################################################### */
/* ###################################################################################### */



/* ################ MASCARA DE NOME E SOBRENOME (Gerenciar Fornecedor)  ################# */

function formatanomeFornecedor(nome_contato){

  var nome = document.getElementById("nome_contato").value;

  nome = nome.toLowerCase().replace(/(?:^|\s)\S/g, function(capitalize) { return capitalize.toUpperCase(); });

  document.getElementById("nome_contato").value=nome;

}

/* ################ FIM MASCARA DE NOME E SOBRENOME (Gerenciar Fornecedor) ################# */
