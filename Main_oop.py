import datetime

file = open("data_pengguna.txt","a")
class Orang:

    def __init__(self, jenis_kendaraan, no_id, waktu_masuk):
        self.jenis_kendaraan = jenis_kendaraan
        self.no_id = no_id
        self.waktu_masuk = waktu_masuk

no_id = input("No ID E-Money \t: ")
jenis_kendaraan = input("Jenis Kendaraan (Mobil/Motor) \t: ")
waktu_masuk = datetime.datetime.now()

orang1 = Orang(jenis_kendaraan, no_id, datetime.datetime.now())

file.write(f"\n{orang1.no_id} : {orang1.jenis_kendaraan} : {orang1.waktu_masuk}")

