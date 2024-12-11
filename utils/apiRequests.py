import requests

urlbase = "https://api.binance.com/api/v3/ticker/price?symbol="

# busca o valor da moeda api binance 


def obterPreco(moeda):

    try:
        url= f"{urlbase}{moeda}"
        response = requests.get(url)
        return float(response.json()["price"])
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao buscar preço de {moeda}: {e}")
