# FastAPI Project

This is a simple FastAPI project that provides a basic API service. Access to the API requires an API key, which must be passed in the `API_KEY` header.

![ Preview of the API](coin_api.png)

## Tasks checklists

- [x] The exam code should be submitted via a GitHub link.
- [x] Include a `Makefile` so that when running the command `make api`, it will start the API.
- [x] The endpoint should accept the currency symbol as a parameter (e.g., BTC). Internally, it should retrieve information from the following URL:
- [x] The project should have another option for querying a different API of your choice, in case the Mercado Bitcoin URL is unavailable.
- [x] (Optional) Implement a caching system for currency price queries to reduce the number of external API calls and improve the application's performance.
- [x] (Optional) Add basic authentication to the API, allowing only authorized users to access the endpoints.

## Requirements

- Docker & Docker Compose (optional)
- Make (for managing commands)

## Project Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-fastapi-project.git
    cd your-fastapi-project
    ```

2. Run the makefile

    ```bash
    make api
    ```
3. Go to localhost/docs

4. Click in the padlock icon and put the API KEY that you can find below    


## API Key Authentication

To use this API, you must include the following API key in the request headers:

```text
API_KEY: 452f7377b202e85cd6c34d2b4cbe43be
```