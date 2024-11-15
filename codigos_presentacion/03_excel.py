import pandas as pd
import time

# Carga el archivo Excel
file_path = "./codigos_presentacion/data.xlsx"
# Lee el excel
df = pd.read_excel(file_path)

# Imprime todos los datos
print("Datos completos del archivo:")
print(df)

# Filtra los datos.
# En este caso selecciona filas donde una columna cumple una condición
# Registros tales que la columna 'Rol'contiene 'Desarrollador nivel - 2'
df_filtrado = df[df["Rol"] == "Desarrollador nivel - 2"]

# Pausa para observar datos originales
time.sleep(10)

# Imprime los datos filtrados
print("\nDatos filtrados:")
print(df_filtrado)
