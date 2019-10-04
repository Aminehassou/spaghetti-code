import pygame
pygame.init()

def redraw_game_window():
    win.blit(bg, (0,0))
    character.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

window_width = 500
window_height = 500

clock = pygame.time.Clock()

class Character(object):
    def __init__(self, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_height = character_height
        self.character_width = character_width
        self.vel = 4
        self.is_jump = False
        self.is_left = False
        self.is_right = False
        self.is_standing = True
        self.walk_count = 0
        self.jump_count = 10
        self.frame_per_image = 5

    def draw(self, win):
        self.walk_count = (self.walk_count) % (self.frame_per_image * 9)

        if not self.is_standing:
            if self.is_left:
                win.blit(walk_left[self.walk_count//self.frame_per_image], (self.x, self.y))
                self.walk_count += 1

            elif self.is_right:
                win.blit(walk_right[self.walk_count//self.frame_per_image], (self.x, self.y))
                self.walk_count += 1     
        else:
            if self.is_right:
                win.blit(walk_right[0], (self.x, self.y))
            else:
                win.blit(walk_left[0], (self.x, self.y))
            win.blit(char, (self.x, self.y))

class Projectile(object):
    def __init__(self, x, y, radius, color, is_facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.is_facing = is_facing
        self.vel = 8 * is_facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Game")

character = Character(200, 410, 64,64)
bullets = []
run = True

# Main Game Loop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if character.is_left:
            is_facing = -1
        
        elif character.is_right:
            is_facing = 1
            
        else:
            is_facing = 0

        if len(bullets) < 5 and is_facing != 0:
            projectile = Projectile(round(character.x + character.character_width //2), round(character.y + character.character_height//2), 6, (0,0,0), is_facing)
            bullets.append(projectile)

    if keys[pygame.K_LEFT] and character.x > 0: 
        character.x -= character.vel
        character.is_left = True
        character.is_right = False
        character.is_standing = False

    elif keys[pygame.K_RIGHT] and character.x < 500 - character.character_width:  
        character.x += character.vel
        character.is_right = True
        character.is_left = False
        character.is_standing = False

    else:

        character.walk_count = 0

    if not(character.is_jump): 
        if keys[pygame.K_UP]:
            character.is_jump = True
    else:
        if character.jump_count >= -10:
            character.y -= (character.jump_count * abs(character.jump_count)) * 0.5
            character.jump_count -= 1
        else: 
            character.jump_count = 10
            character.is_jump = False
            
    redraw_game_window()

pygame.quit()