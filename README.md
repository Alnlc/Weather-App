# Projeto Previsão do Tempo com Flask

Uma aplicação web, construída com o micro-framework Python Flask, que exibe a previsão do tempo atual e para os próximos 5 dias com base na localização automática do usuário. O projeto se destaca por sua interface dinâmica, que se adapta visualmente para temas de "Dia" e "Noite", e pela riqueza de detalhes climáticos fornecidos.

## 🚀 Aplicação ao Vivo

Você pode acessar a versão ao vivo da aplicação através do seguinte link:

**[🔗 Acesse o Weather-App aqui](https://weather-app-duq3.onrender.com/)**


## 📜 Sumário

1.  **Funcionalidades** ✨
2.  **Preview** 🖼️
3.  **Tecnologias Utilizadas** 🛠️
4.  **Como Instalar e Executar** ⚙️
      - Pré-requisitos
      - Passos para Instalação e Configuração
      - Executando a Aplicação
5.  **Roadmap (Futuras Implementações)** 🗺️

## ✨ Funcionalidades

  * **Previsão Automática por Geolocalização:** Utiliza a API de Geolocalização do navegador para detectar a localização do usuário e exibir a previsão do tempo local.
  * **Previsão para 5 Dias:** Apresenta a previsão estendida, com temperaturas máximas, mínimas e as condições climáticas para os próximos cinco dias.
  * **Detalhes Climáticos:** Exibe informações detalhadas do tempo atual, incluindo velocidade do vento e nível de umidade.
  * **Interface Dinâmica (Dia/Noite):** A aparência da página muda automaticamente para um tema claro ("Dia") ou escuro ("Noite") com base no horário do nascer e pôr do sol da localidade.
  * **Design Responsivo:** Interface totalmente adaptável para uma ótima experiência em desktops e dispositivos móveis.
  * **Fallback com Dados Mockados:** Garante a exibição de uma interface funcional com dados de exemplo caso a geolocalização falhe ou a API externa não responda.

> **Nota:** A aplicação solicitará permissão para acessar sua localização. É necessário conceder essa permissão para que a previsão do tempo seja exibida corretamente.

## 🖼️ Preview


<div align="center">
  <img width="1920" height="1080" alt="Image" src="/app/static/images/previews/day.png" />
</div>

<div align="center">
  <img width="1920" height="1080" alt="Image" src="/app/static/images/previews/night.png" />
</div>


## 🛠️ Tecnologias Utilizadas

  * **Backend:**
    * [Python](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/)
    * [Poetry](https://python-poetry.org)
  * **Frontend:**
    * HTML5, CSS3, JavaScript
    * API de Geolocalização do Navegador
  * **API Externa:**
    * [Weatherbit.io API](https://www.weatherbit.io/) para fornecimento dos dados climáticos.

## ⚙️ Como Instalar e Executar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

  * Python 3.10+
  * Git
  * Poetry (ou `pip` como alternativa)

### Passos para Instalação e Configuração

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/Alnlc/Weather-App](https://github.com/Alnlc/Weather-App)
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd Weather-App
    ```

3.  **Crie e ative um ambiente virtual:**

      * **Para Linux/macOS:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
      * **Para Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

4.  **Configure suas variáveis de ambiente:**
    Copie o arquivo de exemplo `.env.example` para criar seu próprio arquivo de configuração `.env`.

      * **No Linux/macOS:**
        ```bash
        cp .env.example .env
        ```
      * **No Windows:**
        ```bash
        copy .env.example .env
        ```

    Agora, abra o arquivo `.env` e adicione sua chave da API da Weatherbit:

    ```
    # Chave da API obtida no site da Weatherbit
    KEY_API="SUA_CHAVE_DE_API_SECRETA_AQUI"
    ```
    > **Nota:** Você pode obter uma chave de API, incluindo um plano gratuito, no site da [Weatherbit](https://www.weatherbit.io/pricing).

5.  **Instale as dependências do projeto:**
    O projeto utiliza **Poetry**. Para instalar as dependências, execute:

    ```bash
    poetry install
    ```

    > **Alternativa com `pip`:** Se preferir usar o `pip`, você pode primeiro exportar as dependências para um arquivo `requirements.txt` e depois instalá-las.

    > ```bash
    > # Primeiro, exporte as dependências (requer Poetry instalado)
    > poetry export -f requirements.txt --output requirements.txt --without-hashes
    > # Depois, instale com pip
    > pip install -r requirements.txt
    > ```

### Executando a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, inicie o servidor Flask:

```bash
flask run
```
### 🗺️ Roadmap (Futuras Implementações)

Este projeto está em constante evolução. Os próximos passos planejados são:

    [ ] Templates Adaptáveis ao Clima: O plano principal é expandir a funcionalidade dos temas dinâmicos. A interface mudará não apenas entre dia e noite, mas também para refletir o clima atual (ensolarado, nublado, chuvoso, tempestade, etc.), oferecendo uma experiência visual mais rica e imersiva.

    [ ] Pop-ups de Erro: Trocar as mensagens de erro atuais por pop-ups, com a intenção de que, mesmo ao resultar em erro, o usuário possa desfrutar de uma aparência de tela mais agradável.

    [ ] Unidades de Medida Alternativas: Adicionar um botão para alternar a exibição de temperatura entre Celsius (°C) e Fahrenheit (°F).

    [ ] Detalhes Adicionais: Incluir mais dados como índice UV e probabilidade de precipitação.
