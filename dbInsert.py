import pymysql as db
import numpy as np

class query():

    def query(self,stock_name,prediction_data):

        # last row has NAN values bc those values cannot be calculated at time of run. dropped for insertion to db'
        prediction_data.drop(prediction_data.tail().index, inplace=True)

        data=[]
        rows = prediction_data.size/8
        queryString =""
        try:
            connection = db.connect("localhost", "root", "root", "stocks", port=8889)
        except Exception as e:
            print(e)
            return 0, e
        else:
            print("connected")

        for each in prediction_data.index:
            if np.isnan(prediction_data['Prediction'][each]):
                args = [stock_name, str(prediction_data['Date'][each]), 0.0, float(prediction_data['Open'][each]),
                       float(prediction_data['High'][each]),
                       float(prediction_data['Low'][each]), float(prediction_data['Close'][each]),
                       float(prediction_data['Adj Close'][each]),
                       float(prediction_data['Volume'][each])]
                queryString = "INSERT INTO `prediction` (`symbol`,`date`, `prediction`,`open`,`high`,`low`,`close`,`adj_close`,`volume`) " \
                                "VALUES (%s,%s,%s,%s, %s,%s,%s,%s,%s)"
            else:
                args = [stock_name,str(prediction_data['Date'][each]), float(prediction_data['Prediction'][each]), float(prediction_data['Open'][each]),
                   float(prediction_data['High'][each]),
                   float(prediction_data['Low'][each]), float(prediction_data['Close'][each]),
                   float(prediction_data['Adj Close'][each]),
                   float(prediction_data['Volume'][each])]
                queryString = "INSERT INTO `prediction` (`symbol`,`date`, `prediction`,`open`,`high`,`low`,`close`,`adj_close`,`volume`) " \
                            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                cursor = connection.cursor()
                cursor.execute(queryString, args)
                connection.commit()
            except Exception as e:
                print("exception ", e)
            else:
                #print("works")
                data.append(args)
                print(args)

        #print(data)
        return data, rows
        # connection.close()
