import pandas as pd
from datetime import datetime
import requests

class Transform():

  def __init__(self, data: requests.Response):
    self.data = data

  def transform_data(self):
    records = self.data['value']

    transformed_data = []
    for record in records:
      transformed_data.append({
        'ano_mes': record['AnoMes'],
        'quantidadePix': record['quantidadePix'],
        'valorPix': record['valorPix'],
        'quantidadeTED': record['quantidadeTED'],
        'valorTED': record['valorTED'],
        'quantidadeTEC': record['quantidadeTEC'],
        'valorTEC': record['valorTEC'],
        'quantidadeCheque': record['quantidadeCheque'],
        'valorCheque': record['valorCheque'],
        'quantidadeBoleto': record['quantidadeBoleto'],
        'valorBoleto': record['valorBoleto'],
        'quantidadeDOC': record['quantidadeDOC'],
        'valorDOC': record['valorDOC'],
        'timestamp': datetime.now()
      })

    df = pd.DataFrame(transformed_data)

    return df