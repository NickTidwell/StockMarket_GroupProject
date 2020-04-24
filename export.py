import csv
import string
import re
import pymysql as db

#this module exports db queries to .cvs files

class export():

    def runExport(self, output, query, fileName):

        self.tableName=""
        self.fieldNames = []
        #self.selectedFieldNames = []

        #1st step in processing queries to get col names
        checkForAll = re.compile("\*")
        if(checkForAll.search(query)):
            self.returnAllFields(self.findTableStar(query))
        else:
            #self.returnAllFields(self.findTableName(query))
            self.fieldNames = self.selectedFieldNames =self.returnSelectedFields(query)

        # return from db query needs cleaned
        self.temp =[]
        for each in output:
           self.temp.append(each.strip("()").replace("'"," ").replace(",", " "))

        #tokenize a single string to column values & append col headers
        self.finalOutput = self.wrapper(self.temp)
        self.finalOutput.insert(0,self.fieldNames)
        fn = fileName+".csv"
        with open(fn, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in self.finalOutput:
                writer.writerow([row[x] for x in range(len(self.fieldNames))])

    #returns all col names for a given table when = is used in query
    def returnAllFields(self, columnName):
        try:
            connection = db.connect("localhost", "root", "root", "stocks", port=8889)
            cursor = connection.cursor()
            queryString = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=%s"
            rows = cursor.execute(queryString,columnName)
        except Exception as e:
            print("Please try again!")
            return 0, e
        else:
            for each in range(rows):
                self.fieldNames.append(str(cursor.fetchone()).strip("(),'"))
        connection.close()
#helper func to clean ouput that was depreciated
    def cleanse(self,output):
        for each in output:
            print(each)
            try:
                x=0
                #retTableName = re.compile("\\s*(\\s*\\w*\\s*,)|([0-9]*-[0-9]*-[0-9]*\\s,)|([0-9]*.[0-9]*\\s,)*", re.I)
                retTableName = re.compile("[0-9]*.[0-9]*", re.I)
                s = retTableName.search(each)
                fields = s.group()
                # select symbol, prediction from prediction
            except Exception as e:
                print("cleanse",e)
            else:
                print(fields)
    # return col names when * is not used
    def returnSelectedFields(self,query):
        try:
            retTableName = re.compile("SELECT(\\s*\\w*,*\\s*)*FROM", re.I)
            s = retTableName.search(query)
            fields = s.group()
            return self.splitMultFields(fields)
            #select symbol, prediction from prediction
        except Exception as e:
            print(e)
    #helper function in ret table names
    def findTableName(self,query):
        try:
            retTableName = re.compile("TABLE_NAME\\s*='\\w*'", re.I)
            s = retTableName.search(query)
            tableName = s.group()
            finalStr = re.compile("'\\w*'")
            x = finalStr.search(tableName)
            tableName = x.group().strip("'").lower()
        except Exception as e:
            print(e)

#SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='prediction'
    #find table col names when * is used
    def findTableStar(self,query):
        retTableName = re.compile("from\\s*\\w*\\s*", re.I)
        s = retTableName.search(query)
        tableName = s.group().strip("from").strip(" ")
        return tableName
    #helper function in finding col names
    def splitMultFields(self,splitThis):
        temp = []
        splitThis = splitThis.strip("select").strip("from")
        splt = re.compile("[\\w]*")
        s = splt.findall(splitThis)
        for each in s:
           if each.isalnum():
               print(each)
               temp.append(each)
        return temp
# wrapper calls the tokenization of a string that was each row of cleaned up db output
# for somereason doing both wrapper & splitMultfields2 in one function was causing issues
# when appending to a list to return to main function
    def wrapper(self, splitThis):
        work =[]
        for each in splitThis:
            work.append(self.splitMultFields2(each))
        return work

    def splitMultFields2(self,splitThis):
        t1 = []
        #print(splitThis)
        splt = re.compile("[.\\w-]*")
        s = splt.findall(splitThis)
        for x in s:
            if len(x) > 0:
                t1.append(x)
        return t1