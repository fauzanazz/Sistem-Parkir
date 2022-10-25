import json

file_name = "emoney_data.json"

with open(file_name,"r") as data:
    data_emoney = json.load(data)

nim_awal = 19622227
nim_akhir = 19622312

for i in range(nim_awal,nim_akhir+1):
    data_emoney[f"{i}"] = {
        "saldo" : 100000
    }

with open(file_name,"w") as data:
    json.dump(data_emoney, data, indent = 2)

