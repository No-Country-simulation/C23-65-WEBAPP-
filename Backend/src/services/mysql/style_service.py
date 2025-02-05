from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.style import Style

def create_style(db: Session, style_data: dict):
    style = Style(**style_data)
    db.add(style)
    db.commit()
    db.refresh(style)
    return style

def get_style(db: Session, style_id: int):
    return db.query(Style).filter(Style.id == style_id).first()

def get_all_style(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Style)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener estilos: {e}")
        return []

def update_style(db: Session, style_id: int, style_data: dict):
    style = db.query(Style).filter(Style.id == style_id).first()
    if style:
        for key, value in style_data.items():
            setattr(style, key, value)
        db.commit()
        db.refresh(style)
    return style

def delete_style(db: Session, style_id: int):
    style = db.query(Style).filter(Style.id == style_id).first()
    if style:
        db.delete(style)
        db.commit()
    return style