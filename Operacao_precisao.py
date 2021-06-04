# 1.1 + 2.2  Exemplos para operações com precisao
from decimal import Decimal, getcontext
getcontext().prec = 2
Decimal(1.1) + Decimal(2.2)

