from selenium import webdriver
import time

# Inicializa el driver
driver = webdriver.Chrome()

# Cambia a webdriver.Firefox() si se quiere usar Firefox

# Abre Google
driver.get("https://www.google.com")

# Maximiza el navegador web en toda la pantalla
driver.maximize_window()

# Espera unos segundos para cargar google
time.sleep(10)

# Imprime el título de la página
print("Título de la página:", driver.title)

# Cierra el navegador
driver.quit()
