# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke uppercase

salam = "bro!"
print("Normal = ", salam)

# merubah ke uppercase
salam = salam.upper()
print("Upper = ", salam)

# merubah ke lowercase
alay = "Aku kEce AbiEEzzzz"
print("normal = ", alay)
alay = alay.lower()
print("lower = ", alay)

# pengecekan lowercase
salam = "selamat pagi"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha()     <--- untuk mengecek apakah semuanya huruf
# isalnum()     <--- huruf dan angka
# isdecimal()   <--- angka saja
# isspace()     <--- space, tab, newline \n
# istitle()     <--- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## mengecek component startswith() endswith()
cek_start = "Mau kemana kita pagi ini?".startswith("Mau")
print("Start = " + str(cek_start))
cek_end = "Mau kemana kita pagi ini?".endswith("?")
print("Start = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ["Niko", "Rahmadi", "Wiharto"]
print("\n",  pisah)

gabung = " ".join(pisah)
print(gabung)

gabung = "-".join(pisah)
print(gabung)

pisah_lagi = gabung.split("-")
print(pisah_lagi)

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'") # by default akan diberi jarak dengan space

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

center = "center".center(20, ":") # bisa ditentukan pemisahnya dengan yang lain
print("'" + center + "'")

# kebalikan dari alokasi adjustment strip()
center = center.strip(":")
print("'" + center + "'")
kanan = kanan.strip()
print(kanan)



