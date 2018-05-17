import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad2 = turtle.Turtle()
    brad.shape("turtle")
    brad2.shape("turtle")
    brad.color("red")
    brad2.color("black")
    brad.speed(20)
    brad2.speed(10）
    i=0
    while i < 360:
        if  i == 0:
            for k in range(0,4):
                brad.forward(100)
                brad.right(90)
                brad2.forward(200)
                brad2.right(90)
        else:
            for j in range(0,4):
                brad.forward(100)
                brad.right(90)
                brad2.forward(200)
                brad2.right(90)
        brad.right(1)
        brad2.right(1)
        i += 1
    angle = turtle.Turtle()
    angle.shape("arrow")
    angle.color("blue")
    angle.circle(200)
    window.exitonclick()

draw_square()
