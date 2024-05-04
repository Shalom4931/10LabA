#Querying data from the tables (with different filters)
import psycopg2

conn = psycopg2.connect(
	database="PhoneBook",
	user='postgres',
	password='4931',
	host='localhost',
	#port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

#select all
#sql = f"select * from phonebook";

#select filter 
#sql = f"select * from phone_book where name = \'Sasha\' ";


#select with sort filter decrease by first
sql = f"select * from phone_book by order by name desc";


#select with sort filter increase by first
#sql = f"select * from phone_book by order by name asc";


cursor.execute(sql)
info = cursor.fetchall()
print(info)