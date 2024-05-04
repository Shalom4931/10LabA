#upload data from csv file
import psycopg2

conn = psycopg2.connect(
	database="PhoneBook",
	user='postgres',
	password='4931',
	host='localhost',
	port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True
# CSV to TABLE


'''f = open("C:\\Users\\User\\Documents\\uni\\pp2\\lab10\\data.csv", "r")
cursor.copy_from(f, 'phonebook', sep=',')
f.close()
'''

#insert entering user name, phone from console
personal_id = str(input("ID: "))
first = str(input("First name: "))
last = str(input("Last name: "))
num = int(input("Phone number: "))


postgres_insert_query = """ INSERT INTO phone_book VALUES (%s,%s,%s,%s)"""
record_to_insert = (personal_id, first, last, num)
cursor.execute(postgres_insert_query, record_to_insert)

conn.commit()
print("Successfully!");
conn.close()