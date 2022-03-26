from typing import Optional
from pydantic import BaseModel
from src.models.StatusEnum import StatusEnum

class User(BaseModel):
    id: Optional[int]
    admin: bool
    name: str
    email: str
    password: str
    status: StatusEnum
    location: str