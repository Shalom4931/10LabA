#Implement deleting data from tables by username of phone
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

#looking with the first and last name
first_old = str(input("Old first name: "))
last_old = str(input("Old last name: "))

sql = f"select * from phone_book where name =\'{first_old}\' and surname = \'{last_old}\' "
cursor.execute(sql)
info = cursor.fetchall()


if len(info) > 0:
    sql_update = f"Delete from phone_book where name =\'{first_old}\' and surname = \'{last_old}\'; " 
    cursor.execute(sql_update)
    print("Successfully deleted!");
else:
    print("This person's name is not in phonebook")

conn.commit()
conn.close()