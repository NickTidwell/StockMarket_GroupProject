import csv
import string
import string

class export():

    def runExport(self, output):
        test = output[0].strip('()')
        count = 0
        tempStr=""
        for x in test:
            if x != ",":
                tempStr = tempStr + x
            else:
                print(tempStr.lstrip(" "))
                tempStr =""
                count +=1
                continue

        print("count is ", count)

        fieldNames =[]
        for x in range(count):
            fieldNames.append("field_" + str(x))

        for x in fieldNames:
            print(x)
        """
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['tuple_1', 'tuple_2', 'classification']
            writer = csv.writer(csvfile, delimiter=',')
            for row in finalDict:
                tempList = list(row)
                writer.writerow([tempList[0], tempList[1], finalDict[row]]) """