# schemas.py

from typing import List, Optional
from pydantic import BaseModel

# Use this as a sub-model for responses, to avoid recursion.
class BankWithCards(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BankCardBase(BaseModel):
    card_type: str
    category: Optional[List[str]] = None
    special_offer: Optional[List[str]] = None

class BankCardCreate(BankCardBase):
    bank_id: int

class BankCardInDB(BankCardBase):
    cardID: int
    bank: BankWithCards  # Use the non-recursive model here

    class Config:
        orm_mode = True

class BankBase(BaseModel):
    name: str

class BankCreate(BankBase):
    pass

class BankInDB(BaseModel):  # This model is for responses
    id: int
    name: str

    class Config:
        orm_mode = True


class BankCardForBank(BaseModel):
    cardID: int
    card_type: str
    category: Optional[List[str]] = None
    special_offer: Optional[List[str]] = None

    class Config:
        orm_mode = True

class BankWithCards(BaseModel):  # This model is for responses
    id: int
    name: str
    cards: List[BankCardForBank] = []

    class Config:
        orm_mode = True