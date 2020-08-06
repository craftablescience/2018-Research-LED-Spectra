import csv

COLORS = {"Red":15,"Blue":37,"White":36}    # fill with colors when data arrives

cleaner = open("C:\\Users\\Brend\\Desktop\\LED Spectras v2\\MasterFiles\\masterfile.csv","w")
cleaner.write("")
cleaner.close()
del cleaner

try:
    output = open("C:\\Users\\Brend\\Desktop\\LED Spectras v2\\MasterFiles\\masterfile.csv","a")

    output.write("Wavelength (nm),")
    for color in COLORS:
        for i in range(1,COLORS[color] + 1):
            for j in range(1,4):
                output.write("%s %d-%d,"%(color,i,j))
    output.write("\n")

    for h in range(1,2192):
        wave = True
        for color in COLORS:
            for i in range(1,COLORS[color] + 1):
                for j in range(1,4):
                    with open("C:\\Users\\Brend\\Desktop\\LED Spectras v2\\%s %d-%d.csv"%(color,i,j), newline='') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        next(readCSV)
                        csvArray = [row for row in readCSV]
                        for k, row in enumerate(csvArray):
                            if k == h:
                                if wave:
                                    output.write(row[0] + "," + row[1] + ",")
                                    wave = False
                                else:
                                    output.write(row[1] + ",")
                                break
            print(str(color) + ":" + str(h))
        output.write("\n")
finally:
    output.close()
