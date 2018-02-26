import os.path


class Proyecto():

	def __init__(self,archivo):
		self.archivo=archivo

		

			
		

	def archivoExiste(self):
		if os.path.exists(self.archivo):
			return True
		else:
			return False
	  
	def abrirArchivo(self,l):
		pass
	
		
		
		

		 
	
a="hola.txt"

archivo=Proyecto(a)
if archivo.archivoExiste():
	print("hola")
else:
	print ("ruta no existe ese archivo")







		