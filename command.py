import sqlite3

conn = sqlite3.connect('student.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
grade TEXT)
""")

# cursor.execute("""
# INSERT INTO students(name,age,grade)
# VALUES(?,?,?)
# """,("Alice",20,"A+"))
conn.commit()
students_data ={
    ("Bob",19,"B"),
    ("Charlie",21,"A+"),
    ("David",22,"O")
}
# conn.executemany("""
# INSERT INTO students(name,age,grade)
# VALUES(?,?,?)
# """,students_data)
# conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('''
UPDATE students
SET grade =?
WHERE name = ?
''',("A+","Bob")
)    
conn.commit()

cursor.execute('''
DELETE FROM students
WHERE name = ?
''', ("Charlie",))
conn.commit()
conn.close()

