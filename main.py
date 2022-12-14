import re
from lexer import *

#Abre el archivo a leer en modo de solo lectura 
file = open('code2.txt','r')
#Almacena el texto contenido en el archivo, linea por linea
lines = file.readlines()

#Contador de Filas
count = 0
#Lista para guardar todas las palabras separadas
palabras_final = []

for line in lines:
    count += 1
    #Omite todo en la linea que está después del simbolo '#'
    if '#' in line:
        line = line[:line.index('#')]
    
    #Se separa la linea mediante el metodo split()
    words = line.split();
    
    newWords = list()
    for i in range(len(words)):
        if words[i][0] in("'",'"') and words[i][-1] in("'",'"'):
            newWords.append((words[i],count,line.find(words[i])))
        else:
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            for palabra in t:
                newWords.append((palabra, count,line.find(palabra)))
    palabras_final.extend(newWords)

for palabra in palabras_final:
    if esKeyword(palabra[0]):
        print("<{},{},{},{}>".format(palabra[0],"keyword",palabra[1],palabra[2]))
    elif esDelimiter(palabra[0]):
        print("<{},{},{},{}>".format(palabra[0],"delimiter",palabra[1],palabra[2]))
    elif esId(palabra[0]):
        print("<{},{},{},{}>".format(palabra[0],"id",palabra[1],palabra[2]))
    elif esNum(palabra[0]):
        print("<{},{},{},{}>".format(palabra[0],"numero",palabra[1],palabra[2]))
    elif esOperador(palabra[0]):
        print("<{},{},{},{}>".format(palabra[0],"operador",palabra[1],palabra[2]))
    else:
        print("<{},{},{},{}>".format(palabra[0],"invalido",palabra[1],palabra[2]))