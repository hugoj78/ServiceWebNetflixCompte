from fastapi import APIRouter, Depends
from config.db import conn
from src.models.users import users
from src.schemas.users import User
from typing import List
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from sqlalchemy import func, select
from cryptography.fernet import Fernet
from fastapi_simple_security import api_key_security
from enum import Enum
from src.models.StatusEnum import StatusEnum

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)

@router.get(
    "",
    #dependencies=[Depends(api_key_security)],
    response_model=List[User],
    description="Get a list of all users",
)
def get_users():
    return conn.execute(users.select()).fetchall()

@router.get(
    "/{id}",
    #dependencies=[Depends(api_key_security)],
    response_model=User,
    description="Get a single user by Id",
)
def get_users(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@router.post(
    "",
    #dependencies=[Depends(api_key_security)],
    response_model=User, 
    description="Create a new User")
def create_user(user: User):
    new_user = {
        "name": user.name, 
        "email": user.email, 
        "password": user.password, 
        "admin": user.admin, 
        "status": user.status,
        "adress": user.adress,
        "country": user.country
        }
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@router.put(
    "/{id}",
    #dependencies=[Depends(api_key_security)],
    response_model=User, 
    description="Update a user by Id"
)
def update_user(user: User, id: int):
    conn.execute(
        users.update()
        .values(
            id=user.id, 
            name=user.name, 
            email=user.email, 
            password=user.password, 
            admin=user.admin, 
            status=user.status,
            adress=user.adress,
            country=user.country
        )
        .where(users.c.id == id)
    )
    return conn.execute(users.select().where(users.c.id == id)).first()

@router.delete(
    "/{id}",
    #dependencies=[Depends(api_key_security)],
    status_code=HTTP_200_OK
)
def delete_user(id: int):
    conn.execute(
        users.update()
        .values( 
            status=StatusEnum.SUSPENDU.value
        )
        .where(users.c.id == id)
    )

    return conn.execute(users.select().where(users.c.id == id)).first() 

# Delete classique : cependant on ne veut pas supprimer en base mais changer le statut du user par SUSPENDU
# @router.delete(
#     "/{id}",
#     #dependencies=[Depends(api_key_security)],
#     status_code=HTTP_204_NO_CONTENT
# )
# def delete_user(id: int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select().where(users.c.id == id)).first()