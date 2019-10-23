$("#cnpj").keydown(function(){
    try {
        $("#cnpj").unmask();
    } catch (e) {}

    var tamanho = $("#cnpj").val().length;

    if(tamanho < 11){
        $("#cnpj").mask("999.999.999-99");
    } else {
        $("#cnpj").mask("99.999.999/9999-99");
    }

    // ajustando foco
    var elem = this;
    setTimeout(function(){
        // mudo a posição do seletor
        elem.selectionStart = elem.selectionEnd = 10000;
    }, 0);
    // reaplico o valor para mudar o foco
    var currentValue = $(this).val();
    $(this).val('');
    $(this).val(currentValue);
});


//Original = https://jsfiddle.net/z5qmwn1d/

//Alternativo (conflito de Jquery) = https://pt.stackoverflow.com/questions/128039/m%C3%A1scara-para-validar-cpf-e-cnpj-no-mesmo-campo-com-jquery