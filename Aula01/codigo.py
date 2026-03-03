# 'pip install pyautogui' no console para ter o pyautogui no computador (só precisa fazer uma vez por computador)
import pyautogui
import time

#pyautogui.click    -> clica
#pyautogui.write    -> escreve texto
#pyautogui.press    -> aperta uma tecla
#pyautogui.hotkey   -> aperta um atalho

pyautogui.PAUSE = 0.5

#Variáveis

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 0 (casos de captcha)
# esperar 30s para coisas que alguem tem que fazer (preencher captcha, ler um QRcode...)
#time.sleep(30)

# Passo 1: Entrar no sistema da Empresa

#Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Colocar link
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3) #Esperar site carregar

# Passo 2: Fazer Login
pyautogui.click(x=577, y=384) #clicar no campo de email (ver 'auxiliar.py')
pyautogui.write("johnnyandradeamado@gmail.com")

pyautogui.press("tab") #trocar para campo de senha
pyautogui.write("senha muito bacana daora")

pyautogui.press("tab") #ir para o botão de login
pyautogui.press("enter") #logar

time.sleep(3)

# Passo 3: Abrir a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv") #variável tabela criado

# Passo 4: Cadastrar um produto e repetir o código para cada linha

#repete o código. Não é preciso definir linha, Python já faz isso por automático!
for linha in tabela.index: 
    
    pyautogui.click(x=507, y=270)
    
    #str() é transformar o valor em texto, tecnicamente só precisa para os de número, mas por segurança colocamos em tudo.

    codigo = str(tabela.loc[linha, "codigo"]) #localizar informação é entre colchetes
    pyautogui.write(codigo) #código
    pyautogui.press("tab") #passar para o proximo campo

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca) #marca
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo) #tipo
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) #categoria
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco) #preço
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) #custo
    pyautogui.press("tab")

    observacao = str(tabela.loc[linha, "obs"])
    if observacao != "nan": #se não estiver vazio, escreve
        pyautogui.write(observacao) #observação
    pyautogui.press("tab")

    pyautogui.press("enter") #enviou

    pyautogui.scroll(9999) #scrolla a tela para o início
