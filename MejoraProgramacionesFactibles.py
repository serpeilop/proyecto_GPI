from Gantt import *
from DisponibilidadEnTiempo import *
from Histograma import *

class MejoraProgramacionesFactibles:
	def __init__(self, proyecto,frameMain):
		self.proyecto = proyecto
		self.disponibilidad = DisponibilidadEnTiempo(proyecto)
		self.frameMain = frameMain

	def aplicarMejoras(self):
		fin = 9999999
		while True:
			#self.aplicarRetraso()
			#self.aplicarAdelanto()
			nuevoFin = self.proyecto.getTareaFinal().getEarlyStart()
			if(nuevoFin < fin):
				self.aplicarRetraso()
				self.aplicarAdelanto()
				fin = nuevoFin
			else:
				break
				
		self.frameMain.wm_title("Informe: Mejora por el proceso Retraso-Adelanto")
		self.frameMain.resizable(0,0)
		Histograma(self.frameMain, self.proyecto,2,0)
		self.proyecto.mostrarInformacion(self.frameMain,0,0)
		Gantt(self.frameMain,self.proyecto,0,1)

	def aplicarRetraso(self):
		print
		print "RETRASO"
		tareas = self.getTareasParaRetraso(self.proyecto.getTareas())
		self.disponibilidad.consumeRecursosProyecto()

		while len(tareas)>0:
			tarea = tareas.pop(0)
			instanteParaSecuenciar = self.disponibilidad.getInstanteMasTardioRetraso(tarea)
			tarea.setEarlyStart(instanteParaSecuenciar)

		self.calcularNuevoFinProyectoR()


	def aplicarAdelanto(self):
		print
		print "ADELANTO"
		tareas = self.getTareasParaAdelanto(self.proyecto.getTareas())

		while len(tareas)>0:
			tarea = tareas.pop(0)
			instanteParaSecuenciar = self.disponibilidad.getInstanteMasTempranoAdelanto(tarea)
			tarea.setEarlyStart(instanteParaSecuenciar)

		self.calcularNuevoFinProyectoA()

	#Devuelve las tareas ordenadas de Mayor a Menor instante de fin (temprano) 
	def getTareasParaRetraso(self, tareas):
		aux = {}
		listaFinal = []
		for tarea in tareas:
			aux[tarea] = tarea.getFechaFinTemprana()
		
		orden = sorted(aux.items(), key=lambda x: x[1], reverse=True)

		for tupla in orden:
			if (tupla[0].getEsFin()==False) and (tupla[0].getEsInicio()==False): #Esto sobra
				listaFinal.append(tupla[0])

		return listaFinal

	#Devuelve las tareas ordenadas de Menor a Mayor instante de fin (temprano)
	def getTareasParaAdelanto(self, tareas):
		aux = {}
		listaFinal = []
		for tarea in tareas:
			aux[tarea] = tarea.getFechaFinTemprana()
		
		orden = sorted(aux.items(), key=lambda x: x[1])

		for tupla in orden:
			if (tupla[0].getEsFin()==False) and (tupla[0].getEsInicio()==False):
				listaFinal.append(tupla[0])

		return listaFinal

	#Si la nueva programacion no comienza en 0, se actualizan los instantes de comienzo de todas las tareas y, por tanto,
	#el instante de finalizacion del proyecto
	def calcularNuevoFinProyectoR(self):
		tareaFinal = self.proyecto.getTareaFinal()
		fin = tareaFinal.getEarlyStart() #Este es el fin suponiendo que empezamos en el instante 0

		tareaInicio = self.proyecto.getTareaInicio() #Siempre comienza en 0
		
		#Comprobamos si comenzamos en 0
		inicio = 999999
		for tarea in tareaInicio.getSucesoras():
			if inicio > tarea.getEarlyStart():
				inicio =  tarea.getEarlyStart()
		
		#Si no comenzamos, modificamos los inicios para que comencemos en 0
		if inicio > 0:
			tareaFinal.setEarlyStart(fin-inicio)
			tareaFinal.setLateStart(fin-inicio)
			for tarea in self.proyecto.getTareas():
				tarea.setEarlyStart(tarea.getEarlyStart()-inicio)

		print
		print "Mejora PF (R) - Nueva Duracion: "+str(tareaFinal.getEarlyStart())

	def calcularNuevoFinProyectoA(self):
		maximo = 0
		tareaFinal = self.proyecto.getTareaFinal()

		for tarea in tareaFinal.getAntecesoras():
			if maximo < (tarea.getEarlyStart() + tarea.getDuracion()):
				maximo = tarea.getEarlyStart() + tarea.getDuracion()
		tareaFinal.setEarlyStart(maximo)
		tareaFinal.setLateStart(maximo)
		print
		print "Mejora PF (A) - Nueva Duracion: "+str(maximo)





