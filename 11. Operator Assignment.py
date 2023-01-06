

a = 5 # adalah assignment
print("Nilai a : ", a)

a += 5 # artinya adalah a = a + 5
print("Nilai a : ", a)

a -= 5 # artinya adalah a = a - 5
print("Nilai a : ", a)

a *= 5 # artinya adalah a = a * 5
print("Nilai a : ", a)

a /= 5 # artinya adalah a = a / 5
print("Nilai a : ", a)

b = 100
print("\nNilai b : ", b)

# Modulus dan floor division
b %= 3
print("Nilai b : ", b)

b //= 3
print("Nilai b : ", b)

# Pangkat / exponen
b = 5
b **= 3
print("Nilai b : ", b)

# Operasi bitwise
# OR
c = True
print("\nNilai c : ", c)

c |= True
print("Nilai c : ", c)

c = False
c |= False
print("Nilai c : ", c)

# AND
c = True
print("\nNilai c : ", c)
c &= True
print("Nilai c : ", c)
c &= False
print("Nilai c : ", c)

# XOR
c = True
print("\nNilai c : ", c)
c ^= True
print("Nilai c : ", c)
c ^= False
print("Nilai c : ", c)
c ^= True
print("Nilai c : ", c)

# Shifting
d = 0b0001
print("\nNilai d : ", format(d, '04b'))
d <<= 3
print("Nilai d : ", format(d, '04b'))
d >>= 1
print("Nilai d : ", format(d, '04b'))



