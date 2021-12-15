buah = ["apel","jeruk","semangka","nanas"]

for x in buah:
    print(x)

for x in range(5):
    print(x)

for x in range (16,24): #start dan stop
    print(x)

for x in range (3,20,3): #start dan stop
    print(x)

for x in range (-20,8,2): #start dan stop
    print(x)

for x in range (10): #start dan stop
    print("Halo chayankk")

for x in range (0,8,3): #start dan stop
    print("Halo syanttiieek")

nama = []
jumlah = int(input("Masukkan jumlah yang diinginkan = "))

for x in range(jumlah):
    nama.append(input("masukkan nama ke {} :".format (x+1)))

for x in range (1, jumlah+1):
    print(nama[0:x])

i = 0.1
while i < 6.2 :
    print(i)
    i = i + 0.2

# infinite loop
2
for i in range (2):
    for j in range(3):
        print("1:{},j:{}".format(i,j), end=" ")
    print() # tanda bahwa perulangan pertama sudah selesai

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y :
        if i == j:
            z = z + 1
print(z)