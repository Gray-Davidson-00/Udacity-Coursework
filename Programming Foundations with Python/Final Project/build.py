import webbrowser
import turtle

class Building():
    """This class provdes a way to store generic building information"""
    def __init__(self, name, number_of_floors, length, width, gps_lat, gps_long, year_built, architectural_style, google_maps):
        self.name = name
        self.number_of_floors = number_of_floors
        self.length = length
        self.width = width
        self.gps_lat = gps_lat
        self.gps_long = gps_long
        self.year_built = year_built
        self.architectural_style = architectural_style
        self.google_maps = google_maps
        self.color = (1, 0, 0) #default building color if the color override from the child classes is not working. This color is bright red.   
        
    def where_is_it(self):
        webbrowser.open(self.google_maps)


    def draw_building(self):
        the_pen = turtle.Turtle()
        the_pen.penup() # so we don't draw unseemly lines while we're on our way there.  
        the_pen.goto(self.gps_lat, self.gps_long) #sets the start position for this turtle
        the_pen.pendown() #puts the pen back down so we can draw

        the_pen.color("black", self.color)
        the_pen.fill(True)        

        the_pen.seth(165)
        the_pen.forward(self.length/12)
        the_pen.seth(90)
        the_pen.forward(self.number_of_floors*3)
        the_pen.seth(15)
        the_pen.forward(self.width/12)
        the_pen.seth(345)
        the_pen.forward(self.length/12)
        the_pen.seth(270)
        the_pen.forward(self.number_of_floors*3)
        the_pen.seth(195)
        the_pen.forward(self.width/12)

        the_pen.fill(False)
        
        the_pen.seth(90)
        the_pen.forward(self.number_of_floors*3)
        the_pen.seth(165)
        the_pen.forward(self.length/12)
        the_pen.backward(self.length/12)
        the_pen.seth(15)
        the_pen.forward(self.width/12)

class Residential(Building):
    """This class provdes a way to store Residential-Specific information"""
    def __init__(self, name, number_of_floors, length, width, gps_lat, gps_long, year_built, architectural_style, google_maps, number_of_residents, average_apt_price, number_of_apartments):

        age_coeficient = ((float(year_built)-1900)/100) #convert the building's age from roman calendar to [0,1] so it can be used as an (r,g,b) input.

        self.name = name
        self.number_of_floors = number_of_floors
        self.length = length
        self.width = width
        self.gps_lat = gps_lat
        self.gps_long = gps_long
        self.year_built = year_built
        self.architectural_style = architectural_style
        self.google_maps = google_maps
        self.number_of_residents = number_of_residents
        self.average_apt_price = average_apt_price
        self.number_of_apartments = number_of_apartments
        self.color = (0, age_coeficient, 0) # we will set the red and green components of the colorspace to 0 and regulate the blue component by the buiding's age, thus an older building will appear darker.  
        
class Commercial(Building):
    """This class provdes a way to store Commercial-Specific information"""
    def __init__(self, name, number_of_floors, length, width, gps_lat, gps_long, year_built, architectural_style, google_maps, number_of_businesses, type_of_businesses):

        age_coeficient = ((float(year_built)-1900)/100)

        self.name = name
        self.number_of_floors = number_of_floors #convert the building's age from roman calendar to [0,1] so it can be used as an (r,g,b) input.
        self.length = length
        self.width = width
        self.gps_lat = gps_lat
        self.gps_long = gps_long
        self.year_built = year_built
        self.architectural_style = architectural_style
        self.google_maps = google_maps
        self.number_of_businesses = number_of_businesses
        self.type_of_businesses = type_of_businesses
        self.color = (0, 0, age_coeficient) # we will set the red and green components of the colorspace to 0 and regulate the blue component by the buiding's age, thus an older building will appear darker.  

