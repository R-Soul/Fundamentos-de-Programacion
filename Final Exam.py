import re

base = open("generacion.csv","r")
info = open("clima.csv","r")
results = open("results.csv", 'w')

date = re.compile('\d{4}[-]\d{1,}[-]\d{1,}[,]')
dates = []

sqmt = input("How many square meters are we calculating? ")
tarifa = input("Which is the cost per Watt? [Normal is 2.7] ")

cond = True
prices = []
for line in base:
    price = line.split(',')
    prices.append(price[1][:-1])

for line in info:
    date2 = str(re.findall(date, line))
    speed = line.split(',')
    dates.append(date2[2:-2] + str(speed[17]))
    
counter = 1
final = []
total = 0
for item in dates:
    if counter < 1:
        tar = item.split(',')
        if int(tar[-1]) > 23:
            tar[-1] = 23
        money = (float(eval(prices[int(tar[-1])+1]) * float(eval(sqmt)) * float(eval(tarifa))))/1000
        final.append(tar[0]+","+str(money))
        total += money
    counter -= 1

results.write("Fecha,Costo\n")
for item in final:
    results.write(item+"\n")
print("\nEl dinero total generado es de $%s" % (round(total,2)))
info.close()
base.close()
results.close()

###################
#######LEAME#######
###################

#Este archivo debe estar en la misma carpeta que los archivos dados.

#En el archivo de generacion.csv tiene como limite 23, así que si el promedio de viento es mayor a 23, utilicé 23.

#El viento promedio se encuentra en el archivo clima como Mean Velocidad del Viento

#El viento está en km/h en el archivo clima, y en m/s en generación, como el convertir hacía las cantidades
#muy pequeñas, me abstuve de convertirlo. Solo hubiera sido multiplicar por (10/36) para hacerlo m/s.
