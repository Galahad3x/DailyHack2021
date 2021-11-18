import sys
import pygame
import random
import time
from math import floor, tan, radians
from drawings import titles as t

SIZE = WIDTH, HEIGHT = 1024, 700
clock = pygame.time.Clock()
pygame.display.init()
pygame.font.init()

SCREEN = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)

Orange1 = (235, 130, 66)
SoftGreen = (198, 213, 126)
SkyBlue = (162, 205, 205)
AlmostWhite = (240, 240, 240)
SuaveRed = (213, 126, 126)
NormalDarkBlue = (49, 107, 131)
VibrantGreen = (52, 190, 130)
SummerOrange = (255, 179, 25)
BookPage = (249, 216, 167)
colors = [Orange1, SoftGreen, SkyBlue, AlmostWhite, SuaveRed, NormalDarkBlue, VibrantGreen, SummerOrange]
male_mc_names = ["Wyatt", "James", "Jason", "Zero", "Captain", "Shaun"]
female_mc_names = ["Sam", "Jessie", "Stephanie", "Claudia", "Anna", "Elizabeth"]
mc_surnames = ["Mailer", "Bond", "Bourne", "Zhao", "Moustafa", "Mallory", "Solverson", "Gerhardt"]
writer_names = ["Ernest", "Charles", "Ian", "Olivia", "Ada", "Thomas", "Chloe", "William", "Bob", "Isaac", "C.W."]
writer_surnames = ["Cline", "Porta", "Fleming", "Shelby", "B.", "Anderson", "DeNiro", "Russell", "Asimov", "Longbottom"]
genres = ["scifi", "crime", "adventure"]
main_themes = {
	"scifi": ["spaceship", "planet", "vr-videogame", "deadly-tournament"],
	"crime": ["murder", "kidnapping", "vanishing", "organized-crime-recent", "organized-crime-old"],
	"adventure": ["hidden-treasure", "heist", "journey", "magic"]
}
settings = {
	"scifi": {
		"spaceship": ["spaceship", "underwater"],
		"planet": ["forest", "desert", "ice"],
		"vr-videogame": ["dystopian-earth"],
		"deadly-tournament": ["tournament"]
	},
	"crime": {
		"murder": ["big-city", "small-town", "region"],
		"kidnapping": ["big-city", "small-town"],
		"vanishing": ["big-city", "small-town", "region"],
		"organized-crime-recent": ["big-city", "region"],
		"organized-crime-old": ["big-city", "region"]
	},
	"adventure": {
		"hidden-treasure": ["pirate-island", "mansion", "museum"],
		"heist": ["bank", "museum"],
		"journey": ["walking", "road-trip"],
		"magic": ["school", "reign"]
	}
}
things_happening = {
	"scifi": {
		"spaceship": ["stranded", "journey"],
		"planet": ["stranded", "war"],
		"vr-videogame": ["vr-videogame"],
		"deadly-tournament": ["deadly-tournament"]
	},
	"crime": {
		"murder": ["fiction", "cold-case", "true-crime"],
		"kidnapping": ["fiction", "true-crime"],
		"vanishing": ["fiction", "cold-case", "true-crime"],
		"organized-crime-recent": ["fiction", "true-crime"],
		"organized-crime-old": ["fiction", "true-crime"]
	},
	"adventure": {
		"hidden-treasure": ["hidden-treasure"],
		"heist": ["heist"],
		"journey": ["vacation", "escape"],
		"magic": ["magic"]
	}
}
setting_names = {
	"scifi": {
		"spaceship": ["Alabarda", "USS Fighter", "Turbo Traveler",
		              "Apollo " + str(random.choice(["L", "LI", "LII", "LIII", "LIV", "LV"]))],
		"underwater": ["Alabarda", "Zissou", "Turbo Traveler",
		               "Ultramarine " + str(random.choice(["L", "LI", "LII", "LIII", "LIV", "LV"]))],
		"forest": ["Wyh", "Ero", "UC35523a", "Tropicalia"],
		"desert": ["Arrakis", "Mars", "Desolated Desert"],
		"ice": ["Byra", "Pluto", "Glaxiaris"],
		"dystopian-earth": ["OASIS", "Metaverse", "Decentraland", "Double Life"],
		"tournament": ["Deadly Games", "Battle Royale", "Octopus Game"]
	},
	"crime": {
		"small-town": ["Tor", "Fargo", "Luverne", "Narvik", "Matera", "Ennui-sur-Blasé"],
		"big-city": ["New York", "London", "Paris", "Barcelona", "Rio de Janeiro"],
		"region": ["The Ozarks", "California", "The Midwest", "Catalunya", "Spain", "Bodmin"]
	},
	"adventure": {
		"pirate-island": ["Terre-de-Bas", "Isle of Dogs", "Paros", "Isla Mona"],
		"mansion": ["The Portland Beacon", "The Lighthouse", "Conelly's Nook"],
		"museum": ["The JFK Museum", "British History Museum", "Tokyo National Art Center", "The Blofeld Art Gallery"],
		"bank": ["The Continental", "Bank Of USA", "The Golden Grin", "The First World Bank"],
		"walking": ["The 100 Acre Wood", "La Fageda d'en Jordà", "Yosemite", "The Thousand Pines",
		            "The Wildwood Forest"],
		"road-trip": ["Route 66", "Europe", "Yellowstone"],
		"school": ["Hogwarts", "The Magnificent Magic Academy", "The School of Magic"],
		"reign": ["Narnia", "The Fantasy Realm", "Zeitzland", "Izadilonia"]
	}
}
cover_styles = ["background-and-text"]
# , "minimalistic", "title-and-image"

