$(function(){
	$("#cep").on("blur", function () {
		let cep = $(this).val();
		//console.log("Saiu "+ cep);

			$.ajax({       
				url:'http://api.postmon.com.br/v1/cep/'+cep,
				type:'GET',
				dataType:'json',
				success:function (json) {
					if(typeof json.logradouro != 'undefined'){
						$("#endereco").val(json.logradouro);
						//$("#userBairro").val(json.bairro);
						//console.log(json.bairro);
						$("#cidade").val(json.cidade);
						$("#UF").val(json.estado);
						//$("input[name=endereco]").val(json.logradouro)
					}
					$("#user_cel").focus();
					//console.log(json);
			}
		});

	})
})