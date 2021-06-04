#Autor Raissa Vasconcelos
#!/Users/local/bin/python3

def fibonacci(quantidade):
    resultado = [0,1]
    for i in range(2,quantidade):
        #somar os dois ultimos numeros da lista
        resultado.append(sum(resultado[-2:])) 
    return resultado

if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)