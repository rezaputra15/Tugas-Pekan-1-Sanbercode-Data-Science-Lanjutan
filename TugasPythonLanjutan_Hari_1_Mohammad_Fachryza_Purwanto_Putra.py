class manipulasi:
    def __init__(self, text):
        self.data = text
    
    def kapital (self):
        hasil = self.data.capitalize()
        return print (hasil)

    def kecil (self):
        hasil = self.data.lower()
        return print (hasil)

    def besar (self):
        hasil = self.data.upper()
        return print (hasil)

    def pisah (self):
        hasil = self.data.split()
        return print (hasil)

data = "saya tinggal di Indonesia"

m1 = manipulasi(data)

print("data = ",data)
m1.kapital()
m1.kecil()
m1.besar()
m1.pisah()