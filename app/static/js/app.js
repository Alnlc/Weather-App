// CORREÇÃO: Usando querySelector para pegar a div pela sua classe.
const displayDiv = document.querySelector('.display');

function fetchGetAndUpdateWeatherApp(url) {
    fetch(url)
    // CORREÇÃO: Parâmetro 'response' em minúsculo e lógica de retorno corrigida.
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro de rede: ${response.status}`);
        }
        return response.json(); // O return deve vir aqui.
    })
    .then(data => {
        // CORREÇÃO: Lógica de erro invertida.
        if (data.error) { 
            throw new Error(data.error); 
        }

        // Extraindo os dados do objeto 'current'
        const city = data.current.city;
        const temperature = data.current.currentTemp;
        const weather = data.current.description;
        
        // CORREÇÃO: Usando crases (`) para criar um template literal HTML e sintaxe ${} para variáveis.
        displayDiv.innerHTML = `
            <p><strong>Cidade:</strong> ${city}</p>
            <p><strong>Temperatura:</strong> ${temperature}°C</p>
            <p><strong>Clima:</strong> ${weather}</p>
        `;
    })
    .catch(error => {
        // Exibindo o erro na mesma div
        displayDiv.textContent = `Erro: ${error.message}`;
        console.error("Falha na obtenção dos dados do clima:", error);
    });
}

if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            // CORREÇÃO: Usando crases (`) para a string da URL e rota da API atualizada
            const url = `/api/weather?lat=${lat}&lon=${lon}`;
            fetchGetAndUpdateWeatherApp(url);
        },
        (error) => {
            console.warn(`Erro de Geolocalização (código ${error.code}): ${error.message}`);
            // CORREÇÃO: Usando a div que já temos para exibir o erro
            displayDiv.textContent = 'Geolocalização negada. Não é possível obter o clima.';
        }
    );
} else {
    // Caso o navegador seja muito antigo e não suporte a API
    displayDiv.textContent = 'Seu navegador não suporta geolocalização.';
}