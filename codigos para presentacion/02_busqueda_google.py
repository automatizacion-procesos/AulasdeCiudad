from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración: Define el término de búsqueda
termino_busqueda = "Quipux"

# Inicializa el driver
driver = webdriver.Chrome()  
# Usa webdriver.Firefox() si prefieres Firefox

try:
    # Configura la ventana y abre Google
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(2)  # Breve espera para asegurar que la página cargue correctamente

    # Encuentra la barra de búsqueda mediante XPath e ingresa el término
    search_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys(termino_busqueda)
    search_box.send_keys(Keys.RETURN)

    # Espera para que se carguen los resultados
    time.sleep(3)

    # Selecciona y hace clic en el primer resultado usando XPath
    primer_resultado = driver.find_element(By.XPATH, "(//h3)[1]")
    primer_resultado.click()

    # Espera y muestra el título de la página de resultados
    time.sleep(3)
    print("Título de la página de resultados:", driver.title)

finally:
    # Cierra el navegador
    driver.quit()
