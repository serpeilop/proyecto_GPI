from Tabla import *
from datetime import *
from Tkinter import *
from ttk import *

class Fechas:

	festivos =[]
	laborables =[]
	fechaInicio = None
	duracion = 0

	def cambiarFechaInicio(self, dia, mes , ano):
		fechaInicio = date(int(ano),int(mes),int(dia))
		self.fechaInicio = fechaInicio
		self.fixLaborables()
		
	def setFechas(self, ventana_fechas):
		
		dia = StringVar()
		mes = StringVar()
		ano = StringVar()
		diaf = StringVar()
		mesf = StringVar()
		anof = StringVar()
	
		Label(ventana_fechas, text="Fecha de Inicio:").grid(row=0, columnspan=7, sticky=W)
		Label(ventana_fechas, text="Dia:").grid(row=1)
		Entry(ventana_fechas,width=2,textvariable=dia).grid(row=1, column=1)
		Label(ventana_fechas, text="Mes:").grid(row=1, column=2)
		Entry(ventana_fechas,width=2,textvariable=mes).grid(row=1, column=3)
		Label(ventana_fechas, text="Ano:").grid(row=1, column=4)
		Entry(ventana_fechas,width=5,textvariable=ano).grid(row=1, column=5)
		Button(ventana_fechas, text="Cambiar", command=lambda: self.cambiarFechaInicio(dia.get(),mes.get(),ano.get()), width=10).grid(row=1, column=6)
		Label(ventana_fechas, text="Anadir fecha festiva:").grid(row=2, columnspan=7, sticky=W)
		Label(ventana_fechas, text="Dia:").grid(row=3)
		Entry(ventana_fechas,width=2,textvariable=diaf).grid(row=3, column=1)
		Label(ventana_fechas, text="Mes:").grid(row=3, column=2)
		Entry(ventana_fechas,width=2,textvariable=mesf).grid(row=3, column=3)
		Label(ventana_fechas, text="Ano:").grid(row=3, column=4)
		Entry(ventana_fechas,width=5,textvariable=anof).grid(row=3, column=5)
		Button(ventana_fechas, text="Anadir", command=lambda: self.addFestivo(diaf.get(),mesf.get(),anof.get(),ventana_fechas), width=10).grid(row=3, column=6)
		
		self.mostrarFechasFestivas(ventana_fechas)
       	
	
	
	def setDuracion(self, duracion):
		self.duracion = duracion
	
	def getDuracion(self):
		return self.duracion
		
	def addFestivo(self, dia, mes , ano, ventana_fechas):
		fecha = date(int(ano),int(mes),int(dia))
		self.festivos.append(fecha)
		
       		self.mostrarFechasFestivas(ventana_fechas)
	
	def fixLaborables(self):
		self.laborables = []
		for i in range(self.duracion):
			self.laborables.append(self.fechaInicio+timedelta(days=i))
		self.laborables.append(self.fechaInicio+timedelta(days=len(self.laborables)))
	
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
			
		
		
		

		
  