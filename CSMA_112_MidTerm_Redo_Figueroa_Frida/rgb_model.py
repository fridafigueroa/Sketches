x_dim = 500
y_dim = 500
color_mode = RGB
color_max_val = 500
 
def update_agent_location(x_norm, y_norm):
    global agent_x, agent_y
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim
    
def get_current_rgb_values():
     r = random(width)
     g = random(height)
     b = 0
     return r, g, b 
 
