# tidak pakai polymorphism
class Karyawan:
    def __init__(self, nama: str):
        self.nama = nama

class Manager:
    def __init__(self, nama: str):
        self.nama = nama

class Programmer:
    def __init__(self, nama: str):
        self.nama = nama


# --- IMPLEMENTASI TANPA POLYMORPHISM ---

def simulasikan_kerja_tanpa_poly(karyawan):
    # Kita harus mengecek tipe kelas objek satu per satu secara manual
    if isinstance(karyawan, Manager):
        print(f"Manager {karyawan.nama} sedang memimpin rapat divisi.")
    elif isinstance(karyawan, Programmer):
        print(f"Programmer {karyawan.nama} sedang menulis kode dan memperbaiki bug.")
    elif isinstance(karyawan, Karyawan):
        print(f"{karyawan.nama} sedang melakukan pekerjaan umum.")
    else:
        print("Tipe karyawan tidak dikenal!")

# Pembuatan Object
karyawan_biasa = Karyawan("Budi")
bos_toko = Manager("Eko")
developer_handal = Programmer("Andi")

# Eksekusi Fungsi
print("--- Simulasi Hari Kerja (Tanpa Polymorphism) ---")
simulasikan_kerja_tanpa_poly(karyawan_biasa)   # Output: Budi sedang melakukan pekerjaan umum.
simulasikan_kerja_tanpa_poly(bos_toko)         # Output: Manager Eko sedang memimpin rapat divisi.
simulasikan_kerja_tanpa_poly(developer_handal)   # Output: Programmer Andi sedang menulis kode dan memperbaiki bug.


# pakai polymorphism
# class Karyawan:
#     def __init__(self, nama: str):
#         self.nama = nama

#     def bekerja(self):
#         print(f"{self.nama} sedang melakukan pekerjaan umum.")

# class Manager(Karyawan):
#     def bekerja(self):
#         print(f"Manager {self.nama} sedang memimpin rapat divisi.")

# class Programmer(Karyawan):
#     def bekerja(self):
#         print(f"Programmer {self.nama} sedang menulis kode dan memperbaiki bug.")

# def simulasikan_kerja(karyawan):
#     karyawan.bekerja()


# karyawan_biasa = Karyawan("Budi")
# bos_toko = Manager("Eko")
# developer_handal = Programmer("Andi")

# print("--- Simulasi Hari Kerja ---")
# simulasikan_kerja(karyawan_biasa)   
# simulasikan_kerja(bos_toko)         
# simulasikan_kerja(developer_handal)   