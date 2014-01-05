from Fechas import *
from Recursos import *
from Tarea import *

class Proyecto:
	
	tareaInicio = Tarea("Inicio", 0)
	tareaFinal = Tarea("Final", 0)
	tareas = []
	caminoCritico = [] #Array de Tareas
	tareasElegibles = []
	tareasSecuenciadas = []
	fechasProyecto = Fechas()
	recursosProyecto = Recursos()

	def getFechaInicio(self):
		return self.fechasProyecto.getFechaInicio()

	def getFechaFin(self):
		return self.fechasProyecto.getLaborables()[-1]

	def fixLaborables(self):
		self.fechasProyecto.fixLaborables()
		
	def getLaborables(self):
		return self.fechasProyecto.getLaborables()
				
	def setDuracion(self, duracion):
		self.fechasProyecto.setDuracion(duracion)
	
	def getDuracion(self):
		return self.fechasProyecto.getDuracion()

	def setFechas(self, frame):
		self.fechasProyecto.setFechas(frame)
	#return array de tareas
	def getTareas(self):
		return self.tareas

	def setTareas(self, tareas):
		self.tareas = tareas
	def addTarea(self, tarea):
		self.tareas.append(tarea)

	def getCaminoCritico(self):
		return self.caminoCritico

	def setCaminoCritico(self, caminoCritico):
		self.caminoCritico = caminoCritico

	#SOBRA? devuelve array con los recursos del proyecto
	def getRecursos(self):
		return self.recursosProyecto.getRecursos()

	def setRecursos(self,frameRecursos, proyecto):
		self.recursosProyecto.setRecursos(frameRecursos,proyecto, self.tareas)

	# Metodos para Recursos Limitados Serie
	'''
	def getRecursosLimitados(self):
		return self.recursosLimitados

	def setRecursosLimitados(self, recursosLimitados):
		self.recursosLimitados = recursosLimitados
	'''
	# Metodos para Mejora de Programaciones Factibles

	def getTareasElegibles(self):
		return self.tareasElegibles

	#Pone el flag isElegible de las tareas dadas a True
	def setTareasElegibles(self,tareasElegibles):
		self.tareasElegibles = tareasElegibles
		for t in self.tareasElegibles:
			t.setIsElegible(True)

	def getTareasSecuenciadas(self):
		return self.tareasSecuenciadas

	#def setTareasSecuenciadas(self, tareasSecuenciadas):
	#Sobra porque el setIsSecuenciada(True) se hace en RecursosLimitados,  line 22

	def getTareaFinal(self):
		return self.tareaFinal

	def getTareaInicio(self):
		return self.tareaInicio
		
	def mostrarInformacion(self, frameMain):
		tabla = Tabla(frameMain, len(self.tareas)+1,5)
		tabla.set(0,0,"Nombre")
		tabla.set(0,1,"Duracion")
		tabla.set(0,2,"Antecesoras")
		tabla.set(0,3,"Fecha Inicio")
		tabla.set(0,4,"Fecha Fin")
		for i in self.tareas:
			tabla.set(self.tareas.index(i)+1,0,i.getNombre())
			tabla.set(self.tareas.index(i)+1,1,i.getDuracion())
			tabla.set(self.tareas.index(i)+1,2,i.getAntecesoras())
			tabla.set(self.tareas.index(i)+1,3,i.getEarlyStart())
			tabla.set(self.tareas.index(i)+1,4,i.getEarlyStart()+i.getDuracion())

	        tabla.grid(column=1, row =0, rowspan=10, sticky=N)
