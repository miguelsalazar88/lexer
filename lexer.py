import re

#Expresion regular para la verificacion de identificadores.
regex_id = r"^[^\d\W]\w*\Z"

#Metodo que identifica si una palabra es valida para identificador.
def esId(s):
    if re.match(regex_id, s):
        return True
    else:
        return False

#Espresion regular para la verificacion de numeros.
regex_num = r'^[0-9]*[.]{0,1}[0-9]*$'

#Metodo que identifica si una palabra es valida para numero
def esNum(s):
    if re.match(regex_num, s):
        return True
    else:
        return False


# Lista de palabras reservadas del lenguaje Python
tk_keywords = ['False','def','if','raise','None','del','import','return',
                'True','elif','in','try','and','else','is','while','as', 	
                'except','lambda','with','assert','finally','nonlocal','yield',
                'break','for','not','class','from','or','continue','global','pass',
                'self', '__peg_parser__','async']

#Metodo que verifica si la palabra es un keyword reservado
def esKeyword(s):
    if s in tk_keywords:
        return True
    else:
        return False

tk_operadores = ['+','-','*','**','/','//','%','@','<<','>>','&','|','^','~',':=',
                '<','>','<=','>=','==','!=']

def esOperador(s):
    if s in tk_operadores:
        return True
    else:
        return False

# Lista de 
tk_delimiters = ['(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=', '->',
                '+=','-=','*=','/=','//=','%=','@=','&=','|=','^=','>>=','<<=','**=']

def esDelimiter(s):
    if s in tk_delimiters:
        return True
    else:
        return False


