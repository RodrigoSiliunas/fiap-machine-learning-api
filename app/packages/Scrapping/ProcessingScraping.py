import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Processing
from app.packages.CRUDService import CRUDService
from sqlmodel import Session

from app.packages.Scrapping.BaseScraping import BaseScraping


class ProcessingScraping(BaseScraping):
    def __init__(self):
        self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?"
        self.options = {
            'Viníferas': 'subopcao=subopt_01',
            'Americanas e Híbridas': 'subopcao=subopt_02',
            'Uvas de Mesa': 'subopcao=subopt_03',
            'Sem classificação': 'subopcao=subopt_04',
        }
        self.processing_service = CRUDService(Processing)

    def fetch_data(self) -> List[Processing]:
        processings = []

        for key, value in self.options.items():
            for year in range(1970, 2023):
                self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_02&{value}"
                response = requests.get(self.product_url)

                if response.status_code != 200:
                    raise Exception(f"Error fetching data from {self.product_url}. Status code: {response.status_code}.")

                soup = BeautifulSoup(response.text, 'html.parser')
                data = soup.find('table', class_='tb_base tb_dados')
                tbody = data.find('tbody')

                category = None
                for tr in tbody.find_all('tr'):
                    items = tr.find_all('td')

                    if 'tb_item' in items[0].get('class', []):
                        category = items[0].text
                    elif 'tb_subitem' in items[0].get('class', []):
                        processing_quantity = ''.join(
                            filter(str.isdigit, items[1].text))

                        if (processing_quantity is None) or (processing_quantity == ''):
                            processing_quantity = 0

                        processings.append(
                            Processing(
                                name=items[0].text, category=category, subcategory=key, quantity=processing_quantity, year=year))

        return processings

    def populate_database(self, session: Session):
        print('Starting to populate database with data from processings...')
        processings = self.fetch_data()

        for process in processings:
            self.processing_service.check_and_create(session, process)
