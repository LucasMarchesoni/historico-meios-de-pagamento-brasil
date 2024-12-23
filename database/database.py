from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class HistoricoMeioPagamentos(Base):
  __tablename__ = "historico_meio_pagamentos"

  id = Column(Integer, primary_key=True, autoincrement=True)
  ano_mes = Column(String, nullable=False)
  quantidadePix = Column(Integer, nullable=False)
  valorPix = Column(Float, nullable=False)
  quantidadeTED = Column(Integer, nullable=False)
  valorTED = Column(Float, nullable=False)
  quantidadeTEC = Column(Integer, nullable=False)
  valorTEC = Column(Float, nullable=False)
  quantidadeCheque = Column(Integer, nullable=False)
  valorCheque = Column(Float, nullable=False)
  quantidadeBoleto = Column(Integer, nullable=False)
  valorBoleto = Column(Float, nullable=False)
  quantidadeDOC = Column(Integer, nullable=False)
  valorDOC = Column(Float, nullable=False)
  timestamp = Column(DateTime, default=datetime.now(), nullable=False)