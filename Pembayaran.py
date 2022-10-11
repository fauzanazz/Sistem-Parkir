from HitungWaktu import total_waktu
from Input import *

if jenis == "Mobil":
    totalBayar = total_waktu * 5000
    
elif jenis == "Motor":
    totalBayar = total_waktu * 2000

saldo -= totalBayar

if saldo < 0:
    print("Saldo tidak cukup")
    saldo += totalBayar

if saldo > 0:
    print("Pembayaran berhasil")

