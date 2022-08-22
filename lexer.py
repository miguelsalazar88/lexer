import re


# Lista de palabras reservadas del lenguaje Python
reservadas = ['False','def','if','raise','None','del','import','return',
                'True','elif','in','try','and','else','is','while','as', 	
                'except','lambda','with','assert','finally','nonlocal','yield',
                'break','for','not','class','from','or','continue','global','pass',
                'self', '__peg_parser__','async']

asig = ['+=', '-=','*=','@=','/=','%=','&=','|=','^=','<<=','>>=','**=','//=']


tk_par_izq = '('
tk_par_der = ')'
tk_cotr_izq = '['
tk_cor_der = ']'
tk_llave_izq = '{'
tk_llave_der = '}'
tk_decor = '@'
tk_funct_anot = '->'
tk_comment = '#'
tk_dos_pts = ':'





