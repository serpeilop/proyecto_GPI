from DisponibilidadEnTiempo import *
from Gantt import *
from Histograma import *

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
				for tarea in self.proyecto.getTareasElegibles():
					tarea.incrementaValorFIFO()
				print "Las tareas elegibles son: "+str(self.proyecto.getTareasElegibles())
				elegible = self.seleccionarTareaElegible()
				print "Elegimos "+str(elegible.getNombre())
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

	def seleccionarTareaElegible(self):
		
		#En el proyecto tenemos las tareas elegibles ordenadas por el criterio LFT. En este metodo, en caso de que tengan igual numero LFT,
		#aplicamos criterio FIFO para elegir que tarea secuenciar
		sumasLFT = []
		valoresFIFO = []
		tareas = []
		rangoFIFO = 1

		for tarea in self.proyecto.getTareasElegibles():
			sumasLFT.append(tarea.getSumaLFT())
			valoresFIFO.append(tarea.getValorFIFO())
			tareas.append(tarea)

		for i in range(0,len(valoresFIFO)-1):
			if sumasLFT[i] == sumasLFT[i+1]:
				rangoFIFO = i+2
			else:
				break

		nuevaFIFO = valoresFIFO[:rangoFIFO]
		indice = nuevaFIFO.index(max(nuevaFIFO))

		return tareas[indice]

		'''
		if(len(self.proyecto.getTareasElegibles())>0):
			return self.proyecto.getTareasElegibles()[0]
		return None
		'''

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
		self.proyecto.setDuracion(maximo)

		self.frameMain.wm_title("Informe: Programacion Factible con Recursos Limitados")
		self.frameMain.resizable(0,0)
		self.proyecto.fixLaborables()
		Histograma(self.frameMain, self.proyecto,2,0)
		self.proyecto.mostrarInformacion(self.frameMain,0,0)
		Gantt(self.frameMain,self.proyecto,0,1)

		print
		print "Nueva Duracion: "+str(maximo)








