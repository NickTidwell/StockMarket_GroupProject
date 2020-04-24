import pymysql as db
test = "localhost"

def reconect():
    print("Enter in the name of the DB: ")
    dbs = input()
    return dbs

def connect(dbs):
    re = 0
    while re == 0:
        try:
            connection = db.connect(test, "root", "root", dbs, port=8889)
        except Exception as e:
            print(e , " Please try again!")
            return 0
            #dbs = reconect()
        else:
            #print("Connected")
            re = 1
            return connection

#connection = connect(dbs)


#cursor = connection.cursor()
#execute SQL query using execute() method.
#cursor.execute("SELECT * FROM players")

# Fetch a single row using fetchone() method.
#data = cursor.fetchall()
#print(data)


#connection.close()


# disconnect from server
