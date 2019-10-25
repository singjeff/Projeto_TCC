var d = document;

function processar(idTabela) {
    var newRow = d.createElement('tr');
    newRow.insertCell(0).innerHTML = d.getElementsByName('user')[0].value;
    newRow.insertCell(1).innerHTML = d.getElementsByName('senha')[0].value;
    d.getElementById(idTabela).appendChild(newRow);
    return false;
}

/*
<form name="formulario" method="post" onsubmit="return processar('myTable')">  
                                                Nome:  <input type="text" name="user">
                                                Senha: <input type="password" name="senha">
                                                <input type="submit" value="Confirmar"> 
                                                <a href="telaInicial.html" name="voltar">Voltar</a>
                                            </form>
                                            <table border='1' width='250' height='250'>
                                                <tbody id="myTable"></tbody>
                                            </table>
*/