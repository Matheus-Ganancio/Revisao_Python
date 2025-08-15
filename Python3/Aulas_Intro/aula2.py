"""
+   - adição
-   - subtração
*   - multiplicação
//  - divisão inteira
%   - resto da divisão
**  - potenciação
"""

idade = 28
anos_futuros = idade + 5

print(f"in 5 years you will be {anos_futuros} old")

"""operadores relacionais

==  - valor igual, se 5 for == 5 o resultado passa como true
!=  - valor diferente, se 5 for != 5 o resultado passa como false
>   - maior que
<   - menor que
>=  - maior ou igual
<=  - menor ou igual

"""

""" Operadores logicos

and - determina que para retornar true, 2 das coisas precisam ser verdadeiras
or  - determina que para retornar true, 1 das coisas precisam ser verdadeiras
not - quando valor não é verdadeiro ele retorna true pra acao
"""

idade = 20
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)

name = input("Hi there, what is your name? ")
print (f"I hope you're doing well {name}, nice to meet you")

idade = int(input(f"{name} how old you are? "))

if idade >= 18:
    print (f"Okey {name} you can drive")


else :
    print (f"Sorry {name}, you can't drive right now, you are too young")