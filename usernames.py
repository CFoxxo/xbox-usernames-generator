import random

def randomUsername():
	lines = open('adjectives.txt').read().splitlines()
	adj = random.choice(lines)
	lines = open('nouns.txt').read().splitlines()
	noun = random.choice(lines).capitalize()
	return adj + noun + str(random.randint(10,99))
