# marciofjr
# coding: utf-8
# win10

#Sites Downloads:
#https://statusinvest.com.br/acoes/busca-avancada --- 01
#https://statusinvest.com.br/fundos-imobiliarios/busca-avancada --- 02

#Salva:
#01 = C:\@mfj\#Investimentos\StatusInvest\_bsAcoes
#02 = C:\@mfj\#Investimentos\StatusInvest\_bsFIIs

#Modelo:
#01 = 2021.07.01_-_acoes.csv
#02 = 2021.07.01_-_fiis.csv

import sys, os, re, glob, psutil, signal
import requests
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import _find_elements as FEs
from selenium.common.exceptions import *
import requests
from zipfile import ZipFile

# In[3]:
#Pasta Raiz:::
pasta_raiz = os.path.dirname(os.path.realpath(__file__)) #'C:\@mfj\#Investimentos\StatusInvest'

os.chdir(pasta_raiz)
print(pasta_raiz)
#print(os.path.dirname(os.path.realpath(__file__)))
# FIM Pasta Raiz:::



# !!! Atualiza ChromeDriver !!!

# Elimina o chromedriver, caso esteja utilizando, pois nao vamos conseguir atualizar
for pid in (process.pid for process in psutil.process_iter() if process.name()=="chromedriver.exe"):
    try:
        print(f'pid:{pid}')
        os.kill(pid)
    except:
        pass

for process in (process for process in psutil.process_iter() if process.name()=="chromedriver.exe"):
    process.kill()

def atualiza_chromedriver():
    try:
        # remove o chromedriver antes
        os.remove('chromedriver.exe')
        version_atual = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').text
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'
        url_file = 'https://chromedriver.storage.googleapis.com/'
        file_name = 'chromedriver_win32.zip'
        file = requests.get(url_file + version_atual + '/' + file_name)
        with open(file_name, "wb") as code:
            code.write(file.content)
        z = ZipFile(file_name, 'r')
        z.extractall()
        z.close()
        #remove o zip depois
        os.remove(file_name)
    except PermissionError:
        pass

def teste_navegador():
    try:
        browser = webdriver.Chrome()
        browser.get('http://localhost:8000')
    except PermissionError:
        pass
    except:
        print("WebDriver Atualizado !!! (erro)")
        atualiza_chromedriver()
#Verifica se o WebDriver Precisa Atualizar:
a = teste_navegador()
# !!! Atualiza ChromeDriver !!!


#Data Busca
dt_agora = datetime.now() #Hoje
dt_busca = dt_agora.strftime("%Y.%m.%d")

#print(dt_busca)

#Espera Elemento da Página - Unico
def wait_element_load(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        ret_load = 1
        return ret_load
    except TimeoutException:
        ret_load = 0
        return ret_load
    
def remove_arquivo(pst_arq):
    try:
        os.remove(pst_arq)
    except FileNotFoundError:
        pass

# In[4]:
#xdriver = webdriver.Chrome('chromedriver.exe')
#xdriver_exe = f"{pasta_raiz}\\chromedriver.exe"
#xdriver_exe = "C:\@mfj\#Investimentos\StatusInvest\chromedriver.exe"
#xdriver = webdriver.Chrome(executable_path=driver_exe, chrome_options=chromeOptions)

#01 - Abre Navegador
def abre_navegador(url_acesso):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : f"{Pasta_Download}"} #muda a pasta de Donwload
    #chromeOptions.add_argument("--headless")
    chromeOptions.add_experimental_option("prefs",prefs)
    driver_exe = f"{pasta_raiz}\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_exe, chrome_options=chromeOptions)
    driver.maximize_window()
    driver.get(url_acesso)
    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass
    return driver

# In[5]:


#Etapa 01 - bsAcoes
url_acesso = 'https://statusinvest.com.br/acoes/busca-avancada'
Pasta_Download = 'C:\@mfj\#Investimentos\StatusInvest\_bsAcoes'
btt_busca = '//*[@id="main-2"]/div[3]/div/div/div/button[2]'
btt_download = '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a'
driver = abre_navegador(url_acesso)
remove_arquivo(f"{Pasta_Download}/statusinvest-busca-avancada.csv")
remove_arquivo(f"{Pasta_Download}/{dt_busca}_-_acoes.csv")
sleep(1)

#Busca - Clique Botão para Gerar
if wait_element_load(driver, btt_busca) == 1:
    buscaBtn = driver.find_element(By.XPATH, btt_busca)
    driver.execute_script('arguments[0].click();', buscaBtn)
    sleep(1)

#Download Arquivo:
if wait_element_load(driver, btt_download) == 1:
    dwloadBtn = driver.find_element(By.XPATH, btt_download)
    driver.execute_script('arguments[0].click();', dwloadBtn)
    sleep(10) #espera 10 segundos para Download
    #Salva o Arquivo e Renomeia
    old_file = os.path.join(f"{Pasta_Download}", "statusinvest-busca-avancada.csv")
    new_file = os.path.join(f"{Pasta_Download}", f"{dt_busca}_-_acoes.csv")
    os.rename(old_file, new_file)

driver.quit()
#driver.close()
sleep( 10 )


# In[6]:


#Etapa 02 - bsFIIs
url_acesso = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'
Pasta_Download = 'C:\@mfj\#Investimentos\StatusInvest\_bsFIIs'
btt_busca = '//*[@id="main-2"]/div[3]/div/div/div/button[2]'
btt_download = '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a'
driver = abre_navegador(url_acesso)
remove_arquivo(f"{Pasta_Download}/statusinvest-busca-avancada.csv")
remove_arquivo(f"{Pasta_Download}/{dt_busca}_-_fiis.csv")
sleep(1)

#Busca - Clique Botão para Gerar
if wait_element_load(driver, btt_busca) == 1:
    buscaBtn = driver.find_element(By.XPATH, btt_busca)
    driver.execute_script('arguments[0].click();', buscaBtn)
    sleep(1)

#Download Arquivo:
if wait_element_load(driver, btt_download) == 1:
    dwloadBtn = driver.find_element(By.XPATH, btt_download)
    driver.execute_script('arguments[0].click();', dwloadBtn)
    sleep(10) #espera 10 segundos para Download
    #Salva o Arquivo e Renomeia
    old_file = os.path.join(f"{Pasta_Download}", "statusinvest-busca-avancada.csv")
    new_file = os.path.join(f"{Pasta_Download}", f"{dt_busca}_-_fiis.csv")
    os.rename(old_file, new_file)

driver.quit()
#driver.close()
sleep( 10 )


