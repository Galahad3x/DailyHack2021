import Levenshtein as l
import sys

if __name__ in "__main__":
	original_filename = sys.argv[1]
	dictionary_filename = "dictionary.txt"
	try:
		open(dictionary_filename)
	except FileNotFoundError:
		dictionary_filename = "textcorrector/dictionary.txt"
	result_filename = sys.argv[2]
	with open(dictionary_filename, "r") as f:
		dictionary_words = []
		for line in [l.rstrip("\n").rstrip(" ") for l in f.readlines()]:
			dictionary_words.extend(line.split(" "))
	with open(result_filename, "w") as f2:
		with open(original_filename, "r") as f:
			for line in [l.rstrip("\n").rstrip(" ") for l in f.readlines()]:
				for word in line.split(" "):
					if word == "":
						continue
					puntuation = ""
					if not word[-1].isalpha():
						puntuation = word[-1]
						word = word[:-1]
					min_distance = len(word)
					min_word = word
					for word2 in dictionary_words:
						dist = l.distance(word, word2)
						if dist < min_distance:
							min_distance = dist
							min_word = word2
					if min_word != word:
						print("Changed " + word + " for " + min_word)
					f2.write(min_word + puntuation + " ")
				f2.write("\n")
