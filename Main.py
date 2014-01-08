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

#----------------------- EJEMPLOS -------------------------

proyecto.fechasProyecto.cambiarFechaInicio(2,2,1988,proyecto, frameMain)

def crearRecurso(nombre, cantidad):
	proyecto.getRecursos().append(Recurso(nombre,cantidad))
	
def meterTarea(nombre, duracion, antecesoras, recursos):
	
	aux = Tarea(nombre, duracion)  
	if antecesoras!='':
		for j in antecesoras.split(","):
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
	
	for i in recursos:
		for j in proyecto.getRecursos():
			if j.getNombre()==i:
				aux.addRecurso(j,recursos[i])


# -- Ejemplo con 11 Tareas
'''
crearRecurso("R1",6)
crearRecurso("R2",5)

meterTarea("A",5,"",{"R1":3,"R2":2})
meterTarea("B",5,"",{"R1":2,"R2":4})
meterTarea("C",4,"A",{"R1":3,"R2":1})
meterTarea("D",2,"A",{"R1":4,"R2":3})
meterTarea("E",3,"D",{"R1":2})
meterTarea("F",3,"D,",{"R1":1,"R2":1})
meterTarea("G",4,"B",{"R1":3,"R2":1})
meterTarea("H",3,"F,G",{"R1":2,"R2":2})
meterTarea("I",3,"C",{"R1":3,"R2":2})
meterTarea("J",2,"E,I",{"R1":4,"R2":1})
meterTarea("K",3,"J",{"R1":5,"R2":4})
'''
#-- Ejemplo con 30 Tareas

crearRecurso("R1",7)
crearRecurso("R2",6)

meterTarea("A",5,"",{"R1":3,"R2":2})
meterTarea("B",5,"",{"R1":2,"R2":4})
meterTarea("C",4,"A",{"R1":3,"R2":1})
meterTarea("D",2,"A",{"R1":4,"R2":3})
meterTarea("E",3,"D",{"R1":2})
meterTarea("F",3,"D,",{"R1":1,"R2":1})
meterTarea("G",4,"B",{"R1":3,"R2":1})
meterTarea("H",3,"F,G",{"R1":2,"R2":2})
meterTarea("I",3,"C",{"R1":3,"R2":2})
meterTarea("J",2,"E,I",{"R1":4,"R2":1})
meterTarea("K",3,"J",{"R1":5,"R2":4})
meterTarea("L",5,"K",{"R1":3,"R2":2})
meterTarea("M",5,"K",{"R1":2,"R2":4})
meterTarea("N",4,"L",{"R1":3,"R2":1})
meterTarea("O",2,"L",{"R1":4,"R2":3})
meterTarea("P",3,"O",{"R1":2})
meterTarea("Q",3,"O",{"R1":1,"R2":1})
meterTarea("R",4,"M",{"R1":3,"R2":1})
meterTarea("S",3,"Q,R",{"R1":2,"R2":2})
meterTarea("T",3,"N",{"R1":3,"R2":2})
meterTarea("U",2,"P,T",{"R1":4,"R2":1})
meterTarea("V",3,"U",{"R1":5,"R2":4})
meterTarea("W",5,"V",{"R1":3,"R2":2})
meterTarea("X",5,"V",{"R1":2,"R2":4})
meterTarea("Y",4,"W",{"R1":3,"R2":1})
meterTarea("Z",2,"W",{"R1":4,"R2":3})
meterTarea("EE",3,"Z",{"R1":2})
meterTarea("FF",3,"Z,",{"R1":1,"R2":1})
meterTarea("GG",4,"X",{"R1":3,"R2":1})
meterTarea("HH",3,"FF,GG",{"R1":2,"R2":2})
meterTarea("II",3,"Y",{"R1":3,"R2":2})
meterTarea("JJ",2,"EE,II",{"R1":4,"R2":1})
meterTarea("KK",3,"JJ",{"R1":5,"R2":4})


#-----
caminoCritico = CaminoCritico(proyecto)
caminoCritico.calculoCaminoCritico()

proyecto.fixLaborables()

frameGantt = Tk()
frameGantt.wm_title("Gestion de Proyectos: Gantt del Proyecto")
Gantt(frameGantt,proyecto,14,1)

#---------------------- FIN EJEMPLOS ------------------	 



Label(frameMain, text="Nombre: ").grid(row=1)
nom = StringVar()
Entry(frameMain, textvariable=nom).grid(row=2)

Label(frameMain, text="Duracion: ").grid(row=3)
dur = StringVar()
Entry(frameMain, textvariable=dur).grid(row=4)

Label(frameMain, text="Antecesoras: ").grid(row=5)
ant = StringVar()
Entry(frameMain, textvariable=ant).grid(row=6)


def nuevaTarea(nombre, duracion, antecesoras):
	aux = Tarea(nombre, duracion)  
	if antecesoras!='':
		for j in antecesoras.split(","):
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
	
def introducirTarea():
	if proyecto.getFechaInicio()==None:
		tkMessageBox.showerror("Error", "Debes definir una fecha de inicio del proyecto")
	else:
	       	nuevaTarea(nom.get(),int(dur.get()),ant.get())
	       
		
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