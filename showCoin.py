import time
from utils.apiRequests import obterPreco 




# printa preço das moedas

def mostrarPrecos(moedas):

    for moeda in moedas:
        try:
            preco = float(obterPreco(moeda))
            print(f"O preço atual de {moeda}: {preco:,.2f} USDT")
        except Exception as e:
            print(e)

def carregarMoedas(arquivo):
    with open(arquivo, "r") as f:
        return[linha.strip() for linha in f.readlines() if linha.strip()]


def ConsultaPeriodica(moedas, intervalo):

    while True:
        print("\nAtualizando preços...")
        mostrarPrecos(moedas)
        time.sleep(intervalo)



moedas = carregarMoedas("data\moedas.txt")
ConsultaPeriodica(moedas, intervalo=5)
