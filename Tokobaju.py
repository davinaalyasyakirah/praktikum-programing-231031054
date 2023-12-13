class TokoBaju:
    def __init__(self):
        self.daftar_baju = []
        self.harga_baju = []
        self.kategori_baju = []

    def tambah_baju(self):
        nama_baju = input("Masukkan nama baju: ")
        harga = float(input("Masukkan harga baju: "))
        kategori = input("Masukkan kategori baju: ")

        self.daftar_baju.append(nama_baju)
        self.harga_baju.append(harga)
        self.kategori_baju.append(kategori)

        print("Baju berhasil ditambahkan ke dalam stok.")

    def lihat_daftar_baju(self):
        print("===== Daftar Baju =====")
        for i in range(len(self.daftar_baju)):
            print("Nama:", self.daftar_baju[i])
            print("Harga:", self.harga_baju[i])
            print("Kategori:", self.kategori_baju[i])
            print("------------------------")

    def hapus_baju(self):
        nama_baju = input("Masukkan nama baju yang ingin dihapus: ")

        try:
            index = self.daftar_baju.index(nama_baju)
            del self.daftar_baju[index]
            del self.harga_baju[index]
            del self.kategori_baju[index]
            print("Baju berhasil dihapus dari stok.")
        except ValueError:
            print("Baju tidak ditemukan.")

    def cari_baju_by_kategori(self):
        kategori = input("Masukkan kategori baju yang dicari: ")

        print("===== Hasil Pencarian =====")
        for i in range(len(self.daftar_baju)):
            if self.kategori_baju[i].lower() == kategori.lower():
                print("Nama:", self.daftar_baju[i])
                print("Harga:", self.harga_baju[i])
                print("Kategori:", self.kategori_baju[i])
                print("------------------------")

    def urutkan_baju_by_harga(self):
        sorted_indices = sorted(range(len(self.harga_baju)), key=lambda k: self.harga_baju[k])

        print("===== Daftar Baju Urutkan Berdasarkan Harga =====")
        for i in sorted_indices:
            print("Nama:", self.daftar_baju[i])
            print("Harga:", self.harga_baju[i])
            print("Kategori:", self.kategori_baju[i])
            print("------------------------")


def main():
    toko = TokoBaju()

    while True:
        print("===== Menu Toko Baju =====")
        print("1. Tambah Baju")
        print("2. Lihat Daftar Baju")
        print("3. Hapus Baju")
        print("4. Cari Baju Berdasarkan Kategori")
        print("5. Urutkan Daftar Baju Berdasarkan Harga")
        print("0. Keluar")

        pilihan = input("Pilihan Anda: ")

        if pilihan == '1':
            toko.tambah_baju()
        elif pilihan == '2':
            toko.lihat_daftar_baju()
        elif pilihan == '3':
            toko.hapus_baju()
        elif pilihan == '4':
            toko.cari_baju_by_kategori()
        elif pilihan == '5':
            toko.urutkan_baju_by_harga()
        elif pilihan == '0':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
