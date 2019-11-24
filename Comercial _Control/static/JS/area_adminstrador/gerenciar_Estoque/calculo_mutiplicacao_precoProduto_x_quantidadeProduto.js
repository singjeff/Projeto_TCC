// ################### VALOR SOMADO #############

function fmtMoney(n, c, d, t){ 
    var m = (c = Math.abs(c) + 1 ? c : 2, d = d || ",", t = t || ".", 
       /(\d+)(?:(\.\d+)|)/.exec(n + "")), x = m[1].length > 3 ? m[1].length % 3 : 0; 
    return (x ? m[1].substr(0, x) + t : "") + m[1].substr(x).replace(/(\d{3})(?=\d)/g, 
       "$1" + t) + (c ? d + (+m[2] || 0).toFixed(c).substr(2) : ""); 
  }; 
  
  function multiplicar(){
  
    var f = document.forms[0]; 
    var valor1 = parseFloat(f.valorProduto.value.replace('.','').replace(',','.')); 
    var valor2 = parseFloat(f.qtdProduto.value); 
    var valor3 = ('' + ((valor1||0) * (valor2||0))); 
    f.valorTotal.value = fmtMoney(valor3); 
  
    }
  
  // CÓDIGO DA MULTIPLICAÇÃO ( 5 COMENTARIO ) = https://forum.scriptbrasil.com.br/topic/129202-resolvido%C2%A0somar-campos-em-moedas/
  