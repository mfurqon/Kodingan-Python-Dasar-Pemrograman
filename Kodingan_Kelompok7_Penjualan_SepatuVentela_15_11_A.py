nama_pembeli = input('Masukkan nama pembeli: ')
jumlah_item = int(input('Jumlah item: '))
#Append List
kode = []
banyak_produk = []
tipe = []
harga = []
jumlah = []

#Perulangan  berhenti ketika jumlah perulangan input sesuai dengan jumlah item
i = 0
while i < jumlah_item:
    print('Produk Ke-', i+1)
    kode.append(input('Kode Item (VPL/VPH/VEL/VEH/VRL):'))
    banyak_produk.append(int(input('Banyak Produk: ')))

    if kode[i]=='VPL' or kode [i]== 'vpl':
       tipe.append('Ventela Public Low')
       harga.append('250000')
       jumlah.append(banyak_produk [i] * int('250000'))
    elif kode[i]=='VPH' or kode [i]== 'vph':
       tipe.append('Ventela Public High')
       harga.append('230000')
       jumlah.append(banyak_produk [i] * int('230000'))
    elif kode[i]=='VEL' or kode [i]== 'vel':
       tipe.append('Ventela Ethnic Low')
       harga.append('150000')
       jumlah.append(banyak_produk [i] * int('150000'))
    elif kode[i]=='VEH' or kode [i]== 'veh':
       tipe.append('Ventela Ethnic High')
       harga.append('160000')
       jumlah.append(banyak_produk [i] * int('160000'))
    elif kode[i]=='VRL' or kode [i]== 'vrl':
       tipe.append('Ventela Republic Low')
       harga.append('180000')
       jumlah.append(banyak_produk [i] * int('180000'))
    else:
       tipe.append('Kode Tidak Valid')
       harga.append('0')
       jumlah.append(banyak_produk [i] * int('0'))
    i = i + 1

#List product
print('\t\t\t         SELAMAT DATANG DI TOKO SEPATU VENTELA')
print('\t\t\t\t   ' + '-' * 33)
print('\t\t\t                  List Product Item')
print('\t\t\t   ' + '-' * 48)
print('\t\t\t   | Kode Item |      Nama Item       |   Harga   |')
print('\t\t\t   ------------------------------------------------')
print('\t\t\t   |    VPL    | Ventela Public Low   | Rp 250000 |')
print('\t\t\t   |    VPH    | Ventela Public High  | Rp 230000 |')
print('\t\t\t   |    VEL    | Ventela Ethnic Low   | Rp 150000 |')
print('\t\t\t   |    VEH    | Ventela Ethnic High  | Rp 160000 |')
print('\t\t\t   |    VRL    | Ventela Republic Low | Rp 180000 |')
print('\t\t\t   '+'-' * 48) 
print('TOKO SEPATU VENTELA')
#Tanggal dan waktu beli
import datetime
now = datetime.datetime.now()
tanggal = now.strftime("%d-%m-%Y")
jam = now.strftime("%H:%M:%S")
print('Tanggal\t:', tanggal)
print('Waktu\t:', jam)
print('-' * 97)
print("|\tNo.\t|\t\tTipe\t\t|\tHarga\t|\tBanyak\t|\tJumlah\t|")
print('|\t\t|\t\tProduk\t\t|\tSatuan\t|\tBeli\t|\tHarga\t|')
print('-' * 97)

#Perulangan berhenti ketika perulangan list produk yang dibeli sesuai dengan jumlah item
a = 0
while a < jumlah_item:
    print('\t%i\t\t%s\t\t%s\t\t%i \t\t%i' % (a+1, tipe[a], harga[a], banyak_produk[a], jumlah[a]))
    a = a + 1
print('-' * 97)

#Print nama pembeli, subtotal, total, pajak, diskon, total bayar
subtotal = sum(jumlah)
print('Nama Pembeli\t\t\t\t\t:\t'+nama_pembeli)
print('Subtotal \t\t\t\t\t:\tRp {:,}'.format(int(subtotal)).replace(',','.'))
pajak = subtotal * 0.1
total = subtotal + pajak
print('Pajak 10% \t\t\t\t\t:\tRp {:,}'.format(int(pajak)).replace(',','.'))
if total > 400000:
   diskon = total * (5/100)
   setelah_diskon = total - diskon
   print('Potongan harga 5%\t\t\t\t: \tRp {:,}'.format(int(diskon)).replace(',','.'))
   print('Total bayar\t\t\t\t\t: \tRp {:,}'.format(int(setelah_diskon)).replace(',','.'))
