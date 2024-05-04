#Implement updating data in the table (change user first name or phone)
import psycopg2

conn = psycopg2.connect(
	database="PhoneBook",
	user='postgres',
	password='4931',
	host='localhost',
	#port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True

#looking with the first and last name
first_old = str(input("Old name: "))
last_old = str(input("Old surname: "))
num_old = int(input("Old phone number: "))
sql = f"select * from phone_book where name =\'{first_old}\' and surname = \'{last_old}\' and phone_number = \'{num_old}\' "
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
    new_first = str(input("New name: "))
    new_last = str(input("New surname: "))
    new_phone = int(input("New phone number: "))
    sql_update = f"Update phone_book set phone_number =\'{new_phone}\', name =\'{new_first}\', surname =\'{new_last}\' where name =\'{first_old}\' and surname = \'{last_old}\'; " 
    cursor.execute(sql_update)
    print("Successfully!");
else:
    print("This person's name is not in phonebook")

conn.commit()
conn.close()