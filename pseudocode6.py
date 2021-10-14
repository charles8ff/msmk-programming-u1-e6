
num1 = 0
num2 = 0
aux = 0
cont = 0
sumaImp = 0

num1, num2 = input('Introduzca dos números:\n\t>>').split()
print('\n-----------------------------------')
num1 = int(num1)
num2 = int(num2)
if (num1 > num2):
    aux = num2
    num2 = num1
    num1 = aux
else:
    aux = num1
aux = aux +1
while (aux < num2):
    print (str(aux) +', ')
    if (aux %2 == 0):
        cont =cont+1
    else:
        sumaImp = sumaImp + aux
    aux = aux +1
aux = num2-num1

print('\nLos números naturales comprendidos entre '+str (num1) +' y ' + str(num2) + ' son: '+ str(aux) +'.\n')
print('Los números pares comprendidos entre '+str (num1) +' y ' + str(num2) + ' son: '+ str(cont) +'.\n')
print('La suma de los impares comprendidos entre '+str (num1) +' y ' + str(num2) + ' es: '+ str(sumaImp) +'.\n')

