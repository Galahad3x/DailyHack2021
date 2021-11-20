import random

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
			"Tears of " + book.setting_name
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
			"Blood on the Sand",
			"Tears of " + book.setting_name
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
			book.mc_name + ", The Survivor",
			"Tears of " + book.setting_name
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
			"The Story of True Crime in " + book.setting_name
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
			book.setting_name + " Murder Story",
			"The Story of True Crime in " + book.setting_name
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
			"Who Killed " + book.mc_name + "?",
			"The Story of True Crime in " + book.setting_name
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


def crime_organized_recent_fiction(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			book.setting_name + " In Winter",
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + "s",
			"The " + book.mc_lastname + " Concern"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Under " + book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + " Limited",
			"The " + book.mc_lastname + " Concern"
		]
	else:
		titles = [
			"Lords of Crime",
			book.mc_name + ": The Master of " + book.setting_name,
			"The Alternate Economy",
			"Street Wars"
		]
	return random.choice(titles)


def crime_organized_recent_true_crime(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + "s",
			"The " + book.mc_lastname + " Concern",
			"Blood On The Streets"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Under " + book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + " Limited",
			"The " + book.mc_lastname + " Concern"
		]
	else:
		titles = [
			"The Lords of The Underworld",
			book.mc_name + ": The Master of " + book.setting_name,
			"The Alternate Economy",
			"The Alternate Economy of " + book.setting_name
		]
	return random.choice(titles)


def crime_organized_old_fiction(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			book.setting_name + " In Fall",
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + "s",
			"The " + book.mc_lastname + " Concern"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Under " + book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + " Limited",
			"The " + book.mc_lastname + " Concern",
			"Palindrome"
		]
	else:
		titles = [
			"Lords of Crime " + str(random.randint(1920, 1975)),
			book.mc_name + ": The Master of " + book.setting_name,
			"The Alternate Economy: " + str(random.randint(1920, 1975)),
			"The Invisible War of " + book.setting_name
		]
	return random.choice(titles)


def crime_organized_old_true_crime(book):
	if book.setting == "big-city":
		titles = [
			book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + "s",
			"The " + book.mc_lastname + " Concern",
			"Blood On The Streets"
		]
	elif book.setting == "small-town":
		titles = [
			book.setting_name,
			"Under " + book.setting_name,
			"Gangs of " + book.setting_name,
			"The " + book.mc_lastname + " Limited",
			"The " + book.mc_lastname + " Concern"
		]
	else:
		titles = [
			"The Lords of The Underworld",
			book.mc_name + ": The Master of " + book.setting_name,
			"The Alternate Economy",
			"The Alternate Economy of " + book.setting_name
		]
	return random.choice(titles)


def adventure_treasure_island(book):
	titles = [
		book.mc_name + ": Treasure Hunter",
		"The Treasure of " + book.setting_name,
		"Chest of Gold",
		"Pirates of " + book.setting_name,
		book.mc_name + " and The Hidden Treasure"
	]
	return random.choice(titles)


def adventure_treasure_mansion(book):
	titles = [
		book.mc_name + ": Treasure Hunter",
		"The Treasure of " + book.setting_name,
		"The Secret Room",
		"The Mystery of " + book.setting_name,
		book.mc_name + " in " + book.setting_name,
		"From Dusk til " + book.setting_name
	]
	return random.choice(titles)


def adventure_treasure_museum(book):
	titles = [
		book.mc_name + ": Treasure Hunter",
		"The Treasure of " + book.setting_name,
		"The Secret Room ",
		"The Mystery of " + book.setting_name,
		book.mc_name + " visits " + book.setting_name,
		"Under " + book.setting_name
	]
	return random.choice(titles)


def adventure_heist_bank(book):
	titles = [
		"Hands Up",
		"Payday",
		"The Bandits of " + book.setting_name,
		"The " + book.setting_name + " Job",
	]
	return random.choice(titles)


def adventure_heist_museum(book):
	titles = [
		"The Diamond",
		"The " + book.setting_name + " Job",
		"Finders Keepers",
		"Who broke into " + book.setting_name + "?"
	]
	return random.choice(titles)


def adventure_journey_walking(book):
	if book.thing_happening == "vacation":
		titles = [
			"Where are we?",
			"The " + book.mc_lastname + "s in " + book.setting_name,
			book.setting_name + " Local Guide",
			"The magic of " + book.setting_name
		]
	else:
		titles = [
			"No escape",
			"Lost in " + book.setting_name,
			"Who Rules The Land of Denial?",
			"The Law of Inevitability",
			"Escape from " + book.setting_name,
			"The Muddy Road"
		]
	return random.choice(titles)


def adventure_journey_roadtrip(book):
	if book.thing_happening == "vacation":
		titles = [
			"We're the " + book.mc_lastname + "s",
			"Our Last Summer In " + book.setting_name,
			"The Corners of " + book.setting_name,
			book.mc_name + " into the wild",
		]
	else:
		titles = [
			"War in " + book.setting_name,
			"Through " + book.setting_name,
			"Time is Up"
		]
	return random.choice(titles)


def adventure_magic_school(book):
	titles = [
		"Welcome to " + book.setting_name,
		book.mc_name + " and The Hidden Spell",
		book.mc_name + " and The Invisible Shroud",
		"Brilliant"
	]
	return random.choice(titles)


def adventure_magic_reign(book):
	titles = [
		"Welcome to " + book.setting_name,
		book.setting_name,
		"The Kingdom of " + book.setting_name,
		book.mc_name + " visits " + book.setting_name
	]
	return random.choice(titles)