from sqlmodel import create_engine
from sqlmodel import create_engine, Session, SQLModel

"""
==========================================================================
 ➠ Database Configuration File
 ➠ Section By: Rodrigo Siliunas
 ➠ Related system: Database SQLite engine
==========================================================================
"""

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
    for table in SQLModel.metadata.tables.keys():
        model_class = SQLModel.metadata.tables[table].info.get('model_class')
        if model_class:
            count = session.query(model_class).count()
            table_status[table] = (count == 0)
    return table_status
