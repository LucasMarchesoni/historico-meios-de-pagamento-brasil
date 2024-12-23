import os
from dotenv import load_dotenv

load_dotenv()

class Credentials():

  def __init__(self):
    pass

  def database_url(self):
    db_url = os.getenv("DB_URL")

    return db_url