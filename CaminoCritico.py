from Tkinter import *

class CaminoCritico:
	#En esta clase se define la cantidad de recurso que hay disponible en el proyecto
	def __init__(self, proyecto):
		self.proyecto = proyecto

	def calculoCaminoCritico(self):
		for i in self.proyecto.getTareas():
			i.setLateStart(99999999)
			if len(i.getSucesoras())==0:
				self.proyecto.getTareaFinal().setAntecesora(i)
				i.setSucesora(self.proyecto.getTareaFinal())
			elif len(i.getSucesoras())>1 and i.getSucesoras().count(self.proyecto.getTareaFinal())>0:
				i.getSucesoras().remove(self.proyecto.getTareaFinal())
				self.proyecto.getTareaFinal().getAntecesoras().remove(i)
		for ultima in self.proyecto.getTareaFinal().getAntecesoras():
			if ultima.getEarlyStart()+ultima.getDuracion()>self.proyecto.getTareaFinal().getEarlyStart():
				self.proyecto.getTareaFinal().setEarlyStart(ultima.getEarlyStart()+ultima.getDuracion())
				self.proyecto.getTareaFinal().setLateStart(ultima.getEarlyStart()+ultima.getDuracion())
			
		sucesoras = [self.proyecto.getTareaFinal()]		
		while sucesoras.count(self.proyecto.getTareaInicio())!=len(sucesoras):
			auxiliar =[]
			for suc in sucesoras:
				for suc2 in suc.getAntecesoras():
					suc2.setLateStart(min(suc.getLateStart()-suc2.getDuracion(),suc2.getLateStart()))
					suc2.setHolgura(suc2.getLateStart()-suc2.getEarlyStart())
					auxiliar.append(suc2)
			sucesoras=auxiliar
		
			
			
		print "Duracion del proyecto:" + str(self.proyecto.getTareaFinal().getLateStart()) + " dias"
		if self.proyecto.getFechaInicio()!= None:
			print "Empieza el " + str(self.proyecto.getFechaInicio()) + " y acaba el " + str(self.proyecto.getFechaFin())
		else:
			print "No hay fecha de inicio programada"
		print "Camino Critico:"
		for camino in self.proyecto.getTareas():		
			if camino.getHolgura()==0:
				print camino.getNombre()
	
		print "Nombre - Early - Late"
		for pruebas in self.proyecto.getTareas():
			print pruebas.getNombre()+ " " + str(pruebas.getEarlyStart())+ " " + str(pruebas.getLateStart()) + " " + str(pruebas.getHolgura())

		
	
