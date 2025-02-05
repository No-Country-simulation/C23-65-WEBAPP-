from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.culture_period import CulturePeriod

def create_culture_period(db: Session, culture_period_data: dict):
    culture_period = CulturePeriod(**culture_period_data)
    db.add(culture_period)
    db.commit()
    db.refresh(culture_period)
    return culture_period

def get_culture_period(db: Session, culture_period_id: int):
    return db.query(CulturePeriod).filter(CulturePeriod.id == culture_period_id).first()

def get_all_culture_periods(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(CulturePeriod)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener periodos culturales: {e}")
        return []

def update_culture_period(db: Session, culture_period_id: int, culture_period_data: dict):
    culture_period = db.query(CulturePeriod).filter(CulturePeriod.id == culture_period_id).first()
    if culture_period:
        for key, value in culture_period_data.items():
            setattr(culture_period, key, value)
        db.commit()
        db.refresh(culture_period)
    return culture_period

def delete_culture_period(db: Session, culture_period_id: int):
    culture_period = db.query(CulturePeriod).filter(CulturePeriod.id == culture_period_id).first()
    if culture_period:
        db.delete(culture_period)
        db.commit()
    return culture_period