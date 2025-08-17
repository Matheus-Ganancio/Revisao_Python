# Formula IMC = peso kg / altura m(²)

# abaixo de 18.5 → abaixo do peso
# entre 18.5 e 24.9 → peso normal
# entre 25 e 29.9 → sobrepeso
# 30 ou mais → Obesidade


# Entrada de dados

peso = float(input("Enter your weight (kg): "))
altura = float(input("Enter your height(cm): "))

# Calculo do IMC (Índice de Massa Corporal) / BMI (Body Mass Index)

bmi = peso/(altura ** 2 )

# Exibição do resultado
# ": .2f" está fazendo a saída do bmi no print ter 2 casas decimais
print(f"Your BMI is: {bmi: .2f}")

# Classificação
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("ou are at a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")