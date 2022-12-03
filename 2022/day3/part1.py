# 1. listar todas as sacolas
# 2. dividir as string ao meio
# 3. comparar as duas pra achar itens duplicados
# 4. achar a prioridade desses itens duplicados
# 5. somar as prioridades

characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_duplicate_items(first, second):
	return list(set(list(first)).intersection(list(second)))

with open('inputs.txt', 'r') as f:
	b = f.read().splitlines()
	final_sum = 0
	for r in range(len(b)):
		current_rushpack = b[r]
		first_compartment = current_rushpack[0:(len(current_rushpack)//2)]
		second_compartment = current_rushpack[(len(current_rushpack)//2):(len(current_rushpack))]

		common_item = find_duplicate_items(first_compartment, second_compartment)[0]

		priority = characters.index(common_item)

		final_sum += priority

	print(final_sum)	

