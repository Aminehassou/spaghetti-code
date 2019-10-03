import pygame
pygame.init()

def redraw_game_window():
    win.blit(bg, (0,0))
    player.draw(win)
    
    pygame.display.update()

 

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

window_width = 500
window_height = 500

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, player_width, player_height):
        self.x = x
        self.y = y
        self.player_height = player_height
        self.player_width = player_width
        self.vel = 5
        self.is_jump = False
        self.is_left = False
        self.is_right = False
        self.walk_count = 0
        self.jump_count = 10
        self.frame_per_image = 3

    def draw(self, win):
        self.walk_count = (self.walk_count) % (self.frame_per_image * 9)
        if self.is_left:
            win.blit(walk_left[self.walk_count//self.frame_per_image], (self.x, self.y))
            self.walk_count += 1

        elif self.is_right:
            win.blit(walk_right[self.walk_count//self.frame_per_image], (self.x, self.y))
            self.walk_count += 1
        
        else:
            win.blit(char, (self.x, self.y))
         
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Game")

player = Player(200, 410, 64,64)
run = True

# Main Game Loop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.x > 0: 
        player.x -= player.vel
        player.is_left = True
        player.is_right = False

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.player_width:  
        player.x += player.vel
        player.is_right = True
        player.is_left = False

    else:
        player.is_right = False
        player.is_left = False
        player.walk_count = 0

    if not(player.is_jump): 
        if keys[pygame.K_SPACE]:
            player.is_jump = True
    else:
        if player.jump_count >= -10:
            player.y -= (player.jump_count * abs(player.jump_count)) * 0.5
            player.jump_count -= 1
        else: 
            player.jump_count = 10
            player.is_jump = False
            
    redraw_game_window()

pygame.quit()