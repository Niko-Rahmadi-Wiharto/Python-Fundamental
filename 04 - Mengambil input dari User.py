# Input data dari User

data = input("Masukan data: ")

print("Data yang diinput user = ", data, ", tipe = ", type(data))

# Jika ingin mengambil int, maka
angka_int = int(input("Masukan angka: "))
angka_float = float(input("Masukan angka: "))

print("Data = ", angka_float, ", tipe = ", type(angka_float))

# input data untuk data boolean
biner = bool(int(input("Masukan nilai boolean : ")))
print("Data = ", biner, ", tipe = ", type(biner))