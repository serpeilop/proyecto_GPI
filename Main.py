from Tkinter import *
from Tabla import *
from RecursosLimitados import *
from Proyecto import *
from Fechas import *
from CaminoCritico import *
from NivelacionRecursos import *
from Gantt import *
from MejoraProgramacionesFactibles import *
from Flexibilidad import *
import tkMessageBox
from copy import *
from ttk import *

frame = Tk()
#Style().configure("TButton", padding=6, relief="flat", background="#ccc")
frame.wm_title("Gestion de Proyectos")
frame.resizable(0,0)

notebook = Notebook(frame)
notebook.grid()

frameMain = Frame(notebook)
frameFechas = Frame(notebook)
frameRecursos = Frame(notebook)

notebook.add(frameMain, text='Tareas')
notebook.add(frameFechas, text='Fechas')
notebook.add(frameRecursos, text='Recursos')

proyecto = Proyecto()

#------PRUEBAS--------

'''
#Ejercicio Tema 6 (RL)
proyecto.addTarea(Tarea("A", 5))#0
proyecto.addTarea(Tarea("B", 5))#1
proyecto.addTarea(Tarea("C", 4))#2
proyecto.addTarea(Tarea("D", 2))#3
proyecto.addTarea(Tarea("E", 3))#4
proyecto.addTarea(Tarea("F", 3))#5
proyecto.addTarea(Tarea("G", 4))#6
proyecto.addTarea(Tarea("H", 3))#7
proyecto.addTarea(Tarea("I", 3))#8
proyecto.addTarea(Tarea("J", 2))#9
proyecto.addTarea(Tarea("K", 3))#10

proyecto.getTareas()[0].setAntecesora(proyecto.getTareaInicio())
proyecto.getTareas()[0].setSucesora(proyecto.getTareas()[2])
proyecto.getTareas()[0].setSucesora(proyecto.getTareas()[3])

proyecto.getTareas()[1].setAntecesora(proyecto.getTareaInicio())
proyecto.getTareas()[1].setSucesora(proyecto.getTareas()[6])

proyecto.getTareas()[2].setAntecesora(proyecto.getTareas()[0])
proyecto.getTareas()[2].setSucesora(proyecto.getTareas()[8])

proyecto.getTareas()[3].setAntecesora(proyecto.getTareas()[0])
proyecto.getTareas()[3].setSucesora(proyecto.getTareas()[4])
proyecto.getTareas()[3].setSucesora(proyecto.getTareas()[5])

proyecto.getTareas()[4].setAntecesora(proyecto.getTareas()[3])
proyecto.getTareas()[4].setSucesora(proyecto.getTareas()[9])

proyecto.getTareas()[5].setAntecesora(proyecto.getTareas()[3])
proyecto.getTareas()[5].setSucesora(proyecto.getTareas()[7])

proyecto.getTareas()[6].setAntecesora(proyecto.getTareas()[1])
proyecto.getTareas()[6].setSucesora(proyecto.getTareas()[7])

proyecto.getTareas()[7].setAntecesora(proyecto.getTareas()[5])
proyecto.getTareas()[7].setAntecesora(proyecto.getTareas()[6])

proyecto.getTareas()[8].setAntecesora(proyecto.getTareas()[2])
proyecto.getTareas()[8].setSucesora(proyecto.getTareas()[9])

proyecto.getTareas()[9].setAntecesora(proyecto.getTareas()[4])
proyecto.getTareas()[9].setAntecesora(proyecto.getTareas()[8])
proyecto.getTareas()[9].setSucesora(proyecto.getTareas()[10])

proyecto.getTareas()[10].setAntecesora(proyecto.getTareas()[9])
proyecto.getTareas()[10].setSucesora(proyecto.getTareas()[9])

'''
#-------

'''
proyecto.fechasProyecto.cambiarFechaInicio(2,2,1988,proyecto, frameMain)


proyecto.addTarea(Tarea("A", 2))
proyecto.addTarea(Tarea("B", 3))
proyecto.addTarea(Tarea("C", 4))
proyecto.addTarea(Tarea("D", 2))

proyecto.getTareas()[0].setAntecesora(proyecto.getTareaInicio())
proyecto.getTareas()[3].setAntecesora(proyecto.getTareaInicio())
proyecto.getTareas()[2].setAntecesora(proyecto.getTareas()[1])
proyecto.getTareas()[1].setAntecesora(proyecto.getTareas()[0])
proyecto.getTareas()[0].setSucesora(proyecto.getTareas()[1])
proyecto.getTareas()[1].setSucesora(proyecto.getTareas()[2])


proyecto.getTareas()[0].setEarlyStart(0)
proyecto.getTareas()[1].setEarlyStart(2)
proyecto.getTareas()[2].setEarlyStart(5)
proyecto.getTareas()[3].setEarlyStart(0)

proyecto.getTareaInicio().setSucesora(proyecto.getTareas()[0])
proyecto.getTareaInicio().setSucesora(proyecto.getTareas()[3])


proyecto.getRecursos().append(Recurso('Analista',5))

proyecto.getTareas()[0].addRecurso(proyecto.getRecursos()[0], 5)
#proyecto.getTareas()[0].addRecurso(proyecto.getRecursos()[1], 0)
proyecto.getTareas()[1].addRecurso(proyecto.getRecursos()[0], 5)
#proyecto.getTareas()[1].addRecurso(proyecto.getRecursos()[1], 1)
proyecto.getTareas()[2].addRecurso(proyecto.getRecursos()[0], 1)
#proyecto.getTareas()[2].addRecurso(proyecto.getRecursos()[1], 3)
proyecto.getTareas()[3].addRecurso(proyecto.getRecursos()[0], 1)
#proyecto.getTareas()[3].addRecurso(proyecto.getRecursos()[1], 0)


caminoCritico = CaminoCritico(proyecto)
caminoCritico.calculoCaminoCritico()

proyecto.fixLaborables()
Gantt(frameMain,proyecto,14,1)
'''
#-----------------------------


