import pygame
#Initialize the game engine
pygame.init()
#Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
COLORS = [BLACK, WHITE, GREEN]
#Defining pi
PI = 3.141592653
#Defining and opening window size
size = (700, 500)
a = 0
done = False

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    screen = pygame.display.set_mode(size)
    #Title :D
    pygame.display.set_caption("Amine's spaghetti game")
    screen.fill(COLORS[a])
    pygame.display.flip()
    a = (a + 1)%len(COLORS)
    pygame.time.Clock().tick(5)
    print("hello")
