#9.- Escriba una función que usando el módulo tkinter habrá un dialogo para escoger un archivo y regrese el nombre del archivo seleccionado.
#Si lo mandaba llamar después de otras funciones, a veces funcionaba y a veces no. 
import tkinter
def selectfile():
    tkinter.Tk().withdraw()
    return (tkinter.filedialog.askopenfilename())

print("This will ask you to select a file, and will return you that file name and location.")
print(selectfile())
print("")

#1.- Cree una función para que reciba un número y regrese verdadero si es non y falso si es par
def odd(num):
    if int(num) % 2 == 0:
        return False
    return True

print('This prints "True" if the number is Odd, and "False" if it\'s Even.')
print(odd(input("Please input a number: ")))
print("")

#2.- Cree una función para que reciba un número y mediante operaciones bitwise regrese verdadero si es non y falso si es par.
def oddbit(num):
    a = 1
    b = int(num) & a
    if b == 1:
        return True
    return False

print("This will do pretty much the same as the function above.")
print(oddbit(input("Please input a number: ")))
print('')

#3.- Escriba una función que reciba una frase, ejemplo: “Hoy es un dia nublado” y regrese “Hoy Es Un Dia Nublado”
def capitalized(phrase):
    splittxt = phrase.split()
    newphrase = ""
    for words in splittxt:
        newphrase += words.capitalize() + " "
    return newphrase

print('This will print any text you give it, but with every first letter capitalized.')
print(capitalized(input("Please write a phrase of your liking: ")))
print('')

#4.- Escriba una función que simule con números aleatorios el juego de la ruleta rusa y te diga si mueres o vives (se debe de mandar llamar ocho veces y decir en que turno se dispara la pistola).
import random
    
def russianr():
    shots = 0
    alive = True
    while shots != 8 and alive == True:
        shots += 1
        pistolslot = random.randint(0, 5)
        if pistolslot == 0:
            print("You were shot on turn # %s" % (shots))
            alive = False
    if alive == True:
        print("Congratulations! You survived!")
    else:
        print("I'm afraid you are dead.")
            

print("This function will determine if you survived or not a Russian Roulette game. (8 Shots & 6 bullet slots)")
russianr()
print('')

#5.- Escriba una función que reciba como parámetro la distancia de la base de un triángulo rectángulo y el ángulo de uno de sus vértices, la función debe de regresar la distancio del lado contrario al ángulo. Ejem:Trigonometria de un triangulo
import math

def opside(side, angle):
    op = side * (math.sin(math.radians(angle)))
    lastangle = 90 - angle    
    op2 = op / (math.sin(math.radians(lastangle)))
    return op2

print("If you input the base size and the adjacent angle of a right-angled triangle, this function will return the size of the side opposite to that angle.")
print(opside(float(input("Specify the size of the base. ")), float(input("Now specify the angle. (Can't be the 90° angle) "))))
print('')

#6.- Escriba una función que regrese la desviación estándar de la población [1.5, 2.5, 2.5, 3.75, 3.25, 4.75].
import statistics

def stadev(pop):
    return statistics.stdev(pop)

print("This prints the standard deviation of the population: [1.5, 2.5, 2.5, 3.75, 3.25, 4.75].")
print(stadev([1.5, 2.5, 2.5, 3.75, 3.25, 4.75]))
print('')

#7.- Escriba un función que no regrese ningún valor, solo que imprima “Le falta galleta a tu computadora :(” si tiene menos de dos procesadores y “Tienes una super computadora :)” si la computadora tiene dos o más procesadores.
import os

def cpucount():
    if os.cpu_count() > 2:
        print("Tienes una super computadora :)")
    else:
        print("Le falta galleta a tu computadora :(")
    
print("This snippet will say that you have a nice computer if you have 2 or more CPUs. Will tell you it's crappy otherwise. (It'll be in spanish)")
cpucount()
print('')

#8.- Escriba un programa que mande un correo a la cuenta rontiveros@itesm.mx con el asunto “Tarea 5 ejercicio 6” y en el cuerpo “Mensaje enviado desde @nombre” donde @nombre es el nombre de la computadora donde se ejecute el programa.
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail():
    fromaddr = "rsoulschool@gmail.com"
    toaddr = "rontiveros@itesm.mx"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tarea 5 ejercicio 6"
    body = "Mensaje enviado desde " + os.environ['COMPUTERNAME']
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("rsoulschool@gmail.com", "pass123.") #Hice el correo para esta tarea, para usar uno que no tenga protección avanzada abilitada.
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

#Como lo hice: http://en.wikibooks.org/wiki/Python_Programming/Email
print("Sending a mail to rontiveros@itesm.mx...")
sendmail()
print("Done.")
print("")

#10.- Escriba una función que reciba una operación en texto, ejemplo: “2 + 5” y regrese el resultado de la operación.
def evalstr(operation):
    return eval(operation)

print("This function will run an arithmetic operation that is written as a string.")
print(evalstr(input("Write down an arithmetic operation. ")))
print("")
print("Made by: Luis Raúl Arzola López - A01186956")
