# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal



app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}



