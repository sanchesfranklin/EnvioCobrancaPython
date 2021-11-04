'''
 Este script tem como objetivo enviar mensagens automatizadas via Whatsapp
 realizando a cobrança no dia de vencimento para os clientes Gdoor
 Autor: Sanches Santos
'''
import os
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import urllib

## Importar a planilha do google drive com os dados dos clientes

caminhoPlanilhaDrive = "https://docs.google.com/spreadsheets/d/1y1UEGCbaJ5ImZm3w0cGiKJliKmSNp2is/export?format=xlsx"

infoClientesPlanilha = pd.read_excel(caminhoPlanilhaDrive)


data_atual = date.today()
diaAtual = data_atual.day

## Salvando a sessão do Whatsapp (Pra não precisar ficar scaneando QRCode)
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

## Acessando WhatsappWeb
navegador = webdriver.Chrome("./chromedriver", chrome_options=options)
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

## Percorrendo a planilha para recuperar dados p/envios de mensagens
for i, numero in enumerate(infoClientesPlanilha['numero']):
    nomePessoa = infoClientesPlanilha.loc[i, "nome_whats"]
    diaEnvio = infoClientesPlanilha.loc[i, "dia_envio_boleto"]
    situacao = infoClientesPlanilha.loc[i, "situacao"]
    mensagem = f"Olá {nomePessoa}, esta é uma mensagem automática apenas para testar uma funcionalidade. Obrigado pela atenção :)"
    mensagem = urllib.parse.quote(mensagem)
    ## Se estiver no dia do vencimento e a situação estiver ativo, envia a mensagem de cobrança
    if diaAtual == diaEnvio and situacao == "ativo":
        link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(20)

