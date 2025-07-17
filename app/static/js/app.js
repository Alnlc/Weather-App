const displayDiv = document.querySelector('.display');

function fetchGetAndUpdateWeatherApp(url) {
    fetch(url)

    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro de rede: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {

        if (data.error) { 
            throw new Error(data.error); 
        }
        if(!data.current) {
            displayDiv.innerHTML =
                '<p><strong>Não foi possivel obter os dados do clima e do tempo</strong></p>'
            return;
        }

        const city = data.current.city;
        const country = data.current.country;
        const temperature = data.current.currentTemp;
        const weather = data.current.description;
        

        displayDiv.innerHTML = `
            <p><strong>Cidade:</strong> ${city}</p>
            <p><strong>País</strong> ${country}</p>
            <p><strong>Temperatura:</strong> ${temperature}°C</p>
            <p><strong>Clima:</strong> ${weather}</p>
        `;
    })
    .catch(error => {

        displayDiv.textContent = `Erro: ${error.message}`;
        console.error("Falha na obtenção dos dados do clima:", error);
    });
}

if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            const url = `weathermap?lat=${lat}&lon=${lon}`;
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