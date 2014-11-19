import re

identifiers = open("RF00059_vs_UTR_Todas_sp_unicas","r")
findhere = open("UTR_Todas_sp_unicas_linea.txt","r")
extractid = open("results.txt", 'w')

score = re.compile('\d{2}[.]\d{1}')
sequence = re.compile("[a-zA-Z]{3}[-][a-zA-Z]{1}[^ ]*")
keys = []
counter = 0

for line in identifiers:
    score2 = re.findall(score, line)
    data = re.findall(sequence, line)
    if len(score2) > 0:
        if float(score2[0]) >= 35.8:
            if len(data) > 0:
                keys.append(data[0])

byeduplicates = list(set(keys))

findhere2 = []
for item in findhere:
    findhere2.append(item)

for item in byeduplicates:
    cond = False
    for line in findhere2:
        if cond:
            counter += 1
            print(str((counter/len(byeduplicates))*100)[0:4]+"% Done")
            extractid.write(item + "," + line)
            cond = False
            break
        if item in line:
            cond = True

identifiers.close()
extractid.close()

#Este archivo debe estar en la misma carpeta que los archivos dados.
