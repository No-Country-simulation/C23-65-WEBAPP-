from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from src.db.mysql import get_mysql_db
from src.models.mysql_models import PieceImg
import shutil
import os
import uuid

router = APIRouter()

UPLOAD_DIR = "./images"

@router.post("/upload/")
async def upload_image(
    file: UploadFile = File(...),
    archepiece_id: int = Form(None),
    artpiece_id: int = Form(None),
    db: Session = Depends(get_mysql_db),
):
    # Generar un nombre único para el archivo
    file_extension = file.filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{file_extension}"

    # Crear el directorio si no existe
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    # Guardar el archivo en el servidor
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Guardar la referencia en la base de datos
    piece_img = PieceImg(
        file_name=unique_name,
        archepiece_id=archepiece_id,
        artpiece_id=artpiece_id,
        mime_type=file.content_type,
        file_size=os.path.getsize(file_path),
    )
    db.add(piece_img)
    db.commit()

    return {"file_name": unique_name, "path": file_path}
