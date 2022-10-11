from HitungWaktu import total_waktu
from Input import *

if jenis == "mobil":
    totalBayar = total_waktu * 5000
    
elif jenis == "motor":
    totalBayar = total_waktu * 2000

saldo -= totalBayar

if saldo < 0:
    print("Saldo tidak cukup")
    saldo += totalBayar

if saldo > 0:
    print("Pembayaran berhasil")

