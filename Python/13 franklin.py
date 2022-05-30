
##########################################################################################################
# 13-Dars
'''
while True:
    print('Salom')
'''

i = 1
while i <= 10:
    print('Salom', i)
    i += 1

a = 'Hello'; b = 'world!'
print(a, b, sep = '!', end = ' ! \n')

c = 'Ruchka men sen u biz'
for i in c:
    print(i, end = '')
    if i == ' ':
        continue
    print(f' Matn ichida {i}', end = "|")

print('\nfor bilan if ni ishlashi')

for a in 'Hello world!':
    if a == " ":
        print(f'\'{a}\'', end = "|")
        break
    else:
        print(f'\n \'{a}\' Bu belgi yo\'q')




