from Gantt import *
from DisponibilidadEnTiempo import *
from Tabla import *

class Flexibilidad:
	def __init__(self,flexFrame,proyecto):
		self.proyecto = proyecto
		self.disponibilidad = DisponibilidadEnTiempo(proyecto)
		self.flexFrame = flexFrame
		self.resultados = []

	def construirVentana(self):

		#Label(self.flexFrame, text="Flexibilidad: Analisis de holguras").grid(column=2, row=0)
		tabla = Tabla(self.flexFrame, len(self.proyecto.getTareas())+1,4)
		tabla.set(0,0,"Nombre")
		tabla.set(0,1,"HL Retraso")
		tabla.set(0,2,"HL Adelanto")
		tabla.set(0,3,"Instantes Posibles Secuenciacion")

		indice = 0
		for tarea in self.proyecto.getTareas():
			tabla.set(indice+1,0,tarea.getNombre())
			tabla.set(indice+1,1,tarea.getHlRetraso())
			tabla.set(indice+1,2,tarea.getHlAdelanto())
			tabla.set(indice+1,3,self.resultados[indice])
			indice = indice +1
	        tabla.grid(column=2, row =10, rowspan=10, sticky=E)

	def comprobarHolguras(self):
		for tarea in self.proyecto.getTareas():
			print
			print "Holguras de la Tarea "+str(tarea.getNombre())
			self.disponibilidad.consumeRecursosProyecto()
			instantes = self.disponibilidad.comprobarInstantesDondeSePuedeSecuenciar(tarea)
			self.resultados.append(instantes)
			print "Se puede secuenciar en los instantes: "+str(instantes)