elves_rank = []

def sum_items(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

with open('inputs.txt', 'r') as f:
	b = f.read().splitlines()

	arr = []
	for i in b:
		if (i == ''):
			the_very_cool_sum = sum_items(arr)
			elves_rank.append(the_very_cool_sum)

			arr = [] # preparando o array para uma nova checagem
			continue
		else:
			arr.append(int(i))


elves_rank.sort(reverse=True)
print(elves_rank[0] + elves_rank[1] + elves_rank[2]) # the answer omg

