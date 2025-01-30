from sqlalchemy.orm import Session
from src.models.mysql.style import Style

def create_style(db: Session, style_data: dict):
    style = Style(**style_data)
    db.add(style)
    db.commit()
    db.refresh(style)
    return style

def get_style(db: Session, style_id: int):
    return db.query(Style).filter(Style.id == style_id).first()

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