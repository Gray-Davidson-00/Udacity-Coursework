import turtle
import math




    
def draw_shapes ():
    
    draw_interior_triangle()

        


def draw_interior_triangles ():
    m = 3  # order of the gasket
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue", "white")
    brad.speed(3)
    brad.forward(n/2)
    brad.fill(True)
    brad.left(120)
#    while m>0:
    r = math.pow(2,m)
    brad.forward(n/r)
    brad.left(60)
    k = 0
    while k<3:
        brad.forward(n/r)
        brad.left(120)
        k = k+1
    brad.fill(False)
    brad.forward((2*n)/r)
#        m = m-1

def draw_big_triangle ():



    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue", "green")
    angie.speed(3)
    angie.fill(True)
    angie.forward(n/2)
    j = 0
    while j<3:
        angie.left(120)
        angie.forward(n)
        j = j+1
    angie.fill(False)


n = 200 #gasket outer edge size
def draw_shapes ():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_big_triangle ()
    draw_interior_triangles()

    window.exitonclick()



draw_shapes ()
