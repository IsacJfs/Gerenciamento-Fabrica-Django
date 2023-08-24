var buttonMapping = {
    'buttonOrden': './ordem.html',
    'buttonExtrusao': './extrusao.html',
    'buttonImpressao': './impressao.html',
    'buttonCorte': './corte.html'
    };

function handleButtonClick(event) {
    var buttonId = event.currentTarget.id;
    var objectElement = document.getElementById('tabela');
    objectElement.data = buttonMapping[buttonId];
}

for (var buttonId in buttonMapping) {
    document.getElementById(buttonId).addEventListener('click', handleButtonClick);
}
