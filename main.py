import PySimpleGUI as sg
from cotacao import pegar_cotacoes

# É Possivel selecionar um tema para a tela
sg.theme('PythonPlus')
#Criamos o layout, onde cada colchete representa uma linha horizontal na interface
layout = [
    [sg.Text("Pegar Cotação da Moeda")],
    [sg.Text("Opções:")],
    [sg.Text("EUR = Euro"), sg.Text("USD = Dólar Americano"), sg.Text("BTC = Bitcoin")],
    [sg.InputText(key="nome_cotaçao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotaçao")]
]

#Passamos o nome e como será o layout criado da janela através de parâmetros
janela = sg.Window("Cotação das Moedas", layout)

#Criamos um laço infinito para a cada momento ler e armazenar os eventos e valores da janela aberta pelo sg
while True:
    #Sempre precisa ser o evento depois o valor
    evento, valores = janela.read()

    #Criamos um if para identificar se for clicado no evento de fechar a janela ou Cancelar, ele parar o programa
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

    if evento == "Pegar Cotação":
        #Criamos uma variável para armazenar o que o usuário digitou no input
        codigo_cotacao = valores["nome_cotaçao"]
        #Tratando a resposta
        codigo_cotacao = codigo_cotacao.upper().strip()


        #Buscando a cotação da moeda digitada pelo usuário utilizando a função criada e armazenando
        cotacao = pegar_cotacoes(codigo_cotacao)


        #Caso o usuário digite uma cotação inválida
        if cotacao == None:
            janela["texto_cotaçao"].update("Digite uma opção válida!")

        else:
            #Transformando em Float para poder formatar
            cotacao = float(cotacao)

            if codigo_cotacao == "EUR":
                nome_moeda = "Euro"
            elif codigo_cotacao == "USD":
                nome_moeda = "Dólar Americano"
            else:
                nome_moeda == "Bitcoin"

            #Para editar um campo que já existe para mostrar a mensagem da cotação atual, fazemos:
            janela["texto_cotaçao"].update(f'A cotação do {nome_moeda} é de R${cotacao:.2f}')


janela.close()