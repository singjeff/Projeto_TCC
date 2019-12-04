var lista = $('.invert '); // PEGA O ID DAS TDs
  
  $.each(lista, function(index,item){
  
    valor = $(item).text();
    //alert(valor); //Descomente pra mostrar o valor
  
  });


/*PEGAR SÓ O TRECHO DO CÓDIGO ACIMA PRA ELE LER OS VALORES DA TABELA*/
/*CÓDIGO ORIGIAL = https://pt.stackoverflow.com/questions/190782/como-pegar-valores-contidos-em-uma-tabela */

var trace1 = {
    type: 'bar',
    x: [valor], /*COLOCAR A VARIAVEL AQUI*/ 
    y: [valor],
    marker: {
        color: '#C8A2C8',
        line: {
            width: 2.5
        }
    }
};

var data = [ trace1 ];

var layout = { 
  title: 'Quantidade de Fornecedores cadastarados !',
  font: {size: 18}
};

Plotly.newPlot('myDiv', data, layout, {responsive: true});