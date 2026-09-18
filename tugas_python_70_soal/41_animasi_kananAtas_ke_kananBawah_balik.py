import time

tinggi = 10
lebar = 20

for posisi in range(tinggi):
    for i in range(tinggi):
        if i == posisi:
            print(" " * (lebar - 1) + "0")
        else:
            print()
    time.sleep(0.2)
    if posisi != tinggi - 1:
        for k in range(3):
            print()


for posisi in range(tinggi - 1, -1, -1):
    for i in range(tinggi):
        if i == posisi:
            print(" " * (lebar - 1) + "0")
        else:
            print()
    time.sleep(0.2)
    if posisi != 0:
        for k in range(3):
            print()
