#Autor Raissa Vasconcelos
#!/Users/local/bin/python3

def fibonacci(limite):
    resultado = [0,1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:])) #somar os dois ultimos numeros da lista
    return resultado

if __name__ == "__main__":
    for fib in fibonacci(2000):
        print(fib)