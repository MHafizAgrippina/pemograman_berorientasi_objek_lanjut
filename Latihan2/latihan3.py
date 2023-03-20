class Mahasiswa:
    def __init__(self, nama, nim):
     self.nama = nama
     self.nim = nim
    def belajar(self):
     print(self.nama, "sedang belajar")

class Pekerja:
    def __init__(self, nama, pekerjaan):
     self.nama = nama
     self.pekerjaan = pekerjaan
    def bekerja(self):
     print(self.nama, "sedang bekerja")

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
     Mahasiswa.__init__(self, nama, nim)
     Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
     print(self.nama, "sedang bersosialisasi")

mhs_pekerja = MahasiswaPekerja("Hafiz", "210511043", "Programmer")
mhs_pekerja.belajar() # output: Hafiz sedang belajar
mhs_pekerja.bekerja() # output: Hafiz sedang bekerja
mhs_pekerja.bersosialisasi() # output: Hafiz sedang bersosialisasi