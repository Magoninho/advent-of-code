# --- Part Two --- #
# "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

"""
EMPATE:
pedra(A)   	-> pedra(A) 	-> 1pt
papel(B)   	-> papel(B) 	-> 2pt
tesoura(C) 	-> tesoura(C) 	-> 3pt

GANHAR:
pedra(A) 	-> papel(B) 	-> 2pt
papel(B) 	-> tesoura(C) 	-> 3pt
tesoura(C) 	-> pedra(A) 	-> 1pt

DERROTA:
pedra(A)	-> tesoura(C)	-> 3pt
papel(B)	-> pedra(A)		-> 1pt
tesoura(C)	-> papel(B)		-> 2pt
"""

def calculate_final_round_score(round):
	elf, result = round

	score = 0
	shape_score = 0

	# draw
	if result == 'Y':
		score += 3
		shape_score += ' ABC'.index(elf)
	# win
	elif result == 'Z':
		score += 6
		shape_score += ' CAB'.index(elf)
	else:
		shape_score += ' BCA'.index(elf)

	# return the sum of them
	return shape_score + score

with open('inputs.txt', 'r') as f:
	rounds_list = f.read().splitlines()

	final_score = 0
	for r in rounds_list:
		current_round = r.split(' ')
		final_score += calculate_final_round_score(current_round)

	print(final_score)
