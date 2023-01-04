# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang tidak pakai koma(integer)
data_integer = -1
print("Data : ", data_integer, "\n- bertipe ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 10.5
print("Data : ", data_float, "\n- bertipe ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("Data : ", data_string, "\n- bertipe ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = False
print("Data : ", data_bool, "\n- bertipe ", type(data_bool))

### tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("Data : ", data_complex, "\n- bertipe ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double, "\n- bertipe ", type(data_c_double))
