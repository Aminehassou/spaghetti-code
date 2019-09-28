import pygame
pygame.init()

def redraw_game_window():
    global walk_count

    frame_per_image = 3

    win.blit(bg, (0, 0))

    walk_count = (walk_count) % (frame_per_image * 9)

    if is_left:
        win.blit(walk_left[walk_count//frame_per_image], (x, y))
        walk_count += 1

    elif is_right:
        win.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    
    else:
        win.blit(char, (x, y))
        walk_count = 0

    pygame.display.update()    

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

window_width = 500
window_height = 500

clock = pygame.time.Clock()

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Game")

x = 50
y = 400

player_width = 64
player_height = 64

vel = 5

is_left = False
is_right = False
is_jump = False

jump_count = 10
walk_count = 0

run = True

# Main Game Loop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0: 
        x -= vel
        is_left = True
        is_right = False

    elif keys[pygame.K_RIGHT] and x < 500 - player_width:  
        x += vel
        is_right = True
        is_left = False

    else:
        is_right = False
        is_left = False
        walk_count = 0

    if not(is_jump): 
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else: 
            jump_count = 10
            is_jump = False
            
    redraw_game_window()

pygame.quit()