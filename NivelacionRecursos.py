from Histograma import *
from copy import deepcopy
from Gantt import *
from Tkinter import *
from ttk import *

class NivelacionRecursos:
	
	#En esta clase se define la cantidad de recurso que hay disponible en el proyecto
	def __init__(self, proyecto):
		self.proyecto = proyecto
		frame = Tk()
		frame.wm_title("Gestion de Proyectos")
		frame.resizable(0,0)
		porcentaje = 2
		
		Label(frame, text="Porcentaje de aceptacion: ").grid()
		print "Carga actual:"
		for r in proyecto.getRecursos():
			print r.getNombre() + " "+ str(self.calcularCarga(proyecto.getTareas(), proyecto.getRecursos()[proyecto.getRecursos().index(r)]))
		
		porcent = StringVar()
		porcent.set("2")
		Entry(frame, textvariable=porcent).grid()
		Button(frame, text="Introducir", command=lambda: self.cambiarPorcentaje(porcent.get(), porcentaje), width=17).grid()
		Button(frame, text="Calcular", command=lambda: self.calcularNivelacion(self.proyecto, porcentaje, frame), width=17).grid()
		Button(frame, text="Reset", command=lambda: self.reset(self.proyecto, frame), width=17).grid()
		Histograma(frame, proyecto,21,1)
		Gantt(frame, proyecto,0,1,10)
		
	
	def cambiarPorcentaje(self, por, porcentaje):
		print por
	def reset(self, proyecto, frame):
		
		print "Carga actual:"
		for r in proyecto.getRecursos():
			print r.getNombre() + " "+ str(self.calcularCarga(proyecto.getTareas(), proyecto.getRecursos()[proyecto.getRecursos().index(r)]))
		
		Histograma(frame, proyecto,21,1)
		Gantt(frame, proyecto,0,1,10)
			
	def calcularNivelacion(self, proyecto,porcentaje,frame):
		copia = deepcopy(proyecto.getTareas())
		tareasOrdenadas = []
		n = 1
		for i in copia:
			if i.getHolgura()==0:
				n=n+1
		while len(tareasOrdenadas)<n:
			end= 0
			for i , j in enumerate (copia):
				if j.getEarlyStart()+j.getDuracion()>=end and j.getHolgura()!=0 and j not in tareasOrdenadas:
					end= j.getEarlyStart()+j.getDuracion()
					tar = i

			tareasOrdenadas.append(copia[tar])
		
		for i in tareasOrdenadas:
			carga = 9999999
			suma = 0
			early = i.getEarlyStart()
			for j in range(i.getHolgura()-2):
				anterior = deepcopy(copia)
				i.setEarlyStart(i.getEarlyStart()+j)
				#mejora = True
				#for r in i.getRecursos():
				#	if r!=i.getRecursos()[i.getRecursos().index(r)]:
				#		if self.calcularCarga(copia, proyecto.getRecursos()[proyecto.getRecursos().index(r)])/self.calcularCarga(anterior, proyecto.getRecursos()[proyecto.getRecursos().index(r)])<=1+porcentaje/100:
				#			mejora = True
					
				if self.calcularCarga(copia, proyecto.getRecursos()[0])<=carga:
					carga = self.calcularCarga(copia, proyecto.getRecursos()[0])
					suma = j
				print carga			
			i.setEarlyStart(early+suma)
		
		print "Carga actual:"	
		for r in proyecto.getRecursos():
			print r.getNombre() + " "+ str(self.calcularCarga(copia, proyecto.getRecursos()[proyecto.getRecursos().index(r)]))
			
		auxiliar = proyecto.getTareas()	
		proyecto.setTareas(copia)
		Histograma(frame, proyecto,21,1)
		Gantt(frame, proyecto,0,1,10)
		proyecto.setTareas(auxiliar)


		
	def calcularCarga(self, tareas, rec):
		
		cargatotal=0
		for dia in range(self.proyecto.getTareaFinal().getEarlyStart()):
			aux=0
			for tarea in tareas:
				if dia>=tarea.getEarlyStart() and dia<tarea.getEarlyEnd() and rec in tarea.getRecursos():
					aux = aux + tarea.getRecursos()[rec]
			cargatotal = cargatotal + aux * aux
		return cargatotal
		
		
		