import math
def jajarGanjar(alas, tinggi):
    return alas * tinggi 

def persegi(sisi):
    hasil = sisi * sisi
    return hasil

def persegi_panjang(p, l):
    hasil = p * l
    return hasil

def segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi
    return hasil

def lingkaran(jari):
    hasil = math.pi * jari * jari
    return hasil

print("Luas Jajar Ganjar adalah", jajarGanjar(4, 7))
print("Luas Persegi adalah", persegi(4))
print("Luas Persegi Panjang adalah", persegi_panjang(4, 7))
print("Luas Segitiga adalah", segitiga(5, 6))
print("Luas Lingkaran adalah", lingkaran(7))