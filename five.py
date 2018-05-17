import turtle

longest_line = 256

def draw_triangle(t, color, fill, length):
    t.color(color)
    t.fillcolor(fill)
    t.begin_fill()
    for i in range(1, 4):
        t.forward(length)
        if i == 1:
            right = t.pos()
        elif i == 2:
            left = t.pos()
        elif i == 3:
            top = t.pos()
        t.right(120)
    t.end_fill()
    return {'top': top, 'right': right, 'left': left}

def draw_inner_triangle(t, pos, length, color, fill, layers):
    # draw inner triangle
    # pos is outer triangle top point
    # length is outer triangle side length
    # layers is how many layers the result has
    t.penup()
    t.goto(pos)
    points = [pos, ]
    t.setheading(0)
    t.right(60)
    t.pendown()
    t.forward(length / 2)
    t.right(60)
    positions = draw_triangle(t, color, fill, length / 2)
    t.setheading(0)
    points.append(positions['top'])
    points.append(positions['left'])
    print positions
    print  points
    # use iteration, use layers to control and stop the iteration
    if layers > 1:
        for p in points:
            draw_inner_triangle(t, p, length/2, 'blue', 'white', layers-1)
            print p
        print "________________"


window = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed(0.5)

t.right(60)
print draw_triangle(t, 'blue', 'green', longest_line)

draw_inner_triangle(t, (0, 0), longest_line, 'blue', 'white', 4)

window.exitonclick()
