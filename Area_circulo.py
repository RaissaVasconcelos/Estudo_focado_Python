#Programa Circunferência Melhorias
from math import pi
from math import pow

def circulo(raio):
    area = pi * pow(float(raio),2)
    print(area)

#O modulo é usado para deixar o codigo mais privado, definindo o nome do bloco
if __name__ == '__main__':  
    raio = input("Informe o raio: ")
    circulo(raio)
   