from Tabla import *
from datetime import *
from Gantt import *
from Tkinter import *
from ttk import *

class Fechas:

	festivos =[]
	laborables =[]
	fechaInicio = None
	duracion = 0

	def cambiarFechaInicio(self, dia, mes , ano , proyecto , frameMain):
		fechaInicio = date(int(ano),int(mes),int(dia))
		self.fechaInicio = fechaInicio
		self.fixLaborables()
		Gantt(frameMain,proyecto)
		proyecto.mostrarInformacion(frameMain)
		
	def setFechas(self, frameFechas, frameMain , proyecto):
		
		dia = StringVar()
		mes = StringVar()
		ano = StringVar()
		diaf = StringVar()
		mesf = StringVar()
		anof = StringVar()
	
		Label(frameFechas, text="Fecha de Inicio:").grid(row=0, columnspan=7, sticky=W)
		Label(frameFechas, text="Dia:").grid(row=1)
		Entry(frameFechas,width=2,textvariable=dia).grid(row=1, column=1)
		Label(frameFechas, text="Mes:").grid(row=1, column=2)
		Entry(frameFechas,width=2,textvariable=mes).grid(row=1, column=3)
		Label(frameFechas, text="Ano:").grid(row=1, column=4)
		Entry(frameFechas,width=5,textvariable=ano).grid(row=1, column=5)
		Button(frameFechas, text="Cambiar", command=lambda: self.cambiarFechaInicio(dia.get(),mes.get(),ano.get(), proyecto, frameMain), width=10).grid(row=1, column=6)
		Label(frameFechas, text="Anadir fecha festiva:").grid(row=2, columnspan=7, sticky=W)
		Label(frameFechas, text="Dia:").grid(row=3)
		Entry(frameFechas,width=2,textvariable=diaf).grid(row=3, column=1)
		Label(frameFechas, text="Mes:").grid(row=3, column=2)
		Entry(frameFechas,width=2,textvariable=mesf).grid(row=3, column=3)
		Label(frameFechas, text="Ano:").grid(row=3, column=4)
		Entry(frameFechas,width=5,textvariable=anof).grid(row=3, column=5)
		Button(frameFechas, text="Anadir", command=lambda: self.addFestivo(diaf.get(),mesf.get(),anof.get(),frameFechas , proyecto , frameMain), width=10).grid(row=3, column=6)
		
		self.mostrarFechasFestivas(frameFechas)
       	
	
	
	def setDuracion(self, duracion):
		self.duracion = duracion
	
	def getDuracion(self):
		return self.duracion
		
	def addFestivo(self, dia, mes , ano, ventana_fechas , proyecto , frameMain):
		fecha = date(int(ano),int(mes),int(dia))
		self.festivos.append(fecha)
		
       		self.mostrarFechasFestivas(ventana_fechas)

		self.fixLaborables()

		Gantt(frameMain,proyecto)
		proyecto.mostrarInformacion(frameMain)
	
	def fixLaborables(self):
		self.laborables = []
		
		i=0
		while len(self.laborables)!=self.duracion+1:
			if self.fechaInicio+timedelta(days=i) not in self.festivos:
				self.laborables.append(self.fechaInicio+timedelta(days=i))
			i=i+1
		
		
		'''
		fest = 0
		for i in range(self.duracion):
			if self.fechaInicio+timedelta(days=i+fest) in self.festivos:
				fest = fest+1
				self.laborables.append(self.fechaInicio+timedelta(days=i+fest))
			else:
				self.laborables.append(self.fechaInicio+timedelta(days=i+fest))
				
		self.laborables.append(self.fechaInicio+timedelta(days=len(self.laborables)+fest))'''
	
	def getLaborables(self):
		return self.laborables
		
	def addLaborable(self,other):
		self.laborables.append(other)
		
	def getFechaInicio(self):
		return self.fechaInicio
		
	def mostrarFechasFestivas(self, ventana_fechas):
		
       		tabla = Tabla(ventana_fechas, len(self.festivos)+1,1,40)
       		tabla.set(0,0,"Fechas festivas: ")
       		for i in self.festivos:
       			tabla.set(self.festivos.index(i)+1,0,i)
               	tabla.grid(column=7, row =0, rowspan=20, sticky=N)
			
		
		
		

		
  