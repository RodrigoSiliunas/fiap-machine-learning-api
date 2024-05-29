from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs.database import (
    init_db,
    get_session,
    check_tables,
    check_if_tables_empty
)

# Área de importação de rotas;
from app.routes import (
    accounts,
    users,
    products,
    productions,
    processings,
    commercializations,
    importations,
    exportations
)

from app.packages.Scrapping import (
    Scraping,
    ProductScraping,
    ProductionScraping,
    ProcessingScraping,
    CommercializationScraping,
    ImportationScraping,
    ExportationScraping
)

"""
==========================================================================
 ➠ Backend of Machine Learning API - FIAP
 ➠ Section By: Rodrigo Siliunas
 ➠ Related system: Core da nossa aplicação construida com FastAPI
==========================================================================
"""

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Inicializa o banco de dados, verifica se as tabelas já existem, caso não existam, cria-as."""
    tables_exist = check_tables()

    if not all(tables_exist.values()):
        print("Some tables do not exist, creating tables...")
        init_db()

    scrapper = Scraping()
    scraper_classes = {
        'Product': ProductScraping,
        'Production': ProductionScraping,
        'Processing': ProcessingScraping,
        'Commercialization': CommercializationScraping,
        'Importation': ImportationScraping,
        'Exportation': ExportationScraping
    }

    with get_session() as session:
        scrapping_list = [
            'Product',
            'Production',
            'Processing',
            'Commercialization',
            'Importation',
            'Exportation'
        ]
        tables_empty = check_if_tables_empty(session)

        for table_name in scrapping_list:
            if tables_empty.get(table_name.lower(), False):
                scraper_class = scraper_classes[table_name]
                scrapper.scrapers.append(scraper_class())

        if scrapper.scrapers:
            scrapper.populate_database(session)


# Lógica para inicialização do nosso banco de dados;
# TODO: Fazer a verificação, caso as tabelas já estejam criadas não tentar criar novamente.
# TODO: Antes de inicializar a aplicação, disparar uma função que realiza o webscrapping e preenche as tabelas caso elas se encontram vazias.
# SQLModel.metadata.create_all(engine)

# Registro de minhas rotas incluindo elas no router.
app.include_router(accounts)
app.include_router(users)
app.include_router(products)
app.include_router(productions)
app.include_router(processings)
app.include_router(commercializations)
app.include_router(importations)
app.include_router(exportations)
