# Latihan operator bitwise

# int -> 2 : 00000010
# int -> 1 : 00000001
# int -> 9 : 00001001

# 2 | 1 -> 00000011 : 3

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n======= OR ======")
print("nilai : ", a, ", binary : ", format(a,'08b'))
print("nilai : ", b, ", binary : ", format(b,'08b'))
print("-------------------------------(|)")
print("nilai : ", c, ", binary : ", format(c,'08b'))

# bitwise AND (&)
c = a & b
print("\n======= OR ======")
print("nilai : ", a, ", binary : ", format(a,'08b'))
print("nilai : ", b, ", binary : ", format(b,'08b'))
print("-------------------------------(&)")
print("nilai : ", c, ", binary : ", format(c,'08b'))

# bitwise XOR (^)
print("\n======= OR ======")
a = 9
d = (0b11111111) ^ (a)
print("nilai : ", a, "  , binary : ", format(a,'08b'))
print("nilai : ", d, ", binary : ", format(d, '08b'))
