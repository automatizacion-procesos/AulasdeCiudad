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

# Transformamos los datos de teléfono a String para poder escribirlos
datos_reto['Phone Number'] = datos_reto['Phone Number'].astype(str)

# Buscamos el botón de inicio del reto para iniciar el cronómetro
boton_inicio = navegador.find_element(By.XPATH, XPATH_BOTON_START)
boton_inicio.click()


# Iniciamos variable para recorrer el dataframe del reto
fila = 0




#-------------------------------PROCESO----------------------------------------#


# FORMULARIO 1 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1




# FORMULARIO 2 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 3 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 4 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 5 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 6 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 7 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 8 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 9 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()

# Avanzamos a siguiente fila
fila += 1



# FORMULARIO 10 ---------------------------------------------------------
datos_fila = datos_reto.loc[fila]  # Obtenemos los datos de la fila del excel
# Dato 1
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[0])
campo_texto.send_keys(datos_fila[0])
# Dato 2
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[1])
campo_texto.send_keys(datos_fila[1])
# Dato 3
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[2])
campo_texto.send_keys(datos_fila[2])
# Dato 4
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[3])
campo_texto.send_keys(datos_fila[3])
# Dato 5
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[4])
campo_texto.send_keys(datos_fila[4])
# Dato 6
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[5])
campo_texto.send_keys(datos_fila[5])
# Dato 7
campo_texto = navegador.find_element(By.XPATH, CAMPOS_TEXTO[6])
campo_texto.send_keys(datos_fila[6])


# Damos click en el botón submit para continuar con el otro formulario
boton_submit = navegador.find_element(By.XPATH, XPATH_BOTON_SUBMIT)
boton_submit.click()




#---------------------------------FIN-----------------------------------------#


# Tomamos el mensaje del resultado y lo imprimimos en consola
mensaje = navegador.find_element(By.XPATH, XPATH_MENSAJE_RESULTADO)
print(mensaje.text)

# Tiempo para visualizar el resultado
time.sleep (5)

# Eliminamos el archivo del challenge
os.remove(RUTA_DESCARGAS)
