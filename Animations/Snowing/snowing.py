import random
import numpy as np
import math
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1920
SCREEN_TITLE = "Snow Animation"
VIEWPORT_MARGIN = 40

class Snowflake:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_HEIGHT)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        self.shapes = arcade.ShapeElementList()

        color_1 = (0, 10, 12)
        color_2 = (215, 214, 255)
        points = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
        colors = (color_1, color_1, color_2, color_2)
        rectangle = arcade.create_rectangle_filled_with_colors(points, colors)
        self.shapes.append(rectangle)

        self.snowflake_list = None

    def start_snowfall(self):
        self.snowflake_list = []

        for _ in range(1000):
            snowflake = Snowflake()
            snowflake.x = random.randrange(SCREEN_WIDTH + random.randrange(-10, 10))
            snowflake.y = random.randrange(SCREEN_HEIGHT + 200)
            snowflake.size = np.random.poisson(2)
            snowflake.speed = np.random.poisson(40)
            snowflake.angle = random.uniform(math.pi, math.pi * 2)
            self.snowflake_list.append(snowflake)

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        self.shapes.draw()
        for snowflake in self.snowflake_list:
            arcade.draw_circle_filled(snowflake.x, snowflake.y, snowflake.size, arcade.color.WHITE)

    def on_update(self, delta_time):

        for snowflake in self.snowflake_list:
            snowflake.y -= snowflake.speed * delta_time

            if snowflake.y < 0:
                snowflake.reset_pos()

            snowflake.x += snowflake.speed * math.cos(snowflake.angle) * delta_time
            snowflake.angle += delta_time


def main():
    window = MyGame()
    window.start_snowfall()
    arcade.run()


if __name__ == "__main__":
    main()
