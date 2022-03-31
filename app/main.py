from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.users import router as user
from src.routes.health import router as health
from config.openapi import tags_metadata
import os

app = FastAPI(
    title="WebServiceNetflix - Compte",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health)
app.include_router(user)