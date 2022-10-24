import datetime
import os

def write():
    with open("data_masuk.txt", "a") as data_masuk_w:
                                
        no_id = input("Masukkan No ID E-Money   : ")
        jenis_kendaraan = input("Masukkan Jenis Kendaraan : ") # 1=mobil ; 2=motor
        waktu_masuk = str(datetime.datetime.now()) ; waktu_masuk = waktu_masuk[0:19]

        ada = False
        
        with open("data_masuk.txt", "r") as data_masuk_r:
            for baris in data_masuk_r:
                if baris[0:8] == no_id:
                    ada = True
        
        if ada:
            pass

        else:
            data_masuk_w.write(f"\n{no_id}_{jenis_kendaraan}_{waktu_masuk}")

def read():
    with open("data_masuk.txt", "r") as data_masuk_r:
        
        no_id = input("Masukkan No ID E-Money : ")

        tidak_ada = True

        for baris in data_masuk_r:
            if baris[0:8] == no_id:

                tidak_ada = False

                no_id = baris[0:8]
                
                if baris[9] == 1:
                    jenis_kendaraan = "Mobil"
                else:
                    jenis_kendaraan = "Motor"
                
                waktu_masuk = datetime.datetime(int(baris[11:15]), int(baris[16:18]), int(baris[19:21]), int(baris[22:24]), int(baris[25:27]), int(baris[28:30]))

                waktu_keluar = str(datetime.datetime.now())
                waktu_keluar = datetime.datetime(int(waktu_keluar[0:4]), int(waktu_keluar[5:7]), int(waktu_keluar[8:10]), int(waktu_keluar[11:13]), int(waktu_keluar[14:16]), int(waktu_keluar[17:19]))
                
                lama_parkir = waktu_keluar - waktu_masuk

                print(f"Id     : {no_id}")
                print(f"Jenis  : {jenis_kendaraan}")
                print(f"Masuk  : {waktu_masuk}")
                print(f"Keluar : {waktu_keluar}")
                print(f"Durasi : {lama_parkir}")
        
        if tidak_ada:
            print("Silakan coba lagi.")
            enter = input()
            os.system("cls")
            read()

portal = int(input("Portal Masuk(1)/ Portal Keluar(2) : "))

os.system("cls")

if portal == 1:
    write()
elif portal == 2:
    read()


