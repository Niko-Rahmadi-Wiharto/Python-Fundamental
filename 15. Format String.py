# Format string

# contoh generic
# string
nama = "Muhammad"
format_str = f"Halo {nama}, apa kabar?"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka sekarang adalah {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +15
formar_minus = f"minus = {angka_minus:+d}"
formar_plus = f"plus = {angka_plus:+d}"
print(formar_minus)
print(formar_plus)


# bilangan dengan ordo ribuan
angka = 20000000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.9393
format_str = f"desimal = {angka:.3f}"
print(format_str)

# bilangan desimal
angka = 2005.9393
format_str = f"desimal = {angka:10.3f}"
print(format_str)

# memformat persen
persentase = 0.045
formatt_persen = f"persen = {persentase:.2%}"
print(formatt_persen)

# melakukan operasi aritmatika di dalam kurung kurawal (placeholder)
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
biner = oct(angka)
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(angka)
print(format_binary)
print(format_octal)
print(format_hex)