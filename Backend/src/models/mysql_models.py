from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# Modelo de User
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

# Modelo de Profile
class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(Text)
    profile_picture = Column(String(255))
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)

# Modelo de Gallery
class Gallery(Base):
    __tablename__ = "gallery"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)

# Modelo de Artpiece
class Artpiece(Base):
    __tablename__ = "artpiece"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    year = Column(Integer)
    dimension = Column(String(255))
    author_id = Column(Integer, ForeignKey("author.id"))
    medium_id = Column(Integer, ForeignKey("medium.id"))

# Modelo de Author
class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    birth_date = Column(DateTime)
    death_date = Column(DateTime)
    nationality = Column(String(255))

# Modelo de Genre
class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

# Modelo de Style
class Style(Base):
    __tablename__ = "style"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

# Modelo de Medium
class Medium(Base):
    __tablename__ = "medium"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

# Modelo de CulturePeriod
class CulturePeriod(Base):
    __tablename__ = "culture_period"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

# Modelo de Favorite
class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    archeopiece_id = Column(String(255))  # Cambiado a String para ID de MongoDB
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"))
    gallery_id = Column(Integer, ForeignKey("gallery.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

# Modelo de Like
class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    gallery_id = Column(Integer, ForeignKey("gallery.id"))

# Modelo de Comment
class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    gallery_id = Column(Integer, ForeignKey("gallery.id"))

# Modelo de GalleryArtpiece
class GalleryArtpiece(Base):
    __tablename__ = "gallery_artpiece"
    id = Column(Integer, primary_key=True, index=True)
    gallery_id = Column(Integer, ForeignKey("gallery.id"))
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"))
    note = Column(Text)

# Modelo de ArtpieceGenres
class ArtpieceGenres(Base):
    __tablename__ = "artpiece_genres"
    id = Column(Integer, primary_key=True, index=True)
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))

# Modelo de ArtpieceStyles
class ArtpieceStyles(Base):
    __tablename__ = "artpiece_styles"
    id = Column(Integer, primary_key=True, index=True)
    style_id = Column(Integer, ForeignKey("style.id"))
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"))

# Modelo de PieceImg
class PieceImg(Base):
    __tablename__ = "piece_img"
    id = Column(Integer, primary_key=True, index=True)
    file = Column(String(255))  # Guarda el archivo en base64 o URI
    name = Column(String(255))
    archepiece_id = Column(String(255))  # Cambiado a String para ID de MongoDB
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"))
