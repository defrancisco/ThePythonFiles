import turtle

# Configurar turtle
t = turtle.Turtle()
t.speed(5)
turtle.bgcolor("white")

# Función para dibujar un círculo relleno
def circulo(x, y, radio, color):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

# Dibujar la cabeza de Snoopy
circulo(0, 50, 50, "white")  # Cabeza

# Dibujar las orejas
t.color("black")
t.begin_fill()
t.penup()
t.goto(-30, 80)
t.pendown()
t.circle(20, 180)
t.goto(-30, 80)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(30, 80)
t.pendown()
t.circle(-20, 180)
t.goto(30, 80)
t.end_fill()

# Ojos y nariz
circulo(-10, 80, 5, "black")  # Ojo izquierdo
circulo(10, 80, 5, "black")  # Ojo derecho
circulo(20, 60, 7, "black")  # Nariz

# Boca
t.penup()
t.goto(-10, 55)
t.pendown()
t.right(20)
t.circle(10, 120)

# Cuerpo
t.penup()
t.goto(-25, 0)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(40, 180)
t.goto(25, -80)
t.goto(-25, -80)
t.goto(-25, 0)
t.end_fill()

# Collar
t.color("red")
t.penup()
t.goto(-25, 0)
t.pendown()
t.goto(25, 0)

t.hideturtle()
turtle.done()
