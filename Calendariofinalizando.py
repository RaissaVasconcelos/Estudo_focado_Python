
data = input("Insira uma data: ") # A data inserida segue o modelo 12/09/1999

d = (data[0:2])
m = (data[3:5])
a = (data[6:])
d1 = int(d)
m1 = int(m)
a1 = int(a)

if (a1 % 4 == 0) and (a1 % 100 != 0) or (a1 % 400 == 0): #ano bissexto ocorre em duas condi��es divisivel por 4 e n�o por 100 ou divisivel por 4 e 400
             if (m1 == 2):
             elif (d < 30): # Valor m�ximo que o dia pode ter no ano bissexto � 29 
                               print("Data v�lida")
             else:
                          print("Data inv�lida")
             if (m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11):
                          if (d1 < 31):
                                       print("Data v�lida")
                          else:
                                       print("Data inv�lida")
             else:
                          if (d1 < 32):
                                       print("Data v�lida")
                          else:
                                       print("Data inv�lida")
             print(" Ano bissexto � bissexto ")
else:
             if (m1 == 2):
             elif (d1 < 29): # Valor m�ximo que o dia pode ter no ano n�o bissexto � 28 
                          print("Data v�lida")
             else:
                          print("Data inv�lida")
             if (m1 == 04 or m1 == 6 or m1 == 9 or m1 == 11):
                          if (d1 < 31):
                                       print("Data v�lida")
                          else:
                                       print("Data inv�lida")
             else:
                          if (d1 < 32):
                                       print("Data v�lida")
                          else:
                                       print("Data inv�lida")
             print("Ano n�o � bissexto")


