nome = input("Insira se nome completo: ") #O nome inserido tem limite de at� cinco nomes
dividido = nome.split()
print("O primeiro nome �:", dividido[0])
print("O seu ultimo nome �: ", dividido[len(dividido) - 1]) # A fun��o Len mostra o numero de posi��es da string, exemplo Jo�o Pedro Rocha Dutra tem 4 posi��es 
                                                            # Seu ultimo nome est� na posi�o 3, usavamos a equa��o (n de posi��es - 1) 