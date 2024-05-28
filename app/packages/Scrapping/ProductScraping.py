import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Product
from app.packages.CRUDService import CRUDService
from sqlmodel import Session

from app.packages.Scrapping import BaseScraping


class ProductScraping(BaseScraping):
    def __init__(self):
        self.product_url = "http://example.com/products"
        self.product_service = CRUDService(Product)

    def fetch_data(self) -> List[Product]:
        response = requests.get(self.product_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Simulação de scraping de produtos
        products = []
        for item in soup.find_all('div', class_='product'):
            name = item.find('h2').text
            category = item.find('p', class_='category').text
            products.append(Product(name=name, category=category))
        return products

    def populate_database(self, session: Session):
        products = self.fetch_data()
        for product in products:
            self.product_service.create(session, product)
        session.commit()
