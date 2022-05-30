ism = 'Og`abek'
yosh = 11
yil = 2011
oy = "May"
kun = 29
print('Mening ismim ' +ism + '. Salom, men ' + str(yosh) + ' yoshdaman.')
print('Men %(yil)d yil %(kun)d - %(oy)s da tug`ilganman' %{'yil': yil, 'kun': kun, 'oy': oy})
print('Mening ismim %s. Men %d yoshdaman.' %(ism, yosh))
print('Mening ismim %s. Men %d yoshdaman.' %('Husan', yosh))
print('Narsa: %s narxi: %0.2f so`m.' %('daftar', 12000))
print('Mening ismim {}. Men {} yoshdaman.' .format(ism, yosh))
print('Mening ismim {0}. Men {0} {1} yoshdaman.' .format(ism, yosh))
print('Mening ismim {ism}. Men {yosh} yoshdaman.' .format(ism=ism, yosh=yosh))
print(f'Mening ismim {ism}. Yoshim {yosh} da. Endigi yili {yosh + 1} yoshda bo`laman.')
print('5 + 2 = {}' .format(5 + 2))
print(f'5 + 2 = {5 + 2}')
