# Date and time

import datetime as dt # import datetime dan diinisialisai dengan "dt"

hari_ini = dt.date.today() # menggunakan "dt" (asalnya datetime)
print(f"hari ini adalah hari = {hari_ini:%A}, {hari_ini}")
print("Silahkan masukan tanggal, bulan, dan tahun lahir Anda")
tanggal = int(input("tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)

print(f"""
Kamu lahir pada {tanggal_lahir:%A}, {tanggal_lahir}""")

hari_ini = dt.date.today()
print(f"Hari ini tanggal {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur kamu adalah {umur_tahun} tahun {umur_bulan_sisa} bulan")