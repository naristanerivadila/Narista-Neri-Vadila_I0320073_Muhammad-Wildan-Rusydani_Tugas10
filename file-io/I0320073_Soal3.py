print("SOAL 3")
print("- Menambah 1 Biodata -")

print()

print("BIODATA MAHASISWA TEKNIK INDUSTRI UNS 2020")
print("==========================================")

#Ambil input dari user
nama = input("Nama : ")
nim = input("NIM : ")
kelas = input("Kelas : ")
nohp = input("No. HP : ")
alamat = input("Alamat : ")


#format teks
teks = "Nama : {}\nNIM : {}\nKelas : {}\nNo.HP : {}\nAlamat : {}".format(nama, nim, kelas, nohp, alamat)

#Buka file untuk ditulis
file_bio = open("file.txt", "a")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()