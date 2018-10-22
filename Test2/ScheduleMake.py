import time
import mysql.connector

class ScheduleMaker:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ="localhost",
            user ="root"
            password ="mysql11"
            database ="thesis"
        )

        self.mycursor = self.mydb.cursor()
        

    def prepareScheduleMaker(self):
        
    


#notes
##import mysql.connector
##
##mydb = mysql.connector.connect(
##  host="localhost",
##  user="yourusername",
##  passwd="yourpassword",
##  database="mydatabase"
##)
##
##mycursor = mydb.cursor()
##
##mycursor.execute("SELECT * FROM customers")
##
##myresult = mycursor.fetchall()
##
##for x in myresult:
##  print(x)
