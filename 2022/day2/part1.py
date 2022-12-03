# --- Day 2: Rock Paper Scissors --- #
"""
coluna 1
A: pedra
B: papel
C: tesoura

coluna 2:
X: pedra
Y: papel
Z: tesoura

Rock[A] defeats Scissors[Z], Scissors[C] defeats Paper[Y], and Paper[B] defeats Rock[X].
"""

shape_scores = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

defeat_table = [
	['A', 'Z'],
	['C', 'Y'],
	['B', 'X']
]

victory_table = [
	['A', 'Y'],
	['B', 'Z'],
	['C', 'X']
]

draw_table = [
	['A', 'X'],
	['B', 'Y'],
	['C', 'Z']
]

def round_score(round):
	if round in victory_table:
		return 6
	elif round in draw_table:
		return 3
	elif round in defeat_table:
		return 0

def calculate_final_round_score(round):
	player = round[1]

	# this is the score earned from the shapes you select
	shape_score = shape_scores[player]

	# victory, defeat or draw
	score = round_score(round)

	# return the sum of them
	return shape_score + score

with open('inputs.txt', 'r') as f:
	rounds_list = f.read().splitlines()

	final_score = 0
	for r in rounds_list:
		current_round = r.split(' ')
		final_score += calculate_final_round_score(current_round)

	print(final_score)
