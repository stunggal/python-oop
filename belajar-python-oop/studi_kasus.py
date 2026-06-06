class Kendaraan:
    def __init__(self, merk, tahun, warna, plat, kode, status="Tersedia"):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna
        self.plat = plat
        self.kode = kode
        self.status = status

    def info(self):
        return f"{self.merk} {self.tahun} {self.warna} (Plat: {self.plat}, Kode: {self.kode}, Status: {self.status})"

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna, plat, kode, jumlah_pintu):
        super().__init__(merk, tahun, warna, plat, kode)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"Mobil: {super().info()}, Jumlah Pintu: {self.jumlah_pintu}"
    
class Motor(Kendaraan):
    def __init__(self, merk, tahun, warna, plat, kode, jenis_motor):
        super().__init__(merk, tahun, warna, plat, kode)
        self.jenis_motor = jenis_motor

    def info(self):
        return f"Motor: {super().info()}, Jenis Motor: {self.jenis_motor}"
    
class MotorListrik(Motor):
    def __init__(self, merk, tahun, warna, plat, kode, jenis_motor, kapasitas_baterai):
        super().__init__(merk, tahun, warna, plat, kode, jenis_motor)
        self.kapasitas_baterai = kapasitas_baterai

    def info(self):
        return f"Motor Listrik: {super().info()}, Kapasitas Baterai: {self.kapasitas_baterai} kWh"
    
# stok awal
kendaraan_list = [
    Mobil("Toyota", 2020, "Merah", "B 1234 CD", "M001", 4),
    Mobil("Honda", 2018, "Hitam", "B 5678 EF", "M002", 5),
    Motor("Honda", 2019, "Hitam", "B 1245 GH", "MT001", "Sport"),
    Motor("Yamaha", 2021, "Putih", "B 5679 IJ", "MT002", "Matic"),
    MotorListrik("Vespa", 2022, "Merah", "B 1250 KL", "MTL001", "Skuter", 4.5)
]

def tampilkan_semua_kendaraan():
    print("Daftar Kendaraan:")
    for kendaraan in kendaraan_list:
        print(kendaraan.info())

tampilkan_semua_kendaraan()