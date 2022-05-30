# while True:
#    print('Salom')
'''
i = 10
while i <= 10:
    print('Og`abek')
    i += 1
'''
print('Hello', 'world')
print('Hello', 'world', sep = '!', end = ' ! ')

i = 1
while i <= 10:
    print('Salom', i)
    i += 1

c = 'Salom Dunyo!!!'
for a in c:
#    print(a, end=' ')
    if a == ' ':
        continue
    print(f' "{a}" ', end='')
print("\n")
for i in 'Salom Dunyo!':
    if i == 'n':
        break
    print(i, end=' ')
else:
    print('\nNo spaces')

