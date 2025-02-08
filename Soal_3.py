saldoawal = 200000000
saldotarget = 400000000
bungatahunan = 0.1
tahun = 0
saldoakhir = saldoawal
while saldoakhir <= saldotarget:
    saldoakhir += saldoakhir * bungatahunan
    tahun += 1
print(f"Waktu yang dibutuhkan agar uang menjadi minimal {saldotarget} adalah {tahun} tahun.")
print(f"Saldo akhir di tahun ke-{tahun} adalah sekitar {saldoakhir} rupiah.")