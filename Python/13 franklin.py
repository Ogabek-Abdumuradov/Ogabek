
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



print('\n15-Dars ')
sum = 0
for r in range(0, 10):
    for y in range(0, 10):
        z = f'{r}' + f'{y}'
        sum = sum + int(z)
        print(z, ' ', end = '')
    print(r, 'aylanish', sum)

fact = 0
  
for i in range(1, 10):
    fact = fact + i
      
print ("1 dan 9 qo'shilgan sonlar : ",end="")
print (fact)






