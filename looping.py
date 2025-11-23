
while True:
    try:
        batas_input = input("Tentukan BATAS TOTAL BELANJA Anda (Angka): Rp")
        TARGET_HARGA = int(batas_input)
        if TARGET_HARGA <= 0:
            print("Batas belanja harus lebih dari Rp0. Coba lagi.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka yang benar.")
        

total_harga = 0
daftar_belanja_user = {} 

print("Target belanja yang harus dicapai adalah: Rp{TARGET_HARGA}")


while total_harga != TARGET_HARGA:
    print("=================================================")
    print("Total Anda saat ini: Rp{total_harga}")
    
    selisih = abs(total_harga - TARGET_HARGA) # Hitung selisih mutlak
    
    
    if total_harga < TARGET_HARGA:
      
        print("Anda perlu MENAMBAH barang senilai minimal Rp{selisih}.")
        aksi = "TAMBAH"
    else:
        print(f"👉 Anda harus MENGURANGI barang senilai minimal Rp{selisih}.")
        aksi = "KURANGI"
        
    print("=================================================")
    
    
    input_aksi = input(f"Apakah Anda ingin {aksi} barang? (tambah/kurangi/lihat): ").lower()
    

    if input_aksi == 'tambah':
        try:
            nama = input("Nama barang yang ditambahkan: ")
            harga = int(input(f"Harga {nama}: Rp"))
            
           
            total_harga += harga
            daftar_belanja_user[nama] = harga
            print(" '{nama}' (Rp{harga}) berhasil ditambahkan. Total sekarang: Rp{total_harga}")
            
        except ValueError:
            print(" Input harga tidak valid. Coba lagi.")
            
    elif input_aksi == 'kurangi':
        if not daftar_belanja_user:
            print(" Keranjang belanja kosong. Tidak ada yang bisa dikurangi.")
            continue
            
        print("\nItem di keranjang:")
        for nama, harga in daftar_belanja_user.items():
            print("- {nama}: Rp{harga}")
            
        nama_kurangi = input("Ketik nama barang yang ingin dikurangi: ")
        
        if nama_kurangi in daftar_belanja_user:
            harga_kurang = daftar_belanja_user[nama_kurangi]
           
            total_harga -= harga_kurang
            del daftar_belanja_user[nama_kurangi]
            print("🗑️ '{nama_kurangi}' (Rp{harga_kurang}) berhasil dihapus. Total sekarang: Rp{total_harga}")
        else:
            print("Barang tidak ditemukan di keranjang. Coba lagi.")
            
    elif input_aksi == 'lihat':
        print("Item di keranjang:")
        for nama, harga in daftar_belanja_user.items():
            print(f"- {nama}: Rp{harga}")
        
    else:
        print("Aksi tidak dikenal. Pilih 'tambah', 'kurangi', atau 'lihat'.")

print("==================================")
print(" FINAL! TOTAL BELANJA TEPAT Rp{TARGET_HARGA}!")
print("==================================")
print("Daftar Barang Akhir:")
for item, harga in daftar_belanja_user.items():
    print("- {item}: Rp{harga}")

print("----------------------------------")
