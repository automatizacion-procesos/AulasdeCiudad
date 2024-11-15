from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración: Define el término de búsqueda
termino_busqueda = "Quipux"
segundos_sleep = 3
# Inicializa el driver
driver = webdriver.Chrome()

# Configura la ventana y abre Google
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(segundos_sleep)

# Encuentra la barra de búsqueda mediante XPath e ingresa el término
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box.send_keys(termino_busqueda)
search_box.send_keys(Keys.ENTER)
time.sleep(segundos_sleep)

# Selecciona y hace clic en el primer resultado usando XPath
primer_resultado = driver.find_element(By.XPATH, "//h3[1]")
primer_resultado.click()
time.sleep(segundos_sleep)

# Espera y muestra el título de la página de resultados
print("El primer resultado se llama:", driver.title)

# Cierra el navegador
driver.quit()
