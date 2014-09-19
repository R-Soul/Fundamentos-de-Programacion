'''
#1 Declare una variable con el valor 56.78, redondee el número a 56.0 y finalmente conviértalo a entero, pida al usuario un número e imprima el resultado de la
suma del número anterior y el que el usuario capturo.
#2 Cree una función que reciba 10 números y regrese el promedio de los mismos.
#3 Escriba una función que reciba una operación en texto, ejemplo: “2 + 5” y regrese el resultado de la operación.
'''

#Ejercicio 1
num1 = 56.78
rnum1 = num1 // 1
num2 = int(rnum1)
print("If we round down %s we get %s" % (num1,num2))
inum = int(input("Please input a number. "))
sum56 = inum + num2
print("The sum of %s + %s is %s" % (num2,inum,sum56))
print("")

#Ejercicio 2
def avg10(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    total = int(num1) + int(num2) + int(num3) + int(num4) + int(num5) + int(num6) + int(num7) + int(num8) + int(num9) + int(num10)
    avg = int(total / 10)
    return "The average of all the previous numbers is %s" % (avg)
    
print(avg10(input("Please choose 10 numbers to average. (#1) "),input("(#2) "),input("(#3) "),input("(#4) "),input("(#5) "),input("(#6) "),input("(#7) "),input("(#8) "),input("(#9) "),input("(#10) ")))
print("")

#Ejercicio 3
def evalstr(operation):
    return eval(operation)

print(evalstr(input("Please input any operation you desire. ")))
print("")
print("Made by: Luis Raúl Arzola López - A01186956")
