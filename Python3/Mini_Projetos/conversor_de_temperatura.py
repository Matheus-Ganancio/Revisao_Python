# ---Funções
# Fº = (c x 9/5) +32
# Cº = (F -32) x 5/9

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) +32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Conversor de temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha a opção 1 ou 2: ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = celsius_para_fahrenheit(c)
    print(f"{c} C equivalem a {f:.2f}")

elif opcao == "2":
    f = float(input("Digite a temperatura em Farenheit: "))
    c = fahrenheit_para_celsius(f)
    print(f"{f}ºF equivalem a {c:.2f}ºC")

else:
    print("Opção Inválida")