from Tkinter import *

class Recurso:
	#En esta clase se define la cantidad de recurso que hay disponible en el proyecto
	def __init__(self, nombre , disponible):
		self.nombre = nombre
		self.disponible = disponible

	def getDisponible(self):
		return self.disponible

	def setDisponible(self, disponible):
		self.disponible = disponible

	def getNombre(self):
		return self.nombre

	def __repr__(self):
		return str(self)

	def __str__(self):
		return self.nombre
		
	def __eq__(self, other):
		return self.nombre == other
	
	def __hash__(self):
		return hash((self.nombre, self.disponible))
		
	
