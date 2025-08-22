from sklearn import tree

# - Aqui o "x" vai ser como se fossem perguntas e o "y" a checagem com as respostas

# Dados: [nota_prova, nota_prova2]

x = [[9, 10], [1,2], [5,6], [7,8], [2,1], [3, 2]]

# Classes: 1 = aprovado / 0 = reprovado
y = [1, 0, 1, 1, 0, 1]

clf = tree.DecisionTreeClassifier()

# fit é o método para ensinar o modelo com base nos dados
clf = clf.fit(x, y)

# deve prever 1 ou 0
print(clf.predict([[4, 5]]))

# ------------------------

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plot_tree(clf, filled=True)
plt.show()