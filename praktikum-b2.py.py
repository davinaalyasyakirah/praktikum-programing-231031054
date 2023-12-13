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
