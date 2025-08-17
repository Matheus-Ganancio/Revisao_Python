
# Puxa o metodo "somaMultiplicacao" dê "meu_modulo_multiplicacao.py"
from meu_modulo_multiplicacao import somaMultiplicacao

num1 = int(input("Selecione o primeiro valor da multiplicação: "))
num2 = int(input("Selecione o segundo valor da multiplicação: "))

# altera os valores do método de "somaMultiplicacao(a, b)" pelo valor das variaveis
# num1 e num2 
resultado = somaMultiplicacao(num1, num2)

print(f"O resultado do calculo é {resultado}")