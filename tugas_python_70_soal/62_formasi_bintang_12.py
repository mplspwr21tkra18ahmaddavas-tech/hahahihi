# Soal: Tampilkan formasi bintang 12
# Pola:
# 00000000000
# **********0
# **********0
# **********0
# **********0
# Penjelasan: 0 di atas dan kanan
# Asumsi: Kebalikan formasi 11

print("0" * 11)
for i in range(4):
    print("*" * 10 + "0")
