class Mahasiswa:
    pass    

class Universitas:
    nama = ""
    alamat = ""
    
    @staticmethod
    def greeting(nama):
        print(f"Selamat datang {nama} di universitas kami!")
        
    def intro(self):
        print(f"Halo, kami adalah {self.nama} yang beralamat di {self.alamat}.")
        
    def ruangan(self, nama_ruangan):
        print(f"Ruangan {nama_ruangan} berada di universitas {self.nama}.")
        
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

universitas1.greeting("Budi")
universitas1.intro()
universitas1.ruangan("Aula Utama")