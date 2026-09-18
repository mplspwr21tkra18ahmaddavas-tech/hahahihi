print("Masukkan 10 angka:")

angka = int(input("Masukkan angka ke-1: "))
terbesar = angka

for i in range(2, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka > terbesar:
        terbesar = angka

print("Bilangan terbesar adalah: " + str(terbesar))
