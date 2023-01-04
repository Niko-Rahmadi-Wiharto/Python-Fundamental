# Operasi komparasi

# setiap haris dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 4

# lebih besar dari '>'
hasil = a > 2
print(a, ' > ', b, ' = ', hasil)

# lebih kecil dari '<>>'
hasil = a < 2
print(a, ' < ', b, ' = ', hasil)

# lebih besar sama dengan '>='
hasil = a >= 2
print(a, ' >= ', b, ' = ', hasil)

# lebih kecil sama dengan '>'
hasil = a <= 2
print(a, ' <= ', b, ' = ', hasil)

# sama dengan '=='
hasil = a == 2
print(a, ' == ', b, ' = ', hasil)

# is ==> tidak bekerja pada syntax literal (membandingkan objek (variable))
# hasil = a is 4
# ##perbandingan di atas tidak bisa dilakukan pada is dan is not

hasil = a is b
print(a, ' is ', b, ' = ', hasil)

# is not ==> tidak bekerja pada syntax literal (membandingkan objek (variable))
hasil = a is not b
print(a, ' is not ', b, ' = ', hasil)
