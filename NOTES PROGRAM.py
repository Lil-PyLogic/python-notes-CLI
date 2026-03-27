import os
import time
from datetime import datetime

def simpan_history( note_user ):
    with open("catatan.txt", "a") as f:
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        f.write(f"[{waktu}] | CATATAN LOE : {note_user}\n")
    pass

def lihat_history():
    if not os.path.exists("catatan.txt"):
        print("\n(!) Belum ada riwayat transaksi.")
        return
    with open("catatan.txt", "r") as f:
        isi = f.read()
    print("\n=== RIWAYAT TRANSAKSI ===")
    print(isi if isi else "(!) Belum ada riwayat transaksi.")
    pass

def hapus_catatan():
    if not os.path.exists("catatan.txt"):
        print("\n(!) Belum ada catatan.")
        return
    with open("catatan.txt", "r") as f:
        baris = f.readlines()
    if not baris:
        print("\n(!) Belum ada catatan.")
        return
    print("\n=== PILIH CATATAN YANG MAU DIHAPUS ===")
    for i, b in enumerate(baris, 1):
        print(f"  [{i}] {b.strip()}")
    try:
        pilih = int(input(f"\nNomor catatan (1-{len(baris)}), 0 = batal: "))
        if pilih == 0:
            return
        if not (1 <= pilih <= len(baris)):
            print("(!) Nomor tidak valid.")
            return
        baris.pop(pilih - 1)
        with open("catatan.txt", "w") as f:
            f.writelines(baris)
        print("(✓) Catatan berhasil dihapus!")
    except ValueError:
        print("(!) Input harus angka.")

def tulis_ulang_catatan():
    if not os.path.exists("catatan.txt"):
        print("\n(!) Belum ada catatan.")
        return
    with open("catatan.txt", "r") as f:
        baris = f.readlines()
    if not baris:
        print("\n(!) Belum ada catatan.")
        return
    print("\n=== PILIH CATATAN YANG MAU DITULIS ULANG ===")
    for i, b in enumerate(baris, 1):
        print(f"  [{i}] {b.strip()}")
    try:
        pilih = int(input(f"\nNomor catatan (1-{len(baris)}), 0 = batal: "))
        if pilih == 0:
            return
        if not (1 <= pilih <= len(baris)):
            print("(!) Nomor tidak valid.")
            return
        isi_baru = input("Isi catatan baru: ")
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        baris[pilih - 1] = f"[{waktu}] | CATATAN LOE : {isi_baru}\n"
        with open("catatan.txt", "w") as f:
            f.writelines(baris)
        print("(✓) Catatan berhasil diperbarui!")
    except ValueError:
        print("(!) Input harus angka.")

def menu_utama():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== APLIKASI CATATAN TXT ===")
        print ("1. Tambah Catatan")
        print("2. Lihat Catatan")
        print("3. Hapus Catatan")
        print("4. Tulis Ulang Catatan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        
        if pilihan == "1":
            note_user = input("Isi catatan: ")
            simpan_history(note_user)
            print("Catatan tersimpan!")
        
        elif pilihan == '2':
            lihat_history()
            input("tekan ENTER untuk kembali....")        
        elif pilihan == '3':
            hapus_catatan()
            input("tekan ENTER untuk kembali....")
        elif pilihan == '4':
            tulis_ulang_catatan()
            input("tekan ENTER untuk kembali....")
        elif pilihan == '5':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak ada, coba lagi ya!")

# Menjalankan program
if __name__ == "__main__":
    menu_utama()
