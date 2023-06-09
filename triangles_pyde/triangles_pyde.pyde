def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
    

t = 0

def draw():
    global t
    background(255)#white
    translate(width/2,height/2)
    for i in range(90):
        #space the triangles evenly
        #around the circle
        stroke(i*255/90,255,255)
        strokeWeight(4)
        rotate(radians(360/90))
        pushMatrix() #save this orientation
        #go to circumference of circle
        translate(200,0)
        #spin each triangle
        rotate(radians(t+2*i*360/90))
        #draw the triangle
        tri(100)
        #return to saved orientation
        popMatrix()
    t += 0.5

def tri(length):
    noFill() #makes the triangle transparent

    triangle(0,-length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
