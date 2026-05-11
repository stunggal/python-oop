# contoh simpel
# class Kendaraan:
#     def __init__(self, merk, jenis):
#         self.merk = merk
#         self.jenis = jenis

#     def info(self):
#         print(f"Kendaraan ini adalah {self.merk} dengan jenis {self.jenis}.")

# class Mobil(Kendaraan):
#     def hazard_lamp(self):
#         print(f"mobil dengan merk {self.merk} memiliki hazard lamp.")
        
# class Motor(Kendaraan):
#     def hazard_lamp(self):
#         print(f"motor dengan merk {self.merk} tidak memiliki hazard lamp.")
        
# mobil1 = Mobil("Toyota", "SUV")
# mobil1.info()
# mobil1.hazard_lamp()


# motor1 = Motor("Honda", "Scopy")
# motor1.info()
# motor1.hazard_lamp()

# contoh penggunaan super() dan method overriding
# class Kendaraan:
#     def __init__(self, merk, jenis):
#         self.merk = merk
#         self.jenis = jenis

#     def info(self):
#         print(f"Kendaraan ini adalah {self.merk} dengan jenis {self.jenis}.")
        
#     def hazard_lamp(self):
#         print(f"hasil print dari kelas kendaraan")

# class Mobil(Kendaraan):
#     def hazard_lamp(self):
#         print(f"hasil print dari kelas mobil")
        
#     def dari_parent(self):
#         super().hazard_lamp()
        
# class Motor(Kendaraan):
#     def hazard_lamp(self):
#         print(f"hasil print dari kelas motor")
        
#     def dari_parent(self):
#         super().hazard_lamp()
        
# mobil1 = Mobil("Toyota", "SUV")
# mobil1.info()
# mobil1.hazard_lamp()
# mobil1.dari_parent()


# motor1 = Motor("Honda", "Scopy")
# motor1.info()
# motor1.hazard_lamp()
# motor1.dari_parent()


# contoh penggunaan multilevel inheritance
# class Kendaraan:
#     def __init__(self, merk, jenis):
#         self.merk = merk
#         self.jenis = jenis

#     def info(self):
#         print(f"Kendaraan ini adalah {self.merk} dengan jenis {self.jenis}.")
        
# class Mobil(Kendaraan):
#     def hazard_lamp(self):
#         print(f"mobil dengan merk {self.merk} memiliki hazard lamp.")
        
# class Motor(Kendaraan):
#     def hazard_lamp(self):
#         print(f"motor dengan merk {self.merk} tidak memiliki hazard lamp.")
        
# class MotorListrik(Motor):
#     def info_listrik(self):
#         print(f"motor listrik dengan merk {self.merk} memiliki baterai.")
        
# motor_listrik1 = MotorListrik("Yamaha", "Nmax")
# motor_listrik1.info()
# motor_listrik1.hazard_lamp()
# motor_listrik1.info_listrik()

# contoh penggunaan multiple inheritance
class Kendaraan:
    def __init__(self, merk, jenis):
        self.merk = merk
        self.jenis = jenis

    def info(self):
        print(f"Kendaraan ini adalah {self.merk} dengan jenis {self.jenis}.")
    
class Sepeda(Kendaraan):
    def jenis_sepeda(self):
        print("Ini adalah sepeda.")
    
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Sepeda.")
        
class Motor(Kendaraan):
    def jenis_motor(self):
        print("Ini adalah motor.")
        
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Motor.")
            
class SepedaMotor(Sepeda, Motor):
    def info_sepeda_motor(self):
        print("Ini adalah sepeda motor.")
        
sepeda_motor1 = SepedaMotor("Honda", "Sepeda Motor")
sepeda_motor1.info()
sepeda_motor1.jenis_sepeda()
sepeda_motor1.jenis_motor()
sepeda_motor1.cek_diamond_problem()