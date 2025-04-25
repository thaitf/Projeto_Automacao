#Site para teste: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import time
import pandas as pd
import pyautogui as pg
#click > clica
#press > pressiona
#whrite > escreve
#hotkey > atalho (ctrl + c, ctrl + v, etc)
#moveTo > move o mouse para a posição (x, y)

pg.PAUSE = 0.5 #pausa de 0.5 segundo entre os comandos

#entrar no sistema
pg.press('win')
pg.write('chrome')
pg.press('enter')

pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
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
tabela = pd.read_csv('produtos.csv')
pg.click(x=-1156, y=424) 