#=============================================================== 
# data banyak hari pada bulan
# data tahun yang kabisat

bulan30 = [4, 6, 9, 11]           # bulan yang harinya 30
bulan31 = [1, 3, 5, 7, 8, 10 ,12] # bulan yang harinys 31

list_kabisat = [] # list tahun kabisat
for i in range(1, 10000):
    kabisat = True
    if i % 4 != 0:
        kabisat = False
    if i % 100 == 0 and i % 400 != 0:
        kabisat = False
    if kabisat:
        list_kabisat.append(i)
    
#=============================================================== 
# input waktu masuk
 
print("\n============= [PARKING] =============")
print("             PINTU MASUK           \n")
    
tahun_masuk     = int(input("Tahun masuk     : "))
bulan_masuk     = int(input("Bulan masuk     : "))
tanggal_masuk   = int(input("Tanggal masuk   : "))
jam_masuk       = int(input("Jam masuk       : "))
menit_masuk     = int(input("Menit masuk     : "))
detik_masuk     = int(input("Detik masuk     : "))
jenis_kendaraan =     input("Jenis kendaraan : ")

print("\n=====================================")

#=============================================================== 
# mengkonvesi waktu masuk mke satuan detik

waktu_masuk = 0 # waktu masuk dalam satuan detik

for bulan in range(1, bulan_masuk):
    if bulan in bulan30:
        waktu_masuk += 2_592_000 
    elif bulan in bulan31:
        waktu_masuk += 2_678_400
    else:
        if tahun_masuk in list_kabisat:
            waktu_masuk += 2_505_600
        else:
            waktu_masuk += 2_419_200

if tanggal_masuk > 1:
    waktu_masuk += (tanggal_masuk-1)*86_400

waktu_masuk += jam_masuk*3600 + menit_masuk*60 + detik_masuk

#=============================================================== 
# input waktu keluar

print("\n\n============= [PARKING] =============")
print("            PINTU KELUAR             \n")

tahun_keluar   = int(input("Tahun keluar    : "))
bulan_keluar   = int(input("Bulan keluar    : "))
tanggal_keluar = int(input("Tanggal keluar  : "))
jam_keluar     = int(input("Jam keluar      : "))
menit_keluar   = int(input("Menit keluar    : "))
detik_keluar   = int(input("Detik keluar    : "))
saldo_emoney   = int(input("Saldo E-Money   : "))

print("\n=====================================")

#=============================================================== 
# mengkonversi waktu keluar ke satuan detik

waktu_keluar = 0 # waktu keluar dalam satuan detik

for tahun in range(tahun_masuk, tahun_keluar):
    if tahun in list_kabisat:
        waktu_keluar += 31_622_400
    else:
        waktu_keluar += 31_536_000 
    
for bulan in range(1, bulan_keluar):
    if bulan in bulan30:
        waktu_keluar += 2_592_000
    elif bulan in bulan31:
        waktu_keluar += 2_678_400
    else:
        if tahun_keluar in list_kabisat:
            waktu_keluar += 2_505_600
        else:
            waktu_keluar += 2_419_200

if tanggal_keluar > 1:
    waktu_keluar += (tanggal_keluar-1)*86_400

waktu_keluar += jam_keluar*3600 + menit_keluar*60 + detik_keluar

#=============================================================== 
# menghitung durasi parkir

durasi = waktu_keluar - waktu_masuk # (dalam satuan detik)

durasi_jam = durasi // 3600
durasi_menit = durasi % 3600 // 60
durasi_detik = durasi % 3600 % 60

#===============================================================
# menghitung tarif parkir

if jenis_kendaraan == "mobil":
    tarif_1jam = 5000
    tarif_berikutnya = 4000
    tarif_inap = 50000 
else: # jenis_kendaraan == "motor":
    tarif_1jam = 3000
    tarif_berikutnya = 2000
    tarif_inap = 40000

if durasi > 86_400: # masuk ke tarif inap (sehari = 86400 detik)
    tarif = (durasi_jam//24 + 1)*tarif_inap
elif durasi_jam == 0 and durasi_menit < 5: 
    tarif = 0 # di bawah 5 menit gratis
elif durasi_jam == 0:
    tarif = tarif_1jam # di bawah 1 jam masuk tarif jam pertama
else:
    tarif = tarif_1jam + tarif_berikutnya*durasi_jam

#=============================================================== 
# mengecek saldo E-Money

if saldo_emoney >= tarif:
    saldo_cukup = True
    saldo_emoney = saldo_emoney-tarif
else:
    saldo_cukup = False

#=============================================================== 
# reformat angka 

# untuk cetak resi nanti agar tampak lebih rapih karena ada 
# angka nol di depan angka yang hanya satu digit
#
# contohnya angka 7 menjadi 07 saat dicetak

if tanggal_masuk < 10:
    tanggal_masuk = f"0{tanggal_masuk}"

if bulan_masuk < 10:
    bulan_masuk = f"0{bulan_masuk}"

if jam_masuk < 10:
    jam_masuk = f"0{jam_masuk}"

if menit_masuk < 10:
    menit_masuk = f"0{menit_masuk}"

if detik_masuk < 10:
    detik_masuk = f"0{detik_masuk}"

if tanggal_keluar < 10:
    tanggal_keluar = f"0{tanggal_keluar}"

if bulan_keluar < 10:
    bulan_keluar = f"0{bulan_keluar}"

if jam_keluar < 10:
    jam_keluar = f"0{jam_keluar}"

if menit_keluar < 10:
    menit_keluar = f"0{menit_keluar}"

if detik_keluar < 10:
    detik_keluar = f"0{detik_keluar}"

#===============================================================
# cetak tarif parkir

print("\n\n============= [PARKING] =============")
print("")
print("TARIF PARKIR")
print("")
print("*Mobil")
print("Rp 5.000 / Jam pertama")
print("Rp 4.000 / Jam berikutnya")
print("")
print("*Motor")
print("Rp 3.000 / Jam pertama")
print("Rp 2.000 / Jam berikutnyaa")
print("")
print("TARIF INAP")
print("")
print("*Mobil : Rp 50.000 / Hari")
print("*Motor : Rp 40.000 / Hari")
print("")
print("=====================================")

#===============================================================
# cetak resi

if durasi < 0 or tahun_keluar < tahun_masuk: 
    # data tidak valid karena durasi parkir negatif

    print("\n\n============= [PARKING] =============")
    print("")
    print("Data yang anda masukkan tidak valid.")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("=====================================")

elif saldo_cukup:
    # output jika saldo cukup

    print("\n\n============= [PARKING] =============")
    print("            SELAMAT JALAN           \n")
    print(f"Jenis kendaraan : {jenis_kendaraan}")
    print(f"Waktu masuk     : {tanggal_masuk}/{bulan_masuk}/{tahun_masuk} {jam_masuk}:{menit_masuk}:{detik_masuk}")
    print(f"Waktu keluar    : {tanggal_keluar}/{bulan_keluar}/{tahun_keluar} {jam_keluar}:{menit_keluar}:{detik_keluar}")
    print(f"Durasi          : {durasi_jam}j {durasi_menit}m {durasi_detik}d")
    print(f"Tarif           : {tarif}")
    print(f"Sisa saldo      : {saldo_emoney}")
    print("")
    print("=====================================")

else:
    # output jika saldo tidak cukup

    print("\n\n============= [PARKING] =============")
    print("")
    print("Saldo anda tidak cukup.")
    print(f"Tarif : {tarif}")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("=====================================")