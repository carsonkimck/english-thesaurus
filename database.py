import mysql.connector
import config 

con = mysql.connector.connect(
user = config["user"],
password = config["password"],
host = config["host"],
database = config["database"]
)


cursor = con.cursor()
word = input("Enter a word: ")


query = cursor.execute("SELECT * from Dictionary WHERE Expression = '%s' " % word) 
results = cursor.fetchall()



if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")