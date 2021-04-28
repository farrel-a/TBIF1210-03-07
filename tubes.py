import os, argparse, time


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


def csv_writer(file_name, isi, s):  # s : status, "w" to overwrite, "a" to append
    filename = file_name  # nama file di sini
    f = open(filename, s)
    # yang akan diisi ke file.csv
    f.writelines(isi)
    f.close()


def check(n, var_name):  # mencek input pengguna saat menambah item
    if var_name == 'Jumlah' or var_name == 'tahun ditemukan' or var_name == 'tahun':
        try:
            n = int(n)  # jumlah atau tahun harus berupa bilangan bulat
            if n > 0:
                return True
            else:
                print("")
                print(var_name + " harus berupa bilangan bulat positif!")
                return False
        except:  # jumlah harus integer
            print("")
            print(var_name + " harus berupa bilangan bulat positif!")
            return False
    elif var_name == 'tanggal':
        try:
            if n[2] == '/' and n[5] == '/':  # DD/MM/YYYY
                if len(n) < 7:  # minimal DD/MM/Y
                    return False
                else:
                    try:
                        day = int(n[:2])  # ambil hari
                        month = int(n[3:5])  # ambil bulan
                        year = int(n[6:])  # ambil  tahun
                        bulan_30 = [4, 6, 9, 11]  # bulan yang 30 hari
                        if day > 0 and day < 32:
                            if month >= 1 and month <= 12:  # bulan harus 1-12
                                if (year % 400 == 0) or (
                                        year % 4 == 0 and year % 100 != 0):  # tahun kabisat kalender gregorian
                                    if month == 2:
                                        if day > 29:
                                            return False
                                        else:
                                            return True
                                    elif month in bulan_30:
                                        if day > 30:
                                            return False
                                        else:
                                            return True
                                    else:  # 31 hari
                                        if day > 31:
                                            return False
                                        else:
                                            return True

                                else:  # tahun biasa
                                    if month == 2:
                                        if day > 28:
                                            return False
                                        else:
                                            return True
                                    elif month in bulan_30:
                                        if day > 30:
                                            return False
                                        else:
                                            return True
                                    else:  # 31 hari
                                        if day > 31:
                                            return False
                                        else:
                                            return True

                            else:
                                return False
                    except:
                        return False

            else:
                return False
        except:
            return False

    elif var_name == 'ubah':
        try:
            n = int(n)  # harus integer
            return True
        except:
            return False

    elif var_name == 'Rarity':
        n = n.lower()
        if n == 'c' or n == 'b' or n == 'a' or n == 's':  # rarity harus diantara c,b,a,s
            return True
        else:
            print("\nInput rarity tidak valid!")
            return False

    elif var_name == "files":
        # n : string (folder path), var_name : "files"
        os.chdir(n)  # path menuju folder
        if not (os.path.exists("user.csv")):
            f = open("user.csv", "x")
            f.close()
            string = "id;username;nama;alamat;password;role\nU1;rel;Farrel;Jalan Panjang;rel123;admin"
            csv_writer("user.csv", string, "w")
        if not (os.path.exists("gadget.csv")):
            f = open("gadget.csv", "x")
            f.close()
            string = "id;nama;deskripsi;jumlah;rarity;tahun_ditemukan"
            csv_writer("gadget.csv", string, "w")
        if not (os.path.exists("consumable.csv")):
            f = open("consumable.csv", "x")
            f.close()
            string = "id;nama;deskripsi;jumlah;rarity"
            csv_writer("consumable.csv", string, "w")
        if not (os.path.exists("consumable_history.csv")):
            f = open("consumable_history.csv", "x")
            f.close()
            string = "id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah"
            csv_writer("consumable_history.csv", string, "w")
        if not (os.path.exists("gadget_borrow_history.csv")):
            f = open("gadget_borrow_history.csv", "x")
            f.close()
            string = "id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned"
            csv_writer("gadget_borrow_history.csv", string, "w")
        if not (os.path.exists("gadget_return_history.csv")):
            f = open("gadget_return_history.csv", "x")
            f.close()
            string = "id;id_peminjaman;tanggal_pengembalian"
            csv_writer("gadget_return_history.csv", string, "w")

    else:
        return True


