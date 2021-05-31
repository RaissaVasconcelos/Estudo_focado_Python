from random import randint

# Função para sortear valores de 1 a 6
# Se for impar continue
# Se o numero for par e igual ao valor sorteado
# Mostre o print que acertou
# Se não mostre que não acertou


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        print(i)
        continue

    if sortear_dado() == i:
        print("Acertou", i)
        break
else:
    print("Não acertou")
