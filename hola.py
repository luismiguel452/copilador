'''
import os.path


class Proyecto():

	def __init__(self,archivo):
		self.archivo=archivo


			

		

			
		

	def archivoExiste(self):
		if os.path.exists(self.archivo):
			return True
		else:
			return False
	  
	def abrirArchivo(self):
		if not self.archivoExiste:
			print ("archivo no existe")
		else:
			archivo=open(self.archivo,"r")
			for linea in archivo.readlines():
				print(linea)

	
		
		
		

	 
	
a="hola.txt"

archivo=Proyecto(a)
archivo.abrirArchivo()



'''
import ply.lex as lex
import re
import codecs
import os 
import sys


class Lexer(object):
    def __init__(self):

        tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        'ODD', 'ASSING', 'NE', 'LT', 'LTE', 'GT', 'GTE', 'LPARENT','RPARENT',
         'COMMA','SEMMICOLOM', 'DOT', 'UPDATE' ]

        reservadas = {  

        'cmz':'CMZ' 
        'fn':'fn'
        'hi':'HI'
        'thn':'thn'
        'cdo':'CDO'
        'du':'DU'
        'llkal':'LLKAL'
        'knst':'KNST'
        'tro':'TRO'
        'pros':'PROS'
        'sal':'SAL'
        'em':'EM'
        'sino':'SINO'



        }
        

        tokens=tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_ DIVIDE =  r'/'
t_ ODD   =  r'ODD'
t_ASSING =r'='
t_NE    =  r'<>'
t_LT    =  r'<'
t_LTE    =  r'<='
t_GT    =  r'>'
t_GTE    =  r'>='
t_LPARENT    =  r'\('
t_RPARENT    =  r'\)'
t_ COMMA   =  r','
t_SEMMICOLOM    =  r';'
t_DOT    =  r'\.'
t_UPDATE    =  r':='

 def t_ID(self, t) :
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    self.t = t
    if t.value.upper() in keyword:
     t.value = t.value.upper()
     t.type = t.value

     return t


def t_COMMENT(self,t):
    r'\#.*'
    self.t = t
    pass


def t_NUMBER(self,t):
    r'\d+'
    self.t = t
    t.value = int(t.value)
    return t

    def t_error(self,t):
        self.t = t
        print "carcter ilegible '%s'" % t.value[0]
        t.lexer.sikip(1)
	
'''
    
    


import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

import time 


total = 1000
i = 0
while i < total:
    progress(i, total, status='')
    time.sleep(0.81)  # emulating long-playing job
    i += 1

		
