import sqlite3

con = sqlite3.connect("employee.db")
print("database created successfully")

con.execute("create table Employees(id INTEGER primary key AUTOINCREMENT,"
            "name text not null,email text unique not null, address text not null)")

print("table created successfully")
con.close()
