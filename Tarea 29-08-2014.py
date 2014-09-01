#    Crea una función que reciba un número dentro de una cadena y regrese ese número elevado al cuadrado
def square(num):
    x = float(num) ** 2
    print("The square of " + str(num) + " is " + str(x))
    return x
square("52.01314")

#    Cree una función que reciba su fecha de nacimiento en forma de cadena y regrese cuántos años tienes
import datetime
def age(date):
    bday = datetime.datetime.strptime(date, "%d-%m-%Y")
    today = datetime.datetime.today()
    #Note: This operation can only be done with 2 dates.
    totalage = today - bday
    totalage2 = round(totalage.days/ 365, 1)
    print("You're " + str(totalage2) + " years old.")
    return totalage2
age("27-12-1995")

#    Cree una función que reciba una fecha en forma de cadena y regrese verdadero y si el día de la fecha es viernes y falso si no.
def isitfri(date):
    date2 = datetime.datetime.strptime(date, "%d-%m-%Y")
    weekday = date2.weekday()
    if weekday == 4:
        print(True)
        return True
    else:
        print(False)
        return False
isitfri("15-08-2014")

#    Cree una función que reciba una fecha en forma de cadena y regrese la misma fecha, pero dentro de 10 años en formato de cadena “31 (Sunday) August 2014”
def newdate(date):
    date2 = datetime.datetime.strptime(date, "%d-%m-%Y")
    #Note: If date 3 doesn't contain month and day, program will crash. However, ommiting weekday is possible.
    date3 = datetime.date(date2.year + 10, date2.month, date2.day)
    new_date = "{0:%d (%A) %B %Y}".format(date3)
    print(new_date)
newdate("29-08-2004")

#    Cree una función para calcular el índice de masa corporal (que reciba el peso y la estatura como parámetros)
def bmi(weight, height):
    bmi2 = weight / (height**2)
    print("Your BMI is of " + str(round(bmi2,2)))
    return bmi2
bmi(83,1.8)

#    Cree una función para calcular el área de un circulo (que reciba el radio del circulo)
def carea(radio):
    PI = 3.1416
    area = PI * (radio**2)
    print("The area of a circle with a radio of " + str(radio) + " is " + str(area))
    return area
carea(5.3)

#    Cree una función que regrese verdadero si un número es divisible exactamente divisible entre dos y falso si no.
def mod2(num):
    mod = int(num) % 2
    if mod == 0:
        print(True)
        return True
    else:
        print(False)
        return False
mod2(25)

#    Cree una función que regrese verdadero si un número es divisible exactamente divisible entre tres y falso si no.
def mod3(num):
    mod = int(num) % 3
    if mod == 0:
        print(True)
        return True
    else:
        print(False)
        return False
mod3(18)

#    Cree una función que regrese verdadero si un número es divisible exactamente divisible entre dos y entre tres también y falso si no.
def mod23(num):
    mod2 = int(num) % 2
    mod3 = int(num) % 3
    if mod2 == 0:
        if mod3 ==0:
            print(True)
            return True
        else:
            print(False)
            return False
    else:
        print(False)
        return False      
mod23(30)

#    Cree una función que reciba 10 números y regrese el promedio de los mismos.
def average10(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    avg = (num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)/10
    print(avg)
    return(avg)
average10(12,14,15,18,45,86,92,75,84,85)
