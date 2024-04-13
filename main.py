# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

import routers

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(routers.router)


