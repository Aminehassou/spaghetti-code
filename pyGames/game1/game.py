import pygame
pygame.init()

def redraw_game_window():
    text = font.render("Score: {}".format(score), 1, (0, 0, 0))
    win.blit(bg, (0,0))
    win.blit(text, (330, 10))
    character.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

window_width = 825
window_height = 480

score = 0

bullet_sound = pygame.mixer.Sound('bullet.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

class Character(object):
    def __init__(self, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_height = character_height
        self.character_width = character_width
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.is_jump = False
        self.jump_count = 10
        self.x = 60
        self.y = 410
        self.walk_count = 0
        font_hit = pygame.font.SysFont('arial', 100)
        text = font_hit.render('-5', 1, (255, 0, 0))
        center_text_width = (window_width / 2) - (text.get_width() / 2)
        win.blit(text, (center_text_width, 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1

class Enemy(object):
    walk_right = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walk_left = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, x_end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.x_end = x_end
        self.path = [self.x, self.x_end]
        self.walk_count = 0
        self.vel = 3
        self.frame_per_image = 5
        self.health = 10
        self.visible = True
             
    def draw(self, win):
        self.move()
        if self.visible:
            self.walk_count = (self.walk_count) % (self.frame_per_image * 11)
            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count//self.frame_per_image], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count//self.frame_per_image], (self.x, self.y))
                self.walk_count += 1
            health_bar_modifier = 50 - (5 * (10 - self.health))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 120, 0), (self.hitbox[0] - 10, self.hitbox[1] - 20, health_bar_modifier, 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
    
    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
        print("Goblin is hit")
        

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
enemy = Enemy(x = 100, y = 415, width = 64, height = 64, x_end = 450)

bullets = []

shootLoop = 0

run = True

# Main Game Loop
font = pygame.font.SysFont('arial', 30, True)
while run:
    clock.tick(60)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if enemy.visible:
        if character.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and character.hitbox[1] + character.hitbox[3] > enemy.hitbox[1]:
            if character.hitbox[0] + character.hitbox[2] > enemy.hitbox[0] and character.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                character.hit()
                score -= 5

    for bullet in bullets:
        if enemy.visible:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2] and bullet.x + bullet.radius > enemy.hitbox[0]:
                    enemy.hit()
                    hit_sound.play()
                    score += 1 
                    bullets.pop(bullets.index(bullet))

        if bullet.x < window_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bullet_sound.play()

        if character.is_left:
            is_facing = -1
        
        elif character.is_right:
            is_facing = 1
            
        else:
            is_facing = 1
            
        if len(bullets) < 5:
            projectile = Projectile(round(character.x + character.character_width //2), round(character.y + character.character_height//2), 6, (0,0,0), is_facing)
            bullets.append(projectile)
        shootLoop = 1

    if keys[pygame.K_LEFT] and character.x > 0: 
        character.x -= character.vel
        character.is_left = True
        character.is_right = False
        character.is_standing = False

    elif keys[pygame.K_RIGHT] and character.x < window_width - character.character_width:  
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