elif total > 700000:
   diskon = total * (15/100)
   setelah_diskon = total - diskon
   print('Potongan harga 15%\t\t\t\t: \tRp {:,}'.format(int(diskon)).replace(',','.'))
   print('Total bayar\t\t\t\t\t: \tRp {:,}'.format(int(setelah_diskon)).replace(',','.'))
else:
    diskon = 0
    setelah_diskon = total
    print('Potongan harga 0%\t\t\t\t: \tRp {:,}'.format(int(diskon)).replace(',','.'))
    print('Total bayar\t\t\t\t\t: \tRp {:,}'.format(int(setelah_diskon)).replace(',','.'))
    
#Pilihan metode pembayaran; uang tunai, debit, kredit, gopay, dana, ovo
pilihan = input('Metode pembayaran\nTunai/Debit/Kredit/Gopay/Dana/Ovo\t\t:\t')
if pilihan == 'TUNAI' or pilihan == 'tunai':
   cash = int(input('Pembayaran uang tunai\t\t\t\t:\t'))
   print('Uang tunai\t\t\t\t\t: \tRp {:,}'.format(int(cash)).replace(',','.'))
   if cash < setelah_diskon:
      print('Uang anda tidak mencukupi')
   elif cash > setelah_diskon:
      kembali = cash - setelah_diskon
      print('Kembali\t\t\t\t\t\t:\tRp {:,}'.format(int(kembali)).replace(',','.'))
   else:
      uang_pas = 0
      print('Kembali\t\t\t\t\t\t:\tRp {:,}'.format(int(uang_pas)).replace(',','.'))
elif pilihan == 'DEBIT' or pilihan == 'debit':
   no_kartu = input('Masukkan No. Kartu\t\t\t\t:\t')
   kartu = input('Masukkan jenis kartu\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pembeli)
   print('Pembayaran akan ditanggungkan ke No. Kartu\t:\t'+no_kartu)
   if kartu == 'BCA' or kartu == 'bca':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BCA')
   elif kartu == 'BRI' or kartu == 'bri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BRI')
   elif kartu == 'BNI' or kartu == 'bni':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BNI')
   elif kartu == 'MANDIRI' or kartu == 'mandiri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - MANDIRI')
   elif kartu == 'BSI' or kartu == 'bsi':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BSI')
   else:
      print('Jenis kartu\t\t\t\t\t:\tTidak valid')
elif pilihan == 'KREDIT' or pilihan == 'kredit':
   no_kartu = input('Masukkan No. Kartu\t\t\t\t:\t')
   kartu = input('Masukkan jenis kartu\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pembeli)
   print('Pembayaran akan ditanggungkan ke No. Kartu\t:\t'+no_kartu)
   if kartu == 'BCA' or kartu == 'bca':
      print('Jenis kartu\t\t\t\t\t:\tKredit - BCA')
   elif kartu == 'BRI' or kartu == 'bri':
      print('Jenis kartu\t\t\t\t\t:\tKredit - BRI')
   elif kartu == 'BNI' or kartu == 'bni':
      print('Jenis kartu\t\t\t\t\t:\tKredit - BNI')
   elif kartu == 'MANDIRI' or kartu == 'mandiri':
      print('Jenis kartu\t\t\t\t\t:\tKredit - MANDIRI')
   elif kartu == 'BSI' or kartu == 'bsi':
      print('Jenis kartu\t\t\t\t\t:\tKredit - BSI')
   else:
      print('Jenis kartu\t\t\t\t\t:\tTidak valid')
       
elif pilihan == 'GOPAY' or pilihan == 'gopay':
   no_telepon_gopay = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran Gopay dengan atas nama\t\t:\t'+nama_pembeli)
   print('No. Telepon Gopay\t\t\t\t:\t'+no_telepon_gopay)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')

elif pilihan == 'DANA' or pilihan == 'dana':
   no_telpon_dana = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran Dana dengan atas nama\t\t:\t'+nama_pembeli)
   print('No. Telepon Dana\t\t\t\t:\t'+no_telpon_dana)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')

elif pilihan == 'OVO' or pilihan == 'ovo':
   no_telpon_ovo = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran OVO dengan atas nama\t\t\t:\t'+nama_pembeli)
   print('No. Telepon Dana\t\t\t\t:\t'+no_telpon_ovo)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')
else:
    print('Metode pembayaran tidak valid')

print('-' * 97)
print('\t\t\t     Terima kasih telah berbelanja di toko kami')
