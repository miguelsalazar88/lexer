from lexer import *

file = open('code.txt','r')
lines = file.readlines()

count = 0

for line in lines:
    count += 1
    palabras = line.split();
    print(palabras)