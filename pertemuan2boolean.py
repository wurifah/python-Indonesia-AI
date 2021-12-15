# Boolean (True and False)
print(8<9)
a = 200
b = 33
if b>a:
    print("a is greater than b")
if b>=a:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")

nilai = int(input("Masukkan nilai anda : "))
kkm = 70;

if nilai>kkm:
    print("Selamat Anda Lulus")
else:
    print("Anda Harus Mengulang")
    print("== Awokwokwok ==")

x = 7
y = [1,2,3,4,5]

print(y[2]+y[3])

makanan = ["soto","mie ayam","sup"]
makanan.append("bakso")
print(makanan)

minuman = []
harga = []

minuman.append(input("Masukkan Nama Minuman : "))
minuman.append(input("Masukkan Nama Minuman : "))
minuman.append(input("Masukkan Nama Minuman : "))

harga.append(input("Masukkan Harga : "))
harga.append(input("Masukkan Harga : "))
harga.append(input("Masukkan Harga : "))

print(minuman[0],", harga = ",harga[0])
print(minuman[1],", harga = ", harga[1])
print(minuman[2],", harga = ", harga[2])
