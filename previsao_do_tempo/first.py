import requests

API_KEY = "5bd2bc8f2b959b225bf8fc8e76d835d8"
cidade = input("Digite o nome da cidade: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    print(f"Clima em {cidade}: {descricao}, {temperatura}°C")
else:
    print("Cidade não encontrada ou erro na API.")
