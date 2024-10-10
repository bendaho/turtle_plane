import turtle

# Настройка окна
window = turtle.Screen()
window.bgcolor("white")
window.title("Авиалайнер")

# Создание черепахи
airplane = turtle.Turtle()
airplane.speed(5)
airplane.penup()

# Функция для рисования прямоугольника
def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Функция для рисования треугольника
def draw_triangle(t, side, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

# Функция для рисования круга
def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Рисование фюзеляжа
airplane.goto(-150, 0)
airplane.pendown()
draw_rectangle(airplane, 300, 50, "gray")

# Рисование крыльев
airplane.penup()
airplane.goto(-100, 0)
airplane.pendown()
airplane.left(45)
draw_triangle(airplane, 100, "gray")

airplane.penup()
airplane.goto(100, 0)
airplane.pendown()
airplane.right(90)
draw_triangle(airplane, 100, "gray")

# Рисование хвоста
airplane.penup()
airplane.goto(150, 0)
airplane.pendown()
airplane.right(45)
draw_triangle(airplane, 50, "gray")

# Рисование двигателей
airplane.penup()
airplane.goto(-50, -25)
airplane.pendown()
draw_circle(airplane, 20, "white")

airplane.penup()
airplane.goto(50, -25)
airplane.pendown()
draw_circle(airplane, 20, "white")

# Рисование окон
airplane.penup()
airplane.goto(-140, 10)
airplane.pendown()
for _ in range(6):
    draw_circle(airplane, 5, "blue")
    airplane.penup()
    airplane.forward(50)
    airplane.pendown()

# Завершение рисования
airplane.hideturtle()
turtle.done()
