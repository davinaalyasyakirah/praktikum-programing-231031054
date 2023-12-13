nama = 'DAVINA ALYA SYAKIRAH'
nim  = '231031054'
meet = 'Praktikum 4 B'
prodi = 'Sistem Informasi B'
email = 'davinaaismail@gmail.com'
tgl = '11 Oktober 2023'
sp = 40
print (len(nama))
print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp)+f'\r{meet}')
print(prodi.rjust(sp))
print(email.rjust(sp)+f'\r{tgl}')
print('-'*sp)

paragraf = '''Halo, selamat datang perkenalkan nama saya {} dengan NIM {} dari prodi {}. Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

print('# --------8+++++++++')
x = 9
hasil = x>8
print(x,'hasilnya adalah',hasil)

print('# --------8+++++++++')
x = 9
hasil = x<8
print(x,'hasilnya adalah',hasil)

print('--------4+++++++++8---------')
x = 5
hasil = x<8>4
print(x,'hasilnya adalah',hasil)

print('++++++++4--------8+++++++++')
x = 9
# cek1 = x<4 true
hasil = x<8>4
# cek2 = x>8 false
print(x,'hasilnya adalah',hasil)
# cetak hasil
print('++++++++4--------8+++++++++')
x = 2
hasil = x<8>4
print(x,'hasilnya adalah',hasil)



