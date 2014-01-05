from Tkinter import *
from ttk import *


class Gantt:
	
	
	def __init__(self, frame, proyecto):

		tareas = proyecto.getTareas()
		duracion = proyecto.getDuracion()

		n = len(tareas)
		
		#TAMANYO
		altura=20
		ancho=40

		w = Canvas(frame, width=80+ancho*duracion, height=80+altura*n)
		w.grid(column=1, row=13,columnspan=6 , sticky=W)

		w.create_line(40, 40+altura*n, 40, 40)
		w.create_line(40, 40+altura*n, 40+ancho*duracion, 40+altura*n)
		
		for j in range(duracion+1):
			w.create_line(40+ancho*j,40+altura*n,40+ancho*j,50+altura*n)
			w.create_text(40+ancho*j,60+altura*n,text=proyecto.getLaborables()[j].strftime('%d/%b'), font=("Purisa",10))

		for i in tareas:
			if i.getHolgura()==0:
				w.create_rectangle(40+ancho*i.getEarlyStart(), 40+altura*tareas.index(i), 40+ancho*i.getEarlyStart()+ancho*i.getDuracion(), 40+altura+altura*tareas.index(i), fill="red")
			else:
				w.create_rectangle(40+ancho*i.getEarlyStart(), 40+altura*tareas.index(i), 40+ancho*i.getEarlyStart()+ancho*i.getDuracion(), 40+altura+altura*tareas.index(i), fill="blue")
			w.create_text(20,40+(altura/2)+altura*tareas.index(i),text=i.getNombre())
			
		