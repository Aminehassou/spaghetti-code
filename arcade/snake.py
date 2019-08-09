import arcade
import random
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 1

class Snake:
    def __init__(self, start_x, start_y, end_x, end_y, change_x, change_y):    
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        # Draw the snake with the instance variables.
        arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y, arcade.color.RED, 2)
    
    def update(self):
        # Move the snake
        self.start_x += self.change_x
        self.start_y += self.change_y
        self.end_x += self.change_x
        self.end_y += self.change_y        
'''
class dot(arcade.sprite):
    self.center_x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
    self.center_y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
'''
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.snake = Snake(2, 2, 50, 2, 0, 0)

    def on_draw(self):
        # Called whenever we need to draw the window.
        arcade.start_render()
        self.snake.draw()
    def update(self, delta_time):
        self.snake.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.snake.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.snake.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.snake.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.snake.change_y = -MOVEMENT_SPEED



def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()