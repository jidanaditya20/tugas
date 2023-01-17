total = 0
barang = []
harga = []

while True :
    print("""Daftar Barang\n
    1. Kue \t 6000
    2. Roti \t 6000
    3. Es teh \t 5000
    4. Kerupuk \t 2000
    5. Nasi goreng \t 8000
    6. Gorengan \t 1000
    """)

    kode = int(input("Masukkan kode barang :"))
    if kode == 1:
        barang.append('kue')
        harga.append(6000)
        total += 6000
    elif kode == 2 :
        barang.append('roti')
        harga.append(6000)
        total += 6000
    elif kode == 3 :
        barang.append('es teh')
        harga.append(5000)
        total += 5000
    elif kode == 4 :
        barang.append('kerupuk')
        harga.append(2000)
        total += 2000
    elif kode == 5 :
        barang.append('nasi goreng')
        harga.append (8000)     
        total += 8000
    elif kode == 6 :
        barang.append('gorengan')
        harga.append (1000)
        total += 1000
    else:
        print('kode tidak valid')

    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't' :
        print("")
        break

print('baranag yang dibeli :', barang)
print('harga barangnya :', harga)
print('total yang harus dibayar :', total, "\n")

uang = int(input("masukkan uang pembayaran : "))
if uang > total :
    print('kembaliannya :', uang - total)
elif uang == total :
    print('uang pas')
else:
    print("uangnya kurang", uang - total)

