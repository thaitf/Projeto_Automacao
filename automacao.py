#Site para teste: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import time
import pandas as pd
import pyautogui as pg
#click > clica
#press > pressiona
#whrite > escreve
#hotkey > atalho (ctrl + c, ctrl + v, etc)
#moveTo > move o mouse para a posição (x, y)

pg.PAUSE = 0.3 #pausa de 0.3 segundo entre os comandos

#entrar no sistema
pg.press('win')
pg.write('chrome')
pg.press('enter')

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pg.write(site)
pg.press('enter')
time.sleep(3) #espera 3 segundos para carregar a página

#login
pg.click(x=-1152, y=564) #clica no campo de login na tela do meu pc
pg.write('pythonimpressionador@gmailcom')
pg.press('tab') 
pg.write('123456')
pg.press('tab')
pg.press('enter') 
time.sleep(3) 

#importar dados
tabela = pd.read_csv('produtos.csv') #se o arquivo estiver na mesma pasta do script, não precisa do caminho completo
   
#cadastrar produtos
for l in tabela.index: 
    pg.click(x=-1156, y=424)
    codigo = tabela.loc[l, "codigo"] 
    pg.write(str(codigo)) 
    pg.press('tab')
    marca = tabela.loc[l, "marca"] 
    pg.write(str(marca))
    pg.press('tab')
    tipo = tabela.loc[l, "tipo"] 
    pg.write(str(tipo)) 
    pg.press('tab')
    categoria = tabela.loc[l, "categoria"] 
    pg.write(str(categoria))
    pg.press('tab')
    preco_unitario = tabela.loc[l, "preco_unitario"] 
    pg.write(str(preco_unitario))
    pg.press('tab')
    custo = tabela.loc[l, "custo"] 
    pg.write(str(custo))
    pg.press('tab')
    obs = tabela.loc[l, "obs"] 
    # quando o valor for vazio p pandas chama de nan
    if pd.isna(obs):
        pg.write('')
    else:
        pg.write(str(obs))
    pg.press('tab')
    pg.press('enter')
    pg.scroll(10000)
    # scroll positivo = sobe 10000 pixels
    # scroll negativo = desce 10000 pixels
