import arcade
import time
import random
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
RADIUS = 32
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.timer = 0
        self.score = 0
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.appear_sound = arcade.load_sound('pop.ogg')

        # Create our ball
        self.coin_list = None
    
    def coin_respawn(self):
        self.coin_list[0].center_x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
        self.coin_list[0].center_y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
        arcade.play_sound(self.appear_sound)   
        self.timer = 0

    def setup(self):
        self.player_sprite = arcade.Sprite("coin.png", 0.5)
        self.coin_list = arcade.SpriteList()
        self.player_sprite.center_x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
        self.player_sprite.center_y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
        self.coin_list.append(self.player_sprite)
        print(self.coin_list)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        score_text = 'Score = {}'.format(self.score)
        arcade.draw_text(score_text, 10, 20, arcade.color.WILD_STRAWBERRY, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and distance(x, y, self.coin_list[0].center_x, self.coin_list[0].center_y) <= RADIUS:
            print('Left mouse button was pressed')
            print(x, y)
            self.coin_respawn()
            self.score += 5

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer >= 2:
            self.coin_respawn()

def main():
    window = MyGame(640, 480, "Drawing Example")
    window.setup()
    arcade.run()

main()