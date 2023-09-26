# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da Empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> Atalho ou combinação de teclas (Alt+tab, por exemplo)

# Tempo que o pyautogui demora para executar cada comando
pyautogui.PAUSE = 0.5

#Abrindo o Chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

#Entrar no Link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")

# Esperar o site carregar
time.sleep(3)

# Passo 2: Fazer Login
# Damos um click de acordo com o x e y de onde está o campo que queremos escrever DE ACORDO COM SEU MONITOR
#x e y, clicks = 1,2 ou 3, etc
pyautogui.click(x=936, y=384)
pyautogui.write("vinicius.teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("@Senha")
pyautogui.press("tab")
pyautogui.press("Enter")



# Passo 3: Importar a Base de Dados de Produtos
import pandas
tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=822, y=279)

    #Precisa ser igual está escrito na tabela
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]

    # Preencher os campos
    # Como vamos escrever um número, os números precisam ser convertidos para str
    # Duas Maneiras de fazer tanto colocando dentro de uma variável, quanto colocando direto na linha
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    # Validando o campo OBS (caso seja vazio
    if not pandas.isna((obs)):
        pyautogui.write(str(obs))

    #Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("Enter")
    # Scroll levando para topo da página
    # Números positivos para scroll para cima e scroll para baixo negativos
    pyautogui.scroll(50000)


# Passo 5: Repetir o cadastro para todos os produtos
# FEITO

