#declare variables
num1 = 0
num2 = 0
aux = 0
cont = 0
sumaImp = 0
#input
num1, num2 = input('Introduzca dos números:\n\t>> ').split()#splits inputs
print('\n-----------------------------------')#just for clarity
num1 = int(num1)#change from char to int
num2 = int(num2)
#order the numbers
if (num1 > num2):
    aux = num2
    num2 = num1
    num1 = aux
else:
    aux = num1
aux += 1 # shorthand for aux = aux +1, we have to increase by 1 here to start the loop correctly

#start loop
while (aux < num2):
    print (str(aux) +', ')
    if (aux %2 == 0):
        cont += 1 #counting even numbers
    else:
        sumaImp = sumaImp + aux #adding odd numbers
    aux += 1
aux = num2-num1 # use aux to tell how many numbers are
#output
print('\nLos números naturales comprendidos entre '+str (num1) +' y ' + str(num2) + ' son: '+ str(aux) +'.\n')
print('Los números pares comprendidos entre '+str (num1) +' y ' + str(num2) + ' son: '+ str(cont) +'.\n')
print('La suma de los impares comprendidos entre '+str (num1) +' y ' + str(num2) + ' es: '+ str(sumaImp) +'.\n')