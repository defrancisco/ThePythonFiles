import turtle
import random

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("white")
pantalla.title("Flor con texto")

# Crear el turtle
t = turtle.Turtle()
t.speed(0)  # Máxima velocidad

# Función para dibujar un pétalo
def petalo(color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(50, 60)  # Curva de un lado
        t.left(120)
        t.circle(50, 60)  # Curva del otro lado
        t.left(120)
    t.end_fill()

# Función para dibujar una flor con pétalos
def flor(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(6):  # 6 pétalos
        petalo(color)
        t.right(60)

# Dibujar varias flores en posiciones aleatorias
colores = ["red", "blue", "purple", "orange", "pink"]
for _ in range(5):  # 5 flores
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(colores)
    flor(x, y, color)

# Escribir texto en el centro
t.penup()
t.goto(-40, -20)
t.pendown()
t.color("black")
t.write("Flowers!", font=("Arial", 24, "bold"))

t.hideturtle()
pantalla.mainloop()
