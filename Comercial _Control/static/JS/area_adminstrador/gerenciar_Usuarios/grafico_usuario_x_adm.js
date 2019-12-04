var lista = $('.tipoUsuario '); // PEGA O ID DAS TDs

var contador_usuarios = 0;
var contador_admistradores = 0;
    
  $.each(lista, function(index,item){
  
    valor = $(item).text();

    if (valor == 1){

        contador_usuarios ++;

        //alert(numero_de_usuario); //Descomente pra mostrar o valor
    }
    else{

        contador_admistradores++;

        //alert(numero_de_adminstrador)
    }
    

  });




   // Line
   var ctx = document.getElementById("grafico_usuario_x_ADM").getContext('2d');
   var grafico_usuario_x_ADM = new Chart(ctx, {
       type: 'bar',
       data: {
           labels: ["Usuarios", "Adminstradores"],
           datasets: [{
               label: 'Quantidade Cadastrada',
               data: [contador_usuarios, contador_admistradores] ,
               backgroundColor: [
                   'rgba(255, 99, 132, 0.2)',
                   'rgba(54, 162, 235, 0.2)',
                   'rgba(255, 206, 86, 0.2)',
                   'rgba(75, 192, 192, 0.2)',
                   'rgba(153, 102, 255, 0.2)',
                   'rgba(255, 159, 64, 0.2)'
               ],
               borderColor: [
                   'rgba(255,99,132,1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
                   'rgba(75, 192, 192, 1)',
                   'rgba(153, 102, 255, 1)',
                   'rgba(255, 159, 64, 1)'
               ],
               borderWidth: 1
           }]
       },
       options: {
           scales: {
               yAxes: [{
                   ticks: {
                       beginAtZero: true
                   }
               }]
           }
       }
   });


