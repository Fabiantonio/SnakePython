import turtle
import time
import random

#Configuración inicial
dificultad = "normal"  # fácil, normal, difícil
velocidades = {"fácil": 0.15, "normal": 0.1, "difícil": 0.05}
posponer = velocidades[dificultad]

#Marcador
puntuacion = 0
record = 0

#Configuracion ventana
window = turtle.Screen()
window.title("SNAKE GAME")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Línea divisoria
linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.penup()
linea.goto(-300, 250)  # Empezar desde el borde izquierdo
linea.pendown()
linea.forward(600)  # Dibujar línea horizontal
linea.hideturtle()

# Colores para el gradiente de la serpiente
colores_serpiente = ["#00FF00", "#00E000", "#00C000", "#00A000", "#008000"]

#Cabeza Serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color(colores_serpiente[0])
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo snake
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Puntuación: 0         Record: 0", align="center", font=("Courier", 20, "bold"))

# Menú inicial
menu_text = turtle.Turtle()
menu_text.speed(0)
menu_text.color("white")
menu_text.penup()
menu_text.hideturtle()
menu_text.goto(0, 50)

# Variables de estado del juego
jugando = False
en_game_over = False

def mostrar_menu():
    global jugando, en_game_over
    jugando = False
    en_game_over = False
    menu_text.clear()
    menu_text.goto(0, 100)
    menu_text.write("SNAKE GAME", align="center", font=("Courier", 36, "bold"))
    menu_text.goto(0, 20)
    menu_text.write("Presiona ESPACIO para comenzar", align="center", font=("Courier", 14, "normal"))
    menu_text.goto(0, -20)
    menu_text.write("Controles:", align="center", font=("Courier", 14, "normal"))
    menu_text.goto(0, -50)
    menu_text.write("↑ ↓ → ← para mover", align="center", font=("Courier", 14, "normal"))
    menu_text.goto(0, -80)
    menu_text.write(f"Dificultad: {dificultad} (Presiona D para cambiar)", align="center", font=("Courier", 14, "normal"))
    
    # Ocultar serpiente y comida
    cabeza.goto(1000, 1000)
    comida.goto(1000, 1000)
    for segmento in segmentos:
        segmento.goto(1000, 1000)

def mostrar_game_over():
    global jugando, en_game_over
    jugando = False
    en_game_over = True
    menu_text.clear()
    menu_text.goto(0, 50)
    menu_text.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
    menu_text.goto(0, -20)
    menu_text.write(f"Puntuación final: {puntuacion}", align="center", font=("Courier", 14, "normal"))
    menu_text.goto(0, -50)
    menu_text.write("Presiona ESPACIO para volver al menú", align="center", font=("Courier", 14, "normal"))

def iniciar_juego():
    global jugando, en_game_over
    if not jugando:
        if en_game_over:
            mostrar_menu()  # Si estamos en game over, volver al menú principal
        else:
            jugando = True
            menu_text.clear()
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            comida.goto(0, 100)

def game_over():
    # Limpiar el juego
    for segmento in segmentos:
        segmento.goto(1000,1000)
    segmentos.clear()
    
    # Resetear marcador    
    global puntuacion
    texto.clear()
    texto.write(f"Puntuación: {puntuacion}         Record: {record}", align="center", font=("Courier", 20, "bold"))
    
    # Mostrar menú de game over
    mostrar_game_over()

def cambiar_dificultad():
    global dificultad, posponer
    if not jugando and not en_game_over:  # Solo permitir cambiar dificultad en el menú principal
        if dificultad == "fácil":
            dificultad = "normal"
        elif dificultad == "normal":
            dificultad = "difícil"
        else:
            dificultad = "fácil"
        posponer = velocidades[dificultad]
        menu_text.clear()
        mostrar_menu()

def Arriba():
    if jugando and cabeza.direction != "down":
        cabeza.direction = "up"
def Abajo():
    if jugando and cabeza.direction != "up":
        cabeza.direction = "down"
def Derecha():
    if jugando and cabeza.direction != "left":
        cabeza.direction = "right"
def Izquierda():
    if jugando and cabeza.direction != "right":
        cabeza.direction = "left"

# Función de movimiento
def Movimiento():
    if cabeza.direction == "up":
        cabeza.sety(cabeza.ycor() + 20)
    if cabeza.direction == "down":
        cabeza.sety(cabeza.ycor() - 20)
    if cabeza.direction == "right":
        cabeza.setx(cabeza.xcor() + 20)
    if cabeza.direction == "left":
        cabeza.setx(cabeza.xcor() - 20)

#Teclado
window.listen()
window.onkeypress(Arriba, "Up")
window.onkeypress(Abajo, "Down")
window.onkeypress(Derecha, "Right")
window.onkeypress(Izquierda, "Left")
window.onkeypress(iniciar_juego, "space")
window.onkeypress(cambiar_dificultad, "d")

# Mostrar menú inicial
mostrar_menu()

while True:
    window.update()

    if jugando:
        #Colisiones bordes
        if cabeza.xcor()>280 or cabeza.xcor()<-280 or cabeza.ycor()>240 or cabeza.ycor()<-280:
            game_over()

        #Colisiones de comida
        if cabeza.distance(comida)<20:
            x=random.randint(-280,280)
            y=random.randint(-280,250)
            comida.goto(x,y)

            nuevo_segmento=turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            # Asignar color según la posición en la serpiente
            color_index = len(segmentos) % len(colores_serpiente)
            nuevo_segmento.color(colores_serpiente[color_index])
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)
            
            #Aumentar marcador
            puntuacion += 10
            if puntuacion > record:
                record = puntuacion
            texto.clear()
            texto.write(f"Puntuación: {puntuacion}         Record: {record}", align="center", font=("Courier", 20, "bold"))

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
            if segmento.distance(cabeza) < 20:
                game_over()

        time.sleep(posponer)

turtle.mainloop()