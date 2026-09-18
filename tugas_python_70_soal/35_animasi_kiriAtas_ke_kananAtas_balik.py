import time

lebar = 20

for posisi in range(lebar):
    baris = ""
    for i in range(lebar):
        if i == posisi:
            baris = baris + "0"
        else:
            baris = baris + " "
    print(baris, end="\r")
    time.sleep(0.1)
print()

for posisi in range(lebar - 1, -1, -1):
    baris = ""
    for i in range(lebar):
        if i == posisi:
            baris = baris + "0"
        else:
            baris = baris + " "
    print(baris, end="\r")
    time.sleep(0.1)
print()
