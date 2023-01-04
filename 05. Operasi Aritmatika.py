a = 9
b = 4

# Operasi pertambahan
hasil = a + b
print(a, " + ", b, " = ", hasil)

# Operasi pengurangan
hasil = a - b
print(a, " - ", b, " = ", hasil)

# Operasi perkalian
hasil = a * b
print(a, " * ", b, " = ", hasil)

# Operasi pembagian
hasil = a / b
print(a, " / ", b, " = ", hasil)

# Operasi exponen (pangkat)
hasil = a ** b
print(a, " ** ", b, " = ", hasil)

# Operasi modulus
hasil = a % b
print(a, " % ", b, " = ", hasil)

# Operasi floor division
hasil = a // b
print(a, " // ", b, " = ", hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-temannya * / ** % //
    4. pertambahan dan pengurangan
'''
x = 3
y = 2
z = 5

hasil = (x + y) - 3 * (x * y)
print(hasil)