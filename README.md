## Machine Learning API - FIAP

Este repositório contém o código da API desenvolvida para o desafio técnico proposto durante a pós-graduação em Machine Learning Engineering na FIAP. O desafio consiste em consumir dados da Embrapa e criar uma API com autenticação JWT para obter dados referentes à vitivinicultura.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e de alta performance para construir APIs com Python 3.7+ baseado em padrões como OpenAPI e JSON Schema.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Validação de dados e definição de tipos usando Python com suporte ao uso de dados tipados.
- **[SQLite](https://www.sqlite.org/index.html)**: Banco de dados SQL leve, usado para armazenamento local.
- **[SQLModel](https://sqlmodel.tiangolo.com/)**: Biblioteca para interagir com bancos de dados, combinando Pydantic e SQLAlchemy.
- **[Requests](https://docs.python-requests.org/en/latest/)**: Biblioteca HTTP para fazer requisições de forma simples e elegante.
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)**: Biblioteca para extrair dados de arquivos HTML e XML.

## Funcionalidades

- Autenticação JWT para proteger as rotas da API.
- Consumo de dados da Embrapa referentes à vitivinicultura.
- Endpoints para obter dados de produções, produtos, usuários, exportações, etc.
- Paginação para lidar com grandes volumes de dados.
- Raspagem (webscrapping) de dados usando BeautifulSoup4.

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. Clone o repositório:
    ```sh
    git clone https://github.com/RodrigoSiliunas/fiap-machine-learning-api.git
    cd fiap-machine-learning-api
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv enviroments
    source enviroments/bin/activate  # No Windows, use `\enviroments\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    python -m pip install -r requirements.txt -e .
    ```

4. Execute a aplicação:
    ```sh
    python main.py
    ```

5. Acesse a documentação em Swagger da API em:
    ```
    http://localhost:8000/docs
    ```

## Exemplos de Uso

### Obter Produções por Ano

Endpoint: `/productions/year/{year}`

```sh
curl -X GET "http://127.0.0.1:8000/productions/year/2022" -H "Authorization: Bearer <seu_token_jwt>"
```

### Obter Produções por Categoria

Endpoint: `/productions/category/{category}`

```sh
curl -X GET "http://127.0.0.1:8000/productions/category/uva" -H "Authorization: Bearer <seu_token_jwt>"
```

### Paginação

Endpoint: `/productions`
Parâmetros de query: `limit`, `offset`

```sh
curl -X GET "http://127.0.0.1:8000/productions?limit=10&offset=0" -H "Authorization: Bearer <seu_token_jwt>"
```

### Estrutura do Projeto
```sh
.
├── app
│   ├── configs
│   │    ├── database.py
│   │    └── enviroments.py
│   ├── database
│   │    └── fast-api-ml.db
│   ├── models
│   │    ├── __init__.py
│   │    ├── Commercialization.py
│   │    ├── Exportation.py
│   │    ├── Importation.py
│   │    ├── Product.py
│   │    ├── Production.py
│   │    ├── User.py
│   │    └── ValidToken.py
│   └── packages
│   │    ├── __init__.py
│   │    ├── Auth.py
│   │    ├── CRUDService.py
│   │    └── Scrapping
│   │       ├── __init__.py
│   │       ├── BaseScraping.py
│   │       ├── CommercializationScraping.py
│   │       ├── ExportationScraping.py
│   │       ├── ImportationScraping.py
│   │       ├── ProcessingScraping.py
│   │       ├── ProductionScraping.py
│   │       ├── ProductScraping.py
│   │       └── Scraping.py
│   └── routes
│       ├── __init__.py
│       ├── accounts.py
│       ├── commercializations.py
│       ├── exportations.py
│       ├── importations.py
│       ├── processings.py
│       ├── productions.py
│       ├── products.py
│       ├── users.py
│       └── schemas
│           ├── __init__.py
│           ├── UserLogin.py
│           └── UserRegister.py
├── enviroments
├── requirements.txt
├── .gitignore
├── .env
├── setup.py
├── main.py
├── LICENSE
└── README.md
```
### Contribuição

Sinta-se à vontade para contribuir com este projeto. Para isso:

    1. Faça um fork do projeto.
    2. Crie uma branch para sua feature (git checkout -b feature/fooBar).
    3. Commit suas alterações (git commit -m 'Add some fooBar').
    4. Faça um push para a branch (git push origin feature/fooBar).
    5. Abra um Pull Request.

### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhe.


### Detalhes Importantes:
1. **Autenticação JWT**: Certifique-se de fornecer um token JWT válido ao usar os exemplos de cURL.
2. **Bibliotecas**: Algumas bibliotecas se encontram em versões desatualizadas na data de publicação desse repositório, isso é intencional.

