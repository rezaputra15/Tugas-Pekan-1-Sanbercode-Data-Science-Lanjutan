import csv, json, pandas as pd

class tugas_json:
    def __init__(self):
        pass

    def csv_to_json(self):
        csvFile = open(csvFilePath, 'r', encoding='utf-8') 
        data = csv.reader(csvFile, delimiter=',') 
        next(data)
        list_provinsi = []
        for baris in data:
            provinsi = {}
            detail = {}
            provinsi['Provinsi'] = baris[1]
            detail['Pulau Bernama'] = baris[2]
            detail['Pulau Tak Bernama'] = baris[3]
            detail['Total'] = baris[4]
            provinsi['Detail'] = detail
            list_provinsi.append(provinsi)

        with open(jsonFilePath, 'w', encoding='utf-8') as write_file:
            json.dump(list_provinsi, write_file, indent = 4)

    def json_to_pandas(self):
        with open(jsonFile2, 'r', encoding='utf-8') as jsonF:
            data = json.load(jsonF)
            data_negara = pd.DataFrame(data)
        return print(data_negara)

csvFilePath = r'pulau_indonesia.csv'
jsonFilePath = r'Fachryza.json'
jsonFile2 = r'country_full.json'

tugas = tugas_json()
tugas.csv_to_json()
tugas.json_to_pandas()