add_library('sound')
import rgb_model as model
import microphone

#Numbers of circles 
num_circle = 150 
t = 2

def setup():
    size(1000,1000)
    colorMode(model.color_mode, model.color_max_val)
    microphone.initialize(this, AudioIn, Amplitude)
    frameRate(10)

def draw():
    sound_level = microphone.get_level()
    agent_x = sound_level
    agent_y = 0.3
    model.update_agent_location(agent_x, agent_y)

    r, g, b = model.get_current_rgb_values()
    
    background(0)
    fill(r,g,b)
    translate(width/2, height/2)
    for i in range(num_circle):
        rotate(radians(390/num_circle))
        #fill(r,g,b)
        pushMatrix()
        translate(150,150)
        rotate(radians(t+3*i*390/num_circle))
        x = model.agent_x
        y = model.agent_y
        ellipse(x,y,15,15)
        popMatrix()
