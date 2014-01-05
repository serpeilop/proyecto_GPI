from Tkinter import *
from Tabla import *
from RecursosLimitados import *
from Proyecto import *
from Fechas import *
from CaminoCritico import *
from NivelacionRecursos import *
from Gantt import *
from MejoraProgramacionesFactibles import *
from ttk import *
from Flexibilidad import *
import tkMessageBox

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


proyecto.getRecursos().append(Recurso('Analista',2))
proyecto.getRecursos().append(Recurso('Programador',3))


proyecto.getTareas()[0].addRecurso(proyecto.getRecursos()[0], 1)
proyecto.getTareas()[1].addRecurso(proyecto.getRecursos()[0], 1)
proyecto.getTareas()[2].addRecurso(proyecto.getRecursos()[1], 3)
proyecto.getTareas()[3].addRecurso(proyecto.getRecursos()[0], 1)

caminoCritico = CaminoCritico(proyecto)
caminoCritico.calculoCaminoCritico()
'''
#-----------------------------


Label(frameMain, text="Nombre: ").grid()
nom = StringVar()
Entry(frameMain, textvariable=nom).grid()

Label(frameMain, text="Duracion: ").grid()
dur = StringVar()
Entry(frameMain, textvariable=dur).grid()

Label(frameMain, text="Antecesoras: ").grid()
ant = StringVar()
Entry(frameMain, textvariable=ant).grid()

def introducirTarea():
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

	proyecto.setRecursos(frameRecursos, frameMain, proyecto)
	
	proyecto.mostrarInformacion(frameMain)
	
	caminoCritico = CaminoCritico(proyecto)
	caminoCritico.calculoCaminoCritico()
	Gantt(frameMain,proyecto)
                
def calcularRL():
	if len(proyecto.getRecursos()) == 0:
		tkMessageBox.showerror("Error", "Debes crear y asignar recursos.")
	else:
		print 'Recursos Limitados: Calculo del esquema Serie'
		recLimitados = RecursosLimitados(proyecto,frameMain) 
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
		progFactibles = MejoraProgramacionesFactibles(proyecto,frameMain)
		progFactibles.aplicarMejoras()

def flexibilidad():
	if len(proyecto.getRecursos()) == 0:
		tkMessageBox.showerror("Error", "Debes crear y asignar recursos.")
	else:
		print 'Flexibilidad'
		flexibilidad = Flexibilidad(frameMain,proyecto)
		flexibilidad.comprobarHolguras()
		
def nivelacionRecursos():
	nivelacionRecursos = NivelacionRecursos(proyecto)
	nivelacionRecursos.mostrarNivelacion()

Button(frameMain, text="Introducir", command=introducirTarea, width=17).grid()
Label(frameMain, text=" ").grid()
Label(frameMain, text="Opciones: ").grid()
Button(frameMain, text="Nivelacion de Recursos", command=nivelacionRecursos, width=17).grid()
Button(frameMain, text="Recursos Limitados", command=calcularRL, width=17).grid()
Button(frameMain, text="Mejora Progr. Factibles", command=mejoraPF, width=17).grid()
Button(frameMain, text="Flexibilidad", command=flexibilidad, width=17).grid()

proyecto.mostrarInformacion(frameMain)

proyecto.setFechas(frameFechas)
proyecto.setRecursos(frameRecursos, frameMain, proyecto)

frame.mainloop()         