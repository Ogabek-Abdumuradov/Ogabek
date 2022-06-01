################################################
# 14-Dars
'''
i = 15
a = 100

while i <= a:
    print('Hello world!', i)
    i += 1
else:
    print('qilindi')
'''

royxat = [1, 2, 'so`z', ['Og`abek', 'jiloviq'], 45, True, False]
l2 = list('salom')
l3 = list((1, 2, 3))
l4 = [i for i in 'salom']
l5 = [i for i in 'salom dunyo' if i != ' ' and i != 'd']
l6 = [i for i in 'salom dunyo' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
l7 = list(range(0, 11))
for k in range(1, 3):
    print(f'Tashqi sanash #{k}')    
print(royxat, l2, l3, l4, l5, l6, l7, sep='\n')
for j in range(1, 3):
    print(f'\t range bilan sanash #{j}')
"""
ss = 'hello' 'world'
print(ss)

c = 'Sen'
a = 'Men'
s = 123
# p = 'String'
print('String', 101, 12.5, c, a, s)
"""

z = 'Laylak keldi'
for karam_bobo in z:
    print(karam_bobo, end = '')

muniranisevaman = True
royxat1 = ['Kitob', 'daftar', 'ruchka', 'qalam', muniranisevaman]
# print(royxat1)

ogabek = list('Munira')
tel = list((99, 156, 12, 23))
ozod = [quyon for quyon in 'Ozodbek']
print(royxat1, ogabek, tel, ozod, sep = '\n')

print(list(range(10)))
print(list(range(2, 9)))
print(list(range(1963, 2023)))
print(list(range(1963, 2023, 2)))
print(list(range(1963, 2023, -1)))
print(list(range(1963, 2023, -2)))
