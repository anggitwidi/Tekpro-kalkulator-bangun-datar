import math

def luas_persegi(s):
    return s * s

def keliling_persegi(s):
    return 4 * s

def luas_persegi_panjang(p,l):
    return p * l

def keliling_persegi_panjang(p,l):
    return 2 * (p + l)

def luas_segitiga(a,t):
    return 0.5 * a * t

def keliling_segitiga(s1,s2,s3):
    return s1 + s2 + s3

def luas_lingkaran(r):
    return math.pi * (r ** 2)

def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_jajar_genjang(a,t):
    return a * t

def keliling_jajar_genjang(s1, s2):
    return 2 * (s1 + s2)

while True:
    print("Kalkulator Bangun Datar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    
    pilihan = int(input("Pilih jenis bangun datar (1/2/3/4/5): "))
    operasi = int(input("Pilih operasi (1.luas 2.keliling): "))
    
    if pilihan == 1:
        s = float(input("Masukkan panjang sisi persegi: "))
        if operasi == 1 :
            hasil = luas_persegi(s)
        elif operasi == 2 :
            hasil = keliling_persegi(s)
    elif pilihan == 2:
        p = float(input("Masukkan panjang persegi panjang: "))
        l = float(input("Masukkan lebar persegi panjang: "))
        if operasi == 1 :
            hasil = luas_persegi_panjang(p,l)
        elif operasi == 2 :
            hasil = keliling_persegi_panjang(p,l)
    elif pilihan == 3 :
        a = float(input("Masukkan panjang alas segitiga: "))
        t = float(input("Masukkan tinggi segitiga: "))
        if operasi == 1 :
            hasil = luas_segitiga(a,t)
        elif operasi == 2 :
            s1 = float(input("Masukkan panjang sisi pertama segitiga: "))
            s2 = float(input("Masukkan panjang sisi kedua segitiga: "))
            s3 = float(input("Masukkan panjang sisi ketiga segitiga: "))
            hasil = keliling_segitiga(s1, s2, s3)
    elif pilihan == 4:
        r = float(input("Masukkan panjang jari-jari lingkaran: "))
        if operasi == 1 :
            hasil = luas_lingkaran(r)
        elif operasi == 2 :
            hasil = keliling_lingkaran(r)
    elif pilihan == 5:
        a = float(input("Masukkan panjang alas jajar genjang: "))
        t = float(input("Masukkan tinggi jajar genjang: "))
        if operasi == 1 :
            hasil = luas_jajar_genjang(a,t)
        elif operasi == 2 :
            s1 = float(input("Masukkan panjang sisi sejajar pertama jajar genjang: "))
            s2 = float(input("Masukkan panjang sisi sejajar kedua jajar genjang: "))
            hasil = keliling_jajar_genjang(s1,s2)
    else:
        print("anda buta kah? pilihan cuma 5 sattt!!!")
        break
    print(f"Hasil {'luas'if operasi == 1 else 'keliling'}: {hasil}")
