import GUI
import sys

def printMenu(argv,textFile):
    if argv == "1":
        print "Gui Interface"
        GUI.startGUI()
    elif argv == "2":
        print "text line interface"
    elif argv == "3":
        print "text file interface"
        #text.startText(textFile)

printMenu(sys.argv[1])
