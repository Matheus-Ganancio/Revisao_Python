# Sintaxe da função → def nome_da_funcao():

def saudacao():
    print("Hello World")

saudacao()

# --- dá para delegar uma variavel no parametro e definir ao chamar

def seu_nome_e(nome):
    print(f"Your name is {nome}")

seu_nome_e("Matheus")


def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Result: ", resultado)

# ------ Exercicio
# Funcao retorna se o numero é par ou impar
# depois retorna o numero inputado pelo usuario

input_usuario = int(input("chose any number: "))

numero_salvo = input_usuario

def par_impar():
    if input_usuario % 2 == 0 :
        print("Numero Par")

    else:
        print("Numero Impar")

par_impar()
print(f"O numero digitado foi: {input_usuario}")