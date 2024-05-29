from typing import List
from sqlmodel import Session
from app.packages.Scrapping import BaseScraping

class Scraping:
    def __init__(self, scrapers: List[BaseScraping] = []):
        self.scrapers = scrapers

    def populate_database(self, session: Session):
        for scraper in self.scrapers:
            scraper.populate_database(session)
