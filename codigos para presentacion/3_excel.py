import pandas as pd

# Carga el archivo Excel
file_path = 'data.xlsx'
# Lee el excel
df = pd.read_excel(file_path)

# Verifica si el archivo tiene datos
if df.empty:
    print("El archivo Excel está vacío.")
else:
    # Imprime todos los datos
    print("Datos completos del archivo:")
    print(df)

    # Filtra los datos (por ejemplo, selecciona filas donde una columna específica cumple una condición)
    # Aquí, suponemos que hay una columna llamada 'Role in Company' y queremos filtrar los valores iguales a 'Programmer'
    df_filtrado = df[df['Rol'] == 'Desarrollador nivel - 2']

    # Imprime los datos filtrados
    print("\nDatos filtrados:")
    print(df_filtrado)

