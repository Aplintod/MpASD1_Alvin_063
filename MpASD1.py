class PipinStore:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class AdminPipinStore:
    def __init__(self):
        self.diamond = {
            1: PipinStore("113 Diamond", 29000),
            2: PipinStore("170 Diamond", 44000),
            3: PipinStore("219 Diamond", 59000),
            4: PipinStore("284 Diamond", 73000),
            5: PipinStore("340 Diamond", 95000)
        }

# FYI : Harga dan amount DM nya ambil dari XcashShop.com, Top Up di XcashShop yahh hehehe :D

    def ingpo_stok(self):
        print("List Diamond Ready :")
        for key, item in self.diamond.items():
            print(f"{key}. {item.name} : Rp {item.price}")

    def tambah_amount(self, name, price):
        amount_baru = PipinStore(name, price)
        num = len(self.diamond) + 1
        self.diamond[num] = amount_baru
        print(f"{amount_baru.name} harganya Rp{amount_baru.price} Yaahh")

    def update_harga(self, list_amount, harga_baru):
        if list_amount in self.diamond:
            self.diamond[list_amount].price = harga_baru
            print(f"Harga {self.diamond[list_amount].name} ganti jadi Rp{harga_baru} yaahh.")
        else:
            print("Gaada Pilihan nya banh :D.")

    def hapus_amount(self, list_amount):
        if list_amount in self.diamond:
            del self.diamond[list_amount]
            print("Okeh Amountnya Udah Dihapus .")
        else:
            print("Gaada Pilihannya banh :D.")

admin = AdminPipinStore()

while True:
    print("-"*50)
    print("Mau Ngapain Nihh? \n")
    print("1. Cek List Diamond Ready")
    print("2. Tambah Amount Baru")
    print("3. Update Harga Diamond")
    print("4. Hapus Amount")
    print("5. Keluar Ajah")
    print("-"*50)

    choice = input("Masukkan pilihan loe : ")
    print("-"*50)
    
    if choice == '1':
        admin.ingpo_stok()
    elif choice == '2':
        name = input("Masukkan Amount Baru : ")
        price = int(input("Masukkan Harga : "))
        admin.tambah_amount(name, price)
    elif choice == '3':
        list_amount = int(input("Mau Update Yang Mana? : "))
        harga_baru = int(input("Masukkan Harga Baru : "))
        admin.update_harga(list_amount, harga_baru)
    elif choice == '4':
        list_amount = int(input("Mau Hapus Yang Mana? : \n"))
        admin.hapus_amount(list_amount)
    elif choice == '5':
        print("Makasi Yahh :D")
        print("-"*50)
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
