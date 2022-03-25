from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, Boolean, Enum
from config.db import meta, engine
from src.models.StatusEnum import StatusEnum

users = Table(
    "user",
    meta,
    Column("id", Integer, primary_key=True),
    Column("admin", Boolean),
    Column("name", String(45)),
    Column("email", Text, unique=True),
    Column("password", Text),
    Column("status", Enum(StatusEnum)),
)

meta.create_all(engine)