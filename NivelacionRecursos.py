from Tkinter import *

class NivelacionRecursos:
	#En esta clase se define la cantidad de recurso que hay disponible en el proyecto
	def __init__(self, proyecto):
		self.proyecto = proyecto
		
	def mostrarNivelacion(self):
		
		copia = []
		for i in self.proyecto.getTareas():
			copia.append(i)
		cargatotal=0
		for dia in range(self.proyecto.getTareaFinal().getEarlyStart()):
			for rec in self.proyecto.getRecursos():
				aux=0
				for tarea in self.proyecto.getTareas():
					if dia>=tarea.getStart() and dia<tarea.getEnd() and rec in tarea.getRecursos():
						aux = aux + tarea.getRecursos()[rec]
				carga = aux * aux
				cargatotal = cargatotal + carga
				print str(dia) + " | " + str(rec) + " " + str(aux)
		print "Carga total: " + str(cargatotal)


		
	
