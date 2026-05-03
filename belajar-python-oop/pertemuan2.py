class Mahasiswa:
    pass    

class Universitas:
    nama = ""
    alamat = ""
    
mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()

print(mahasiswa1)
print(mahasiswa2)

universitas1 = Universitas()
universitas1.nama = "Universitas Darussalam"
universitas1.alamat = "Gontor Ponorogo"

universitas2 = Universitas()
universitas2.nama = "Universitas Negeri Malang"
universitas2.alamat = "Malang"

print(universitas1.nama)
print(universitas1.alamat)
print(universitas2.nama)
print(universitas2.alamat)
