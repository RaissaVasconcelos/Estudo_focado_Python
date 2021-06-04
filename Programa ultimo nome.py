nome = input("Insira se nome completo: ") #O nome inserido tem limite de até cinco nomes
dividido = nome.split()
print("O primeiro nome é:", dividido[0])
print("O seu ultimo nome é: ", dividido[len(dividido) - 1]) # A função Len mostra o numero de posições da string, exemplo João Pedro Rocha Dutra tem 4 posições 
                                                            # Seu ultimo nome está na posião 3, usavamos a equação (n de posições - 1) 