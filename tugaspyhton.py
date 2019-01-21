print(" \t MENGHITUNG LUAS BANGUN DATAR")
print(" \t =--------------------------= ")
print(" \t mukhlis rifai")
print(" \n ")

def luas_lingkaran():
    x = float(input("Masukkan Jari Jari :"))
    luas = 22/7*x*x
    print("Luas Lingkaran adalah : ",luas,"cm2")
def luas_persegi():
    x = float(input("Panjang Sisi : "))
    luasp = x*x
    print("Luas Persegi adalah :",luasp," cm2")
def luas_segitiga():
    x = float(input("Masukkan Alas Segitiga : "))
    y = float(input("Masukkan Tinggi Segitiga : "))
    a = 0.5*x*y
    print("Luas Segitiga adalah : ",a,"cm2")
def sg_fb():
    a = 0
    b = 1
    c = 0
    for i in range(10):
        print(a,"",end="")
        c = a + b
        a = b 
        b = c
def segitiga_sksk():
    x = float(input("Masukkan Alas Segitiga : "))
    y = float(input("Masukkan Tinggi Segitiga : "))
    a = (x*x) + (y*y)
    print("Sisi Miring Segitiga Siku-siku adalah : ",a,"cm2")

pil = int(input("Pilih Program : \n 1. Mengitung Luas Lingkaran \n 2. Mengitung Luas Persegi \n 3. Mengitung Luas Segitiga \n 4. Segitiga Fibonacci \n 5. Segitiga Siku-Siku \n 6. Exit \n  Masukkan Pilihan Anda : (1-6) "))
if pil == 1:
    luas_lingkaran()
elif pil == 2:
    luas_persegi()
elif pil == 3:
    luas_segitiga()
elif pil == 4:
    sg_fb()
elif pil == 5:
    segitiga_sksk()
elif pil == 6:
    exit()    
else:
    print("\n Pilihan Anda Salah ")
tanya =  input("\n \n Ingin Coba Lagi ? (Ya/Tidak)")
if tanya == "y": 
    print("OK")
    import tugaspyhton
elif tanya == "t":
    print("TERIMAKASIH \nKeep Semendehoy")
    exit()
