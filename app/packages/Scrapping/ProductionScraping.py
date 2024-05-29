import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Production, Product
from app.packages.CRUDService import CRUDService
from sqlmodel import Session, select

from app.packages.Scrapping.BaseScraping import BaseScraping


class ProductionScraping(BaseScraping):
    def __init__(self):
        self.year = 1970
        self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.year}&opcao=opt_02"
        self.product_service = CRUDService(Production)

    def fetch_data(self, products: list[dict]) -> List[Product]:
        productions = []

        for _ in range(self.year, 2024):
            response = requests.get(self.product_url)

            if response.status_code != 200:
                raise Exception(f"Error fetching data from {self.product_url}. Status code: {response.status_code}.")

            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('table', class_='tb_base tb_dados')
            tbody = data.find('tbody')

            for tr in tbody.find_all('tr'):
                items = tr.find_all('td')

                if any('tb_item' in td.get('class', []) for td in items):
                    continue

                # Tratamento da quantidade de produtos;
                production_quantity = ''.join(filter(str.isdigit, items[1].text))

                if (production_quantity is None) or (production_quantity == ''):
                    production_quantity = 0

                product = list(filter(lambda product: product.get('name') == items[0].text, products))
                production = Production(year=self.year, quantity=production_quantity, product_id=product[0].get('id'))
                productions.append(production)

            self.year += 1
            self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.year}&opcao=opt_02"
        return productions

    def populate_database(self, session: Session):
        products = session.exec(select(Product)).all()
        product_dicts = [product.dict() for product in products]

        print('Starting to populate database with data from productions...')
        productions = self.fetch_data(product_dicts)

        for production in productions:
            self.product_service.check_and_create(session, production)
