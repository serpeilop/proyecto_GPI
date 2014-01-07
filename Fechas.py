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
	domingos = True

	def cambiarFechaInicio(self, dia, mes , ano , proyecto , frameMain):
		fechaInicio = date(int(ano),int(mes),int(dia))
		self.fechaInicio = fechaInicio
		self.fixLaborables()
		if len(proyecto.getTareas())!=0:
			Gantt(frameMain,proyecto, 14,1)
		proyecto.mostrarInformacion(frameMain)
		
	def setFechas(self, frameFechas, frameMain , proyecto):
		
		dia = StringVar()
		mes = StringVar()
		ano = StringVar()
		diaf = StringVar()
		mesf = StringVar()
		anof = StringVar()
		domingos = IntVar()
	
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
		
		domingos.set(1)
		Checkbutton(frameFechas, text="Domingos son festivos", variable=domingos , command=lambda: self.activarDomingos(frameMain, proyecto)).grid()
		
		self.mostrarFechasFestivas(frameFechas)
       	
	
	
	def setDuracion(self, duracion):
		self.duracion = duracion
	
	def getDuracion(self):
		return self.duracion
	
	def activarDomingos(self, frameMain, proyecto):
		
		self.domingos = not self.domingos
		
		self.fixLaborables()

		Gantt(frameMain,proyecto,14,1)
		proyecto.mostrarInformacion(frameMain)
			
	def addFestivo(self, dia, mes , ano, ventana_fechas , proyecto , frameMain):
		fecha = date(int(ano),int(mes),int(dia))
		self.festivos.append(fecha)
		
       		self.mostrarFechasFestivas(ventana_fechas)

		self.fixLaborables()

		Gantt(frameMain,proyecto,14,1)
		proyecto.mostrarInformacion(frameMain)
	
	def fixLaborables(self):
		self.laborables = []
		
		i=0
		while len(self.laborables)!=self.duracion+1:
			if self.fechaInicio+timedelta(days=i) not in self.festivos and not(self.domingos and (self.fechaInicio+timedelta(days=i)).weekday()==6):
				self.laborables.append(self.fechaInicio+timedelta(days=i))
			i=i+1
		
		
	
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
			
		
		
		

		
  