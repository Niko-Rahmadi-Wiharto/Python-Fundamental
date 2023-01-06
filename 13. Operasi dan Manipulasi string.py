# Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Niko"
nama_tengah = "Rahmadi"
nama_akhir = "Wiharto"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string

panjang = len(nama_lengkap)
print("panjang karakternya : ", panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di data string

d = 'to'
status = d in nama_lengkap # case sensitive dan bisa match dengan lebih dari satu karakter
print("'" + d + "'" + " ada di  " + nama_lengkap + " = " + str(status))

d = 'rr'
status = d not in nama_lengkap
print("'" + d + "'" + " tidak ada di  " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " +nama_lengkap[0])
print("index ke-1 : " +nama_lengkap[1])
print("index ke-2 : " +nama_lengkap[2])
print("index ke-3 : " +nama_lengkap[3])
print("index ke-4 : " +nama_lengkap[-4])

print("\nindex ke-[0,3] : " + nama_lengkap[0:4])
print("\nindex ke-[0,3] : " + nama_lengkap[3:20])

# item paling kecil
print("paling kecil : " + min(nama_lengkap) + " dengan ASCII code " + str(ord(min(nama_lengkap))))

# item paling besar
print("paling besar : " + max(nama_lengkap) + " dengan ASCII code " + str(ord(max(nama_lengkap))))

ascii_code = ord(" ")
print("ASCII code untuk space adalah ", str(ascii_code))
ascii_code = ord("t")
print("ASCII code untuk space adalah ", str(ascii_code))
data = 200
print("char untuk ASCII 200 adalah " + chr(data)) # mencari character dari ASCII code

# 4. Operator dalam bentuk method

data = "Saya suka belajar coding"
jumlah = data.count("o")
print("Jumlah o pada kata '" + data + "' adalah " + str(jumlah))