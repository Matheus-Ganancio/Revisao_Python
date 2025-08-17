# CPF tem 11 digitos
# formatação: 123.456.789-00
# só possui numeros
# não possui sequência repetida: 999.999.999-99

# --- limpeza de dados ---
# pega a variavel inputada, no caso o cpf e usa .replace para remover os
# caracteres especiais
cpf = input("digite seu CPF (Com ou sem pontuação): ")
cpf = cpf.replace(".", "").replace(".", "")


# --- verificação básica, seguindo 3 regras
# 1 regra, verifica se tem apenas números
if not cpf.isdigit():
    print("CPF deve conter apenas números.")

# 2 regra, usa a função "len" para verificar se o tamanho(length) é diferente de 11
elif len(cpf) != 11:
    print("CPF deve conter exatamente 11 dígitos.")

# 3 regra, usa o valor do index [0] do input do cpf pelo usuário e confere "=="
# nos 11 digitos "*11", para caso o usuario use o mesmo digito em todo o cpf, ele não aceite
elif cpf == cpf[0] * 11:
    print("CPF inválido: sequência repetida.")
else:
    print("CPF válido!")