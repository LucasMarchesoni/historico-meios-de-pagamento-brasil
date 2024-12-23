from extract.extract import Extract
from transform.transform import Transform
from load.load import Load

url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosMensalDA(AnoMes=@AnoMes)?@AnoMes='200401'&$top=10000&$format=json&$select=AnoMes,quantidadePix,valorPix,quantidadeTED,valorTED,quantidadeTEC,valorTEC,quantidadeCheque,valorCheque,quantidadeBoleto,valorBoleto,quantidadeDOC,valorDOC"

extract = Extract(url)

data = extract.response()

transform = Transform(data)

df = transform.transform_data()

load = Load(df, "historico_meios_de_pagamento.json")

load.load_to_postgres()