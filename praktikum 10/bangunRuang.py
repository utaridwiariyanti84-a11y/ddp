import math

def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok(p,l,t):
    hasil = p * l * t
    return hasil 

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga 
    hasil = luas_alas * tinggi_prisma
    return hasil 

def tabung(jari, tinggi):
    luas_alas = math.pi * jari * jari
    hasil = luas_alas * tinggi
    return hasil

def kerucut(jari, tinggi):
    luas_alas = math.pi * jari * jari
    hasil = (1/3) * luas_alas * tinggi
    return hasil

print("Volum Tabung adalah", tabung(3, 5))
print("Volum Kerucut adalah", kerucut(3, 5))

