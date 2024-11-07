# External libraries
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd


resultados = []
df = pd.read_excel('paises.xlsx')

# Ingresamos a Google
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')





# -------------------------------------------------------------------


# Aplicar su lógica para la extracción de las capitales de los países.


# -------------------------------------------------------------------





# Creamos el archivo de resultados
pd.DataFrame(resultados).to_excel('resultados_capitales.xlsx', index=False)
