from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional, List

# MongoDB Models
# Modelo de GalleryArtpiece
class GalleryArtpieceInDB(BaseModel):
    id: str
    gallery_id: str
    artpiece_id: str
    note: str

    class Config:
        orm_mode = True

# Modelo de ArtpieceStyles
class ArtpieceStylesInDB(BaseModel):
    id: str
    style_id: str
    artpiece_id: str

    class Config:
        orm_mode = True

# Modelo de ArtpieceGenres
class ArtpieceGenresInDB(BaseModel):
    id: str
    artpiece_id: str
    genre_id: str

    class Config:
        orm_mode = True

# Modelo de PieceImg
class PieceImgInDB(BaseModel):
    id: str
    file: str
    name: str
    archeopiece_id: str
    artpiece_id: str

    class Config:
        orm_mode = True

# Modelo de ProfileFollowing
class ProfileFollowingInDB(BaseModel):
    id: str
    from_profile_id: str
    to_profile_id: str

    class Config:
        orm_mode = True

# Modelo de Archeopiece
class ArcheopieceInDB(BaseModel):
    id: str
    name: str
    object_type: str
    production_date: str
    material: str
    technique: str
    dimensions: str
    description: str
    findspot: str
    current_location: str
    culture_period_id: str

    class Config:
        orm_mode = True

# MySQL Models
# Modelo de User
class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True


# Modelo de Profile
class ProfileBase(BaseModel):
    bio: Optional[str] = None
    profile_picture: Optional[str] = None

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileInDB(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class ProfileResponse(ProfileInDB):
    user: UserInDB  # Incluye información del usuario asociado al perfil

    class Config:
        orm_mode = True

class UserResponse(UserInDB):
    profile: Optional[ProfileInDB] = None  # Información del perfil asociado al usuario

    class Config:
        orm_mode = True
        
# Modelo de Gallery
class GalleryBase(BaseModel):
    image_url: str
    description: Optional[str] = None

class GalleryCreate(GalleryBase):
    owner_id: int

class GalleryInDB(GalleryBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

# Modelo de Artpiece
class ArtpieceBase(BaseModel):
    image_url: Optional[str] = None
    year: Optional[int] = None
    dimension: Optional[str] = None

class ArtpieceCreate(ArtpieceBase):
    author_id: int
    medium_id: int

class ArtpieceInDB(ArtpieceBase):
    id: int
    author_id: int
    medium_id: int

    class Config:
        orm_mode = True

# Modelo de Author
class AuthorBase(BaseModel):
    name: str
    birth_date: Optional[datetime] = None
    death_date: Optional[datetime] = None
    nationality: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorInDB(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de Genre
class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreInDB(GenreBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de Style
class StyleBase(BaseModel):
    name: str

class StyleCreate(StyleBase):
    pass

class StyleInDB(StyleBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de Medium
class MediumBase(BaseModel):
    name: str

class MediumCreate(MediumBase):
    pass

class MediumInDB(MediumBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de CulturePeriod
class CulturePeriodBase(BaseModel):
    name: str

class CulturePeriodCreate(CulturePeriodBase):
    pass

class CulturePeriodInDB(CulturePeriodBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de Favorite
class FavoriteBase(BaseModel):
    created_at: datetime

class FavoriteCreate(FavoriteBase):
    archeopiece_id: str  # Usar String para MongoDB ID
    artpiece_id: int
    gallery_id: int
    user_id: int

class FavoriteInDB(FavoriteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Modelo de Like
class LikeBase(BaseModel):
    created_at: datetime

class LikeCreate(LikeBase):
    user_id: int
    gallery_id: int

class LikeInDB(LikeBase):
    id: int

    class Config:
        orm_mode = True

# Modelo de Comment
class CommentBase(BaseModel):
    content: str
    created_at: datetime

class CommentCreate(CommentBase):
    user_id: int
    gallery_id: int

class CommentInDB(CommentBase):
    id: int

    class Config:
        orm_mode = True
