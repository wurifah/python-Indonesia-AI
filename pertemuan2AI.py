# User input
nama = input("Masukkan Nama Anda: ")
umur = input("Umur = ")
print("nama = "+ nama)
print("umur = "+ umur)

# Menghitung luas Persegi Panjang
panjang = int(input("Masukkan nilai panjang = ")) #harus di integerkan karena user input otomatis string
lebar   = int(input("Masukkan nilai lebar = "))
l = panjang*lebar
kel = 2*(panjang+lebar)
print("Luas Persegi panjang = {} cm2, dan kelilingnya = {} cm".format(l,kel)) #format untuk memanggil hasil

# String operation
a = "Halo dunia";
print(nama[1:3]) #karakter dimulai angka 0 # : artinya sampai # mulai dari 1 sampe 7
print(len(nama))

y = "Indonesia AI"
print(y[2:4])
print(len(y))

