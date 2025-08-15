# Arrays, o codigo abaixo chama o segundo valor[1] dentro do valor dentro do array frutas
# Pois array se inicia em 0 e não 1, então o valor 1 é o segundo valor

frutas = ["maca", "banana", "laranja"]
print(frutas[1])

# append adiciona um valor ao final da lista
frutas.append("uva")
print(frutas)

#------------------------
# --- tuplas
# São imutaveis e usam parênteses

cores = ("vermelho", "azul", "verde")
print(cores[0])

#---------------------------------
# ---- Dicionários
# armazenam pares de chaves e valor
# usam chaves {}
# no exemplo ao chamar o nome, é chamado "ana" pois é o valor dado ao nome

aluno = {"nome": "ana", "idade": 22}
print(aluno["nome"])
aluno["idade"] = 23
print(aluno)
aluno["nome"] = "Beatriz"
print(aluno)

#-------------------------
# conjuntos
# não ordenados e não repetidos
# {} ou a função set()
# no exemplo retorna 1, 2, 3 pq não pode repetir valores+

numeros = {1,2,3,3,2,1}
print(numeros)