import json ; import datetime ; import os

file_name = "data.json"

with open(file_name, "r") as data:
        data_pengguna = json.load(data)

def cls():
    os.system("cls")

def durasi(no_id):

    wm = data_pengguna[f"{no_id}"][0]["waktu masuk"]
    wm = datetime.datetime(int(wm[0:4]), int(wm[5:7]), int(wm[8:10]), int(wm[11:13]), int(wm[14:16]), int(wm[17:19]))

    wk = str(datetime.datetime.now())
    wk = datetime.datetime(int(wk[0:4]), int(wk[5:7]), int(wk[8:10]), int(wk[11:13]), int(wk[14:16]), int(wk[17:19]))

    with open(file_name, "w") as data:
        data_pengguna[f"{no_id}"][0]["waktu keluar"] = wk

    return str(wk-wm)

def check(no_id):

    file_name = "data.json"

    if no_id in data_pengguna.keys():
        return True
    else:
        return False

def masuk():

    no_id = input("Masukkan No ID E-Money   : ")

    while check(no_id):
        cls()
        print("E-Money Card kamu sudah terpakai, silakan gunakan yang lain")
        no_id = input("Masukkan No ID E-Money   : ")

    jenis_kendaraan = input("Masukkan Jenis Kendaraan : ").lower() # 1=mobil ; 2=motor
    waktu_masuk = str(datetime.datetime.now()) ; waktu_masuk = waktu_masuk[0:19]

    data_pengguna[f"{no_id}"] = {
        "jenis kendaraan": jenis_kendaraan, 
        "waktu masuk": waktu_masuk
    }

    with open(file_name, "w") as data:
        json.dump(data_pengguna, data, indent = 2)

def keluar():

    no_id = input("Masukkan No ID E-Money   : ")

    while check(no_id) == False:
        cls()
        print("E-Money Card kamu tidak terdaftar, silakan gunakan yang lain")
        no_id = input("Masukkan No ID E-Money   : ")
    
    lama_parkir = durasi(no_id)
    jenis_kendaraan = data_pengguna[f"{no_id}"][0]["jenis kendaraan"]
    waktu_masuk = data_pengguna[f"{no_id}"][0]["waktu masuk"]
    waktu_keluar = data_pengguna[f"{no_id}"][0]["waktu keluar"]

    print(f"Id     : {no_id}")
    print(f"Jenis  : {jenis_kendaraan}")
    print(f"Masuk  : {waktu_masuk}")
    print(f"Keluar : {waktu_keluar}")
    print(f"Durasi : {lama_parkir}")


    del data_pengguna[f"{no_id}"]
 
    with open(file_name, "w") as data:
        json.dump(data_pengguna, data, indent = 2)

cls()
portal = int(input('''
----------------------
Masuk [0] | Keluar [1]
----------------------\n
'''))

if portal:
    cls()
    keluar()
else:
    cls()
    masuk()