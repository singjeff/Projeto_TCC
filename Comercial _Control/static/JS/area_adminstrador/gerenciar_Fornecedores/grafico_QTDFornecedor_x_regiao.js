var lista = $('.UF_Fornecedor'); // PEGA A CLASSE DAS TDs
var contador_fornecedor_de_TO = 0;
var contador_fornecedor_de_BA = 0;
var contador_fornecedor_de_SE = 0;
var contador_fornecedor_de_PE = 0;
var contador_fornecedor_de_AL = 0;
var contador_fornecedor_de_RN = 0;
var contador_fornecedor_de_CE = 0;
var contador_fornecedor_de_PI = 0;
var contador_fornecedor_de_MA = 0;
var contador_fornecedor_de_AP = 0;
var contador_fornecedor_de_PA = 0;
var contador_fornecedor_de_RR = 0;
var contador_fornecedor_de_AM = 0;
var contador_fornecedor_de_AC = 0;
var contador_fornecedor_de_RO = 0;
var contador_fornecedor_de_MT = 0;
var contador_fornecedor_de_MS = 0;
var contador_fornecedor_de_GO = 0;
var contador_fornecedor_de_PR = 0;
var contador_fornecedor_de_SC = 0;
var contador_fornecedor_de_RS = 0;
var contador_fornecedor_de_SP = 0;
var contador_fornecedor_de_MG = 0;
var contador_fornecedor_de_RJ = 0;
var contador_fornecedor_de_ES = 0;
var contador_fornecedor_de_DF = 0;



$.each(lista, function (index, item) {

  valor = $(item).text();

  if (valor == 'TO') {

    contador_fornecedor_de_TO++;
  }

  if (valor == 'BA') {

    contador_fornecedor_de_BA++;
  }

  if (valor == 'SE') {

    contador_fornecedor_de_SE++;
  }

  if (valor == 'PE') {

    contador_fornecedor_de_PE++;
  }

  if (valor == 'AL') {

    contador_fornecedor_de_AL++;
  }

  if (valor == 'RN') {

    contador_fornecedor_de_RN++;
  }

  if (valor == 'CE') {

    contador_fornecedor_de_CE++;
  }

  if (valor == 'PI') {

    contador_fornecedor_de_PI++;
  }

  if (valor == 'MA') {

    contador_fornecedor_de_MA++;
  }

  if (valor == 'AP') {

    contador_fornecedor_de_AP++;
  }

  if (valor == 'PA') {

    contador_fornecedor_de_PA++;
  }

  if (valor == 'RR') {

    contador_fornecedor_de_RR++;
  }

  if (valor == 'AM') {

    contador_fornecedor_de_AM++;
  }

  if (valor == 'AC') {

    contador_fornecedor_de_AC++;
  }

  if (valor == 'RO') {

    contador_fornecedor_de_RO++;
  }

  if (valor == 'MT') {

    contador_fornecedor_de_MT++;
  }

  if (valor == 'MS') {

    contador_fornecedor_de_MS++;
  }

  if (valor == 'GO') {

    contador_fornecedor_de_GO++;
  }

  if (valor == 'PR') {

    contador_fornecedor_de_PR++;
  }

  if (valor == 'SC') {

    contador_fornecedor_de_SC++;
  }

  if (valor == 'RS') {

    contador_fornecedor_de_RS++;
  }

  if (valor == 'SP') {

    contador_fornecedor_de_SP++;
  }

  if (valor == 'MG') {

    contador_fornecedor_de_MG++;
  }

  if (valor == 'RJ') {

    contador_fornecedor_de_RJ++;
  }

  if (valor == 'ES') {

    contador_fornecedor_de_ES++;
  }

  if (valor == 'DF') {

    contador_fornecedor_de_DF++;
  }


});

// Código do mapa = https://jsfiddle.net/LucasBassetti/qrd0nvx2/2/

