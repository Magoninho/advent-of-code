greater_until_now = 0

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
			if (the_very_cool_sum > greater_until_now):
				greater_until_now = the_very_cool_sum

			arr = [] # preparando o array para uma nova checagem
			continue
		else:
			arr.append(int(i))

print(greater_until_now) # the answer omg