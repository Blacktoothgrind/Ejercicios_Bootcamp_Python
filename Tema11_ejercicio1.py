import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Natalia', 'Insfran')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Gildo', 'Aguero')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Lionel', 'Sanchez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Ricardo', 'Darin')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Parada', 'Enciso')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Rolando', 'Mota')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Natalia', 'Suarez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Ronaldo', 'Cruz')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Natalia'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()
