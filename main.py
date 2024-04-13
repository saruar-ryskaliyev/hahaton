# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import routers



app = FastAPI()


app.include_router(routers.router)


