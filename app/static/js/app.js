const displayDiv = document.querySelector('.display');
const displayDivCurr = document.querySelector('.display-current');
const displayDivFore = document.querySelector('.display-forecast');
const loadingMessage = document.querySelector('.loading-message');



function fetchGetAndUpdateWeatherApp(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro de rede: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            loadingMessage.style.display = 'none';
            displayDiv.classList.add('loaded');

            if (data.error) {
                throw new Error(data.error);
            }

            if (!data.current) {
                displayDivCurr.innerHTML = '<p><strong>Não foi possível obter os dados do clima</strong></p>';
                return;
            }

            // Current Weather
            const city = data.current.city;
            const temperature = data.current.currentTemp;
            const weather = data.current.description;
            const wind = data.current.wind;
            const humidity = data.current.rh;
            const icon = `https://www.weatherbit.io/static/img/icons/${data.current.icon}.png`;

            const time = new Date(data.current.time);
                    const formattedDate = time.toLocaleDateString('pt-BR', {
                        weekday: 'short',
                        day: '2-digit',
                        month: '2-digit'
                    });

            displayDivCurr.innerHTML = `
                <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <img src="${icon}" alt="${weather}" style="width: 80px; height: 80px;">
                    <h2>${city}</h2>
                    <p style="font-size: 2rem; font-weight: bold;">${temperature}°C</p>
                    
                    <div class="weather-details">
                        <p><strong>Clima</strong><br>${weather}</p>
                        <p><strong>Vento</strong><br>${wind} m/s</p>
                        <p><strong>Umidade</strong><br>${humidity}%</p>
                    </div>
                </div>
            `;

            // Forecast Weather
            if (data.forecast && data.forecast.length > 0) {
                let forecastHTML = '';

                data.forecast.forEach(day => {
                    const highTemp = day.highTemp;
                    const lowTemp = day.lowTemp;
                    const description = day.description;
                    const icon = `https://www.weatherbit.io/static/img/icons/${day.icon}.png`;


                    const date = new Date(day.date);
                    const formattedDate = date.toLocaleDateString('pt-BR', {
                        weekday: 'short',
                        day: '2-digit',
                        month: '2-digit'
                    });

                    forecastHTML += `
                        <div class="forecast-day">
                            <p><strong>${formattedDate}</strong></p>
                            <img src="${icon}" alt="${description}" class="forecast-icon">
                            <p><strong>Max</strong> ${highTemp}°C</p>
                            <p><strong>Min</strong> ${lowTemp}°C</p>
                            <p>${description}</p>
                        </div>
                    `;
                });

                displayDivFore.innerHTML = forecastHTML;
            } else {
                displayDivFore.innerHTML = "<p>Não foi possível obter a previsão do tempo.</p>";
            }
        })
        .catch(error => {
            loadingMessage.innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`;
            console.error("Falha na obtenção dos dados do clima:", error);
        });
}

// Função para obter localização e buscar dados do clima
function initializeWeatherApp() {
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

                let errorMessage = '';
                switch(error.code) {
                    case error.PERMISSION_DENIED:
                        errorMessage = 'Geolocalização negada pelo usuário. Por favor, permita o acesso à localização.';
                        break;
                    case error.POSITION_UNAVAILABLE:
                        errorMessage = 'Localização não disponível. Verifique sua conexão.';
                        break;
                    case error.TIMEOUT:
                        errorMessage = 'Timeout na obtenção da localização. Tente novamente.';
                        break;
                    default:
                        errorMessage = 'Erro desconhecido na obtenção da localização.';
                        break;
                }

                loadingMessage.innerHTML = `<p style="color: orange;">${errorMessage}</p>`;
            },
            {
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 600000 // 10 minutos
            }
        );
    } else {
        loadingMessage.innerHTML = '<p style="color: red;">Seu navegador não suporta geolocalização.</p>';
    }
}

// Inicializar o app quando a página carregar
document.addEventListener('DOMContentLoaded', initializeWeatherApp);
document.addEventListener('DOMContentLoaded', () => {
            const descriptionContainer = document.querySelector('.description-container');

            if (descriptionContainer) {
                descriptionContainer.addEventListener('click', () => {
                    descriptionContainer.classList.toggle('active');
                });
            }
        });