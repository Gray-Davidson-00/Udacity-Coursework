import pandas as pd 
import build
import turtle

#
#   ----- Code to acquire data from Excel -----
#

xl = pd.ExcelFile("/Users/Gale-Force-Computing/Documents/Programming/Udacity-Coursework/Programming Foundations with Python/Final Project/Building_Data.xlsx")
contents = xl.parse("Sheet1", header=None) #"header=None" is necessary here because without it, the first cell of each column is read as the column's title and is not included as data. 

matrix = contents.as_matrix(columns=None) # convert the data to a matrix
m = matrix

#print(matrix)
#print(matrix[3,4])

#use square brackets when calling a particular loction in a matrix
#note that the matrix's first element is located at "0,0"


#
#   ----- Code to build building objects -----
#

# The code for class Building is contained in build.py in the same folder as this document.


#commercial buildings
chrysler_tower = build.Commercial(m[0,1], m[2,1], m[3,1], m[4,1], m[5,1], m[6,1], m[7,1], m[8,1], m[9,1], m[13,1], m[14,1])
big_ben = build.Commercial(m[0,4], m[2,4], m[3,4], m[4,4], m[5,4], m[6,4], m[7,4], m[8,4], m[9,4], m[13,4], m[14,4])
transamerica = build.Commercial(m[0,2], m[2,2], m[3,2], m[4,2], m[5,2], m[6,2], m[7,2], m[8,2], m[9,2], m[13,2], m[14,2])

#residential buildings
space_needle = build.Residential(m[0,5], m[2,5], m[3,5], m[4,5], m[5,5], m[6,5], m[7,5], m[8,5], m[9,5], m[10,5], m[11,5], m[12,5])
eiffel_tower = build.Residential(m[0,6], m[2,6], m[3,6], m[4,6], m[5,6], m[6,6], m[7,6], m[8,6], m[9,6], m[10,6], m[11,6], m[12,6])
fawlty_towers = build.Residential(m[0,3], m[2,3], m[3,3], m[4,3], m[5,3], m[6,3], m[7,3], m[8,3], m[9,3], m[10,3], m[11,3], m[12,3])


#   -----  Code to call instance methods and draw buildings -----

def draw_buildings ():
    window = turtle.Screen()
    window.bgcolor('#b56666') #a lovely shade of rose.

#we will use this turtle to draw a horizon line.  
    horizon_line = turtle.Turtle()
    horizon_line.penup()
    horizon_line.goto(-300,0)
    horizon_line.pendown()
    horizon_line.goto(300,0)

#draw each building in sequence
    chrysler_tower.draw_building() 
    transamerica.draw_building()
    fawlty_towers.draw_building()
    big_ben.draw_building()
    space_needle.draw_building()
    eiffel_tower.draw_building()
    window.exitonclick()


draw_buildings()










