import pygame
pygame.init()

def redraw_game_window():
    win.blit(bg, (0,0))
    character.draw(win)
    enemy.draw(win)
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

class Enemy(object):
    walk_right = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walk_left = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, enemy_width, enemy_height, x_end):
        self.x = x
        self.y = y
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.x_end = x_end
        self.path = [self.x, self.x_end]
        self.walk_count = 0
        self.vel = 3
        self.frame_per_image = 5
             
    def draw(self, win):
        self.move()
        self.walk_count = (self.walk_count) % (self.frame_per_image * 11)
        if self.vel > 0:
            win.blit(self.walk_right[self.walk_count//self.frame_per_image], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(self.walk_left[self.walk_count//self.frame_per_image], (self.x, self.y))
            self.walk_count += 1
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0

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

character = Character(x = 200, y = 410, character_width = 64, character_height = 64)
enemy = Enemy(x = 100, y = 410, enemy_width = 64, enemy_height = 64, x_end = 450)
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
            is_facing = 1
            
        if len(bullets) < 5:
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