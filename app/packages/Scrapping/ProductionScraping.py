import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Production, Product
from app.packages.CRUDService import CRUDService
from sqlmodel import Session

from app.packages.Scrapping import BaseScraping


class ProductionScraping(BaseScraping):
    def __init__(self):
        self.production_url = "http://example.com/productions"
        self.production_service = CRUDService(Production)
        self.product_service = CRUDService(Product)

    def fetch_data(self, session: Session) -> List[Production]:
        response = requests.get(self.production_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Simulação de scraping de produções
        productions = []
        products = self.product_service.get_all(session)

        for item in soup.find_all('div', class_='production'):
            year = int(item.find('span', class_='year').text)
            quantity = int(item.find('span', class_='quantity').text)
            product_name = item.find('span', class_='product_name').text

            product_id = next(
                (p.id for p in products if p.name == product_name), None)
            if product_id:
                productions.append(Production(
                    year=year, quantity=quantity, product_id=product_id))
        return productions

    def populate_database(self, session: Session):
        productions = self.fetch_data(session)
        for production in productions:
            self.production_service.create(session, production)
        session.commit()
