# PROGRAM PENGELOLAAN INVENTARIS BARANG TOKO
# Mata Kuliah: Algoritma dan Pemrograman


print("=" * 50)
print("       APLIKASI INVENTARIS BARANG TOKO")
print("=" * 50)

# 1. Memasukkan data barang
barang = input("Masukkan nama barang       : ").strip()

while not barang:
    print("Nama barang tidak boleh kosong!")
    barang = input("Masukkan nama barang       : ").strip()

# Validasi stok awal
while True:
    try:
        stok_barang = int(input("Masukkan stok awal         : "))
        if stok_barang < 0:
            print("Stok tidak boleh negatif!")
        else:
            break
    except ValueError:
        print("Input harus berupa angka!")

# Variabel pencatatan transaksi
total_masuk = 0
total_keluar = 0

print("\nData barang berhasil disimpan!")
print("-" * 50)

# 2. Menu utama program
while True:
    print("\n========== MENU INVENTARIS ==========")
    print("1. Tambah Stok Barang")
    print("2. Kurangi Stok Barang")
    print("3. Lihat Informasi Stok")
    print("4. Keluar Program")
    print("=====================================")

    menu = input("Pilih menu (1-4): ")

    # 3. Proses barang masuk
    if menu == "1":
        try:
            masuk = int(input("Jumlah barang masuk: "))

            if masuk <= 0:
                print("Jumlah harus lebih dari nol!")
            else:
                stok_barang += masuk
                total_masuk += masuk

                print("\nBarang berhasil ditambahkan!")
                print("Stok saat ini:", stok_barang)

        except ValueError:
            print("Masukkan jumlah dengan angka yang benar!")

    # 4. Proses barang keluar
    elif menu == "2":
        try:
            keluar = int(input("Jumlah barang keluar: "))

            if keluar <= 0:
                print("Jumlah harus lebih dari nol!")

            elif keluar > stok_barang:
                print("\nPeringatan! Stok tidak mencukupi.")
                print("Stok tersedia:", stok_barang)

            else:
                stok_barang -= keluar
                total_keluar += keluar

                print("\nBarang berhasil dikeluarkan!")
                print("Sisa stok:", stok_barang)

        except ValueError:
            print("Masukkan jumlah dengan angka yang benar!")

    # 5. Menampilkan informasi barang
    elif menu == "3":
        print("\n========== INFORMASI BARANG ==========")
        print("Nama Barang       :", barang)
        print("Stok Tersedia     :", stok_barang)
        print("Total Barang Masuk:", total_masuk)
        print("Total Barang Keluar:", total_keluar)
        print("======================================")

    # 6. Mengakhiri program
    elif menu == "4":
        print("\n========== LAPORAN AKHIR =============")
        print("Nama Barang        :", barang)
        print("Stok Awal          :", stok_barang + total_keluar - total_masuk)
        print("Total Barang Masuk :", total_masuk)
        print("Total Barang Keluar:", total_keluar)
        print("Stok Akhir         :", stok_barang)
        print("======================================")
        print("Terima kasih telah menggunakan aplikasi!")
        break

    else:
        print("Menu tidak tersedia! Silakan pilih 1 sampai 4.")