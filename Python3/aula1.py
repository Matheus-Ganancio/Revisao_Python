# tipos de dados

# int
door_passcode = 142

# string
name1 = "Matheus"

# float
height = 1.77

# bool
door_locked = True


print (door_passcode)
print (name1)
print (height)
print (door_locked)

# 2 ----------------------------------------------------------------------------------------

# f-string, use para formatação quando for imprimir frases, assim não é necessário declarar tudo para string, tipo str(DoorPasscode)
print (f"A porta tem a senha de {door_passcode} use para abrir a porta que tem o tamanho de {height} o suficiente para {name1} Entrar")

name2 = input("What is your name? ")
print (f"welcome {name2}!")


# aqui está especificando o int antes do input pq temos que antecipar o tipo do valor a ser recebido
age = int(input(f"Okey {name2}, now tell me your age: "))
print (f"so, {name2}, your age are {age}")

# 3 ----------------------------------------------------------------------

number = int(input(f"now {name2} chose a number: "))
twice = number * 2
print(f"now when we multiply your number({number}) by 2, we obtain {twice}")