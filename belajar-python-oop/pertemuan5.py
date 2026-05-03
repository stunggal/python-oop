class Rekening:
    def __init__(self, nama, saldo, pin):
        self.nama_pemilik = nama
        self.saldo = saldo
        self.pin = pin
        
    def info(self, pin):
        if pin != self.pin:
            print("PIN salah.")
            return
        print(f"Nama Pemilik: {self.nama_pemilik}")
        print(f"Saldo: {self.saldo}")

    def deposit(self, jumlah, pin):
        if pin != self.pin:
            print("PIN salah.")
            return
        if jumlah <= 0:
            print("Jumlah deposit harus lebih besar dari 0.")
            return
        self.saldo += jumlah
        print(f"Deposit sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")

    def withdraw(self, jumlah, pin):
        if pin != self.pin:
            print("PIN salah.")
            return
        if jumlah <= 0:
            print("Jumlah penarikan harus lebih besar dari 0.")
            return
        if jumlah > self.saldo:
            print("Saldo tidak cukup untuk melakukan penarikan.")
        else:
            self.saldo -= jumlah
            print(f"Penarikan sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")
            
rekening1 = Rekening("Budi", 1000000, "1234")
rekening1.info("1234")
rekening1.info("12345")
rekening1.deposit(500000, "1234")
rekening1.withdraw(200000, "1234")
rekening1.withdraw(1500000, "1234")