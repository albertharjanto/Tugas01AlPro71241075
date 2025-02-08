hargaemaspergram1 = 650000
hargaemaspergram2 = 685000
hargaemaspergram3 = 715000
hargaemas1 = hargaemaspergram1 * 25
hargaemas2 = hargaemaspergram2 * 25
hargaemas3 = hargaemaspergram2 * 15
hargaemas4 = hargaemaspergram3 * 40
modal1 = hargaemas1
modal2 = hargaemas1 + hargaemas3
keuntungan1 = hargaemas2 - modal1
keuntungan2 = hargaemas4 - modal2
persen1 = (keuntungan1/modal1) * 100
persen2 = (keuntungan2/modal2) * 100
print("Pembelian pertama:")
print("Keuntungan Gerard adalah Rp.", keuntungan1)
print (f"Keuntungan Gerard dalam persen adalah {round(persen1,2)} %")
print("Pembelian kedua:")
print("Keuntungan Gerard adalah Rp.", keuntungan2)
print(f"Keuntungan Gerard dalam persen adalah {round(persen2,2)} %")