data = "ini adalah string pertamaku"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. menggunakan single quote '.....'
    2. menggunakan double quote "....."
'''

data = 'Menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)

## menggunakan single dan double quote

print('\n"Halo, apa kabar"')
print("ini adalah hari jum'at")

# 2. Menggunakan tanda backslash \

# membuat tanda ' menjadi string
print('Mari shalat jum\'at')
print("g\'day, isn't it?")

# membuat Backslash menjadi string
print("C:\\user\\Niko")

# tab
print("Ucup \t\t\totong, jauhan")

# backspace
print("Ucup \botong, deketan")

# newline
print("baris pertama. \nbaris kedua") # LF -> line feed (UNIX, MAC OS, LINUX)
print("baris pertama.\rbaris kedua.") # CR -> carriage return (comodore, acorn, lisp)
print("baris pertama.\n\rbaris kedua.") # CRLF -> line feed carriage return (windows)

# 3. String literal

# hati-hati
print('C:\new folder') #akan salah path nya

# menggunakan raw
print(r'C:\New Folder\User\biko')

# multiline literal string
print("""
Nama : Niko
Kelas : Jambu
""")

# multiline literal string dan raw
print(r"""
Nama : Niko
Kelas : Jambu
Path : C:\User\niko
""")
