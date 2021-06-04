# Autor: Raissa Vasconcelos Mendes
#!/Users/local/bin/python3
# fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=",")
    for i in range(0,10):
        proximo = penultimo + ultimo
        print(f'{proximo}', end=",")
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
