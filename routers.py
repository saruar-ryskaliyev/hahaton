from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db
from fastapi import HTTPException


router = APIRouter()

@router.post("/banks/", response_model=schemas.BankInDB)
def create_bank(bank: schemas.BankCreate, db: Session = Depends(get_db)):
    db_bank = models.Bank(name=bank.name)
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    return db_bank



@router.delete("/banks/{bank_id}/cards/{card_id}")
def delete_card(bank_id: int, card_id: int, db: Session = Depends(get_db)):
    db_card = db.query(models.BankCard).filter(models.BankCard.bank_id == bank_id).filter(models.BankCard.cardID == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    db.delete(db_card)
    db.commit()
    return {"message": "Card deleted"}


@router.get("/banks/{bank_id}", response_model=schemas.BankWithCards)
def read_bank(bank_id: int, db: Session = Depends(get_db)):
    db_bank = db.query(models.Bank).filter(models.Bank.id == bank_id).first()
    if db_bank is None:
        raise HTTPException(status_code=404, detail="Bank not found")
    # It's important to query for the bank cards here to make sure they are included in the response.
    db_bank.cards = db.query(models.BankCard).filter(models.BankCard.bank_id == bank_id).all()
    return db_bank

@router.put("/banks/{bank_id}", response_model=schemas.BankInDB)
def update_bank(bank_id: int, bank: schemas.BankCreate, db: Session = Depends(get_db)):
    db_bank = db.query(models.Bank).filter(models.Bank.id == bank_id).first()
    if db_bank is None:
        raise HTTPException(status_code=404, detail="Bank not found")
    db_bank.name = bank.name
    db.commit()
    db.refresh(db_bank)
    return db_bank


@router.post("/cards/", response_model=schemas.BankCardInDB)
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

@router.get("/cards/{card_id}", response_model=schemas.BankCardInDB)
def read_card(card_id: int, db: Session = Depends(get_db)):
    db_card = db.query(models.BankCard).filter(models.BankCard.cardID == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card

@router.delete("/cards/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db)):
    db_card = db.query(models.BankCard).filter(models.BankCard.cardID == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    db.delete(db_card)
    db.commit()
    return {"message": "Card deleted"}

@router.put("/cards/{card_id}", response_model=schemas.BankCardInDB)
def update_card(card_id: int, card: schemas.BankCardCreate, db: Session = Depends(get_db)):
    db_card = db.query(models.BankCard).filter(models.BankCard.cardID == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    db_card.card_type = card.card_type
    db_card.category = card.category
    db_card.special_offer = card.special_offer
    db.commit()
    db.refresh(db_card)
    return db_card