import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Product
from app.packages.CRUDService import CRUDService
from sqlmodel import Session

from app.packages.Scrapping.BaseScraping import BaseScraping


class ProductScraping(BaseScraping):
    def __init__(self):
        self.year = 1970
        self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.year}&opcao=opt_02"
        self.product_service = CRUDService(Product)

    def fetch_data(self) -> List[Product]:
        # Simulação de scraping de produtos
        products = []

        for _ in range(self.year, 2024):
            response = requests.get(self.product_url)

            if response.status_code != 200:
                raise Exception(f"Error fetching data from {self.product_url}. Status code: {response.status_code}.")

            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('table', class_='tb_base tb_dados')
            tbody = data.find('tbody')

            category = None
            for tr in tbody.find_all('tr'):
                item_list = tr.find_all('td')

                if 'tb_item' in item_list[0].get('class', []):
                    category = item_list[0].text
                elif 'tb_subitem' in item_list[0].get('class', []):
                    products.append(Product(name=item_list[0].text, category=category))

            self.year += 1
            self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self.year}&opcao=opt_02"
        return products

    def populate_database(self, session: Session):
        print('Starting to populate database with data from products...')
        products = self.fetch_data()

        for product in products:
            self.product_service.check_and_create(session, product)



if __name__ == "__main__":
    scraping = ProductScraping()
    scraping.fetch_data()
