import pandas as pd

# Criando um arquivo CSV simples manualmente

with open("alunos.csv", "w") as arquivo:
    arquivo.write("nome,idade,nota\n")
    arquivo.write("Juliana,22,8.5\n")
    arquivo.write("Carlos,24,7.0\n")
    arquivo.write("Mariana,21,9.2\n")

# Lendo o CSV com pandas

df = pd.read_csv("alunos.csv")
print(df)

# -- index=False serve para não salvar o número da linha como coluna
df.to_csv("novos_dados.csv", index=False)

