nama_pelanggan = input('Masukkan nama pelanggan: ')
jumlah_item = int(input('Jumlah item: '))
kode = []
banyak_produk = []
tipe = []
harga = []
jumlah = []

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

print('    SELAMAT DATANG DI TOKO SEPATU VENTELA')
print('    ' + '-' * 37)
print(' ' * 15 + 'List Product Item')
print('-' * 48)
print('| Kode Item |      Nama Item       |   Harga   |')
print('------------------------------------------------')
print('|    VPL    | Ventela Public Low   | Rp 250000 |')
print('|    VPH    | Ventela Public High  | Rp 230000 |')
print('|    VEL    | Ventela Ethnic Low   | Rp 150000 |')
print('|    VEH    | Ventela Ethnic High  | Rp 160000 |')
print('|    VRL    | Ventela Republic Low | Rp 180000 |')
print('-' * 48) 
print('TOKO SEPATU VENTELA')
import datetime
now = datetime.datetime.now()
tanggal = now.strftime("%d-%m-%Y")
jam = now.strftime("%H:%M:%S")
print('Tanggal\t:\t', tanggal)
print('Waktu\t:\t', jam)
print('-' * 99)
print("|\tNo.\t|\t\tTipe\t\t|\tHarga\t|\tBanyak\t|\tJumlah\t|")
print('|\t\t|\t\tProduk\t\t|\tSatuan\t|\tBeli\t|\tHarga\t|')
print('-' * 99)

a = 0
while a < jumlah_item:
    print('\t%i\t\t%s\t\t%s\t\t%i \t\t%i' % (a+1, tipe[a], harga[a], banyak_produk[a], jumlah[a]))
    a = a + 1
print('-' * 99)
subtotal = sum(jumlah)
print('Subtotal \t\t\t\t\t:\tRp {:,}'.format(int(subtotal)).replace(',','.'))
pajak = subtotal * 0.1
total = subtotal + pajak
print('Pajak 10% \t\t\t\t\t:\tRp {:,}'.format(int(pajak)).replace(',','.'))
#print('Total :\t\tRp.', total)
if total < 700000:
   diskon = total * (5/100)
   setelah_diskon = total - diskon
   print('Potongan harga 5%\t\t\t\t: \tRp {:,}'.format(int(diskon)).replace(',','.'))
   print('Total bayar\t\t\t\t\t: \tRp {:,}'.format(int(setelah_diskon)).replace(',','.'))
else:
   diskon = total * (15/100)
   setelah_diskon = total - diskon
   print('Potongan harga 15%\t\t\t\t: \tRp {:,}'.format(int(diskon)).replace(',','.'))
   print('Total bayar\t\t\t\t\t: \tRp {:,}'.format(int(setelah_diskon)).replace(',','.'))

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
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pelanggan)
   print('Pembayaran akan ditanggungkan ke No. Kartu\t:\t'+no_kartu)
   if kartu == 'BCA' or kartu == 'bca':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BCA')
   elif kartu == 'BRI' or kartu == 'bri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BRI')
   elif kartu == 'BNI' or kartu == 'bni':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BNI')
   elif kartu == 'MANDIRI' or kartu == 'mandiri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - MANDIRI')
   else:
      print('Jenis kartu\t\t\t\t\t:\tDebit - BSI')
      
elif pilihan == 'KREDIT' or pilihan == 'kredit':
   no_kartu = input('Masukkan No. Kartu\t\t\t\t:\t')
   kartu = input('Masukkan jenis kartu\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pelanggan)
   print('Pembayaran akan ditanggungkan ke No. Kartu\t:\t'+no_kartu)
   if kartu == 'BCA' or kartu == 'bca':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BCA')
   elif kartu == 'BRI' or kartu == 'bri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BRI')
   elif kartu == 'BNI' or kartu == 'bni':
      print('Jenis kartu\t\t\t\t\t:\tDebit - BNI')
   elif kartu == 'MANDIRI' or kartu == 'mandiri':
      print('Jenis kartu\t\t\t\t\t:\tDebit - MANDIRI')
   else:
      print('Jenis kartu\t\t\t\t\t:\tDebit - BSI')

elif pilihan == 'GOPAY' or pilihan == 'gopay':
   no_telepon_gopay = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pelanggan)
   print('No. Telepon Gopay\t\t\t\t:\t'+no_telepon_gopay)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')

elif pilihan == 'DANA' or pilihan == 'dana':
   no_telpon_dana = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pelanggan)
   print('No. Telepon Dana\t\t\t\t:\t'+no_telpon_dana)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')

else:
   no_telpon_ovo = input('Masukkan No. Telepon\t\t\t\t:\t')
   id_transaksi = input('Masukkan ID Transaksi\t\t\t\t:\t')
   print('Pembayaran dengan atas nama\t\t\t:\t'+nama_pelanggan)
   print('No. Telepon Dana\t\t\t\t:\t'+no_telpon_ovo)
   print('ID Transaksi\t\t\t\t\t:\t'+id_transaksi)
   print('Status pembayaran\t\t\t\t:\tBerhasil')

print('-' * 99)
print('Thank you for bringing happiness to us. We hope you feel that too. Enjoy the package',nama_pelanggan)
