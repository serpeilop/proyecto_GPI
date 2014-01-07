from Tkinter import *


class Histograma:
	
	
	def __init__(self, frame, proyecto , row=0, col=0):

		duracion = proyecto.getDuracion()
		
		#for child in frame.winfo_children():
		#    child.destroy()
		for num,rec in enumerate(proyecto.getRecursos()):
			cargas = []		
			for dia in range(duracion):	
				aux=0
				for tarea in proyecto.getTareas():
					if dia>=tarea.getStart() and dia<tarea.getEnd() and rec in tarea.getRecursos():
						aux = aux + tarea.getRecursos()[rec]

				cargas.append(aux)
		
			n = max(max(cargas)+2,rec.getDisponible()+2)		
			altura=30
			ancho=40

			w = Canvas(frame, width=80+ancho*duracion, height=80+altura*n)
			w.grid(row=num+row,column=col)
			
			w.create_text(40+((ancho*duracion)/2),20,text=rec.getNombre())
			

		
			for m in range(n+1):
				w.create_line(30, 40+altura*(n-m), 40, 40+altura*(n-m))
				w.create_text(20,40+altura*(n-m),text=str(m))

			for j in range(duracion+1):
				w.create_line(40+ancho*j,40+altura*n,40+ancho*j,50+altura*n)
				w.create_text(40+ancho*j,60+altura*n,text=proyecto.getLaborables()[j].strftime('%d/%b'), font=("Verdana",7))

			for i, j in enumerate(cargas):
				w.create_rectangle(40+ancho*i, 40+altura*n, 40+ancho+ancho*i, 40+(n-j)*altura, fill="blue")
			
			#EJES
			w.create_line(40, 40+altura*n, 40, 40)
			w.create_line(40, 40+altura*n, 40+ancho*duracion, 40+altura*n)
			#Limite disponible
			w.create_line(40,40+(n-rec.getDisponible())*altura,40+ancho*duracion,40+(n-rec.getDisponible())*altura, fill="red")
			
			
		