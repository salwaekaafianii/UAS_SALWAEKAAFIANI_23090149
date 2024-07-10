from soal_3 import Restoran

restaurant_queue = Restoran()

while True:
    print("\nPilih operasi yang ingin Anda lakukan:")
    print("1. Tambah pesanan ke antrian")
    print("2. Hapus pesanan dari depan antrian")
    print("3. Tampilkan antrian saat ini")
    print("0. Keluar")

    choice = input("Masukkan pilihan (0/1/2/3): ")

    if choice == "1":
        order = input("Masukkan pesanan baru: ")
        restaurant_queue.enqueue(order)
        print(f"Pesanan '{order}' ditambahkan ke antrian.")
    
    elif choice == "2":
        removed_order = restaurant_queue.dequeue()
        if removed_order:
            print(f"Pesanan '{removed_order}' telah dihapus dari antrian.")
        else:
            print("Antrian kosong, tidak ada yang dihapus.")
    
    elif choice == "3":
        restaurant_queue.display_queue()
    
    elif choice == "0":
        print("Program selesai.")
        break
    
    else:
        print("Pilihan tidak valid. Masukkan 0, 1, 2, atau 3.")
