#pelo pep8 existe uma convenção em priorizar constantes com letras maiusculas 
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]

for texto in textos: #variavel texto é uma string
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Possui pelo menos uma palavra proibida:', palavra)
            break

    else:
        print('Texto autorizado:', texto)
        
