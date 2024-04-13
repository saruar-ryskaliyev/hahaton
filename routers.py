from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List


import models, schemas

from database import SessionLocal, get_db  # Import your database session setup

router = APIRouter()


@router.post("/banks/", response_model=schemas.Bank)
def create_bank(bank: schemas.BankCreate, db: Session = Depends(get_db)):
    db_bank = models.Bank(name=bank.name)
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    return db_bank


@router.post("/cards/", response_model=schemas.BankCard)
def create_card(card: schemas.BankCardCreate, db: Session = Depends(get_db)):
    db_card = models.BankCard(
        bank_id=card.bank_id,
        card_type=card.card_type,
        category=card.category,
        special_offer=card.special_offer
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card
