# GET       → Buscar dados
# POST      → Enviar dados
# PUT/PATCH → Atualizar dados
# DELETE    → Excluir dados

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

resposta = requests.get(url)

print("Status da requisição: ", resposta.status_code)
print("Conteúdo da resposta: ", resposta.text)

# -- converte o conteúdo para python
dados = resposta.json()
print("Título: ", dados["title"])
print("Conteudo: ", dados["body"])


# ----------------

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
resposta = requests.get(url)
cotacao = resposta.json()

dolar = cotacao["USDBRL"]["bid"]
print(f"Cotação do dólar agora: R$ {dolar}")
