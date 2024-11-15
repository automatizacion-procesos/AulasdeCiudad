from selenium import webdriver
import time

# Inicializa el driver
driver = webdriver.Chrome()

# Abre Google
driver.get("https://www.google.com")

# Maximiza el navegador para que ocupe toda la pantalla
driver.maximize_window()

# Espera unos segundos para mostrar el funcionamiento
time.sleep(10)

# Imprime el título de la página
print("Título de la página:", driver.title)

# Cierra el navegador
driver.quit()
