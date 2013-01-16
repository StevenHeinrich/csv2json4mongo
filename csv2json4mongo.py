import csv

def csv2json4mongo(inputCSV='sample.csv', mongoDocuments='sample.mongo', xField='Lon', yField='Lat'):
    try:
        csvFile = csv.reader(open(inputCSV, 'r'), delimiter = ',', quotechar = '"')
        jsonDocsFile = open(mongoDocuments, 'w')
    except:
        print 'Could not read input file.'
        exit()
    is_header = True
    is_firstRow = True
    for row in csvFile:
        geoPoint = ""
        if(is_header):
            header = row
            is_header = False
        else:
            if is_firstRow == False:
                jsonDocsFile.write('\n')
            jsonDocsFile.write('{')
            column = 0 
            while column < len(header):
                if header[column] == xField:
                    geoPoint += "[" + str(row[column]) + ","
                if header[column] == yField:
                    geoPoint += str(row[column]) + "]"
                jsonDocsFile.write('"' + header[column] + '":"' + row[column] + '"')
                jsonDocsFile.write(', ')
                column += 1
            jsonDocsFile.write('"MongoPoint": ' + geoPoint)
            jsonDocsFile.write("}")
            is_firstRow = False
    jsonDocsFile.write('\n')
    return True
