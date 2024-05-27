import turtle
import time
import random

#Dar velocidad
posponer=0.1

#Marcador
puntuacion=0
record=0

#Configuracion ventana
window=turtle.Screen()
window.title("SNAKE")
window.bgcolor("black")
window.setup(width=600,height=600)
window.tracer(0)

#Cabeza Serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction=("stop")

#Comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo snake
segmentos=[]

#Texto
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Puntuación:0         Record: 0", align="center",font=("Courier",15,"normal"))

#Funciones
def Arriba():
	cabeza.direction="up"
def Abajo():
	cabeza.direction="down"
def Derecha():
	cabeza.direction="right"
def Izquierda():
	cabeza.direction="left"

def Movimiento():
	if cabeza.direction=="up":
		y=cabeza.ycor()
		cabeza.sety(y+20)
	if cabeza.direction=="down":
		y=cabeza.ycor()
		cabeza.sety(y-20)
	if cabeza.direction=="right":
		x=cabeza.xcor()
		cabeza.setx(x+20)
	if cabeza.direction=="left":
		x=cabeza.xcor()
		cabeza.setx(x-20)

#Teclado
window.listen()
window.onkeypress(Arriba, "Up")
window.onkeypress(Abajo, "Down")
window.onkeypress(Derecha, "Right")
window.onkeypress(Izquierda, "Left")


while True:
	window.update()

	#Colisiones bordes
	if cabeza.xcor()>280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction="stop"

		#Borrar segmentos
		for segmento in segmentos:
			segmento.goto(1000,1000)
		segmentos.clear()

		#Resetear marcador
		score=0
		texto.clear()
		texto.write(f"Puntuación:0         Record: {record}", align="center",font=("Courier",15,"normal"))

	#Colisiones de comida
	if cabeza.distance(comida)<20:
		y=random.randint(-200,280)
		x=random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento=turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("green")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)
		#Aumentar marcador
		puntuacion+=10
		if puntuacion>record:
			record=puntuacion
		texto.clear()
		texto.write(f"Puntuación:{puntuacion}         Record: {record}", 
						align="center",font=("Courier",15,"normal"))

	#Mover el cuerpo de la serpiente
	totalseg=len(segmentos)
	for index in range(totalseg -1,0,-1):
		x=segmentos[index-1].xcor()
		y=segmentos[index-1].ycor()
		segmentos[index].goto(x,y)

	if totalseg>0:
		x=cabeza.xcor()
		y=cabeza.ycor()
		segmentos[0].goto(x,y)

	Movimiento()

	#Colisiones con el cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza)<20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction="stop"
			#Borrar segmentos
			for segmento in segmentos:
				segmento.goto(1000,1000)
			segmentos.clear()
			
		#Borrar marcador	
		score=0
		texto.clear()
		texto.write(f"Puntuación:0         Record: {record}", align="center",font=("Courier",15,"normal"))

	time.sleep(posponer)

turtle.mainloop()