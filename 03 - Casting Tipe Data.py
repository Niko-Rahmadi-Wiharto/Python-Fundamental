# Belajar Casting Tipe Data
# merubah dari satu tipe ke tipe yang lain

# INTEGER
print("======INTERGER======")
data_int = 9
print("Nilai = ", data_int, ", tipe= ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai integer adalah 0
print("Nilai = ", data_float, ", tipe= ", type(data_float))
print("Nilai = ", data_str, ", tipe= ", type(data_str))
print("Nilai = ", data_bool, ", tipe= ", type(data_bool))

# FLOAT
print("\n======FLOAT======")
data_float = 9.0
print("Nilai = ", data_float, ", tipe= ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float adalah 0
print("Nilai = ", data_int, ", tipe= ", type(data_int))
print("Nilai = ", data_str, ", tipe= ", type(data_str))
print("Nilai = ", data_bool, ", tipe= ", type(data_bool))

# BOOLEAN
print("\n======BOOLEAN======")
data_bool = True
print("Nilai = ", data_bool, ", tipe= ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai float adalah 0
print("Nilai = ", data_int, ", tipe= ", type(data_int))
print("Nilai = ", data_str, ", tipe= ", type(data_str))
print("Nilai = ", data_float, ", tipe= ", type(data_float))

# STRING
print("\n======STRING======")
data_str = "10"
print("Nilai = ", data_str, ", tipe= ", type(data_str))

data_int = int(data_str) # string harus angka
data_bool = bool(data_str) # false jika string kosong
data_float = float(data_str) # string harus angka
print("Nilai = ", data_int, ", tipe= ", type(data_int))
print("Nilai = ", data_bool, ", tipe= ", type(data_bool))
print("Nilai = ", data_float, ", tipe= ", type(data_float))
