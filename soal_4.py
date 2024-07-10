class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def set_nama(self, nama):
        self.nama = nama
    
    def set_warna(self, warna):
        self.warna = warna
    
    def set_rasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f'Buah {self.nama} memiliki warna {self.warna} dan rasanya {self.rasa}'

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin
    
    def set_vitamin(self, vitamin):
        self.vitamin = vitamin
    
    def information(self):
        return f'Mangga {self.nama} memiliki warna {self.warna}, rasanya {self.rasa}, dan mengandung vitamin {self.vitamin}'


mangga_hijau = Mangga('Mangga Harum Manis', 'Hijau', 'Manis', 'C')


print(mangga_hijau.information()) 
mangga_hijau.set_nama('Mangga Alphonso')
print(mangga_hijau.information())  
