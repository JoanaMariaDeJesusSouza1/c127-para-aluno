from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Defina o método de coleta de dados dos exoplanetas
def scrape():

    for i in range(0,10):
        print(f'Coletando dados da página {i+1} ...' )
        
        # Objeto BeautifulSoup

        # Loop para encontrar o elemento dentro das tags ul e li
       

        # Encontre todos os elementos na página e clique para passar para a próxima página
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# Chamando o método    
scrape()

# Defina o cabeçalho

# Defina o dataframe do pandas

# Converta para CSV
