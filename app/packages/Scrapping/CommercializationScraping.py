import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Commercialization, Product
from app.packages.CRUDService import CRUDService
from sqlmodel import Session, select

from app.packages.Scrapping.BaseScraping import BaseScraping


class CommercializationScraping(BaseScraping):
    def __init__(self):
        self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano=1970&opcao=opt_04"
        self.product_service = CRUDService(Product)
        self.commercialization_service = CRUDService(Commercialization)

    def fetch_products_data(self) -> List[Product]:
        products = []

        for year in range(1970, 2024):
            self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?" \
                f"ano={year}&opcao=opt_04"
            response = requests.get(self.product_url)

            if response.status_code != 200:
                raise Exception(f"Error fetching data from "
                                f"{self.product_url}. Status code: {response.status_code}.")

            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('table', class_='tb_base tb_dados')
            tbody = data.find('tbody')

            category = None
            for tr in tbody.find_all('tr'):
                item_list = tr.find_all('td')

                if 'tb_item' in item_list[0].get('class', []):
                    category = ' '.join(str(item_list[0].text).replace('\n', '').split())
                elif 'tb_subitem' in item_list[0].get('class', []):
                    products.append(
                        Product(name=' '.join(str(item_list[0].text).replace('\n', '').split()), category=category))

        return products

    def fetch_data(self, products: list[dict]) -> List[Commercialization]:
        commercializations = []

        for year in range(1970, 2024):
            self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?" \
                f"ano={year}&opcao=opt_04"
            response = requests.get(self.product_url)

            if response.status_code != 200:
                raise Exception(f"Error fetching data from "
                                f"{self.product_url}. Status code: {response.status_code}.")

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

                product = list(filter(lambda product: product.get('name') == ' '.join(str(items[0].text).replace('\n', '').split()), products))
                commercialization = Commercialization(year=year, quantity=production_quantity, product_id=product[0].get('id'))
                commercializations.append(commercialization)

        return commercializations

    def populate_database(self, session: Session):
        print('Starting to populate database with data from commercialization...')
        products_in_page = self.fetch_products_data()

        for product in products_in_page:
            self.product_service.check_and_create(session, product)

        products = session.exec(select(Product)).all()
        product_dicts = [product.dict() for product in products]

        commercializations = self.fetch_data(product_dicts)
        for commercialization in commercializations:
            self.commercialization_service.check_and_create(
                session, commercialization)
