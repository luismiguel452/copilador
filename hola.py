'''
import os.path


class Proyecto():

	def __init__(self,archivo):
		self.archivo=archiv


			

		

			
		

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

		
