var isEditing = false,
	tempNameValue = "",
    tempDataValue = "";
	tempEmailValue = "";
	

	// Pra criar um novo editar, coloque o novo campo acima e vá adicionando abaixo (ATENÇÃO NOS NOMES)

// Handles live/dynamic element events, i.e. for newly created edit buttons
$(document).on('click', '.edit', function() {
	var parentRow = $(this).closest('tr'),
		tableBody = parentRow.closest('tbody'),
		tdName = parentRow.children('td.name'),
        tdData = parentRow.children('td.data'),
        tdEmail = parentRow.children('td.email');

	if (isEditing) {
		var nameInput = tableBody.find('input[name="name"]'),
            dataInput = tableBody.find('input[name="data"]'),
            emailInput = tableBody.find('input[name="email"]'),

			tdNameInput = nameInput.closest('td'),
            tdDataInput = dataInput.closest('td'),
            tdEmailInput = emailInput.closest('td'),

			currentEdit = tdNameInput.parent().find('td.edit');

		if ($(this).is(currentEdit)) {
			// Save new values as static html ####### AQUI ONDE SALVA OS VALORES ALTERADOS ########
			var tdNameValue = nameInput.prop('value'),
                tdDataValue = dataInput.prop('value'),
                tdEmailValue = emailInput.prop('value');

			tdNameInput.empty();
            tdDataInput.empty();
            tdEmailInput.empty();

			tdNameInput.html(tdNameValue);
            tdDataInput.html(tdDataValue);
            tdEmailInput.html(tdEmailValue);
		} else {
			// Restore previous html values
			tdNameInput.empty();
            tdDataInput.empty();
            tdEmailInput.empty();

			tdNameInput.html(tempNameValue);
            tdDataInput.html(tempDataValue);
            tdEmailInput.html(tempEmailValue);

            
		}
		
		
		// Display static row
		currentEdit.html('<a class="btn btn-success btn-xs" ><span class="glyphicon glyphicon-edit"></span>Editar</a>');
		isEditing = false;
	} else {
		// Display editable input row ##### AQUI FICA O SALVAR (2° CLICK)
		isEditing = true;
		$(this).html('<a class="btn btn-primary btn-xs" ><span class="glyphicon glyphicon-edit"></span>Salvar</a>');

		var tdNameValue = tdName.html(),
            tdDataValue = tdData.html();
            tdEmailValue = tdEmail.html();

		// Save current html values for canceling an edit
		tempNameValue = tdNameValue;
        tempDataValue = tdDataValue;
        tempEmailValue = tdEmailValue;

		// Remove existing html values
		tdName.empty();
        tdData.empty();
        tdEmail.empty();

		// Create input forms
		tdName.html('<input type="text" name="name" value="' + tdNameValue + '">');
        tdData.html('<input type="text" name="data" value="' + tdDataValue + '">');
        tdEmail.html('<input type="text" name="email" value="' + tdEmailValue + '">')
	}
});

// Handles live/dynamic element events, i.e. for newly created trash buttons
$(document).on('click', '.trash', function() {
	// Turn off editing if row is current input
	if (isEditing) {
		var parentRow = $(this).closest('tr'),
			tableBody = parentRow.closest('tbody'),
			tdInput = tableBody.find('input').closest('td'),
			currentEdit = tdInput.parent().find('td.edit'),
			thisEdit = parentRow.find('td.edit');

		if (thisEdit.is(thisEdit)) {
			isEditing = false;
		}
	}

	// Remove selected row from table
	$(this).closest('tr').remove();
});


// Original = https://codepen.io/mikewax/pen/YWxwPw