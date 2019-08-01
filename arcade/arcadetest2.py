import arcade
sWidth = 600
sHeight = 600
x = 200
def drawCircle(delta_time):
    arcade.start_render()
    arcade.draw_circle_filled(x, 350, 5, arcade.color.BLACK)
    x+=1
# Open window
def main():
    arcade.open_window(sWidth, sHeight, 'test')
    # Keep instance running
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(drawCircle, 1/60)
    arcade.run()
main()