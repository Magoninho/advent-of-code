inputs = []

with open('inputs.txt', 'r') as f:
    b = f.read().splitlines()
    for i in b:
        inputs.append(int(i))


def get_the_answer():
    for i in inputs:
        for j in inputs:
            if i + j == 2020:
                print(f"{i} + {j} == {i + j}")
                print(f"e a multiplicação é: {i * j}")


get_the_answer()

# TODO: pode ser com ele mesmo?
