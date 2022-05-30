print(3 == 3)
print(3 < 4)
print(3 > 2)
print(5 < 4)
print(9 > 10)
x = 0
if x:
    print('x rost')
else:
    print('x yolg`on')
if 0:            
    print('1 rost')
else:
    print('0 yolg`on')


lampa = input('Svitaforning rangini kiriting: ')

if lampa == 'qizil':
    print('svitaforda qizil')
elif lampa == 'yashil':
    print('svitaforda yashil')
elif lampa == 'sariq':
    print('svitaforda sariq')
else:
    print('bunaqa rang yo`q')

yosh = int(input('Yoshingiz nechada?  '))
if yosh >= 11:
    print('Sizni o`qishga qabul qilamiz!')
else:
    print(f'Sur bo`ttan! Yoshing {yosh} da.\
           \n {11-yosh} yildan keyin kelasan.')
'''
a = 10
b = 5
print("a | b =", a | b)
'''
vaqt = int(input('Vaqtni kiriting: '))
if vaqt < 12 or vaqt > 13:
    print('Xush kelibsiz!')
else:
    print('Yopiq')
    
