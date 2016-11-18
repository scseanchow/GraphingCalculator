import sys
# driver file for graphing Calculator
# takes in command line args to start respective program (1,2,3) ,
# (gui,text line, text file)


def printMenu(argv, textFile):
    if argv == "1":
        print "GUI Interface Started!"
        import GUI
        GUI.startGUI()
    elif argv == "2":
        print "Text Line Interface Started!"
        import textInterface
        textInterface.startText()
    elif argv == "3":
        print "Text File Interface Started!"
        import fileCalc
        fileCalc.fileRead(textFile)

if (len(sys.argv) > 2):
    printMenu(sys.argv[1], sys.argv[2])
else:
    printMenu(sys.argv[1], "NULL")
