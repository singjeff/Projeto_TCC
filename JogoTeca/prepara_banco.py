import pyodbc
print('Conectando...')


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-6181A8Q\SQLEXPRESS;'
                      'Database=JogoTeca;'
                      'Trusted_Connection=yes;')


# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

cursor = conn.cursor()

cursor.execute ('''
    CREATE TABLE jogo (
      id int identity(1,1) not null,
      nome varchar(50)  NOT NULL,
      categoria varchar(40) NOT NULL,
      console varchar(20) NOT NULL,
      constraint pkid PRIMARY KEY (id)
    )

    CREATE TABLE usuario (
      id varchar(8)  NOT NULL,
      nome varchar(20)  NOT NULL,
      senha varchar(8)  NOT NULL,
      constraint pk_id PRIMARY KEY (id)
    )
    ''')



# inserindo usuarios

cursor.executemany('INSERT INTO usuario (id, nome, senha) VALUES (?, ?, ?)',
      [('luan', 'Luan Marques', 'flask'),
      ('nico', 'Nico', '7a1'),
      ('danilo', 'Danilo', 'vegas')])


cursor.execute('select * from usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO jogo (nome, categoria, console) VALUES (?, ?, ?)',
      [
            ('God of War 4', 'Ação', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS'),
      ])

cursor.execute('select * from jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito


conn.commit()
cursor.close()
conn.close()
