print('praktikum-1')
print('Nama Lengkap: Davina Alya Syakirah')
print('NIM         : 231031054')
print('Prodi       : Sistem Informasi')
print()
angkatan = 2023
print('Angkatan adalah '+str(angkatan))

print()
a=20
print('data adalah',a)
print('Tipe data adalah',type(a))

print()
b=20.0
print('data adalah',b)
print('Tipe data adalah',type(b))

print()
kampus='Institut Teknologi BJ Habibie'
print('data adalah',kampus)
print('Tipe data adalah',type(kampus))

print()
log= False
print('Data adalah',log)
print('Tipe data adalah',type(log))

print()
c = complex(2,3)
print('Data adalah',c)
print('Tipe data dalah',type (c))

print()
p=10
q=5
hasil = p+q
print('Hasil',p,'+',q,'=',hasil)

print()
p=10
q=5
hasil = p-q
print('Hasil',p,'-',q,'=',hasil)

print()
p=10
q=5
hasil = p*q
print('Hasil',p,'*',q,'=',hasil)

print()
p=10
q=5
hasil = p/q
print('Hasil',p,'/',q,'=',hasil)

print()
p=10
q=5 
hasil = p%q
print('Hasil',p,'%',q,'=',hasil)

print()
p=10
q=5
hasil = p**q
print('Hasil',p,'**',q,'=',hasil)

print()
p=10
q=5
hasil = p//q
print('Hasil',p,'//',q,'=',hasil)

######################################
print()
bi = False
print('Nilai bi menjadi=',bi)
bi |= True
print('Nilai bi|= true menjadi=',bi)

print()
bi = False
print('Nilai bi menjadi=',bi)
bi &= True
print('Nilai bi&= true menjadi=',bi)

print()
bi = True
print('Nilai bi menjadi=',bi)
bi ^= True
print('Nilai bi^= true menjadi=',bi)

######################################
print()
a = 7
print('Nilai adalah a=',a)

hasil = a == 7
print('Apakah a=7 ?', hasil)
hasil = a>7
print('Apakah a>7 ?', hasil)
hasil = a<7
print('Apakah a<7 ?', hasil)
hasil = a != 7
print('Apakah a!=7 ?', hasil)
hasil = a >= 7
print('Apakah a>=7 ?', hasil)
hasil = a <= 7
print('Apakah a!=7 <', hasil)

######################################
print()
a = True
b = False

hasil = a and a
print(a,'and',a,'adalah=',hasil)
hasil = a and b
print(a,'and',b,'adalah=',hasil)
hasil = b and a
print(b,'and',a,'adalah=',hasil)
hasil = b and b
print(b,'and',b,'adalah=',hasil)

print()
hasil = a or a
print(a,'or',a,'adalah=',hasil)
hasil = a or b
print(a,'or',b,'adalah=',hasil)
hasil = b or a
print(b,'or',a,'adalah=',hasil)
hasil = b or b
print(b,'or',b,'adalah=',hasil)

print()
hasil = a ^ a
print(a,'xor',a,'adalah=',hasil)
hasil = a ^ b
print(a,'xor',b,'adalah=',hasil)
hasil = b ^ a
print(b,'xor',a,'adalah=',hasil)
hasil = b ^ b
print(b,'xor',b,'adalah=',hasil)

print()
hasil = not  a
print('not',a,'adalah=',hasil)
hasil = not b
print('not',b,'adalah=',hasil)
