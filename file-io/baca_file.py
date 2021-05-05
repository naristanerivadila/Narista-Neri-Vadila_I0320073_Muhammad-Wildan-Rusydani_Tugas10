print("- MEMBACA FILE PERBARIS -")

#buka file
file_puisi = open("puisi.txt","r")

#baca isi file
print(file_puisi.readlines())

#tutup file
file_puisi.close()

print()
print()

print("- MEMBACA SEMUA TEKS -")

file_puisi = open("puisi.txt","r")

#baca isi file
puisi = file_puisi.read()

#cetak isi file
print(puisi)

#tutup file
file_puisi.close()

print()
print()

print("- Menulis dengan mode W -")
print("Selamat Datang di Program Biodata")
print("=================================")

#Ambil input dari user
nama = input("Nama : ")
umur = input("Umur : ")
alamat = input("Alamat : ")

#format teks
teks = "Nama : {}\nUmur : {}\nAlamat : {}".format(nama, umur, alamat)

#Buka file untuk ditulis
file_bio = open("biodata.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()

print()
print()

print("- Menyisipkan Data ke File -")
print("Selamat Datang di Program Biodata")
print("=================================")

#Ambil input dari user
nama = input("Nama : ")
umur = input("Umur : ")
alamat = input("Alamat : ")

#format teks
teks = "Nama : {}\nUmur : {}\nAlamat : {}".format(nama, umur, alamat)

#Buka file untuk ditulis
file_bio = open("biodata.txt", "a")

#tulis teks ke file
file_bio.write(teks)

print()
print()

print("- Membuat Direktori -")
#Nama_File: mkdir.py

import os

def main():
    os.mkdir("unit")

ifname = 'main'

main()

print()
print()

