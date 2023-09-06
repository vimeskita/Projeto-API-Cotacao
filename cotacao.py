import requests

#Moedas válidas: USD,EUR,BTC
def pegar_cotacoes(codigo_moeda):
    try:
        #Fazemos a requisição do código de moeda passado pelo usuário
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        #Pegamos a requisição da moeda e convertemos para um Json que é armazenado em forma de dicionario
        requisicao_dic = requisicao.json()
        #Dentro do Json armazenamos o preço da cotação que vem como parâmetro bit dentro da variável
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None
