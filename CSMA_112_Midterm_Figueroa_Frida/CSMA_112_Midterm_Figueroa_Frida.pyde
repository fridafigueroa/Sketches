import hsv_model as model
import agent as Agent
t = 3

def setup():
    size(model.dim_x,model.dim_y)
    model.set_color_mode()
    
def draw():
    global t, direction_X, direction_Y,started
    background(0)
    
    
    #speed of the circles
    if Agent.started == True:
        Agent.speed_circles()
        
    # Controls the direction of the circles with keys (q,w,e,s)
    if keyPressed:
        if key == 'q':
            Agent.direction_X += -5
        if key == 'e': 
            Agent.direction_X += 5
        if key == 'w':
            Agent.direction_Y += -5
        if key == 's': 
            Agent.direction_Y += 5
            
    #Draws the circles and rotates them according to the key thats being pressed 
    translate(width/2, height/2)
    for i in range(Agent.num_circle):
        rotate(radians(390/Agent.num_circle))
        pushMatrix()
        translate(150,150)
        rotate(radians(t+3*i*390/Agent.num_circle))
        stroke(3*i,255,255)
        noFill()
        ellipse(Agent.direction_X,Agent.direction_Y,15,15)
        popMatrix()
