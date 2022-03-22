startX = 250
startY = 250
directionX = 4
directionY = 1 


def setup():
    size(500,500)
    background(0,0,100)
    colorMode(HSB,800,100,100)
    #colorMode(HSB,random(800),random(100),random(100))

def draw():
    global startX , directionX , startY , directionY 
    i = frameCount % 800
    H = i
    S = 100
    B = 100  
    startX= startX + directionX
    startY= startY + directionY
    startY= startY + directionY
    startX= startX + directionX
    fill(H,S,B,100)
    ellipse(startX, startY, 20, 20)
    
    if startX > width:
        directionX =-directionX
        
    if startY > height:
        directionY =-directionY
        
    if startX < 0:
        directionX = -directionX
        
    if startY < 0:
        directionY = -directionY
    
