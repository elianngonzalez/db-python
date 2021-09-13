#iniciar con pipenv python3

# Importa pandas y sqlite3
import pandas as pd
import sqlite3

# Crea una conexión a la base de datos SQLite
con = sqlite3.connect("c:\\Users\\Elian Gonzalez\\Documents\\db\\vacunas")
# Usa read_sql_query de pandas para extraer el resultado
# de la consulta a un DataFrame
df = pd.read_sql_query('SELECT nombre, apellido,dni,domicilio, fecha_nac AS nacido_en FROM personas order by nombre', con)

df2=pd.read_sql_query('SELECT nombre, dosis ,intervalo ,edad_min FROM vacunas',con)


# Verifica que el resultado de la consulta SQL está
# almacenado en el DataFrame
print(df2.head())
print()
print()
print(df.head())

# No te olvides de cerrar la conexión
con.close()