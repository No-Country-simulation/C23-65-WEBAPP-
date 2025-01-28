from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional, List
from pydantic.config import ConfigDict

# MongoDB Models
class GalleryArtpieceInDB(BaseModel):
    id: str
    gallery_id: str
    artpiece_id: str
    note: str

    model_config = ConfigDict(from_attributes=True)

class ArtpieceStylesInDB(BaseModel):
    id: str
    style_id: str
    artpiece_id: str

    model_config = ConfigDict(from_attributes=True)

class ArtpieceGenresInDB(BaseModel):
    id: str
    artpiece_id: str
    genre_id: str

    model_config = ConfigDict(from_attributes=True)

class PieceImgInDB(BaseModel):
    id: str
    file: str
    name: str
    archeopiece_id: str
    artpiece_id: str

    model_config = ConfigDict(from_attributes=True)

class ProfileFollowingInDB(BaseModel):
    id: str
    from_profile_id: str
    to_profile_id: str

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

# MySQL Models
class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ProfileBase(BaseModel):
    bio: Optional[str] = None
    profile_picture: Optional[str] = None

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileInDB(ProfileBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class ProfileResponse(ProfileInDB):
    user: UserInDB

    model_config = ConfigDict(from_attributes=True)

class UserResponse(UserInDB):
    profile: Optional[ProfileInDB] = None

    model_config = ConfigDict(from_attributes=True)

class GalleryBase(BaseModel):
    image_url: str
    description: Optional[str] = None

class GalleryCreate(GalleryBase):
    owner_id: int

class GalleryInDB(GalleryBase):
    id: int
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

class AuthorBase(BaseModel):
    name: str
    birth_date: Optional[datetime] = None
    death_date: Optional[datetime] = None
    nationality: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorInDB(AuthorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreInDB(GenreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class StyleBase(BaseModel):
    name: str

class StyleCreate(StyleBase):
    pass

class StyleInDB(StyleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class MediumBase(BaseModel):
    name: str

class MediumCreate(MediumBase):
    pass

class MediumInDB(MediumBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CulturePeriodBase(BaseModel):
    name: str

class CulturePeriodCreate(CulturePeriodBase):
    pass

class CulturePeriodInDB(CulturePeriodBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class FavoriteBase(BaseModel):
    created_at: datetime

class FavoriteCreate(FavoriteBase):
    archeopiece_id: str
    artpiece_id: int
    gallery_id: int
    user_id: int

class FavoriteInDB(FavoriteBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LikeBase(BaseModel):
    created_at: datetime

class LikeCreate(LikeBase):
    user_id: int
    gallery_id: int

class LikeInDB(LikeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CommentBase(BaseModel):
    content: str
    created_at: datetime

class CommentCreate(CommentBase):
    user_id: int
    gallery_id: int

class CommentInDB(CommentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
