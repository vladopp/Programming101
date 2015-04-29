import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
"""
fill_table_query = """
INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
VALUES("Ivan Ivanov", 5000, 10000, "Software Developer"),
("Rado Rado", 500, 5, "Technical Support"),
("Ani", 123, 321, "Crawler"),
("Ivo Ivo", 10000, 100000, "CEO"),
("Petar Petrov", 3000, 1000, "Marketing Manager")
"""

cursor.execute(create_table_query)
cursor.execute(fill_table_query)
conn.commit()
