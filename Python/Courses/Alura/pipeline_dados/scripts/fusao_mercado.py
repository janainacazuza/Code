import json

path_json = 'data_raw/dados_empresaA.json'

with open(path_json, 'r') as file:
    dados_json = json.load(file)

print(dados_json[0])