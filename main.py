'''accediendo a una base de datos de datos solo con python y sqlite3'''
import sqlite3
'''creo una coneccion con mi archivo de datos'''
coneccion= sqlite3.connect('C:\\Users\\Elian Gonzalez\\Desktop\\db-py\\db-python\\db\\vacunas')
'''creo un objeto cursor '''
cur= coneccion.cursor()

'''con el cursor ejecuto las consultas sql'''
cur.execute('SELECT nombre, apellido,dni,domicilio, fecha_nac AS nacido_en FROM personas order by nombre ;')
'''extraigo todos los datos y los guardo en una variable'''
data1=cur.fetchall()

cur.execute('SELECT nombre, apellido,dni,domicilio, fecha_nac AS nacido_en FROM personas order by nombre ;')
'''extraigo el primer dato que encuentre y lo guardo en una variable'''
data2=cur.fetchone()

print(data1)
print()
print()
print()
print(data2)

'''cierro la coneccion'''
coneccion.close()

