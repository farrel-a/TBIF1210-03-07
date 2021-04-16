def csv_reader(file_name):
    filename = file_name  # nama file di sini
    f = open(filename, "r")  # read mode membuka file csv dan disimpan dalam variabel f
    length = len(f.readlines())  # panjang baris/jumlah line pada file csv
    f.close()  # menutup file
    z = []  # inisialisasi array kosong untuk isi data csv
    for l in range(length):
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
    return z

def csv_writer(file_name, isi, s): #s : status, "w" to overwrite, "a" to append
    filename = file_name  #nama file di sini
    f = open(filename, s)
    #yang akan diisi ke file.csv
    f.writelines(isi)
    f.close()

def check(n, var_name): #mencek input pengguna saat menambah item
    if var_name == 'Jumlah' or var_name == 'tahun ditemukan':
        try:
            n = int(n) #jumlah atau tahun harus berupa bilangan bulat
            if n > 0:
                return True
            else:
                print("")
                print(var_name + " harus berupa bilangan bulat positif!")
                return False
        except:
            print("")
            print(var_name + " harus berupa bilangan bulat positif!")
            return False
    elif var_name == 'Rarity':
        n = n.lower()
        if n == 'c' or n == 'b' or n == 'a' or n == 's': #rarity harus diantara c,b,a,s
            return True
        else:
            print("\nInput rarity tidak valid!")
            return False
    else:
        return True

def id_check(n, ref_list): #memvalidasi id yang dimasukkan
    i = 1
    if len(n)<2: #id harus lebih dari 2 karakter
        print("\nID salah. Format penulisan ID: {G/C}{bilangan bulat}\ncontoh: G3, C5, G17")
        return False
    else:
        n = n[1:] #mengambil kode angka dari id
        try:
            f = int(n) #mencek apakah kode angka id adalah bilangan bulat
            if len(ref_list)<2:
                return True
            else:
                while i<len(ref_list): #mencari id yang sama dalam file csv
                    if arr[i][0] == n:
                        print("\nGagal menambahkan item karena ID sudah ada")
                        return False
                        break
                    else:
                        return True
        except:
            print("\nID salah. Format penulisan ID: {G/C}{bilangan bulat}\ncontoh: G3, C5, G17")
            return False

def op_tambahitem(id, temp_list, ref_file, ref_arr, total):
    while True:
        if not(id_check(id, ref_arr)):
            return []
            break
        temp_list.append(id[1])
        tag_list = csv_reader(ref_file)[0]
        tag_list.pop(0)
        for i in tag_list: #[nama, deskripsi, jumlah......]
            if i == 'tahun_ditemukan':
                i = "tahun ditemukan"
            else:
                i = i.capitalize()
            x = input("Masukkan " + i + ": ")
            if not(check(x, i)):
                break
            if i == 'Rarity':
                x = x.upper()
            temp_list.append(x)
            total += 1
        if total == len(tag_list)-1:
            print("\nItem telah berhasil ditambahkan ke database.")
            return temp_list
        else:
            return []


def tambahitem():
    temp_gadget =[]
    temp_cons = []
    total = 0
    id = input("Masukan ID: ")
    if id[0].lower() == 'c':
        x = op_tambahitem(id, temp_cons, 'consumable.csv', ac_cus, total)
        return x
    elif id[0].lower() == 'g':
        x = op_tambahitem(id, temp_gadget, 'gadget.csv', ag_cus, total)
        return x
    else:
        print("\nGagal menambahkan item karena ID tidak valid")
        return[]

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
    if len(arr_ra) == 1: #data kosong
        print("Tidak ada data pengambilan consumables.")
    else : # len(arr_ra) != 1
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
ag_def = csv_reader('gadget.csv') #inisialisasi array gadget sementara
ag_cus = csv_reader('gadget.csv')
ac_def = csv_reader('consumable.csv') #inisialisasi array consumable sementara
ac_cus = csv_reader('consumable.csv')

while True:
    a = input(">>> ")
    if a == 'login':
        login()
    elif a == 'tambahitem':
        new_item = tambahitem()
        if len(new_item) == 6: #gadget
            ag_cus.append(new_item)
        elif len(new_item) == 5: #consumable
            ac_cus.append(new_item)
     #ngetes apakah sudah masuk ke array sementaranya
    elif a == "gadget":
        print(gadget)
    elif a == "consumable":
        print(cons)
    elif a == "riwayatambil":
        riwayatambil()
    elif a == "help":
        x = "admin"  # fadlin nanti tolong bikin status logged_in nya sebagai admin atau user, ini hanya contoh
        help(x)
    elif a == 'exit':
        break

