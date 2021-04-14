def csv_reader(file_name):
    filename = file_name  # nama file di sini
    f = open(filename, "r")  # read mode membuka file csv dan disimpan dalam variabel f
    length = len(f.readlines())  # panjang baris/jumlah line pada file csv
    f.close()  # menutup file
    l = 0  # inisialisasi baris pertama (indeks 0)/first_elmt(l)
    z = []  # inisialisasi array kosong untuk isi data csv
    while l < length:
        f = open(filename, "r")
        a = f.readlines()[l]  # membaca indeks ke-l atau line ke-(l+1)
        c = 0  # inisialisasi variabel jumlah koma
        for i in a:
            if i == ';':  # mendeteksi ada koma sebagai pemisah
                c += 1  # jumlah koma
        d = 1  # first_elmt
        start = 0
        b = []  # array kosong untuk diisi data tiap baris
        while (d <= c):
            for i in range(len(a)):
                if a[i] == ";":
                    stop = i
                    b.append(a[start:stop])  # menambahkan isi masing-masing data pada baris
                    start = i + 1
                    d += 1  # next_elmt (d)
        if l == length - 1:
            b.append(a[start:(len(a))])
        else:
            b.append(a[start:(len(a) - 1)])
        z.append(b)  # menambah array b (data line ke-(l+1)/indeks 0 ke array z)
        f.close()
        l += 1  # next_elmt (l)
    return z

def csv_writer(file_name, isi, s): #s : status, "w" to overwrite, "a" to append
    filename = file_name  #nama file di sini
    f = open(filename, s)
    #yang akan diisi ke file.csv
    f.writelines(isi)
    f.close()

def login():
    while True:
        a = input("Username: ")
        p = input("Password: ")
        if a == "farrel" and p=="rel111":
            print("Logged in !\n")
            break
        else:
            print("Wrong Username/Password")

def riwayatambil():
    filename = "consumable_history.csv"
    arr_ra = csv_reader(filename)
    i = len(arr_ra)-1
    flag1 = True
    while flag1 :
        flag2 = True
        for x in range(5): #descending per 5 data
            print(f"ID Pengambilan : {arr_ra[i][0]}")
            print(f"Nama Pengambil : {arr_ra[i][1]}")
            print(f"Nama Consumable : {arr_ra[i][2]}")
            print(f"Tanggal Pengambilan : {arr_ra[i][3]}")
            print(f"Jumlah : {arr_ra[i][4]} \n")
            if i-1 == 0 :
                flag1 = False
                flag2 = False
                break
            else:
                i-=1
        while flag2 :
            tambahan = input("Tampilkan 5 data berikutnya? (Y/N) : ")
            print()
            if tambahan.lower() == 'n':
                flag1 = False
                flag2 = False
            elif tambahan.lower()=='y':
                flag2 = False
            else:
                print("Masukan Salah! Silahkan Ulangi")
        if flag1 == False and flag2==False:
            break

def help(x) :
    if x == "user" :
        print(" ================== HELP ==================")
        print(" login - untuk melakukan login ke dalam sistem")
        print(" carirarity - untuk mencari gadget dengan rarity tertentu")
        print(" caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
        print(" pinjam - untuk melakukan peminjaman gadget")
        print(" kembalikan - untuk mengembalikan gadget secara seutuhnya")
        print(" minta - untuk meminta consumable yang tersedia")
        print(" savedata - untuk melakukan penyimpanan ke dalam file")
        print(" help - untuk memberikann panduan penggunaan sistem")
    elif x == "admin" :
        print(" ================== HELP ==================")
        print(" register - untuk melakukan registrasi user baru")
        print(" carararity - untuk mencari gadget dengan rarity tertentu")
        print(" caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
        print(" tambahitem - untuk melakukan penambahan item")
        print(" hapusitem - untuk menghapus suatu item pada database")
        print(" ubahjumlah - untuk mengubah jumlah gadget dan consumable yang terdapat didalam sistem")
        print(" riwayatpinjam - untuk melihat riwayat peminjaman gadget")
        print(" riwayatkembali - untuk melihat riwayat pengembalian gadget")
        print(" riwayatambil - untuk melihat riwayat pengambilan consumable")
        print(" savedata - untuk melakukan penyimpanan ke dalam file")
        print(" help - untuk memberikan panduan penggunaan sistem")

#main program
while True:
    a = input(">>> ")
    if a == 'login':
        login()
    elif a == "riwayatambil":
        riwayatambil()
    elif a == "help":
        x = "admin"  # fadlin nanti tolong bikin status logged_in nya sebagai admin atau user, ini hanya contoh
        help(x)
    elif a == 'exit':
        break
