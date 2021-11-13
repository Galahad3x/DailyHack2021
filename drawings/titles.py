import drawings as d
import random


def empty(book):
	return "WIP"


def scifi_spaceship_spaceship(book):
	if book.thing_happening == "spaceship":
		titles = [
			"Aboard the " + book.setting_name,
			book.setting_name,
			"Space Frontier",
			"The " + book.setting_name + "'s Journey"
		]
	else:
		titles = [
			"Alone",
			book.setting_name,
			"The Story of " + book.mc_name,
			"Lost Between The Stars"
		]
	return random.choice(titles)


def scifi_spaceship_underwater(book):
	if book.thing_happening == "spaceship":
		titles = [
			"Aboard the " + book.setting_name,
			book.setting_name,
			"The Depth of The Ocean",
			"The " + book.setting_name + "'s Journey",
			"Under the Ocean",
			"The Aquatic Life of " + book.mc_name,
		]
	else:
		titles = [
			"Alone",
			book.setting_name,
			"The Story of " + book.mc_name,
			"Lost Under The Waves",
			"Come Up For Air",
			"Underwater"
		]
	return random.choice(titles)


def scifi_planet_forest(book):
	if book.thing_happening == "stranded":
		titles = [
			"Welcome to " + book.setting_name,
			"Between The Trees of " + book.setting_name,
			"Jungle",
			"Drown in Green",
			"Ground Control to " + book.mc_name
		]
	else:
		titles = [
			"Jungle",
			"Welcome to " + book.setting_name,
			"Battle for " + book.setting_name,
		]
	return random.choice(titles)


def scifi_planet_desert(book):
	if book.thing_happening == "stranded":
		titles = [
			"Welcome to " + book.setting_name,
			"Between The Dunes of " + book.setting_name,
			"Dune",
			"Under the Sand",
			"Oasis of Space"
		]
	else:
		titles = [
			"Dune",
			"Welcome to " + book.setting_name,
			"Battle for " + book.setting_name,
			"Blood on the Sand"
		]
	return random.choice(titles)


def scifi_planet_ice(book):
	if book.thing_happening == "stranded":
		titles = [
			"Welcome to " + book.setting_name,
			"Between The Glaciers of " + book.setting_name,
			"Cold",
			"Frostbite",
			"Ground Control to " + book.mc_name
		]
	else:
		titles = [
			"Glaciers",
			"Welcome to " + book.setting_name,
			"Battle for " + book.setting_name,
			book.mc_name + ", The Survivor"
		]
	return random.choice(titles)


def scifi_vr_videogame(book):
	titles = [
		book.setting_name,
		"Enter The " + book.setting_name,
		"Into The " + book.setting_name,
		"Ready Player One",
		"The Online Adventures of " + book.mc_name
	]
	return random.choice(titles)


def scifi_deadly_tournament(book):
	titles = [
		book.setting_name,
		"Winner Takes All: " + book.setting_name,
		"The " + book.setting_name,
		book.mc_name + " In The " + book.setting_name
	]
	return random.choice(titles)


def crime_murder_fiction(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Murder in " + book.setting_name,
			book.setting_name + " Confidential",
			book.mc_name + ", Police Detective",
			"Who Killed " + book.mc_name + "?"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Murder in " + book.setting_name,
			book.mc_name + ", Police Detective",
			"Who Killed " + book.mc_name + "?",
			"A Killer Is Among Us"
		]
	else:
		titles = [
			"Murder in " + book.setting_name,
			"Terror In " + book.setting_name,
			"The Beast of " + book.setting_name,
			"Who Killed " + book.mc_name + "?",
			book.setting_name + " Murder Story"
		]
	return random.choice(titles)


def crime_murder_true_crime(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Murder in " + book.setting_name,
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Who Killed " + book.mc_name + "?",
			book.setting_name + " Murder Story"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Murder in " + book.setting_name,
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Who Killed " + book.mc_name + "?",
			book.setting_name + " Murder Story"
		]
	else:
		titles = [
			"Murder in " + book.setting_name,
			"Terror In " + book.setting_name,
			"The Beast of " + book.setting_name,
			"Who Killed " + book.mc_name + "?",
			book.setting_name + " Murder Story"
		]
	return random.choice(titles)


def crime_murder_cold_case(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			book.setting_name + " In Winter",
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Who Killed " + book.mc_name + "?"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			book.setting_name + " in " + str(random.randint(1979, 1994)),
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Who Killed " + book.mc_name + "?"
		]
	else:
		titles = [
			"Murder in " + book.setting_name,
			"Terror In " + book.setting_name,
			"The Beast of " + book.setting_name,
			"Who Killed " + book.mc_name + "?"
		]
	return random.choice(titles)


def crime_kidnapping_fiction(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Kidnapped in " + book.setting_name,
			book.setting_name + ": " + str(random.randint(30, 90)) + " Days Kidnapped",
			book.mc_name + ", Police Detective",
			"Who Took " + book.mc_name + "?"
		]
	else:
		titles = [
			book.setting_name,
			"Kidnapped in " + book.setting_name,
			book.setting_name + ": " + str(random.randint(30, 90)) + " Days Kidnapped",
			"Who Took " + book.mc_name + "?"
		]
	return random.choice(titles)


def crime_kidnapping_true_crime(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Kidnapped in " + book.setting_name,
			book.setting_name + ": " + str(random.randint(30, 90)) + " Days Kidnapped",
			"The Kidnapping of " + book.mc_name,
			"Who Took " + book.mc_name + "?"
		]
	else:
		titles = [
			book.setting_name,
			"Kidnapped in " + book.setting_name,
			book.setting_name + ": " + str(random.randint(30, 90)) + " Days Kidnapped",
			"Who Took " + book.mc_name + "?",
			"A " + book.setting_name + " Kidnapping"
		]
	return random.choice(titles)

def crime_vanishing_fiction(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Vanishing in " + book.setting_name,
			"The Vanishing Of " + book.mc_name,
			book.mc_name + ", Police Detective",
			"Where Is " + book.mc_name + "?"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Vanishing in " + book.setting_name,
			"The Vanishing Of " + book.mc_name,
			"Where Is " + book.mc_name + "?"
		]
	else:
		titles = [
			"Vanishing in " + book.setting_name,
			"Where Is " + book.mc_name + "?",
			"Searching"
		]
	return random.choice(titles)


def crime_vanishing_true_crime(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"The Real Story Of " + book.mc_name,
			"The Vanishing Of " + book.mc_name,
			"Where Is " + book.mc_name + "?"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Vanishing in " + book.setting_name,
			"The Vanishing Of " + book.mc_name,
			"Where Is " + book.mc_name + "?"
		]
	else:
		titles = [
			"Vanishing in " + book.setting_name,
			"Where Is " + book.mc_name + "?",
			"Searching"
		]
	return random.choice(titles)


def crime_vanishing_cold_case(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			book.setting_name + " In Winter",
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Who Killed " + book.mc_name + "?"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			book.setting_name + " in " + str(random.randint(1979, 1994)),
			"Under " + book.setting_name,
			"The Real Story of " + book.mc_name,
			"Where Is " + book.mc_name + "?"
		]
	else:
		titles = [
			"Vanishing in " + book.setting_name,
			"Disappearance",
			"Have You Seen This Person?",
			"Who Killed " + book.mc_name + "?"
		]
	return random.choice(titles)

