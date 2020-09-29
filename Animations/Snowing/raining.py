import random
import numpy as np
import math
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1920
SCREEN_TITLE = "rain Animation"
VIEWPORT_MARGIN = 40



class Raindrop:
	def __init__(self):
		self.x = random.randrange(SCREEN_WIDTH + random.randrange(-10, 10))
		self.y = random.randrange(SCREEN_HEIGHT + 200)
		self.speed = np.random.poisson(40)
		
	def fall(self):
		self.y = self.y - self.speed

	def reset_pos(self):
		self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
		self.x = random.randrange(SCREEN_HEIGHT)


class MyGame(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)
		self.shapes = arcade.ShapeElementList()
		background_bottom_color = (0, 0, 0)
		background_top_color = (0, 0, 0)
		points = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
		colors = (background_bottom_color, background_bottom_color, background_top_color, background_top_color)
		rectangle = arcade.create_rectangle_filled_with_colors(points, colors)
		self.shapes.append(rectangle)
		self.raindrop_list = None

	def start_rainfall(self):
		self.raindrop_list = []
		for _ in range(1000):
			raindrop = Raindrop()
			self.raindrop_list.append(raindrop)
		self.set_mouse_visible(False)

	def on_draw(self):
		arcade.start_render()
		self.shapes.draw()
		for raindrop in self.raindrop_list:
			arcade.draw_line(raindrop.x, raindrop.y, raindrop.x, raindrop.y + 10, arcade.color.BLUE)


	def on_update(self, delta_time):
		for raindrop in self.raindrop_list:
			raindrop.fall()
			if raindrop.y < 0:
				raindrop.reset_pos()


def main():
    window = MyGame()
    window.start_rainfall()
    arcade.run()


if __name__ == "__main__":
    main()
