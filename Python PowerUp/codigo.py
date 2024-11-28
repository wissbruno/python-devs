# Step 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

import pyautogui
import time

# pyautogui.write - > escrever texto
# pyautogui.click - > clicar mouse
# pyautogui.press - > apertar tecla
# pyautogui.hotkey - > apertar um atalho de teclado (ex: ctrl + c)

pyautogui.PAUSE = 0.5

# abrir navegador
# apertar a tecla win (Windows)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Step 2: Fazer login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pausa de 3 seg
time.sleep(2)

# email
pyautogui.click(x=676, y=408)
pyautogui.write("brunowissteste@gmail.com")

# senha
pyautogui.press("tab")
pyautogui.write("123456")

# botao login
pyautogui.click(x=959, y=566)
time.sleep(2)

# Step 3: Importar a base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Step 4: Cadastrar 1 produto

# para cada linha da minha tabela
for linha in tabela.index:
    # selecionar o primeiro campo
    pyautogui.click(x=723, y=286)
    # texto = string = str()

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(10000)

# Step 5: Repetir o processo de cadastro até acabar os produtos

