class Rekening:
    def __init__(self, nama, saldo, pin):
        self.nama_pemilik = nama
        self.saldo = saldo
        self.pin = pin
        
    def __str__(self):
        return f"Rekening {self.nama_pemilik} dengan saldo {self.saldo}"
    
    def __eq__(self, other):
        if isinstance(other, Rekening):
            return self.nama_pemilik == other.nama_pemilik and self.saldo == other.saldo
        return False
    
rekening1 = Rekening("Budi", 1000000, "1234")
rekening2 = Rekening("Budi", 1000000, "1234")
rekening3 = Rekening("Siti", 500000, "5678")
print(rekening1)
print(rekening2)
print(rekening3)
print(rekening1 == rekening2)  # True
print(rekening1 == rekening3)  # False