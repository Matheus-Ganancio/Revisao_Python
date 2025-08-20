import matplotlib.pyplot as plt


# Dados simples

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]



# Criando o gráfico

plt.plot(x, y)
plt.title("Gráfico de Exemplo")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()



# -- GRAFICO COM VELAS

nomes = ["Ana", "Carlos", "Julia"]
notas = [8.5, 7.0, 9.2]



plt.bar(nomes, notas)
plt.title("Notas dos Alunos")
plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.show()

categorias = ["Python", "JavaScript", "Java", "C++"]
preferencias = [40, 30, 20, 10]

plt.pie(preferencias, labels=categorias, autopct="%1.1f%%")
plt.title("Preferência por linguagens")
plt.show()

plt.savefig("GráficoPizza.png")