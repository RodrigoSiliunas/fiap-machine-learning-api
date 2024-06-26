from typing import Type, TypeVar, Generic, List
from sqlmodel import SQLModel, Session, select

T = TypeVar("T", bound=SQLModel)


class CRUDService(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def create(self, session: Session, obj_in: T) -> T:
        session.add(obj_in)
        session.commit()
        session.refresh(obj_in)
        return obj_in

    def get(self, session: Session, id: int) -> T:
        return session.get(self.model, id)

    def get_all(self, session: Session) -> List[T]:
        return session.exec(select(self.model)).all()

    def update(self, session: Session, obj_in: T) -> T:
        session.add(obj_in)
        session.commit()
        session.refresh(obj_in)
        return obj_in

    def delete(self, session: Session, id: int) -> None:
        obj = session.get(self.model, id)
        if obj:
            session.delete(obj)
            session.commit()

    def check_and_create(self, session: Session, obj_in: T) -> T:
        fields_to_check = {field.name for field in self.model.__fields__.values() if field.name != "id"}
        obj_values = {field: getattr(obj_in, field) for field in fields_to_check}

        # Build a query to check for existing objects with matching values
        existing_obj = session.exec(
            select(self.model).filter_by(**obj_values)
        ).first()

        if not existing_obj:
            # No existing object found, create a new one
            return self.create(session, obj_in)

        return None
