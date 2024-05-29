import requests
from bs4 import BeautifulSoup

from typing import List
from app.models import Importation
from app.packages.CRUDService import CRUDService
from sqlmodel import Session

from app.packages.Scrapping.BaseScraping import BaseScraping


class ImportationScraping(BaseScraping):
    def __init__(self):
        self.options = {
            'Vinhos de mesa': 'subopcao=subopt_01',
            'Espumantes': 'subopcao=subopt_02',
            'Uvas frescas': 'subopcao=subopt_03',
            'Uvas passas': 'subopcao=subopt_04',
            'Suco de uva': 'subopcao=subopt_05'
        }
        self.importation_service = CRUDService(Importation)

    def fetch_data(self) -> List[Importation]:
        importations = []

        for key, value in self.options.items():
            for year in range(1970, 2024):
                self.product_url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_05&{value}"
                response = requests.get(self.product_url)

                if response.status_code != 200:
                    raise Exception(f"Error fetching data from " \
                                    f"{self.product_url}. Status code: {response.status_code}.")

                soup = BeautifulSoup(response.text, 'html.parser')
                data = soup.find('table', class_='tb_base tb_dados')
                tbody = data.find('tbody')

                for tr in tbody.find_all('tr'):
                    columns = tr.find_all('td')

                    country = str(columns[0].text).replace('\n', '').strip()
                    weight = ''.join(filter(str.isdigit, columns[1].text))
                    value = ''.join(filter(str.isdigit, columns[2].text))

                    if (weight is None) or (weight == ''):
                        weight = 0
                    if (value is None) or (value == ''):
                        value = 0

                    importations.append(
                        Importation(country=country, category=key, weight=weight, value=value, year=year))

        return importations

    def populate_database(self, session: Session):
        print('Starting to populate database with data from importations...')
        importations = self.fetch_data()

        for importation in importations:
            self.importation_service.check_and_create(session, importation)
