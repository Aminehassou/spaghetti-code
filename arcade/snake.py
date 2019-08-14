import arcade
import random
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
INDENT = 2
SNAKE_SCALE = 25

class Snake(arcade.Sprite):
    def spawn(self):
        self.center_x = random.randint(SNAKE_SCALE, SCREEN_WIDTH - SNAKE_SCALE)
        self.center_y = random.randint(SNAKE_SCALE, SCREEN_HEIGHT - SNAKE_SCALE)
       

'''
cla ss dot(arcade.sprite):
    self.center_x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
    self.center_y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
'''
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        self.player_list = None
        self.dot_list = None
        self.player_sprite = None
        self.X_SPEED = 0
        self.Y_SPEED = 0
        self.counter = 0
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self):
        # Called whenever we need to draw the window.
        arcade.start_render()
        self.player_list.draw()

    def setup(self):
        self.snake = Snake("dot.png", SNAKE_SCALE)
        self.snake.spawn()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.snake)
        for x in range(1, 4):
            dot = arcade.Sprite('dot.png', SNAKE_SCALE)
            dot.center_x = self.player_list[0].center_x - (SNAKE_SCALE*x)
            dot.center_y = self.player_list[0].center_y
            self.player_list.append(dot)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.X_SPEED = -2
            self.Y_SPEED = 0
        elif key == arcade.key.RIGHT:
            self.X_SPEED = 2
            self.Y_SPEED = 0
        elif key == arcade.key.UP:
            self.X_SPEED = 0
            self.Y_SPEED = 2
        elif key == arcade.key.DOWN:
            self.X_SPEED = 0
            self.Y_SPEED = -2
          
    
    def update(self, delta_time):
        for index in range(1, len(self.player_list)):
            LAST_MOVED_X = self.player_list[index-1].center_x
            LAST_MOVED_Y = self.player_list[index-1].center_y
            self.player_list[index].center_x = LAST_MOVED_X
            self.player_list[index].center_y = LAST_MOVED_Y

        self.player_list[0].center_x += self.X_SPEED
        self.player_list[0].center_y += self.Y_SPEED
        
        print(self.X_SPEED, self.Y_SPEED)
       

def main():
    window = MyGame(640, 480, "Drawing Example")
    window.setup()
    arcade.run()


main()