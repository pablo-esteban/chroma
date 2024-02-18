import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

with open('essential.csv') as file:
    next(file)
    for line in file:
        row = line.strip('\n').split(',')
        print(line)
        try:
            cursor.execute(
                "INSERT INTO colours (hex, name) VALUES (?, ?)", row
            )
        except sqlite3.InternalError:
            print('>>>>', row)

connection.commit()
connection.close()
