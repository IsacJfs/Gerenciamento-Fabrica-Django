document.getElementById('inputQuantity').addEventListener('change', function() {
    // Obtém o valor selecionado
    var quantity = this.value;

    // Limpa o contêiner de inputs
    var container = document.getElementById('inputContainer');
    container.innerHTML = '';

    // Cria e adiciona os grupos de entrada de acordo com a quantidade selecionada
    for (var i = 1; i <= quantity; i++) {
        // Cria a div do grupo de entrada
        var groupDiv = document.createElement('div');
        groupDiv.className = 'input-group input-group-sm mb-3 mt-3 col-6';

        var label = document.createElement('p');
        label.className = 'me-3'
        label.textContent = 'Peso da bobina:';
        // Cria o span com o número da sequência
        var span = document.createElement('span');
        span.className = 'input-group-text';
        span.id = 'inputGroup-sizing-sm';
        span.textContent = 'Bobina ' + i; // Substitui o # pelo número da sequência

        // Cria o input
        var input = document.createElement('input');
        input.type = 'text';
        input.className = 'form-control';
        input.setAttribute('aria-label', 'Sizing example input');
        input.setAttribute('aria-describedby', 'inputGroup-sizing-sm');
        input.placeholder = 'peso em kg'

        // Adiciona o span e o input à div do grupo de entrada
        groupDiv.appendChild(label);
        groupDiv.appendChild(span);
        groupDiv.appendChild(input);

        // Adiciona a div do grupo de entrada ao contêiner
        container.appendChild(groupDiv);
    }

    var botao = document.createElement('button');
    botao.className = 'btn btn-outline-secondary';
    botao.type = 'button';
    botao.textContent = 'Salvar';

    container.appendChild(botao)

});