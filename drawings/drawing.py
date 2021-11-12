import sys
import pygame
import random
import time
from math import floor, tan, radians

SIZE = WIDTH, HEIGHT = 1024, 700
clock = pygame.time.Clock()
pygame.display.init()

SCREEN = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)

Orange1 = (235, 130, 66)
SoftGreen = (198, 213, 126)
SkyBlue = (162, 205, 205)
AlmostWhite = (240, 240, 240)
SuaveRed = (213, 126, 126)
NormalDarkBlue = (49, 107, 131)
VibrantGreen = (52, 190, 130)
SummerOrange = (255, 179, 25)
colors = [Orange1, SoftGreen, SkyBlue, AlmostWhite, SuaveRed]

seed = time.time()
random.seed(int(seed))
print(int(seed))


def draw_tablecloth_1(pattern_total_size, pattern_inner_size, bg_color, line_color, line_width):
	SCREEN.fill(bg_color)
	x = random.randint(0, floor(pattern_inner_size * 0.8))
	lines_difference = (pattern_total_size - pattern_inner_size) // 2
	while x <= WIDTH:
		pygame.draw.line(SCREEN, line_color, (x, 0), (x, HEIGHT), line_width)
		x += lines_difference
		pygame.draw.line(SCREEN, line_color, (x, 0), (x, HEIGHT), line_width)
		x += pattern_inner_size
	y = random.randint(0, floor(pattern_inner_size * 0.8))
	while y <= HEIGHT:
		pygame.draw.line(SCREEN, line_color, (0, y), (WIDTH, y), line_width)
		y += lines_difference
		pygame.draw.line(SCREEN, line_color, (0, y), (WIDTH, y), line_width)
		y += pattern_inner_size
	pygame.display.flip()


def brushStrike(x, y, len2, color, starting_size=30, direction=True):
	global SCREEN
	if direction:
		hev = vev = 5
	else:
		hev = -5
		vev = 5
	a = 255
	size = starting_size
	for ii in range(len2):
		rect_size = (size * 2, size * 2)
		s = pygame.Surface(rect_size)
		s = pygame.Surface.convert_alpha(s)
		# s.set_colorkey((0, 0, 0, 255))
		s.set_alpha(a - ii * 4)
		pygame.draw.circle(s, color, (size, size), size)
		pygame.Surface.blit(SCREEN, s, (x, y))
		x += hev
		y += vev
		size -= (starting_size // len2)


def brushBomb():
	for i in range(10):
		clock.tick(100)
		brushLen = random.randint(20, 35)
		startSize = random.randint(0, 50)
		color_ind = random.randint(0, 2)
		x = random.randint(0, 1024)
		y = random.randint(0, 700)
		brushStrike(x, y, brushLen, colors[color_ind], startSize, True)
		brushStrike(x + 100, y, brushLen, colors[color_ind], startSize, False)
		pygame.display.flip()


def draw_can(can_size, can_color, can_topleft):
	can_rect = pygame.Rect((0, 0), can_size)
	s = pygame.Surface(can_size)
	shadow1_surface = s.copy()
	s.set_colorkey((0, 0, 0))
	pygame.draw.rect(s, can_color, can_rect, border_radius=3)
	SCREEN.blit(source=s, dest=can_topleft)
	starter_alpha = min(255, can_size[0] // 3) - 10
	for i in range(can_size[0] // 3):
		shadow1_surface.fill((255, 255, 255))
		shadow1_surface.set_colorkey((255, 255, 255))
		shadow1_surface.set_alpha(starter_alpha - i - 1)
		pygame.draw.line(shadow1_surface, (0, 0, 0), (can_rect.topleft[0] + i, can_rect.topright[1]),
		                 (can_rect.topleft[0] + i, can_rect.topright[1] + can_rect.height))
		SCREEN.blit(source=shadow1_surface, dest=can_topleft)
	return can_rect


def point_shadow_over_90(point, x, y):
	return tuple([point[0] - x, point[1] + y])


def point_shadow_under_90(point, x, y):
	return tuple([point[0] + x, point[1] + y])


def draw_book_shadow(s_angle, s_height, n_of_pages, book_topleft, book_size):
	x = (n_of_pages // 8) * s_height
	if s_angle > 90:
		y = floor(tan(radians(180 - s_angle)) * x)
		topleft_shadow = point_shadow_over_90(book_topleft, x, y)
		book_bottomleft = (book_topleft[0], book_topleft[1] + book_size[1])
		bottomleft_shadow = point_shadow_over_90(book_bottomleft, x, y)
		book_bottomright = (book_topleft[0] + book_size[0], book_topleft[1] + book_size[1])
		bottomright_shadow = point_shadow_over_90(book_bottomright, x, y)
		polygon_points = [book_topleft, topleft_shadow, bottomleft_shadow, bottomright_shadow, book_bottomright,
		                  book_bottomleft]
	else:
		y = floor(tan(radians(s_angle)) * x)
		book_topright = (book_topleft[0] + book_size[0], book_topleft[1])
		topright_shadow = point_shadow_under_90(book_topright, x, y)
		book_bottomleft = (book_topleft[0], book_topleft[1] + book_size[1])
		bottomleft_shadow = point_shadow_under_90(book_bottomleft, x, y)
		book_bottomright = (book_topleft[0] + book_size[0], book_topleft[1] + book_size[1])
		bottomright_shadow = point_shadow_under_90(book_bottomright, x, y)
		polygon_points = [book_topright, topright_shadow, bottomright_shadow, bottomleft_shadow, book_bottomleft,
		                  book_bottomright]
	s = pygame.Surface(SIZE)
	s.set_alpha(180)
	s.fill((0, 0, 255))
	s.set_colorkey((0, 0, 255))
	pygame.draw.polygon(s, (0, 0, 0), polygon_points)
	SCREEN.blit(source=s, dest=(0, 0))


if __name__ in "__main__":
	book_n_of_pages = random.randint(120, 600)
	sun_angle = random.randint(30, 150)
	if sun_angle == 90:
		sun_angle = 91
	sun_height = random.randint(1, 3)
	total_size = random.randint(100, 280)
	inner_size = random.randint(max(20, total_size - 120), total_size - 40)
	bg_color = random.choice([AlmostWhite, SkyBlue])
	line_color = random.choice([Orange1, SuaveRed, SoftGreen])
	line_w = random.randint(1, 3) * 2
	draw_tablecloth_1(total_size, inner_size, bg_color, line_color, line_w)
	can_width = random.randint(160, 220) * 2
	can_height = random.randint(160, 300) * 2
	can_topleft = (WIDTH // 2 - can_width // 2, HEIGHT // 2 - can_height // 2)
	pygame.draw.rect(SCREEN, (0, 0, 0),
	                 pygame.Rect((can_topleft[0] - 2, can_topleft[1] - 2), (can_width + 4, can_height + 4)),
	                 border_radius=3)
	can_rect = draw_can((can_width, can_height), random.choice([NormalDarkBlue, SummerOrange, VibrantGreen]),
	                    can_topleft)
	draw_book_shadow(sun_angle, sun_height, book_n_of_pages, can_topleft, (can_width, can_height))
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type != pygame.QUIT and event.type != pygame.KEYDOWN:
				continue
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()
