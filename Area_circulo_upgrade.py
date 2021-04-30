# Programa Circunferência Melhorias
from math import pi
from math import pow
import sys
import errno


class TerminalColor():
    # codigo pra cor vermelha
    ERRO = '\033[91m'
    # codigo pra voltar a cor normal
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print(30*"--")
    print(TerminalColor.ERRO + "E necessário informar o raio do circulo" +
          TerminalColor.NORMAL)
    print("Sintaxe: {} <raio>" .format(sys.argv[0]))
    print(30*"--")


# O modulo é usado para deixar o codigo mais privado, definindo o nome do bloco
if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)  # Erro informa que a operaçao nao foi permitida
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 'O raio deve ser um valor numerico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)  # Erro informa que o argumento é invalido
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Area: {area}')
