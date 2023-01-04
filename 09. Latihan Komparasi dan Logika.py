# Latihan komparasi dan logika

# membuat gabungan area rentang dari angka

# ++++++3-----10+++++

inputUser = float(input("Masukan angka yang bernilai kurang dari 3 dan lebih dari 10: "))

isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

isCorrect = (inputUser < 3) or (inputUser > 10)
print("Angka yang diinput = ", isCorrect)

isCorrect = isLebihDari or isKurangDari
print("Angka yang diinput = ", isCorrect)