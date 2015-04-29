import sqlite3


db = sqlite3.connect("company.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def lsit_employees():
    result = cursor.execute("SELECT id, name, position FROM employees")
    db.commit()
    for row in result.fetchall():
        print(row["id"], row["name"], row["position"])


def monthly_spending():
    salaries = cursor.execute("SELECT monthly_salary FROM employees")
    summ = sum([x["monthly_salary"] for x in salaries])
    print("The company is spending ${} every month!".format(summ))


def yearly_spending():
    salaries = cursor.execute("SELECT monthly_salary, yearly_bonus FROM employees")
    summ = sum([x["monthly_salary"]*12 + x["yearly_bonus"] for x in salaries])
    print("The company is spending ${} every year!".format(summ))


def add_employee():
    name = input("name: ")
    monthly_salary = input("monthly_salary: ")
    yearly_bonus = input("yearly_bonus: ")
    position = input("position: ")
    cursor.execute("INSERT INTO employees(name, monthly_salary, yearly_bonus, position) VALUES(\"{}\", {}, {}, \"{}\")".format(name, int(monthly_salary), int(yearly_bonus), position))
    db.commit()


def delete_employee():
    employee_id = input("id: ")
    employee = cursor.execute("SELECT name FROM employees WHERE id = {}".format(int(employee_id)))
    employee = employee.fetchone()
    print(employee["name"]+" was deleted")
    cursor.execute("DELETE FROM employees WHERE id = {}".format(int(employee_id)))
    db.commit()


def update_employee():
    employee_id = input("id: ")
    name = input("name: ")
    monthly_salary = input("monthly_salary: ")
    yearly_bonus = input("yearly_bonus: ")
    position = input("position: ")
    cursor.execute("UPDATE employees SET name = \"{}\", monthly_salary = {}, yearly_bonus = {}, position = \"{}\" WHERE id = {}".format(name, monthly_salary, yearly_bonus, position, employee_id))
    db.commit()


is_not_finished = True
while is_not_finished:
    command = input("command>")
    if command == "list_employees":
        lsit_employees()
    elif command == "monthly_spending":
        monthly_spending()
    elif command == "yearly_spending":
        yearly_spending()
    elif command == "add_employee":
        add_employee()
    elif command == "delete_employee":
        delete_employee()
    elif command == "update_employee":
        update_employee()
    elif command == "exit":
        is_not_finished = False
