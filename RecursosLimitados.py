from DisponibilidadEnTiempo import *
from Gantt import *

class RecursosLimitados:
	def __init__ (self, proyecto, frameMain):
		self.proyecto = proyecto
		self.dispobibilidadActual = DisponibilidadEnTiempo(self.proyecto)
		self.frameMain = frameMain

	def aplicarEsquemaSerie(self):
		instanteParaSecuenciar = 0

		for sucesora in self.proyecto.getTareaInicio().getSucesoras():
			self.proyecto.getTareasElegibles().append(sucesora)
		self.proyecto.setTareasElegibles(self.ordenarTareasLFT(self.proyecto.getTareasElegibles()))
		
		#self.proyecto.setTareasElegibles(self.ordenarTareasLFT(self.proyecto.getTareaInicio().getSucesoras()))

		cont = 0
		while(len(self.getTareasPorSecuenciar())>0):
			cont = cont +1
			print
			print "--- Paso "+str(cont)
			if(len(self.proyecto.getTareasElegibles())>0):
				print "Las tareas elegibles son: "+str(self.proyecto.getTareasElegibles())+" Analizamos la primera:"
				elegible = self.seleccionarTareaElegible()
				instanteSecPrec = self.getInstanteSecuenciacionPrecedentes(elegible)
				instanteParaSecuenciar = self.dispobibilidadActual.getInstanteMasTemprano(elegible,instanteSecPrec)

				elegible.setEarlyStart(instanteParaSecuenciar)
				#elegible.setLateStart(None)

				self.proyecto.getTareasSecuenciadas().append(elegible)
				elegible.setIsSecuenciada(True)
				self.proyecto.getTareasElegibles().remove(elegible)
				elegible.setIsElegible(False)
				
				for tarea in elegible.getSucesoras():
					if(self.proyecto.getTareasElegibles().count(tarea) == 0): #Si entre las tareasElegibles no esta tarea
						tarea.setIsElegible(True)
						self.proyecto.getTareasElegibles().append(tarea)
						aux = self.proyecto.getTareasElegibles()
						self.proyecto.setTareasElegibles(self.ordenarTareasLFT(aux))
			#self.proyecto.setTareasElegibles(self.ordenarTareasLFT(self.proyecto.getTareasElegibles()))	
		self.calcularNuevoFinProyecto()					

	def getTareasPorSecuenciar(self):
		porSecuenciar = [] #Array de Tareas
		for tarea in self.proyecto.getTareas():
			if (tarea.getIsSecuenciada()==False and tarea.getEsFin()==False and tarea.getEsInicio()==False):
				porSecuenciar.append(tarea)
		return porSecuenciar

	#Devuelve la primera
	def seleccionarTareaElegible(self):
		if(len(self.proyecto.getTareasElegibles())>0):
			return self.proyecto.getTareasElegibles()[0]
		return None

	def getInstanteSecuenciacionPrecedentes(self,tarea):
		a = 0
		for t in tarea.getAntecesoras():
			if (a < (t.getEarlyStart()+t.getDuracion())):
				a = t.getEarlyStart()+t.getDuracion()
		return a 
		
	#Devuelve las tareas ordenadas por el criterio LFT
	#LFT: prioridad a minima fecha de finalizacion mas tardaa
	def ordenarTareasLFT(self, tareas):
		aux = {}
		listaFinal = []
		for tarea in tareas:
			aux[tarea] = tarea.getSumaLFT()
		
		#Aqui se ordenan de menor a mayor fecha de finalizacion tardia
		ordenLFT = sorted(aux.items(), key=lambda x: x[1])

		for tupla in ordenLFT:
			listaFinal.append(tupla[0])

		return listaFinal

	def calcularNuevoFinProyecto(self):
		maximo = 0
		tareaFinal = self.proyecto.getTareaFinal()

		for tarea in tareaFinal.getAntecesoras():
			if maximo < (tarea.getEarlyStart() + tarea.getDuracion()):
				maximo = tarea.getEarlyStart() + tarea.getDuracion()
		tareaFinal.setEarlyStart(maximo)
		tareaFinal.setLateStart(maximo)

		Gantt(self.frameMain,self.proyecto,1)
		print
		print "Nueva Duracion: "+str(maximo)








