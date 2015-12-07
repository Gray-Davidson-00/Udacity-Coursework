import turtle

def draw_shapes ():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")

    k = 0
    while k<36:
        i=0
        while i<4:
            brad.forward(100)
            brad.right(90)
            i = i+1
        brad.right(10)
        k = k+1
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    kim = turtle.Turtle()
    kim.color("purple")
    j = 0
    while j<3:
        kim.right(120)
        kim.forward(200)
        j = j+1
        
    window.exitonclick()
draw_shapes()
