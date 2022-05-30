a = int(input('Kalkulyatorga xush kelibsiz!\nBirinchi raqamni kiriting:')) 

b = int(input('Ikkinchi raqamni kiriting:')) 

c = input('/ * + - ni kiriting:')

# print(a, b, c)

#aa = a.isdigit()

#bb = b.isdigit()

#if aa == False and bb == False:
 #   print('Siz raqamni noto`g`ri kiritdingiz.' )
#el
if c =='+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c =='/':    
    print(a/b)
elif c =='*':
    print(a*b)
else:
    print('Amallarni noto`gri kiritdingiz.')
