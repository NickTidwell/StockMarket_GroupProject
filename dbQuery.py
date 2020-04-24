import dbGUI
import mainGUI
import pymysql as db
# executes queries
class query():

    rows =0
    def query(self,queryString):
        #connection = db.connect("localhost", "root", "root", "project_test", port=8889)
        try:
            connection = db.connect("localhost", "root", "root", "stocks", port=8889)
            cursor = connection.cursor()
            rows = cursor.execute(queryString)
        except Exception as e:
            print("Please try again!")
            return 0, e
            # dbs = reconect()
        else:
            data = []
            for each in range(rows):
                data.append(str(cursor.fetchone()))
            connection.close()
            return data,rows


#que = query()
#que.query("SELECT * FROM players")