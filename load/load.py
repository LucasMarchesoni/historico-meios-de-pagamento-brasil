import os
import pandas as pd
from tinydb import TinyDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Base, HistoricoMeioPagamentos
from database.credentials import Credentials
from log.logging import Logging

class Load():

  def __init__(self, data: pd.DataFrame, db_name: str):
    self.data = data
    self.db_name = db_name
    self.log = Logging()

  def load_to_nosql_db(self):
    if not os.path.exists('data'):
      os.makedirs('data')

    db_path = os.path.join('data', self.db_name)
    db = TinyDB(db_path)
    data_dict = self.data.to_dict(orient='records')
    db.insert_multiple(data_dict)
    self.log.get_logger().info("Data saved successfully on tinydb")

  def load_to_postgres(self):
    credentials = Credentials()
    url = credentials.database_url()
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    self.create_table(engine)

    self.save_on_postgres(session, self.data)

  def create_table(self, engine):
    Base.metadata.create_all(engine)
    self.log.get_logger().info("Table created successfully")

  def save_on_postgres(self, session, data):
    session.query(HistoricoMeioPagamentos).delete()
    self.log.get_logger().info("Table registers deleted successfully")
    session.commit()

    for _, row in data.iterrows():
      new_register = HistoricoMeioPagamentos(
        ano_mes=row['ano_mes'],
        quantidadePix=row['quantidadePix'],
        valorPix=row['valorPix'],
        quantidadeTED=row['quantidadeTED'],
        valorTED=row['valorTED'],
        quantidadeTEC=row['quantidadeTEC'],
        valorTEC=row['valorTEC'],
        quantidadeCheque=row['quantidadeCheque'],
        valorCheque=row['valorCheque'],
        quantidadeBoleto=row['quantidadeBoleto'],
        valorBoleto=row['valorBoleto'],
        quantidadeDOC=row['quantidadeDOC'],
        valorDOC=row['valorDOC'],
        timestamp=row['timestamp']
      )

      session.add(new_register)

    session.commit()
    session.close()
    self.log.get_logger().info("Data saved successfully on postgres")