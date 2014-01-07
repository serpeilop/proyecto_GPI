from Histograma import *
from Gantt import *
from Tkinter import *
from ttk import *

class NivelacionRecursos:
	#En esta clase se define la cantidad de recurso que hay disponible en el proyecto
	def __init__(self, proyecto):
		self.proyecto = proyecto
		self.frame = Tk()
		self.frame.wm_title("Gestion de Proyectos")
		self.frame.resizable(0,0)
		
		Label(self.frame, text="Porcentaje de aceptacion: ").grid()
		por = StringVar()
		Entry(self.frame, textvariable=por).grid()
		Button(self.frame, text="Introducir", command=lambda: self.cambiarPorcentaje(por.get()), width=17).grid()
		Button(self.frame, text="Calcular", command=lambda: self.calcularNivelacion(), width=17).grid()
		Histograma(self.frame, proyecto,21,1)
		Gantt(self.frame, proyecto,0,1,10)
		
	
	def cambiarPorcentaje(self, porcentaje):
		prueba = 5
		prueba = porcentaje
		print prueba
		
	def calcularNivelacion(self):
		
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


		
	
