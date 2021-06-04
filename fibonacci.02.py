# Autor: Raissa Vasconcelos Mendes
#!/Users/local/bin/python3
# fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=",")
    while (ultimo < limite):
        penultimo, ultimo = ultimo, penultimo + ultimo #usando packing pra trocar a variavel
        print(f'{ultimo}', end=",")


if __name__ == '__main__':
    fibonacci(2000)
