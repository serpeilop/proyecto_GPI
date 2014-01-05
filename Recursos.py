from Tkinter import *
from Recurso import *
from Tabla import *
from Histograma import *
from ttk import *

class Recursos:

	recursos = []
		
	def getRecursos(self):
		return self.recursos
		
	def crearRecurso(self, nombre, capacidad, frameCrear, frameAsignar, var_recurso):
		recurso = Recurso(str(nombre), int(capacidad))
		self.recursos.append(recurso)
		
       		tabla = Tabla(frameCrear, len(self.recursos)+1,2,20)
       		tabla.set(0,0,"Nombre")
       		tabla.set(0,1,"Cantidad")
       		for i in self.recursos:
       			tabla.set(self.recursos.index(i)+1,0,i.getNombre())
       			tabla.set(self.recursos.index(i)+1,1,i.getDisponible())
               	tabla.grid(column=1, row =0, rowspan=25, sticky=N)
		
		menu_recurso = OptionMenu(frameAsignar, var_recurso,"Elija recurso", *self.recursos)
		menu_recurso.config(width=18)
		menu_recurso.grid(column=0, row= 7)
		
	def asignarRecurso(self,rec, tar , cant, tareas, proyecto, frameHistograma):
		
		tareas[tareas.index(str(tar))].addRecurso(self.recursos[self.recursos.index(str(rec))],int(cant))
		
		Histograma(frameHistograma, proyecto)

		
	def setRecursos(self, frameRecursos, proyecto,tareas):
		

		notebook = Notebook(frameRecursos, width=630, height=500)
		notebook.grid(row=0)
		
		frameCrear = Frame(notebook)
		frameAsignar = Frame(notebook)
		frameHistograma = Frame(notebook)
		
		notebook.add(frameCrear, text='Crear Recursos')
		notebook.add(frameAsignar, text='Asignar Recursos')
		notebook.add(frameHistograma, text='Histogramas')
		
		
		var_recurso = StringVar()
		var_tarea = StringVar()
		
		nombre = StringVar()
		dispo = StringVar()
		
		#ANADIR RECURSOS
		
		Label(frameCrear, text="Nombre:").grid(row=0)
		Entry(frameCrear,textvariable=nombre).grid(row=1)
		Label(frameCrear, text="Cantidad:").grid(row=2)
		Entry(frameCrear,textvariable=dispo).grid(row=3)
		Button(frameCrear, text='Crear', command=lambda: self.crearRecurso(nombre.get(),dispo.get(), frameCrear,frameAsignar, var_recurso)).grid(row=4)
		
 		#ASIGNAR RECURSOS
		
		Label(frameAsignar, text="Asignar recursos:").grid(row=5)
		Label(frameAsignar, text="Recurso:").grid(row=6)
		
		
		
		if len(self.recursos)>0:
			menu_recurso = OptionMenu(frameAsignar, var_recurso,"Elija recurso", *self.recursos)
			menu_recurso.config(width=18)
			menu_recurso.grid(column=0, row= 7)
		else:
			menu_recurso = OptionMenu(frameAsignar, var_recurso, "No hay recursos")
			menu_recurso.config(width=18)
			menu_recurso.grid(column=0, row= 7)
			
		Label(frameAsignar, text="A tarea:").grid(row=8)
		

		if len(tareas)>0:
			menu_tarea = OptionMenu(frameAsignar, var_tarea, "Elija tarea", *tareas)
			menu_tarea.config(width=18)
			menu_tarea.grid(column=0, row= 9)
		else:
			menu_tarea = OptionMenu(frameAsignar, var_tarea, "No hay tareas")
			menu_tarea.config(width=18)
			menu_tarea.grid(column=0, row= 9)
		
		cant = StringVar()
		Label(frameAsignar, text="Cantidad:").grid(row=10)
		Entry(frameAsignar,textvariable=cant).grid(row=11)
		
		Button(frameAsignar, text='Asignar', command=lambda: self.asignarRecurso(var_recurso.get(),var_tarea.get(),cant.get(),tareas, proyecto, frameHistograma)).grid(row=12)
		
		###########

		
       		tabla = Tabla(frameCrear, len(self.recursos)+1,2,20)
       		tabla.set(0,0,"Nombre")
       		tabla.set(0,1,"Cantidad")
       		for i in self.recursos:
       			tabla.set(self.recursos.index(i)+1,0,i.getNombre())
       			tabla.set(self.recursos.index(i)+1,1,i.getDisponible())
               	tabla.grid(column=1, row =0, rowspan=25, sticky=N)
	
