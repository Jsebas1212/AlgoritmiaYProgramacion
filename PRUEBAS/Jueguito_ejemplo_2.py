import turtle

# --- 1. CONFIGURACIÓN DE LA PANTALLA ---
ventana = turtle.Screen()
ventana.title("Super Pong 3000 :3")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0) # Hace que el juego corra fluido

# --- 2. CREACIÓN DE OBJETOS ---
# Raqueta Izquierda (Jugador A)
raqueta_a = turtle.Turtle()
raqueta_a.speed(0)
raqueta_a.shape("square")
raqueta_a.color("blue")
raqueta_a.shapesize(stretch_wid=5, stretch_len=1) # Estiramos el cuadrado para hacer un rectángulo
raqueta_a.penup()
raqueta_a.goto(-350, 0)

# Raqueta Derecha (Jugador B)
raqueta_b = turtle.Turtle()
raqueta_b.speed(0)
raqueta_b.shape("square")
raqueta_b.color("red")
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup()
raqueta_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
# Velocidad de la pelota (puedes cambiar estos números)
pelota.dx = 0.2
pelota.dy = 0.2

# --- 3. FUNCIONES DE MOVIMIENTO ---
def raqueta_a_arriba():
    y = raqueta_a.ycor()
    if y < 250: # Límite superior
        raqueta_a.sety(y + 20)

def raqueta_a_abajo():
    y = raqueta_a.ycor()
    if y > -240: # Límite inferior
        raqueta_a.sety(y - 20)

def raqueta_b_arriba():
    y = raqueta_b.ycor()
    if y < 250:
        raqueta_b.sety(y + 20)

def raqueta_b_abajo():
    y = raqueta_b.ycor()
    if y > -240:
        raqueta_b.sety(y - 20)

# Conectar teclado
ventana.listen()
ventana.onkeypress(raqueta_a_arriba, "w")
ventana.onkeypress(raqueta_a_abajo, "s")
ventana.onkeypress(raqueta_b_arriba, "Up") # Flecha arriba
ventana.onkeypress(raqueta_b_abajo, "Down") # Flecha abajo

# --- 4. BUCLE PRINCIPAL DEL JUEGO ---
while True:
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote en los bordes (Arriba y Abajo)
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1 # Invertir dirección

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Si la pelota sale por los lados (Punto anotado)
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1 # Sale hacia el otro lado

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1

    # Choques con las raquetas
    if (340 < pelota.xcor() < 350) and (raqueta_b.ycor() - 50 < pelota.ycor() < raqueta_b.ycor() + 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (-350 < pelota.xcor() < -340) and (raqueta_a.ycor() - 50 < pelota.ycor() < raqueta_a.ycor() + 50):
        pelota.setx(-340)
        pelota.dx *= -1