from HitungWaktu import total_waktu
from Input import jenis, saldo

if jenis == "mobil":
    totalBayar = total_waktu * 5000
    
elif jenis == "motor":
    totalBayar = total_waktu * 2000

if saldo < totalBayar:
    print("Saldo tidak cukup")
    

if saldo > totalBayar:
    print("Pembayaran berhasil")
    saldo -= totalBayar
