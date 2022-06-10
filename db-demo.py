import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "sharad",
    password = "sharad"
)

print(db)

dbquery = "CREATE DATABASE IF NOT EXISTS mydatabase"

mycursor = db.cursor()
mycursor.execute(dbquery)

mycursor.execute("USE mydatabase")

mydatabaseTable = """
    CREATE TABLE IF NOT EXISTS employee(
        id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        age INT
    )"""

mycursor.execute(mydatabaseTable)

# ins = """INSERT INTO employee (first_name, last_name, age) VALUES ('Sharad','Shrestha',20),('Himal','Karki',21)"""

# mycursor.execute(ins)
# db.commit()

upd = "UPDATE employee SET first_name = 'Himal Jung Noob' WHERE first_name = 'Himal Jung'"
mycursor.execute(upd)
db.commit()