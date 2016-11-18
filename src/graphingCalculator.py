import GUI
import sys
import fileCalc

def printMenu(argv,textFile):
    if argv == "1":
        print "Gui Interface"
        GUI.startGUI()
    elif argv == "2":
        print "text line interface"

    elif argv == "3":
        print "text file interface"
        fileCalc.fileRead(textFile)
        #text.startText(textFile)
if (len(sys.argv) > 2):
    printMenu(sys.argv[1],sys.argv[2])
else:
    printMenu(sys.argv[1],"NULL")
