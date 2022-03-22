import hsv_model as model
from random import randint

def setup():
    global size
    noFill()
    strokeWeight(1)
    model.set_color_mode()
    size(model.x_dim, model.y_dim,P3D)
    size = randint(100,200)

def draw():
    global size
    background(0)

    '''
    color_val = model.get_agent_location_color()
    x,y = model.get_agent_location_xy()
    
    '''    
    # location of the sphere
    translate(width/2,height/2,0)

    #movement of the sphere
    rotateX(float(mouseX * 1.5)/width*2)
    rotateY(float(frameCount* 1.5) /height*2)

    # Sphere
    noFill()
    stroke(3*90,255,255)
    sphere(size)
