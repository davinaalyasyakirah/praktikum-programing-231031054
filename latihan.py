vd = {'key1' : 'Nilai 1',
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3',
      }
print(vd)
# mengakses data
print(vd.get('key1'))
print(vd['key1'])
print('\n'*2)
data = {'nama' : 'Thomas',
        'nim'  : 'B2311109',
        'lulus': False
        }
print(data)
# mengakses data
print('NAMA: ',data['nama'])
print('NIM : ',data['nim'])

# mengupdate dan menambah data
data['nama'] = 'Dimas'  # update
data['Nama'] = 'Dimas'  # tambah data
print(data)

del data['nim']
# data.update({'nama':'Dimas'})
print(data)

print('NAMA: ',data['nama'])

kuliah = {'nama'   : 'Thomas',
          'nim'    : 'B2311108',
          'matkul' : {'mk1' : 'Pemrograman',
                      'mk2' : 'Kalkulus Dasar',
                      'mk3' : 'Agama',
                      }
          }
print(kuliah['matkul']['mk3']) #mengambil matkul ke 3


print(kuliah['matkul'].keys()) #cek semua keys di dalam matkul
kuliah['matkul']['mk4'] = 'Sains Terpadu'

print(kuliah['matkul'])
print(kuliah['matkul'].values()) #cek semua nilai dalam matkul

# print(kuliah.has_key("nama"))
# kuliah['nim'] = [',']
print(kuliah.items())
print(kuliah)