title_functions = {
	"scifi": {
		"spaceship": {
			"spaceship": t.scifi_spaceship_spaceship,
			"underwater": t.scifi_spaceship_underwater,
		},
		"planet": {
			"forest": t.scifi_planet_forest,
			"ice": t.scifi_planet_ice,
			"desert": t.scifi_planet_desert
		},
		"vr-videogame": {
			"dystopian-earth": t.scifi_vr_videogame
		},
		"deadly-tournament": {
			"tournament": t.scifi_deadly_tournament
		}
	},
	"crime": {
		"murder": {
			"fiction": t.crime_murder_fiction,
			"true-crime": t.crime_murder_true_crime,
			"cold-case": t.crime_murder_cold_case
		},
		"kidnapping": {
			"fiction": t.crime_kidnapping_fiction,
			"true-crime": t.crime_kidnapping_true_crime
		},
		"vanishing": {
			"fiction": t.crime_vanishing_fiction,
			"true-crime": t.crime_vanishing_true_crime,
			"cold-case": t.crime_vanishing_cold_case
		},
		"organized-crime-recent": {
			"fiction": t.crime_organized_recent_fiction,
			"true-crime": t.crime_organized_recent_true_crime
		},
		"organized-crime-old": {
			"fiction": t.crime_organized_old_fiction,
			"true-crime": t.crime_organized_old_true_crime
		}
	},
	"adventure": {
		"hidden-treasure": {
			"pirate-island": t.adventure_treasure_island,
			"mansion": t.adventure_treasure_mansion,
			"museum": t.adventure_treasure_museum
		},
		"heist": {
			"bank": t.adventure_heist_bank,
			"museum": t.adventure_heist_museum
		},
		"journey": {
			"walking": t.adventure_journey_walking,
			"road-trip": t.adventure_journey_roadtrip
		},
		"magic": {
			"school": t.adventure_magic_school,
			"reign": t.adventure_magic_reign
		}
	}
}

seed = time.time()
random.seed(int(seed))
print(int(seed))


