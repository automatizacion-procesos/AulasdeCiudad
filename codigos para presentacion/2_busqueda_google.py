from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración: define lo que quieres buscar
termino_busqueda = "Quipux"

# Inicializa el driver
driver = webdriver.Chrome()  
# Cambia a webdriver.Firefox() si usas Firefox

driver.maximize_window()

# Abre Google
driver.get("https://www.google.com")
time.sleep(20)

# Encuentra la barra de búsqueda e ingresa el término
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(termino_busqueda)

# Realiza la búsqueda
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Espera para cargar los resultados
primer_resultado = driver.find_element(By.CSS_SELECTOR, "h3")
primer_resultado.click()
time.sleep(10)

# Espera unos segundos para cargar los resultados y muestra el título de la página de resultados
time.sleep(10)
print("Título de la página de resultados:", driver.title)

# Cierra el navegador
driver.quit()
