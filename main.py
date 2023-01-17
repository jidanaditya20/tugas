angka1 = input("angka 1: ")
angka2 = input("angka 2: ")
try:
    total = int(angka1) + int(angka2)
    print(total)
except:
    print("Hasil error karena ada yang bukan angka")
else:
    print("Hasil adalah", total)
finally:
    print("Program selesai")
    
