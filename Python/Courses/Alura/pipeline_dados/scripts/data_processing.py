import json
import csv

class Data:
    def __init__(self, path, type_data):
        self.path = path
        self.type_data = type_data
        self.data = self.reading_data()
        self.column_name = self.get_columns()
 
 
    def reading_json(self):
    
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        
        return dados_json


    def reading_csv(self):    
        
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv


    def reading_data(self):
        dados = []

        if self.type_data == 'json':
            dados = self.reading_json()
        elif self.type_data == 'csv':
            dados = self.reading_csv()
        else:
            print('Tipo de arquivo não suportado')
        
        return dados


    def get_columns(self):
        return list(self.data[-1].keys())


    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.data:
                dict_temp = {}
                for old_key, value in old_dict.items():
                        dict_temp[key_mapping[old_key]] = value
                new_dados.append(dict_temp)

        self.data = new_dados
        self.column_name = self.get_columns()


    def size_data(dados):
        return len(dados)


    def join_data(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA)
        combined_list.extend(dadosB)

        return combined_list


    def transform_data_table(dados, nome_colunas):
        dados_combinados_tabela = []
        for row in dados:
            linha = []
            for coluna in nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
            
        return dados_combinados_tabela


    def save_data(dados, path):
        with open(path, 'w') as file:
            writer = csv.writer(file)
            for row in dados:
                writer.writerows(dados)

   