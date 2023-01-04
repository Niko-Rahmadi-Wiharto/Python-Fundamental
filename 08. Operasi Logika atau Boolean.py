# Operasi logika atau boolean

# not, or, and, xor

print("\n======NOT======")
a = True
c = not a
print("Data boolean = ", a)
print("Data c = ", c)

print("\n======OR======") # Jika salah satu / seluruhnya True maka hasilnya true
a = True
b = True
c = a or b
print(a, " or ", b, " = ", c)

print("\n======AND======") # akan false jika salah satu false
a = True
b = True
c = a and b
print(a, " and ", b, " = ", c)

print("\n======XOR======") # akan true jika salah satu True
a = True
b = True
c = a ^ b
print(a, " xor ", b, " = ", c)