Label(frameMain, text="Nombre: ").grid(row=1)
nom = StringVar()
Entry(frameMain, textvariable=nom).grid(row=2)

Label(frameMain, text="Duracion: ").grid(row=3)
dur = StringVar()
Entry(frameMain, textvariable=dur).grid(row=4)

Label(frameMain, text="Antecesoras: ").grid(row=5)
ant = StringVar()
Entry(frameMain, textvariable=ant).grid(row=6)


def introducirTarea():
	if proyecto.getFechaInicio()==None:
		tkMessageBox.showerror("Error", "Debes definir una fecha de inicio del proyecto")
	else:
	        aux = Tarea(nom.get(), int(dur.get()))  
	        if ant.get()!='':
			for j in ant.get().split(","):
				for i in proyecto.getTareas():
	                        	if i.getNombre()==j:
	                                	aux.setAntecesora(i)
	                               	 	i.setSucesora(aux)
						if(i.getEarlyStart()+i.getDuracion()>aux.getEarlyStart()):
							aux.setEarlyStart(i.getEarlyStart()+i.getDuracion())
		else:
			aux.setEarlyStart(0)
			aux.setAntecesora(proyecto.getTareaInicio())
			proyecto.getTareaInicio().setSucesora(aux)    
			     
	        proyecto.addTarea(aux)
		
		proyecto.setRecursos(frameRecursos, proyecto)

		caminoCritico = CaminoCritico(proyecto)
		caminoCritico.calculoCaminoCritico()
		proyecto.fixLaborables()
		proyecto.mostrarInformacion(frameMain)
		Gantt(frameMain,proyecto,14,1)
                
def calcularRL():
	if len(proyecto.getRecursos()) == 0:
		tkMessageBox.showerror("Error", "Debes crear y asignar recursos.")
	else:
		print 'Recursos Limitados: Calculo del esquema Serie'
		recLimFrame = Tk()
		copiaProyecto = deepcopy(proyecto) 
		recLimitados = RecursosLimitados(copiaProyecto,recLimFrame) 
		recLimitados.aplicarEsquemaSerie()
		#camino critico calcula fechas tardias (YA HECHO)
		#recalcula fechas proyecto
		#calcula holguras

def mejoraPF():
	if len(proyecto.getRecursos()) == 0:
		tkMessageBox.showerror("Error", "Debes crear y asignar recursos.")
	else:
		print 'Mejora Programaciones Factibles'
		#calcularRL()
		mejoraFrame = Tk()
		copiaProyecto = deepcopy(proyecto)
		progFactibles = MejoraProgramacionesFactibles(copiaProyecto,mejoraFrame)
		progFactibles.aplicarMejoras()

def flexibilidad():
	if len(proyecto.getRecursos()) == 0:
		tkMessageBox.showerror("Error", "Debes crear y asignar recursos.")
	else:
		print 'Flexibilidad'
		flexFrame = Tk()
		copiaProyecto = deepcopy(proyecto)
		flexibilidad = Flexibilidad(flexFrame,copiaProyecto)
		flexibilidad.comprobarHolguras()
		flexibilidad.construirVentana()
		
def nivelacionRecursos():
	nivelacionRecursos = NivelacionRecursos(proyecto)
	nivelacionRecursos.mostrarNivelacion()

Button(frameMain, text="Introducir", command=introducirTarea, width=17).grid(row=7)
Label(frameMain, text=" ").grid(row=8)
Label(frameMain, text="Opciones: ").grid(row=9)
Button(frameMain, text="Nivelacion de Recursos", command=nivelacionRecursos, width=17).grid(row=10)
Button(frameMain, text="Recursos Limitados", command=calcularRL, width=17).grid(row=11)
Button(frameMain, text="Mejora Progr. Factibles", command=mejoraPF, width=17).grid(row=12)
Button(frameMain, text="Flexibilidad", command=flexibilidad, width=17).grid(row=13)
#Scrollbar(frameMain).grid(column=3, rowspan=15)
proyecto.mostrarInformacion(frameMain)

proyecto.setFechas(frameFechas, frameMain, proyecto)
proyecto.setRecursos(frameRecursos, proyecto)



frame.mainloop()         