import re

identifiers = open("RF00059_vs_UTR_Todas_sp_unicas","r")
extractid = open("results.txt", 'w')

score = re.compile('\d{2}[.]\d{1}')
sequence = re.compile("[a-zA-Z]{3}[-][a-zA-Z]{1}[^ ]*")
keys = []

for line in identifiers:
    score2 = re.findall(score, line)
    data = re.findall(sequence, line)
    if len(score2) > 0:
        if float(score2[0]) >= 35.8:
            if len(data) > 0:
                keys.append(data[0])

k = list(set(keys))
for item in k:
    extractid.write(item+"\n")
    
findthese = open("results.txt", 'r')
#NEED THE REST

identifiers.close()
extractid.close()

#Este archivo debe estar en la misma carpeta que los archivos dados.
