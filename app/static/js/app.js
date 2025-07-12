const displayDiv = getElementByClass(display);

function fetchGetAndUpdateWeatherApp(url) {
    fetch
    .then(Response => {
        if (!response.ok){
            throw new Error ('Erro $(response.status): Dados não obtidos');
            return response,json() 
        }
    })
    .then(data =>{
        if(!data.error) {
            throw new Error(data.error); 
        }
        const city = data.nome;
        const temperature= data.main.temp;
        const weather=data.weather[0].description;

        displayDiv.innerHTML =
            <><p><strong>Cidade:</strong>$(city)</p>
            <p>Temperatura:$(temperature)</p>
            <p>clima:$(weather)</p></>
            
    })
    .catch(error =>){
        displayDiv,textContent = "Error $(error.message)";

    }
}


if ('geolocation' in navigator){
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const url = '/app/weathermap?lat=${lat}&lon=${lon}'
            fetchGetAndUpdateWeatherApp(url);

        },
        (error) =>{
            console.warn(`Erro de Geolocalização (código ${error.code}): ${error.message}`);
            infoClimaDiv.textContent = 'Geolocalização negada. Por favor, use a busca manual.';
        }
    )
}else {
            // Caso o navegador seja muito antigo e não suporte a API
            infoClimaDiv.textContent = 'Seu navegador não suporta geolocalização. Use a busca manual.';
        }

