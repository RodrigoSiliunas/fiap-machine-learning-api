from sqlmodel import create_engine, Session, SQLModel, inspect
from app.models import (
    Product,
    Production,
    User,
    Processing,
    Commercialization,
    Importation,
    Exportation
)

DATABASE_URL = "sqlite:///app/database/fast-api-ml.db"
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

def check_tables():
    inspector = inspect(engine)
    tables_in_db = inspector.get_table_names()
    tables_in_models = SQLModel.metadata.tables.keys()
    tables_status = {
        table: table in tables_in_db for table in tables_in_models}
    return tables_status

def check_if_tables_empty(session: Session):
    table_status = {}

    for table_name, table_obj in SQLModel.metadata.tables.items():
        model_class = table_obj.info.get('model_class')

        if model_class is not None:
            count = session.query(eval(f'{model_class}')).count()
            table_status[table_name] = (count == 0)
    return table_status
