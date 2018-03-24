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
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Amine's spaghetti game")
pygame.draw.rect(screen, GREEN, [50,50,100,100])

while not done:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        



    #Title :D
    screen.fill(COLORS[a])
    pygame.display.flip()
    a = (a + 1)%len(COLORS)
    pygame.time.Clock().tick(5)
    print("hello")
