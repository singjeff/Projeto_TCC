import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-6181A8Q\SQLEXPRESS;'
                      'Database=Comercial_Controll;'
                      'Trusted_Connection=yes;')

cursor= conn.cursor()

i=int(input("Digite id: ")) 
dec= str(input("Digite seu nome: "))

cursor.execute("INSERT INTO Tipo_Pessoa(id_tipo_pessoa,descricao) VALUES (?,?)",i,dec)
''''
cursor.execute("TRUNCATE TABLE Tipo_Pessoa")
'''

cursor.execute("select * from Comercial_Controll.dbo.Tipo_Pessoa")

cursor.
for row in cursor:
    print(row)


conn.commit()
cursor.close()
conn.close()


