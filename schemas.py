from typing import List, Optional
from pydantic import BaseModel

class BankBase(BaseModel):
    name: str

class BankCreate(BankBase):
    pass

class Bank(BankBase):
    id: int
    cards: List["BankCard"] = []

    class Config:
        orm_mode = True

class BankCardBase(BaseModel):
    card_type: str
    category: Optional[List[str]] = None
    special_offer: Optional[List[str]] = None

class BankCardCreate(BankCardBase):
    bank_id: int

class BankCard(BankCardBase):
    cardID: int
    bank: Bank

    class Config:
        orm_mode = True

Bank.update_forward_refs()  # This is used to resolve forward references
