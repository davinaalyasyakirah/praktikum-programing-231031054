nim = [2,3,1,0,3,1,0,5,4]
print(nim)
# akses item
print('item indeks:0',nim[0])
print('item indeks:3',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6]',nim[-6])
print('item indeks 5: [-4]',nim[-4])
print('item indeks -7: [2]',nim[2])
print('item indeks 2: [-7]',nim[-7])
# akses indeks batas
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3,....: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:-1]}')
print(f'item indeks [:8]: {nim[:-1]}')
# pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:-5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# nested list 
kelas = [('Matkul1',2),
         ('Matkul2',3)]
print(kelas)
kelas.append(('Matkul3',2))
print(kelas)
# tambahan matkul 4 dan 5 dan sksnya

# mata kuliah 1: Matkul1 dengan 2 sks
# mata kuliah 2: Matkul2 dengan 3 sks
# mata kuliah 3: Matkul3 dengan 2 sks
# mata kuliah 4: Matkul4 dengan .. sks
# mata kuliah 5: Matkul5 dengan .. sks

data = [('Davina Alya Syakirah',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem INformasi B','Ganjil')]

# nama mahasiswa: Davina Alya Syakirah
# inisial Davina Alya Syakirah: DAS
# nim Davina Alya Syakirah: 231031054
# program Davina Alya Syakirah: S1-Reguler Sistem Informasi B
# angkatan Davina Alya Syakirah: Ganjil-2023
# total sks Davina Alya Syakirah: 11
# jumlah nilai Davina Alya Syakirah: 5
# nilai tertinggi Davina Alya Syakirah: 99
# nilai terendah Davina Alya Syakirah: 76
# rata-rata nilai Davina Alya Syakirah: 92.25

