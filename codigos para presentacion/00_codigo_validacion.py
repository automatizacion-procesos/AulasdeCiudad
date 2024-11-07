from selenium import webdriver
import time
import pandas as pd

try:
    # Inicializa el driver
    driver = webdriver.Chrome()

    # Cambia a webdriver.Firefox() si se quiere usar Firefox

    # Abre Google
    driver.get("https://www.google.com")

    # Maximiza el navegador web en toda la pantalla
    driver.maximize_window()

    # Espera unos segundos para cargar google
    # time.sleep(10)

    # Imprime el título de la página
    print("Título de la página:", driver.title)

    df = pd.DataFrame(columns=['titulo'])

    # Agregar un dato (por ejemplo, una fila de datos)
    df1 = pd.DataFrame([{'titulo': str(driver.title)}])
    df = pd.concat([df, df1], ignore_index= True)
    # Guardar el DataFrame en un archivo CSV
    df.to_csv('archivo.csv', index=False)


    # Cierra el navegador
    driver.quit()

    print('Realizo todos los pasos de forma exitosa')
except Exception  as e:
    print('Hubo error en la ejecucion del codigo', e)

