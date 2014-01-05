# Disponiblididades de los recursos segun avanza el proyecto
# Atributos: proyecto, disponibilidades

# disponibilidades es un diccionario (C1,V1) donde:
# 	la Clave es es el tiempo
# 	el Valor un Diccionario (C2,V2) donde: 
#		la Clave es un objeto Recurso
#		el Valor contiene la cantidad disponible del Recurso(C2) en ese instante de tiempo(C1)

class DisponibilidadEnTiempo:

	def __init__(self, proyecto):
		self.proyecto = proyecto
		self.disponibilidades = {}
		self.initDisponibilidades()

	#Inicializa el diccionario "disponibilidades", un elemento (C1,V1) donde:
	#La Clave es un instante de tiempo y el Valor un diccionario (C2,V2)
	def initDisponibilidades(self):
		for i in range(self.proyecto.getTareaFinal().getLateStart()):
			self.disponibilidades[i] = self.obtieneListaRecursosProyectoInicializada()

	#Devuelve un Diccionario (C2,V2) que sera el Valor del diccionario "disponibilidades" donde: 
	#La Clave es un objeto Recurso y el Valor contiene la cantidad disponible del Recurso(C2) lleno al maximo
	def obtieneListaRecursosProyectoInicializada(self): 
		recursosEnInstante = {}
		recursosEnElProyecto = self.proyecto.getRecursos()
		for recurso in recursosEnElProyecto:
			recursosEnInstante[recurso] = recurso.getDisponible()
		return recursosEnInstante

	#Nos dice si hay recursos suficientes para iniciar la tarea en ese instante
	def esPosibleSecuenciar(self,tarea,instante):
		print
		print "ANALISIS: La tarea se puede secuenciar (iniciar) en el instante: "+str(instante)
		for i in range(instante,tarea.getDuracion()+instante):
			#if (self.disponibilidades.has_key[i]==False):
			if ((i in self.disponibilidades) == False):
				#disponibilidades es un Diccionario, no un Array. La i es la Clave, no un indice de un array
				self.disponibilidades[i] = self.obtieneListaRecursosProyectoInicializada()

		for i in range(instante,tarea.getDuracion()+instante):
			print "		En el instante "+str(i)+" : Neces Recurso VS Disponibilidad"
			dispEnInstante = self.disponibilidades[i] #Disponibilidad de los recursos en el instante i
			for recurso in dispEnInstante.keys():
				print "			"+str(tarea.getNecesidadesRecurso(recurso))+" VS "+str(dispEnInstante[recurso])
				if tarea.getNecesidadesRecurso(recurso) > dispEnInstante[recurso]:
					print "		No hay suficiente!"
					return False
		return True

	#Punto 2
	def getInstanteMasTemprano(self,tarea, instante):
		instanteSecuenciar = instante
		while (self.esPosibleSecuenciar(tarea,instanteSecuenciar)==False):
			instanteSecuenciar = instanteSecuenciar+1
		print "		Si hay suficiente!"
		self.consumeRecursos(tarea, instanteSecuenciar)
		return instanteSecuenciar

	def consumeRecursos(self,tarea,instante):
		for i in range(instante, instante+tarea.getDuracion()):
			dispEnInstante = self.disponibilidades[i] #Disponibilidad de los recursos en el instante i
			for recurso in dispEnInstante.keys():
				self.disponibilidades[i][recurso] = self.disponibilidades[i][recurso] - tarea.getNecesidadesRecurso(recurso)

	#Punto 2 
	def consumeRecursosProyecto(self):
		self.initDisponibilidades()
		for tarea in self.proyecto.getTareas():
			if (tarea.getEsFin()==False) and (tarea.getEsInicio()==False):
				self.consumeRecursos(tarea,tarea.getEarlyStart())

	#Punto 2 - RETRASO - Devuelve el instante mas tardio en el que hay recursos disponibles para la tarea
	def getInstanteMasTardioRetraso(self, tarea):
		hlRetraso = tarea.getHlRetraso()
		instanteSecuenciar = tarea.getEarlyStart()+hlRetraso
		print "Holgura Libre Retraso Tarea "+str(tarea.getNombre())+" : "+str(hlRetraso) 

		if hlRetraso== 0:
			return instanteSecuenciar

		#La tarea a mover devuelve los recursos consumidos en su posicion actual
		self.devuelveRecursos(tarea)

		#Calculamos el instante mas tardio donde se puede secuenciar la tarea. En caso de no ser factible ninguno dentro
		# de la HLR, el instanteSecuenciar sera el inicial de esa tarea, pues en ese instante si era factible. 
		while self.esPosibleSecuenciar(tarea,instanteSecuenciar)==False:
			instanteSecuenciar = instanteSecuenciar -1

		#Consume recursos de su nueva posicion
		self.consumeRecursos(tarea, instanteSecuenciar)

		return instanteSecuenciar

	#Punto 2 - ADELANTO - Devuelve el instante mas temprano en el que hay recursos disponibles para la tarea
	def getInstanteMasTempranoAdelanto(self,tarea):
		hlAdelanto = tarea.getHlAdelanto()
		instanteSecuenciar = tarea.getEarlyStart() - hlAdelanto
		print "Holgura Libre Adelanto Tarea "+str(tarea.getNombre())+" : "+str(hlAdelanto) 

		if hlAdelanto== 0:
			return instanteSecuenciar

		#La tarea a mover devuelve los recursos consumidos en su posicion actual
		self.devuelveRecursos(tarea)

		#Calculamos el instante mas temprano donde se puede secuenciar la tarea. En caso de no ser factible ninguno dentro
		# de la HLA, el instanteSecuenciar sera el inicial de esa tarea, pues en ese instante si era factible. 
		while self.esPosibleSecuenciar(tarea,instanteSecuenciar)==False:
			instanteSecuenciar = instanteSecuenciar +1

		#Consume recursos de su nueva posicion
		self.consumeRecursos(tarea, instanteSecuenciar)

		return instanteSecuenciar
		
	#Punto 2 
	def devuelveRecursos(self,tarea):
		instante = tarea.getEarlyStart()
		for i in range(instante,instante+tarea.getDuracion()):
			dispEnInstante = self.disponibilidades[i] #Disponibilidad de los recursos en el instante i
			for recurso in dispEnInstante.keys():
				self.disponibilidades[i][recurso] = self.disponibilidades[i][recurso] + tarea.getNecesidadesRecurso(recurso)

	#Punto 4: Flexibilidad
	def comprobarInstantesDondeSePuedeSecuenciar(self,tarea):
		instantesParaSecuenciar = []

		#La tarea a analizar devuelve los recursos consumidos en su posicion actual, para que no haya errores
		self.devuelveRecursos(tarea)

		#Parte 1: Instantes donde se puede secuenciar dentro de la HLR
		hlRetraso = tarea.getHlRetraso()
		print "		HLR: "+str(hlRetraso) 

		instanteSecuenciar = tarea.getEarlyStart()+hlRetraso
		
		if hlRetraso!= 0:
			while (instanteSecuenciar!=tarea.getEarlyStart()):
				if self.esPosibleSecuenciar(tarea,instanteSecuenciar)==True:
					instantesParaSecuenciar.append(instanteSecuenciar)
				instanteSecuenciar = instanteSecuenciar -1
		

		#Parte 2: Instantes donde se puede secuenciar dentro de la HLA
		hlAdelanto = tarea.getHlAdelanto()
		print "		HLA: "+str(hlAdelanto) 

		instanteSecuenciar = tarea.getEarlyStart() - hlAdelanto

		if hlAdelanto!= 0:
			while instanteSecuenciar!=tarea.getEarlyStart():
				if self.esPosibleSecuenciar(tarea,instanteSecuenciar)==True:
					instantesParaSecuenciar.append(instanteSecuenciar)
				instanteSecuenciar = instanteSecuenciar +1

		#Dejamos el consumo de recursos como estaba al principio
		self.consumeRecursos(tarea, tarea.getEarlyStart())
		
		return instantesParaSecuenciar
