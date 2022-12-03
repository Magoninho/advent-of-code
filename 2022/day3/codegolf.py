# 1. listar todas as sacolas
# 2. dividir as string ao meio
# 3. comparar as duas pra achar itens duplicados
# 4. achar a prioridade desses itens duplicados
# 5. somar as prioridades

with open("inputs.txt", "r") as f:
    b = f.read().splitlines()
    final_sum = 0
    for r in range(len(b)): final_sum += " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(list(set(list(b[r][0 : (len(b[r]) // 2)])).intersection(list(b[r][(len(b[r]) // 2) : (len(b[r]))])))[0])
    print(final_sum)

