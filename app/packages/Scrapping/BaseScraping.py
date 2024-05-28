from abc import ABC, abstractmethod
from sqlmodel import Session

class BaseScraping(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def populate_database(self, session: Session):
        pass

