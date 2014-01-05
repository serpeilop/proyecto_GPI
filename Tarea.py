class Tarea:
    def __init__(self,nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion
        self.antecesoras = []
        self.sucesoras = []
        self.start = 0
        self.end = 0
        self.earlystart=0
        self.latestart=999999999
        self.holgura=-1
        self.holguralibre=-1
        self.recursos = {} # C= Recurso, V=Consumo
        self.isSecuenciada = False
        self.isElegible = False

    def getNombre(self):
        return self.nombre

    def getDuracion(self):
        return self.duracion

    def getProyecto(self):
        return self.proyecto

    def getEarlyStart(self):
        return self.earlystart

    def setEarlyStart(self,other):
        self.earlystart=other
        self.start = other
        self.end = other+self.duracion
    
    def getLateStart(self):
        return self.latestart

    def getStart(self):
	   return self.start
    
    def getEnd(self):
	   return self.end
  
    def setStart(self, other):
	   self.start = other
   
    def setEnd(self,other):
	   self.end = other	

    def setLateStart(self,other):
        self.latestart=other

    def getSucesoras(self):
        return self.sucesoras

    def setSucesora(self,other):
        self.sucesoras.append(other)

    def getAntecesoras(self):
        return self.antecesoras

    def setAntecesora(self,other):
        self.antecesoras.append(other) 

    def getEsInicio(self):
        #return self.incio
        return self.nombre == "Inicio"

    def setEsInicio(self, other):
        self.inicio = other

    def getEsFin(self):
        ##return self.esFin
        return self.nombre == "Final"

    def setEsFin(self,esFin):
        self.esFin = esFin
   
    def getHolgura(self):
        return self.holgura
    
    def setHolgura(self,other):
        self.holgura=other
               
    def addRecurso(self,recurso,cantidad):
        self.recursos[recurso] = cantidad
        
    def getRecursos(self):
	   return self.recursos

    def getNecesidadesRecurso(self,recurso):
        if recurso in self.recursos:
            return self.recursos[recurso]
        else:
            return 0

    def getIsSecuenciada(self):
        return self.isSecuenciada

    def setIsSecuenciada(self,value):
        self.isSecuenciada = value

    def getIsElegible(self):
        return self.isElegible

    def setIsElegible(self,value):
        self.isElegible = value

    #Devuelve fecha de finalizacion mas tardia 
    def getSumaLFT(self):
        return self.latestart + self.duracion

    #Devuelve fecha de finalizacion mas temprana
    def getFechaFinTemprana(self):
        return self.earlystart + self.duracion
        
    def getHlRetraso(self):
        if (self.getEsFin()) or (self.getEsInicio()):
            return 0
        minimo = 999999999
        for tarea in self.sucesoras:
            if minimo > tarea.getEarlyStart():
                minimo = tarea.getEarlyStart()
        minimo = minimo - (self.duracion + self.earlystart)
        return minimo

    def getHlAdelanto(self):
        if (self.getEsFin() or self.getEsInicio()):
            return 0
        maximo = 0
        for tarea in self.antecesoras:
            if maximo<(tarea.getEarlyStart()+tarea.getDuracion()):
                maximo = tarea.getEarlyStart()+tarea.getDuracion()
        maximo = self.earlystart - maximo
        return maximo

    '''    
    def getFechaInicio():
    def setFechaInicio():
    def getFechaFin():
    def setFechaFin():
    def getHolguraTotal():
    def setHolguraTotal():
    def getHolguraLibre():
    def setHolguraLibre():
    def getUsoRecursos():
    def setUsoRecursos():
    def getHLAdelanto():
'''
		                
    def __repr__(self):
        return str(self)
                
    def __str__(self):
        return self.nombre
        
    def __eq__(self, other):
        return self.nombre == other

    def __hash__(self):
        return hash(self.nombre)

  