boolean1 = True
print(boolean1)
 
#Esto se puede acortar con solo utilizar print(not boolean1), además de que al utilizar not en lugar de una operación aritmética (me refiero a boolean -= boolean), ya no sería necesario definir como boolean.
boolean1 -= boolean1
#La variable es asignada como boolean para evitar que imprima como 1 o 0, por utilizar una operación.
boolean1 = bool(boolean1)
print(boolean1)
 
number = 4
print(number)
 
number += 4
print(number)
 
number += 2.25
print(number)
 
#Variable copiada para ser utilizada en los ejercicios siguientes.
number2 = number
number = round(number,0)
print(number)
 
#Aqui se utiliza una tercera variable para dejar a number2 intacta, y se usa number2, porque number ya fué redondeada.
number3 = number2/1.15
#Redondeado a 11 decimales para dar lo mismo que el resultado dado en BlackBoard.
number3 = round(number3,11)
print(number3)
 
#Se usa number2 al ser igual que number antes de ser dividida (para dar lo mismo que en BlackBoard).
number2 = number2 // 1.15
print(number2)
 
number4 = 5%2
print(number4)
 
number4 = 4/2
print(number4)
 
#El ejercicio pedía 4/3, pero como según BlackBoard el resultado es 1, utilicé una división entera.
number4 = 4//3
print(number4)
 
number4 = 9845**24
print(number4)
 
string1 = "Hola variable"
print(string1)
 
string1 += " tipo cadena"
print(string1)
 
radius = 10
pie = 3.1416
area = (pie*(radius**2))
area = round(area,4)
print(area)
 
cdegrees = 12
fdegrees = (cdegrees * (9/5)) + 32
#Utilicé integer para que el resultado fuera igual que en BlackBoard (solo los enteros).
fdegrees = int(fdegrees)
print(fdegrees)
 
weight = 72
height = 1.85
bmi = weight/(height**2)
bmi = round(bmi,10)
print(bmi)