def id_check(n):  # memvalidasi id yang dimasukkan
    i = 1  # i = 1 karena indeks ke-0 berisi tag_list
    if len(n) < 2:  # id harus lebih dari 2 karakter
        return False
    else:
        n = n[1:]  # mengambil kode angka dari id
        try:
            f = int(n)  # mencek apakah kode angka id adalah bilangan bulat
            if f > 0:
                return True
            else:
                return False
        except:
            return False


def find_id(n, ref_list): #mencari apakah ada  gadget/cosumables dengan id yang diinput pengguna 
    n = n.upper()
    i = 1
    while i < len(ref_list):
        if ref_list[i][0] == n:
            return True
            break
        else:
            i += 1
    return False


def op_tambahitem(id, temp_list, ref_file, ref_arr, total):
    while True:
        if not (id_check(id)):#memvlidasi input id
            print("\nID salah. Format penulisan ID: {G/C}{bilangan bulat}\ncontoh: G3, C5, G17")
            return []
            break
        if find_id(id, ref_arr):#mencari apakah id ada
            print("\nGagal menambahkan item karena ID sudah ada")
            return []
            break
        temp_list.append(id)#menambahkan atribut id ke dalam array baru
        tag_list = csv_reader(ref_file)[0] #[id, nama, desc.....]
        tag_list.pop(0)
        for i in tag_list:  # [nama, deskripsi, jumlah......]
            if i == 'tahun_ditemukan':
                i = "tahun ditemukan"
            else:
                i = i.capitalize()
            x = input("Masukkan " + i + ": ")
            if not (check(x, i)):
                break
            if i == 'Rarity':
                x = x.upper()
            temp_list.append(x)
            total += 1
        if total == len(tag_list):
            print("\nItem telah berhasil ditambahkan ke database.")
            return temp_list
        else:
            return []


def tambahitem():
    temp_gadget = []
    temp_cons = []
    total = 0
    id = input("Masukan ID: ")
    id = id.upper()
    if id[0].lower() == 'c':
        s = op_tambahitem(id, temp_cons, 'consumable.csv', ac_cus, total)
        return s
    elif id[0].lower() == 'g':
        s = op_tambahitem(id, temp_gadget, 'gadget.csv', ag_cus, total)
        return s
    else:
        print("\nGagal menambahkan item karena ID tidak valid")
        return []


def hapusitem():
    id = input("Masukkan ID item: ")
    id = id.upper()
    if id[0].lower() == 'g':
        if op_ask_id(id, ag_cus):
            return delete_by_id(id, ag_cus)
        else:
            return ag_cus
    elif id[0].lower() == 'c':
        if op_ask_id(id, ac_cus):
            return delete_by_id(id, ac_cus)
        else:
            return ac_cus
    else:
        print('\nTidak ada item dengan ID tersebut.')


def delete_by_id(n, ref_list):
    i = 1
    while i < len(ref_list):
        if ref_list[i][0] == n:  # mencari id yang sama dalam file csv
            while True:
                ask = input('Apakah Anda yakin ingin menghapus ' + ref_list[i][1] + ' (Y/N)? ')
                if ask.lower() == 'y':
                    ref_list.pop(i)
                    print("\nItem telah berhasil dihapus dari database")
                    return ref_list
                    break
                elif ask.lower() == 'n':
                    print('\nTidak jadi melakukan aksi.')
                    return ref_list
                    break
                else:
                    ask = input('Apakah Anda yakin ingin menghapus ' + ref_list[i][1] + ' (Y/N)? ')
        else:
            i += 1
    print('\nTidak ada item dengan ID tersebut.')
    return ref_list


