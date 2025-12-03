import sqlite3

# connecting to database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# reading SQL-script from file
with open("queries.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

# execute all queries from file
cursor.executescript(sql_script)

# save changes
conn.commit()
conn.close()
