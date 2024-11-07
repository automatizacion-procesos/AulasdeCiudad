import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


#----------------------------CONFIGURACIONES----------------------------------#

# Ruta donde se guardan los archivos descargados
RUTA_DESCARGAS = 'D:/Users/felipe.gonzalez/Downloads/challenge.xlsx' # Cambiar ruta a la de su equipo

# Xpaths de los campos del formulario que debemos llenar
CAMPOS_TEXTO = (
    '//input[@ng-reflect-name="labelFirstName"]',       # First Name
    '//input[@ng-reflect-name="labelLastName"]',        # Last Name
    '//input[@ng-reflect-name="labelCompanyName"]',     # Company Name
    '//input[@ng-reflect-name="labelRole"]',            # Role in Company
    '//input[@ng-reflect-name="labelAddress"]',         # Addres
    '//input[@ng-reflect-name="labelEmail"]',           # Email
    '//input[@ng-reflect-name="labelPhone"]'            # Phone Number
)

# Xpath botón para continuar con el siguiente formulario
XPATH_BOTON_SUBMIT = '//input[@value="Submit"]'

# Xpath del botón de descarga del archivo
XPATH_BOTON_DESCARGA = '//a[@href="./assets/downloadFiles/challenge.xlsx"]'

# Xpath del botón que inicia el reto
XPATH_BOTON_START = '//button[contains(., Start)]'

# Xpath del mensaje final del reto
XPATH_MENSAJE_RESULTADO = '//div[@class="message2"]'

# Dirección del sitio web del reto
URL_RETO = 'https://rpachallenge.com/'


# Definición de objeto que inicia y detiene el ChromeDriver
s = Service()

# Inicializar las opciones
opciones_chrome = Options()
#Para evitar que se genere en consola el error por el bluetooth bloqueado:
opciones_chrome.add_experimental_option('excludeSwitches', ['enable-logging']) 







#-------------------------------INICIO----------------------------------------#

# Inicializamos del chromedriver
navegador = webdriver.Chrome(service = s, options = opciones_chrome)

# Maximizamos la ventana del navegador
navegador.maximize_window()

# Navegamos al sitio web del reto
navegador.get(URL_RETO)

# Buscamos el botón para descargar el archivo y le damos click
boton_descarga = navegador.find_element(By.XPATH, XPATH_BOTON_DESCARGA)
boton_descarga.click()

# Esperamos que la descarga se complete
print('Esperando descarga...')
time.sleep(5)

# Leemos el archivo del reto
datos_reto = pd.read_excel(RUTA_DESCARGAS)

# Buscamos el botón de inicio del reto para iniciar el cronómetro
boton_inicio = navegador.find_element(By.XPATH, XPATH_BOTON_START)
boton_inicio.click()

# Buscamos el botón submit desde el principio, ya que no es necesario buscarlo
# varias veces
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)



#-------------------------------PROCESO----------------------------------------#

cantidad_columnas = len(datos_reto.columns)   # Resultado: 7
lista_columnas = range(cantidad_columnas)     # Resultado: [0,1,2,3,4,5,6]

cantidad_filas = len(datos_reto)              # Resultado: 10
lista_filas = range(cantidad_filas)           # Resultado: [0,1,2,3,4,5,6,7,8,9]



# FORMULARIOS

for fila in lista_filas:

    datos_fila = datos_reto.loc[fila]  #Obtenemos los datos de la fila del excel

    for i in lista_columnas:
        campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[i])
        campo_texto.send_keys(str(datos_fila[i]))

    # Damos click en el botón submit para continuar con el otro formulario
    boton_submit.click()




#---------------------------------FIN-----------------------------------------#


# Tomamos el mensaje del resultado y lo imprimimos en consola
mensaje = navegador.find_element(By.XPATH, XPATH_MENSAJE_RESULTADO)
print(mensaje.text)


# Tiempo para visualizar el resultado
time.sleep (5)

# Eliminamos el archivo del challenge
os.remove(RUTA_DESCARGAS)