def op_ask_id(id, ref_arr):
    while True:
        if not (id_check(id)):
            print("\nID salah. Format penulisan ID: {G/C}{bilangan bulat}\ncontoh: G3, C5, G17")
            return False
            break
        if not (find_id(id, ref_arr)):
            print('\nTidak ada item dengan ID tersebut.')
            return False
            break
        return True


def ubahjumlah():
    id = input("Masukkan ID item: ")
    id = id.upper()
    if id[0].lower() == 'g':
        if op_ask_id(id, ag_cus):
            return op_ubahjumlah(id, ag_cus)
        else:
            return ag_cus
    elif id[0].lower() == 'c':
        if op_ask_id(id, ac_cus):
            return op_ubahjumlah(id, ac_cus)
        else:
            return ac_cus
    else:
        print('\nTidak ada item dengan ID tersebut.')


def op_ubahjumlah(id, ref_list):
    i = 1
    while i < len(ref_list):  # mencari id yang sama dalam file csv
        if ref_list[i][0] == id:
            ask = input('Masukkan Jumlah: ')
            if check(ask, 'ubah'):
                ask = int(ask)
                sum = int(ref_list[i][3]) + ask
                if sum < 0:
                    print("")
                    print(str(abs(ask)) + " " + ref_list[i][1] + " gagal dibuang karena stok kurang. Stok sekarang: " +
                          ref_list[i][3] + " (< " + str(abs(ask)) + ")")
                    return ref_list
                    break
                elif ask > 0:
                    print('')
                    print(str(abs(ask)) + " " + ref_list[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(sum))
                    ref_list[i][3] = str(sum)
                    return ref_list
                    break
                else:
                    print('')
                    print(str(abs(ask)) + " " + ref_list[i][1] + " berhasil dibuang. Stok sekarang: " + str(sum))
                    ref_list[i][3] = str(sum)
                    return ref_list
                    break
            else:
                print('\nMasukkan harus berupa bilangan bulat!')
                return ref_list
        else:
            i += 1
        print('Tidak ada item dengan ID tersebut.')
        return ref_list


def pinjam():
    id = input("Masukkan ID item: ")
    id = id.upper()
    if id[0].lower() == 'g':
        if op_ask_id(id, ag_cus):
            return op_pinjam(id, ag_cus, agbh_cus, user_Logged)
        else:
            return ag_cus
    elif id[0].lower() == 'c':
        print("\nHanya bisa meminjam gadget! (tidak bisa consumables)")
        return ag_cus
    else:
        print('\nTidak ada item dengan ID tersebut.')


def op_pinjam(id, ref_list, borrow_list, user_Logged):
    i = 1
    j = 1
    name = ''
    x = 1
    isPernahPinjam = False
    while x < len(ref_list):
        if ref_list[x][0] == id:
            name = ref_list[x][1]
            break
        else:
            x += 1
    while j < len(borrow_list):
        # print(borrow_list[j][1:3])
        # print([user_Logged[1], name])
        if borrow_list[j][1:3] == [user_Logged[2], name]:  # berarti dah pernah minjem gadget yang sama
            print('\nAnda tidak dapat meminjam gadget yang sama!')
            isPernahPinjam = True
            break
        else:
            j += 1
    if not (isPernahPinjam):
        date = input("Tanggal peminjaman: ")
        if check(date, 'tanggal'):
            n = input("Jumlah Peminjaman: ")
            if check(n, 'Jumlah'):
                while i < len(ref_list):
                    if id == ref_list[i][0]:
                        sum = int(ref_list[i][3]) - int(n)
                        if sum < 0:
                            print('Gadget tidak cukup')
                            return ref_list
                        else:
                            j = 0
                            while j < len(borrow_list):
                                j += 1
                            borrow = [str(j), user_Logged[2], ref_list[i][1], date, n]
                            global agbh_cus
                            agbh_cus.append(borrow)
                            ref_list[i][3] = str(sum)
                            print()
                            print("Item " + ref_list[i][1] + " (X" + n + ") berhasil dipinjam!")
                            return ref_list

                return ref_list  # INI SEMENTARA
            else:
                return ref_list
        else:
            print('\nTanggal tidak valid (MM/DD/YYYY), perhatikan tahun kabisat!')
            return ref_list
    else:
        return ref_list


def kembalikan(arr1, arr2, arr3):
    # arr1 : agbh, arr2 : agrh, arr3 : ag
    arr_IDGL = []  # inisialisasi ID Gadget List yang belum dikembalikan
    N1 = len(arr1)
    N2 = len(arr2)
    N3 = len(arr3)
    for i in range(1, N1):
        if arr1[i][5] == "False" and (arr1[i][2] not in arr_IDGL):
            arr_IDGL.append(arr1[i][2])
    no = 1
    if arr_IDGL == []:
        print("Tidak ada yang bisa dikembalikan")
    else:
        print()
        for IDG in arr_IDGL:
            for i in range(N3):
                if IDG == arr3[i][0]:
                    print(f"{no}. {arr3[i][1]}")
                    no += 1
        print()
        while True:
            np = int(input("Masukan nomor peminjaman: "))
            if np >= 1 and np <= (len(arr_IDGL)):
                break
            else:
                print("Masukan salah!")
        while True:
            tgl = input("Tanggal pengembalian: ")
            if check(tgl, 'tanggal'):
                break
            else:
                print("Masukan salah!")
        np = int(arr_IDGL[np - 1][1])
        jml = 0
        id_peminjaman = []
        for i in range(N1):
            if arr3[np][0] == arr1[i][2]:
                jml += int(arr1[i][4])
                id_peminjaman.append(arr1[i][0])
                arr1[i][5] = "True"
                arr3[np][3] = str(int(arr3[np][3]) + int(arr1[i][4]))
        id = N2
        idp = ""
        for i in range(len(id_peminjaman)):
            if i != (len(id_peminjaman) - 1):
                idp += id_peminjaman[i]
                idp += ","
            else:
                idp += id_peminjaman[i]
        arr_return = [f"R{id}", idp, tgl]
        arr2.append(arr_return)
        print(f"\nItem {arr3[np][1]} (x{jml}) telah dikembalikan.")
        return arr2


def riwayat(arr, mode):
    if mode == "p":  # pinjam (gadget)
        arr_rp = arr
        i = len(arr_rp) - 1
        if len(arr_rp) == 1:  # data kosong
            print("Tidak ada data peminjaman gadget.")
        else:  # len(arr_rp) != 1
            flag1 = True
            while flag1:
                flag2 = True
                for x in range(5):  # descending per 5 data
                    print(f"ID Peminjaman : {arr_rp[i][0]}")
                    print(f"Nama Pengambil : {arr_rp[i][1]}")
                    print(f"Nama Gadget : {arr_rp[i][2]}")
                    print(f"Tanggal Peminjaman : {arr_rp[i][3]}")
                    print(f"Jumlah : {arr_rp[i][4]} \n")
                    if i - 1 == 0:
                        flag1 = False
                        flag2 = False
                        break
                    else:
                        i -= 1
                while flag2:
                    tambahan = input("Tampilkan 5 data berikutnya? (Y/N) : ")
                    print()
                    if tambahan.lower() == 'n':
                        flag1 = False
                        flag2 = False
                    elif tambahan.lower() == 'y':
                        flag2 = False
                    else:
                        print("Masukan Salah! Silahkan Ulangi")
                if flag1 == False and flag2 == False:
                    break
    elif mode == "k":  # kembali (gadget)
        arr_rk = arr
        i = len(arr_rk) - 1
        if len(arr_rk) == 1:  # data kosong
            print("Tidak ada data pengembalian gadget.")
        else:  # len(arr_rk) != 1
            flag1 = True
            while flag1:
                flag2 = True
                for x in range(5):  # descending per 5 data
                    print(f"ID Pengembalian : {arr_rk[i][0]}")
                    print(f"Nama Pengambil : {arr_rk[i][1]}")
                    print(f"Tanggal Pengembalian : {arr_rk[i][2]} \n")
                    if i - 1 == 0:
                        flag1 = False
                        flag2 = False
                        break
                    else:
                        i -= 1
                while flag2:
                    tambahan = input("Tampilkan 5 data berikutnya? (Y/N) : ")
                    print()
                    if tambahan.lower() == 'n':
                        flag1 = False
                        flag2 = False
                    elif tambahan.lower() == 'y':
                        flag2 = False
                    else:
                        print("Masukan Salah! Silahkan Ulangi")
                if flag1 == False and flag2 == False:
                    break
    elif mode == "a":  # ambil (consumable)
        arr_ra = arr
        i = len(arr_ra) - 1
        if len(arr_ra) == 1:  # data kosong
            print("Tidak ada data pengambilan consumables.")
        else:  # len(arr_ra) != 1
            flag1 = True
            while flag1:
                flag2 = True
                for x in range(5):  # descending per 5 data
                    print(f"ID Pengambilan : {arr_ra[i][0]}")
                    print(f"Nama Pengambil : {arr_ra[i][1]}")
                    print(f"Nama Consumable : {arr_ra[i][2]}")
                    print(f"Tanggal Pengambilan : {arr_ra[i][3]}")
                    print(f"Jumlah : {arr_ra[i][4]} \n")
                    if i - 1 == 0:
                        flag1 = False
                        flag2 = False
                        break
                    else:
                        i -= 1
                while flag2:
                    tambahan = input("Tampilkan 5 data berikutnya? (Y/N) : ")
                    print()
                    if tambahan.lower() == 'n':
                        flag1 = False
                        flag2 = False
                    elif tambahan.lower() == 'y':
                        flag2 = False
                    else:
                        print("Masukan Salah! Silahkan Ulangi")
                if flag1 == False and flag2 == False:
                    break


def minta(arr1, arr2):
    # arr_m : ac
    # arr_ch : ach
    arr_m = arr1
    arr_ch = arr2
    found = False
    while not (found):
        id = input("Masukkan ID item: ")
        for i in range(1, len(arr_m)):
            if id.upper() == arr_m[i][0]:
                found = True
                r_idx = i  # pointer index consumable
        if found:
            break
        else:
            print("ID item tidak tersedia. Silakan Ulangi!")
    if int(arr_m[r_idx][3]) == 0 :
        print("Item sudah habis!")
        return arr_m, arr_ch
    else:
        while True:
            jml = int(input("Jumlah: "))
            if jml <= int(arr_m[r_idx][3]) and jml > 0:
                break
            elif jml > int(arr_m[r_idx][3]) and jml>0:
                print(f"Permintaan tidak dapat dipenuhi")
                print(f"Jumlah item tersisa : {arr_m[r_idx][3]}")
            else:
                print("Masukan tidak valid!")
        while True:
            tgl = input("Tanggal permintaan: ")
            if check(tgl, 'tanggal'):
                break
            else:
                print("Masukan salah!")
        print(f"Item {arr_m[r_idx][1]} (x{jml}) telah berhasil diambil!")
        arr_m[r_idx][3] = str(int(arr_m[r_idx][3]) - jml)
        id = f"CH{len(arr_ch)}"
        id_pengambil = user_Logged[0]
        id_consumable = arr_m[r_idx][0]
        arr = [id, id_pengambil, id_consumable, tgl, str(jml)]
        arr_ch.append(arr)
        # consumable history belum dimasukkan, sistem login dan identifikasi user belum ada
        return arr_m, arr_ch


def help(x):
    if x == "user":
        print(" ================== HELP ==================")
        print(" login - melakukan login ke dalam sistem")
        print(" carirarity - mencari gadget dengan rarity tertentu")
        print(" caritahun - mencari gadget berdasarkan tahun ditemukan")
        print(" pinjam - melakukan peminjaman gadget")
        print(" kembalikan - mengembalikan gadget secara seutuhnya")
        print(" minta - meminta consumable yang tersedia")
        print(" save - melakukan penyimpanan ke dalam file")
        print(" help - memberikan panduan penggunaan sistem")
    elif x == "admin":
        print(" ================== HELP ==================")
        print(" register - melakukan registrasi user baru")
        print(" login - melakukan login ke dalam sistem")
        print(" carirarity - mencari gadget dengan rarity tertentu")
        print(" caritahun - mencari gadget berdasarkan tahun ditemukan")
        print(" tambahitem - melakukan penambahan item")
        print(" hapusitem - menghapus suatu item pada database")
        print(" ubahjumlah - mengubah jumlah gadget dan consumable yang terdapat didalam sistem")
        print(" riwayatpinjam - melihat riwayat peminjaman gadget")
        print(" riwayatkembali - melihat riwayat pengembalian gadget")
        print(" riwayatambil - melihat riwayat pengambilan consumable")
        print(" save - melakukan penyimpanan ke dalam file")
        print(" help - memberikan panduan penggunaan sistem")

def exit(folder, owd):
    if au_def == au_cus and ag_def == ag_cus and ac_def == ac_cus and ach_def == ach_cus and agbh_def == agbh_cus and agrh_def == agrh_cus:
        print("\nTerima kasih sudah menggunakan Kantong Ajaib, Semoga harimu menyenangkan!")
    else:
        while True:
            Z = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
            if Z.lower() == 'y':
                save(folder, owd, au_cus, ag_cus, ac_cus, ach_cus, agbh_cus, agrh_cus)
                print("Saving...")
                time.sleep(1)
                print("Done!")
                print("Terima kasih sudah menggunakan Kantong Ajaib, Semoga harimu menyenangkan!")
                break
            elif Z.lower() == 'n':
                print("\nTerima kasih sudah menggunakan Kantong Ajaib, Semoga harimu menyenangkan!")
                break
            else:
                print("\nMasukkan salah, ulangi!")


def login():
    M = csv_reader("user.csv")
    found = False
    while not found:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ")
        for i in range(1, len(M)):
            if (M[i][1] == username) and (M[i][4] == password):
                print("\nLogin sukses, selamat datang %s\n" % M[i][2])
                global userID
                userID = username
                global userStatus
                userStatus = M[i][5]
                global user_Logged
                user_Logged = M[i]
                return True
        if not found:
            while True:
                a = input("Username atau password salah, ulangi login (y/n):  ")
                if a.lower() == 'n':
                    return False
                elif a.lower() == 'y':
                    break
                else:
                    print("Masukan salah!")

    # print(userID,userStatus) #Bisa


def register(arr):
    # arr_u : au_cus
    arr_u = arr
    found = True
    while found:
        nama = input("Masukkan nama: ").title().strip()
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        alamat = input("Masukkan alamat: ").title()
        unik = True  # Asumsi masukan awal unik
        for i in range(1, len(arr_u)):  # Validasi username dan password baru terhadap data lama
            if arr_u[i][1] == username:
                unik = False  # Tidak unik
                print("Username sudah tersedia, silakan daftar username lain!")
                break
        if unik == True:
            found = False  # Break loop while
    id = f"U{len(arr_u)}"
    arr_res = [id, username, nama, alamat, password, "user"]
    arr_u.append(arr_res)
    print("User berhasil diregistrasi!")
    return arr_u


def rarity():  # Berdasarkan spesifikasi, input pasti valid (C,B,A,S)
    N = csv_reader("gadget.csv")
    rarity = input(
        "Masukkan rarity: ").upper()  # Input rarity dipastikan selalu benar (C,B,A,S), code upper memaksa selalu kapital
    for i in range(1, len(N)):
        if rarity == N[i][4]:
            print("Hasil pencarian:")
            print("")
            print(f"Nama             : {N[i][0]}")
            print(f"Deskripsi        : {N[i][1]}")
            print(f"Jumlah           : {N[i][2]}")
            print(f"Rarity           : {N[i][3]}")
            print(f"Tahun Ditemukan  : {N[i][4]}")
            print("")


def caritahun():
    N = csv_reader("gadget.csv")
    tahun = input("Masukkan tahun: ")
    kategori = input("Masukkan kategori: ")
    # Array sementara penyimpanan data kategori
    arr = []
    if kategori == "=":
        for i in range(1, len(N)):
            if N[i][5] == tahun:
                arr.append(N[i])
    elif kategori == ">":
        for i in range(1, len(N)):
            if N[i][5] > tahun:
                arr.append(N[i])
    elif kategori == "<":
        for i in range(1, len(N)):
            if N[i][5] < tahun:
                arr.append(N[i])
    elif kategori == ">=":
        for i in range(1, len(N)):
            if N[i][5] >= tahun:
                arr.append(N[i])
    elif kategori == "<=":
        for i in range(1, len(N)):
            if N[i][5] <= tahun:
                arr.append(N[i])
    # Proses array sementara yang menyimpan kategori yang diinginkan
    for i in range(len(arr)):
        print("Hasil pencarian:")
        print("")
        print(f"Nama             : {arr[i][1]}")
        print(f"Deskripsi        : {arr[i][2]}")
        print(f"Jumlah           : {arr[i][3]}")
        print(f"Rarity           : {arr[i][4]}")
        print(f"Tahun Ditemukan  : {arr[i][5]}")
        print("")


def write_to_csv(arr, filename):  # fungsi khusus array to csv
    l1 = len(arr)
    l2 = len(arr[0])
    for i in range(l1):  # jumlah data
        if i == 0:
            s = "w"
            string = ""
        else:
            s = "a"
            string = "\n"
        for j in range(l2):
            string += arr[i][j]
            if j != (l2 - 1):
                string += ";"
        csv_writer(filename, string, s)  #


def save(fldr, OWD, au, ag, ac, ach, agbh, agrh):
    os.chdir(OWD)  # kembali ke folder sebelumnya
    f_path = f"{OWD}/{fldr}"  # folder path
    if not (os.path.exists(f_path)):  # folder tujuan tidak ada
        os.mkdir(f_path)  # membuat folder
    os.chdir(f_path)  # pindah ke folder tujuan
    check(f_path, "files")  # mengecek file (akan dibuatkan csv jika tidak ada)
    write_to_csv(au, "user.csv")
    write_to_csv(ag, "gadget.csv")
    write_to_csv(ac, "consumable.csv")
    write_to_csv(ach, "consumable_history.csv")
    write_to_csv(agbh, "gadget_borrow_history.csv")
    write_to_csv(agrh, "gadget_return_history.csv")


def getowd():
    return os.getcwd()


def load():
    parser = argparse.ArgumentParser(usage="python tfile.py <nama_folder>")
    parser.add_argument("nama_folder")
    try:
        args = parser.parse_args()
    except SystemExit:
        print()
        print("| Tidak ada nama folder yang diberikan!")
        print("| Usage: python tfile.py <nama_folder>")
        quit(0)
    else:
        folder = args.nama_folder
        path = f"{os.getcwd()}\{folder}"  # os.getcwd() menghasilkan current working directory
        try:
            os.chdir(path)  # change current working directory
        except FileNotFoundError:
            print("Folder tidak ditemukan!")
            quit(0)
        else:
            return folder


# MAIN PROGRAM
owd = getowd()  # original working directory
current_folder = load()  # loading data
check(os.getcwd(), "files")
# def : default, cus : customized
au_def = csv_reader("user.csv")  # inisialisasi array user
au_cus = csv_reader("user.csv")
ag_def = csv_reader('gadget.csv')  # inisialisasi array gadget
ag_cus = csv_reader('gadget.csv')
ac_def = csv_reader('consumable.csv')  # inisialisasi array consumable
ac_cus = csv_reader('consumable.csv')
ach_def = csv_reader("consumable_history.csv")  # inisialisasi array consumable history
ach_cus = csv_reader("consumable_history.csv")
agbh_def = csv_reader("gadget_borrow_history.csv")  # inisialisasi array gadget borrow history
agbh_cus = csv_reader("gadget_borrow_history.csv")
agrh_def = csv_reader("gadget_return_history.csv")  # inisialisasi array gadget return history
agrh_cus = csv_reader("gadget_return_history.csv")

isLoggedIn = False
isAdmin = False
while True:
    a = input(">>> ")
    if a == 'login':
        if not isLoggedIn:
            userStatus = None
            isLoggedIn = login()
            if userStatus == 'admin':
                isAdmin = True
        else:
            print("Anda sudah log in")
    elif a == 'register':  # akses : Admin
        if isLoggedIn and isAdmin:
            au_cus = register(au_cus)
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == 'pinjam':  # akses : user
        if isLoggedIn and not isAdmin:
            pinjam()
            print(agbh_cus)  # buat ngetes apa udah ke update agbh_cus-nya
        elif isLoggedIn and isAdmin:
            print("Anda Admin, akses ini hanya untuk user")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == 'ubahjumlah':  # akses : admin
        if isLoggedIn and isAdmin:
            new_list = ubahjumlah()
            try:
                if len(new_list[0]) == 6: #berarti gadget
                    ag_cus = new_list
                else:
                    ac_cus = new_list
            except:
                pass
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn) or not(isAdmin):
            print("Anda belum login")
    elif a == 'hapusitem':  # akses : admin
        if isLoggedIn and isAdmin:
            new_list = hapusitem()
            try:
                if len(new_list[0]) == 6:
                    ag_cus = new_list
                else:
                    ac_cus = new_list
            except:
                pass
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == 'tambahitem':  # akses : admin
        if isLoggedIn and isAdmin:
            new_item = tambahitem()
            if len(new_item) == 6:  # gadget
                ag_cus.append(new_item)
            elif len(new_item) == 5:  # consumable
                ac_cus.append(new_item)
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
   
    elif a == "minta":  # akses : user
        if isLoggedIn and not isAdmin:
            ac_cus, ach_cus = minta(ac_cus, ach_cus)
        elif isLoggedIn and isAdmin:
            print("Anda admin, akses ini hanya untuk user")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "riwayatambil":  # akses : admin
        if isLoggedIn and isAdmin:
            riwayat(ach_def, "a")
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "riwayatpinjam":  # akses : admin
        if isLoggedIn and isAdmin:
            riwayat(agbh_def, "p")
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "riwayatkembali":  # akses : admin
        if isLoggedIn and isAdmin:
            riwayat(agrh_def, "k")
        elif isLoggedIn and not isAdmin:
            print("Anda user, akses ini hanya untuk admin")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "kembalikan":  # akses : user
        if isLoggedIn and not isAdmin:
            agrh_cus = kembalikan(agbh_cus, agrh_cus, ag_cus)
        elif isLoggedIn and isAdmin:
            print("Anda admin, akses ini hanya untuk user")
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "carirarity":  # akses : admin, user
        if isLoggedIn:
            rarity()
        else:  # not(isLoggedIn)
            print("Anda belum login")
    elif a == "caritahun":  # akses : admin, user
        if isLoggedIn:
            caritahun()
        else:
            print("Anda belum login")
    elif a == "help":  # akses : user,admin
        if isLoggedIn:
            x = userStatus
            help(x)
        else:
            print("Anda belum login")
    elif a == "save":  # akses : user, admin
        if isLoggedIn:
            fldr_input = input("Masukkan nama folder penyimpanan: ")
            save(fldr_input, owd, au_cus, ag_cus, ac_cus, ach_cus, agbh_cus, agrh_cus)
            au_def = csv_reader("user.csv")
            ag_def = csv_reader("gadget.csv")
            ac_def = csv_reader('consumable.csv')
            ach_def = csv_reader("consumable_history.csv")
            agbh_def = csv_reader("gadget_borrow_history.csv")
            agrh_def = csv_reader("gadget_return_history.csv")
            current_folder = fldr_input
            print("Saving...")
            time.sleep(1)
            print(f"Data telah disimpan pada folder {fldr_input}!")
        else:
            print("Anda belum login")
    elif a == "exit":
        exit(current_folder, owd)
        break