class Book:
	def __init__(self, writer_name, mc_name, genre,
	             main_theme, setting, thing_happening, setting_name, cover_style, mc_firstname, mc_lastname):
		self.can_height = random.randint(160, 300) * 2
		self.can_width = random.randint(160, 220) * 2
		self.can_topleft = (WIDTH // 2 - self.can_width // 2, HEIGHT // 2 - self.can_height // 2)
		self.sun_height = random.randint(1, 3)
		self.sun_angle = random.randint(30, 150)
		self.book_n_of_pages = random.randint(120, 400)
		self.mc_lastname = mc_lastname
		self.mc_firstname = mc_firstname
		self.writer_name = writer_name
		self.mc_name = mc_name
		self.genre = genre
		self.main_theme = main_theme
		self.setting = setting
		self.thing_happening = thing_happening
		self.setting_name = setting_name
		self.cover_style = cover_style
		self.title = self.generate_title()

	def draw_book(self):
		if self.sun_angle == 90:
			self.sun_angle = 91
		pygame.draw.rect(SCREEN, (0, 0, 0),
		                 pygame.Rect((self.can_topleft[0] - 2, self.can_topleft[1] - 2),
		                             (self.can_width + 4, self.can_height + 4)),
		                 border_radius=3)
		draw_can((self.can_width, self.can_height), (0, 0, 0),
		         self.can_topleft)
		draw_book_shadow(self.sun_angle, self.sun_height, self.book_n_of_pages, self.can_topleft,
		                 (self.can_width, self.can_height), pages=True)
		draw_book_shadow(self.sun_angle, self.sun_height, self.book_n_of_pages, self.can_topleft,
		                 (self.can_width, self.can_height))

	def generate_title(self):
		if self.genre == "crime":
			return title_functions[self.genre][self.main_theme][self.thing_happening](self)
		return title_functions[self.genre][self.main_theme][self.setting](self)

	def to_string(self):
		stri = {
			"writer": self.writer_name,
			"mc_name": self.mc_name,
			"genre": self.genre,
			"theme": self.main_theme,
			"setting": self.setting,
			"thing": self.thing_happening,
			"setting_name": self.setting_name,
			"cover": self.cover_style
		}
		return str(stri)

	def draw_background(self):
		if self.genre == "scifi":
			book_s = pygame.Surface((self.can_width, self.can_height))
			book_s.set_colorkey((0, 0, 0))
			for i in range(random.randint(10, 15)):
				book.draw_image(book_s, min_size=(self.can_width // 15, self.can_height // 15),
				                max_size=(self.can_width // 10, self.can_height // 10), type="star")
			SCREEN.blit(source=book_s, dest=self.can_topleft)

	def draw_cover(self):
		if self.cover_style == "background-and-text":
			self.draw_background()
			self.write_full_text()

	def draw_image(self, s, min_size, max_size, type):
		image_width = random.randint(min_size[0], max_size[0])
		image_height = random.randint(min_size[1], max_size[1])
		image_x = random.randint(0, self.can_width)
		image_y = random.randint(0, self.can_height)
		pygame.draw.rect(s, random.choice(colors), pygame.Rect((image_x, image_y), (image_width, image_height)))

	def write_full_text(self):
		# Calculate how big every word must be
		total_length = len(self.title.split(" ")) + 2
		letter_height = self.can_height // total_length
		fonts = ["/drawings/fonts/Game Of Squids.ttf", "/drawings/fonts/OriginTech personal use.ttf",
		         "/drawings/fonts/Robot Invaders.ttf", "/drawings/fonts/Robot Invaders Italic.ttf"]
		font_name = sys.path[1] + random.choice(fonts)
		myfont = pygame.font.Font(font_name, letter_height // 2)
		for word in self.title.split(" ") + self.writer_name.split(" "):
			print("Size thing")
			test_s = myfont.render(word, False, (0, 0, 0))
			while test_s.get_width() > self.can_width:
				letter_height = int(floor(letter_height) * 0.8)
				myfont = pygame.font.Font(font_name, letter_height)
				test_s = myfont.render(word, False, (0, 0, 0))
		color = random.choice(colors)
		myfont_small = pygame.font.Font(font_name, letter_height // 2)
		# Draw the words
		y = 0
		for word in self.title.split(" "):
			text_s = myfont.render(word, False, color)
			SCREEN.blit(source=text_s, dest=(
				self.can_topleft[0] + self.can_width // 2 - text_s.get_width() // 2, self.can_topleft[1] + y))
			y += letter_height
		y -= letter_height // 2
		y += 5
		text_s = myfont_small.render("by", False, color)
		SCREEN.blit(source=text_s,
		            dest=(self.can_topleft[0] + self.can_width // 2 - text_s.get_width() // 2, self.can_topleft[1] + y))
		y += letter_height // 2
		for name in self.writer_name.split(" "):
			text_s = myfont.render(name, False, color)
			SCREEN.blit(source=text_s, dest=(
				self.can_topleft[0] + self.can_width // 2 - text_s.get_width() // 2, self.can_topleft[1] + y))
			y += letter_height


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


def draw_book_shadow(s_angle, s_height, n_of_pages, book_topleft, book_size, pages=False):
	if pages:
		x = n_of_pages // 28
		alpha = 255
		color = BookPage
		s_angle = 45
	else:
		x = (n_of_pages // 10) * (s_height / 2)
		alpha = 180
		color = (0, 0, 0)
	if s_angle > 90:
		y = floor(tan(radians(180 - s_angle)) * x)
		topleft_shadow = point_shadow_over_90(book_topleft, x, y)
		book_bottomleft = (book_topleft[0], book_topleft[1] + book_size[1])
		bottomleft_shadow = point_shadow_over_90(book_bottomleft, x, y)
		book_bottomright = (book_topleft[0] + book_size[0], book_topleft[1] + book_size[1])
		bottomright_shadow = point_shadow_over_90(book_bottomright, x, y)
		x2 = n_of_pages // 28
		book_extrapoint = point_shadow_under_90(book_bottomright, x2,
		                                        floor(tan(radians(45)) * x2))
		polygon_points = [book_topleft, topleft_shadow, bottomleft_shadow, bottomright_shadow, book_extrapoint,
		                  book_bottomright, book_bottomleft]
	else:
		y = floor(tan(radians(s_angle)) * x)
		book_topright = (book_topleft[0] + book_size[0], book_topleft[1])
		topright_shadow = point_shadow_under_90(book_topright, x, y)
		book_bottomleft = (book_topleft[0], book_topleft[1] + book_size[1])
		bottomleft_shadow = point_shadow_under_90(book_bottomleft, x, y)
		book_bottomright = (book_topleft[0] + book_size[0], book_topleft[1] + book_size[1])
		bottomright_shadow = point_shadow_under_90(book_bottomright, x, y)
		book_extrapoint = None
		if s_angle > 45:
			x2 = n_of_pages // 28
			book_extrapoint = point_shadow_under_90(book_topright, x2,
			                                        floor(tan(radians(45)) * x2))
		polygon_points = [book_topright, topright_shadow, bottomright_shadow, bottomleft_shadow, book_bottomleft,
		                  book_bottomright]
		if book_extrapoint is not None:
			polygon_lasts = polygon_points[1:]
			new_polygon = [polygon_points[0], book_extrapoint]
			new_polygon.extend(polygon_lasts)
			polygon_points = new_polygon
	s = pygame.Surface(SIZE)
	s.set_alpha(alpha)
	s.fill((0, 0, 255))
	s.set_colorkey((0, 0, 255))
	pygame.draw.polygon(s, color, polygon_points)
	if pages:
		pygame.draw.polygon(s, (0, 0, 0), polygon_points, width=3)
		pygame.draw.line(s, (0, 0, 0), book_bottomright, bottomright_shadow, width=3)
	SCREEN.blit(source=s, dest=(0, 0))


if __name__ in "__main__":
	total_size = random.randint(100, 280)
	inner_size = random.randint(max(20, total_size - 120), total_size - 40)
	bg_color = random.choice([AlmostWhite, SkyBlue])
	line_color = random.choice([Orange1, SuaveRed, SoftGreen])
	line_w = random.randint(1, 3) * 2
	draw_tablecloth_1(total_size, inner_size, bg_color, line_color, line_w)
	# Create book data
	b_genre = random.choice(genres)
	b_theme = random.choice(main_themes[b_genre])
	b_writer = random.choice(writer_names) + " " + random.choice(writer_surnames)
	b_mc_name = random.choice(female_mc_names + male_mc_names)
	b_mc_surname = random.choice(mc_surnames)
	b_mc = b_mc_name + " " + b_mc_surname
	b_setting_type = random.choice(settings[b_genre][b_theme])
	b_thing_happening = random.choice(things_happening[b_genre][b_theme])
	b_setting_name = random.choice(setting_names[b_genre][b_setting_type])
	book = Book(b_writer, b_mc, b_genre, b_theme, b_setting_type, b_thing_happening, b_setting_name,
	            random.choice(cover_styles), b_mc_name, b_mc_surname)
	print(book.to_string())
	print("TITLE: " + book.title)
	book.draw_book()
	# Draw book cover
	book.draw_cover()
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type != pygame.QUIT and event.type != pygame.KEYDOWN:
				continue
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()
