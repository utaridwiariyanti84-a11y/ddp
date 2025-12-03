import bangunRuang as br
import bangunDatar as bd

print("~~~~ BANGUN RUANG ~~~~")
print(f"Volum Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4, 5, 2)}")
print(f"Volum Prisma Segitiga  adalah {br.prisma(5,4,5)}")
print(f"Volum Tabung adalah {br.tabung(3, 5)}")
print(f"Volum Kerucut adalah {br.kerucut(3, 5)}")

print("~~~~ BANGUN DATAR ~~~~")
print(f"Luas JajarGanjar adalah {bd.jajarGanjar(4,7)} ")
print(f"Luas Persegi adalah {bd.persegi(4)} ")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(4, 7)} ")
print(f"Luas Segitiga adalah {bd.segitiga(5, 6)} ")
print(f"Luas Lingkaran adalah {bd.lingkaran(7)} ")