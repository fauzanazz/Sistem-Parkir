import os ; import json ; import datetime
from sre_parse import State ; import time

file_name = "local_data.json"
file_emoney = "emoney_data.json"

with open(file_name, "r") as data:
        data_pengguna = json.load(data)

with open(file_emoney, "r") as data_valid:
        data_emoney = json.load(data_valid)

def cls():
    os.system("cls")

def durasi(no_id):

    wm = data_pengguna[f"{no_id}"]["waktu masuk"]
    wm = datetime.datetime(int(wm[0:4]), int(wm[5:7]), int(wm[8:10]), int(wm[11:13]), int(wm[14:16]), int(wm[17:19]))
    
    global wk

    wk = str(datetime.datetime.now())
    wk = datetime.datetime(int(wk[0:4]), int(wk[5:7]), int(wk[8:10]), int(wk[11:13]), int(wk[14:16]), int(wk[17:19]))
    
    return wk-wm

def tarif(lama_parkir, jenis_kendaraan):

    if jenis_kendaraan == "mobil":
        tarif_1jam = 5000
        tarif_berikutnya = 4000
    else:
        tarif_1jam = 3000
        tarif_berikutnya = 2000
        
    lama_parkir = lama_parkir.total_seconds()

    jam_parkir = lama_parkir//3600

    menit_parkir = lama_parkir%3600//60

    if jam_parkir == 0 and menit_parkir < 5:
        return 0
    elif jam_parkir == 0:
        return tarif_1jam
    else:
        return tarif_1jam + tarif_berikutnya*jam_parkir

def valid(no_id):

    if no_id not in data_emoney.keys():
        return False
    else:
        return True

def sudah_terpakai(no_id):

    if no_id in data_pengguna.keys():
        return True
    else:
        return False

def masuk(no_id, jenis_kendaraan):

    # no_id = input("Masukkan No ID E-Money   : ")

    print(no_id)
    print(type(no_id))

    print(jenis_kendaraan)
    print(type(jenis_kendaraan))

    # if not sudah_terpakai(no_id) and valid(no_id):

    jenis_kendaraan = jenis_kendaraan.lower()

    waktu_masuk = str(datetime.datetime.now()) ; waktu_masuk = waktu_masuk[0:19]

    data_pengguna[f"{no_id}"] = {
        "jenis kendaraan": jenis_kendaraan, 
        "waktu masuk": waktu_masuk
    }

    with open(file_name, "w") as data:
        json.dump(data_pengguna, data, indent = 2)

def keluar(no_id): 
   
    lama_parkir = durasi(no_id)
    jenis_kendaraan = data_pengguna[f"{no_id}"]["jenis kendaraan"]
    waktu_masuk = data_pengguna[f"{no_id}"]["waktu masuk"]
    waktu_keluar = wk

    tarif_parkir = int(tarif(lama_parkir, jenis_kendaraan))

    if  data_emoney[f"{no_id}"]["saldo"] >= tarif_parkir:

        sisa_saldo = data_emoney[f"{no_id}"]["saldo"] - tarif_parkir

        data_emoney[f"{no_id}"]["saldo"] = sisa_saldo

        with open(file_emoney, "w") as data_valid:
            json.dump(data_emoney, data_valid, indent = 2)

        cls()

        print("============= [PARKING] ==============")
        print("")
        print(f"Nomor Id        : {no_id}")
        print(f"Jenis kendaraan : {jenis_kendaraan}")
        print(f"Waktu masuk     : {waktu_masuk}")
        print(f"Waktu keluar    : {waktu_keluar}")
        print(f"Durasi          : {lama_parkir}")
        print(f"Tarif           : {tarif_parkir}")
        print(f"Sisa saldo      : {sisa_saldo}")
        print("")
        print("======================================")

        del data_pengguna[f"{no_id}"]

        with open(file_name, "w") as data:
            json.dump(data_pengguna, data, indent = 2)
    
    else:
        print("Maaf saldo anda tidak cukup")
        print(tarif_parkir)
        
