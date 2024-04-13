from sqlalchemy import Column, Integer, String, ForeignKey, PickleType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bank(Base):
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    cards = relationship("BankCard", back_populates="bank")

class BankCard(Base):
    __tablename__ = "bank_cards"

    cardID = Column(Integer, primary_key=True, index=True)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    card_type = Column(String)
    category = Column(PickleType)  # This will be used to store an array of strings
    special_offer = Column(PickleType)  # This will also store an array of strings

    bank = relationship("Bank", back_populates="cards")
