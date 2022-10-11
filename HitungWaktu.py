from Input import *

if bulan_keluar < bulan_masuk:
    tahun_keluar -= 1
    bulan_keluar += 12
    
if hari_keluar < hari_masuk:
    bulan_keluar -= 1
    hari_keluar += 30
    
if jam_keluar < jam_masuk:
    hari_keluar -= 1
    jam_keluar += 24
    
if menit_keluar < menit_masuk:
    jam_keluar -= 1
    menit_keluar += 60
    
if detik_keluar < detik_masuk:
    menit_keluar -= 1
    detik_keluar += 60

total_tahun = (tahun_keluar - tahun_masuk)
total_bulan = (bulan_keluar - bulan_masuk)
total_hari = (hari_keluar - hari_masuk)
total_jam = (jam_keluar - jam_masuk)
total_menit = (menit_keluar - menit_masuk)
total_detik = (detik_keluar - detik_masuk)

total_waktu = total_tahun*8640 + total_bulan*720 + total_hari*24 +total_jam #dalam jam