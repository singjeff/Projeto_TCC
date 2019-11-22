const btn = document.querySelector("#botaoAdicionar") // Nome do botão do HTML 

btn.addEventListener("click", function(e){
  e.preventDefault()

  const person = getFormValues(form)

  const tr = makeTr(person)

  const table = document.querySelector("#tableLote") // Nome da Tabela no HTML 
  table.appendChild(tr)



  function makeTr(person){
      const tr = document.createElement("tr")
      
     
      const tdCodigoProduto = makeTd(person.codigoProduto)
      const tdNomeProduto = makeTd(person.nomeProduto)
      const tdValorProduto= makeTd(person.valorProduto)
      const tdQtdProduto = makeTd(person.qtdProduto)
      const tdMarcaProduto = makeTd(person.marcaProduto)
      const tdCategoriaProduto = makeTd(person.categoriaProduto)
      const tdValorTotal = makeTd(person.valorTotal)


      tr.appendChild(tdCodigoProduto)
      tr.appendChild(tdNomeProduto)
      tr.appendChild(tdValorProduto)
      tr.appendChild(tdQtdProduto)
      tr.appendChild(tdMarcaProduto)
      tr.appendChild(tdCategoriaProduto)
      tr.appendChild(tdValorTotal)
   

      return tr
  }

  function makeTd(personInfo){
    let td = document.createElement('td')
    td.textContent = personInfo
    return td;
  }

  function getFormValues(form){

    const person = {

        codigoProduto: form.codigoProduto.value,
        nomeProduto: form.nomeProduto.value,
        valorProduto: form.valorProduto.value,
        qtdProduto: form.qtdProduto.value,
        marcaProduto: form.marcaProduto.value,
        categoriaProduto: form.categoriaProduto.value,
        valorTotal: form.valorTotal.value 
      
    }

    return person
  }

})

//Original (código da tabela dinamica) = https://codepen.io/felipe-rodolfo/pen/Rdwogd


// ################### LIMPAR A TABELA DEPOIS DE CLICK NO BOTÃO ADICIONAR #############

document.getElementById("botaoAdicionar").addEventListener("click", function() {

    clearInputUrlNumberText("codigoProduto"); // Nome dos Inputs pra limpar depois que adicionar
    clearInputUrlNumberText("nomeProduto"); 
    clearInputUrlNumberText("valorProduto");
    clearInputUrlNumberText("qtdProduto");
    clearInputUrlNumberText("valorTotal");

  });
  
  function clearInputUrlNumberText(name) {
    var entradas = document.querySelectorAll("input[name='"+name+"']");
    [].map.call(entradas, nomeProduto => nomeProduto.value = '');
  }

// Código para limpar formulario ao click no botão = https://pt.stackoverflow.com/questions/174194/como-limpar-input

// ################### FIM LIMPAR A TABELA DEPOIS DE CLICK NO BOTÃO ADICIONAR #############



// #########################################################################################
// ################## LIMPAR OS COMBOBOX DEPOIS DO CLICK NO BOTÃO ADICIONAR ###############

//                  Marca do produto
$(".btn").on("click", function () { // Nome do botão
  $("select.form-list-marcaProduto option").each(function(i){ // Classe do Select
      $(this).removeAttr("selected");
      if (i == 0) this.selected = true; // onde o "i" é o index desse select, começando em zero
    });
});

//                 Categoria do Produto
$(".btn").on("click", function () { // Nome do botão
  $("select.form-list-categoriaProduto option").each(function(i){ // Classe do Select
      $(this).removeAttr("selected");
      if (i == 0) this.selected = true; // onde o "i" é o index desse select, começando em zero
    });
});





// Código dessa função: http://jsfiddle.net/suhjnxaj/1/

// ################## FIM LIMPAR OS COMBO BOX DEPOIS DO CLICK NO BOTÃO ADICIONAR ###############



