from Gantt import *
from DisponibilidadEnTiempo import *

class Flexibilidad:
	def __init__(self,frameMain,proyecto):
		self.proyecto = proyecto
		self.disponibilidad = DisponibilidadEnTiempo(proyecto)
		self.frameMain = frameMain

	def comprobarHolguras(self):
		for tarea in self.proyecto.getTareas():
			print
			print "Holguras de la Tarea "+str(tarea.getNombre())
			self.disponibilidad.consumeRecursosProyecto()
			instantes = self.disponibilidad.comprobarInstantesDondeSePuedeSecuenciar(tarea)
			print "Se puede secuenciar en los instantes: "+str(instantes)