# Width and Multiline

# Data

data_name = "Niko"
data_umur = 17
data_tinggi = 178.5
data_nomor_sepatu = 44

# String multiline (dengan menggunakan enter, newline \n)
data_string = f"nama = {data_name}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)

# String multiline (kutip triples)
data_string = f"""
nama = {data_name}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""
print(5*"=" + "Data String" + 5*"=")
print(data_string)

# Mengatur lebar
data_string = f"""
nama            = {data_name:>15}
umur            = {data_umur:>15}
tinggi          = {data_tinggi:>15}
nomor sepatu    = {data_nomor_sepatu:>15}
"""
print(5*"=" + "Data String" + 5*"=")
print(data_string)

