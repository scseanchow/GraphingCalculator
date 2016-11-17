import GUI
import sys

def printMenu(argv):
    if argv == "1":
        print "Gui Interface"
        GUI.startGUI()
    elif argv == "2":
        print "text line interface"
    elif argv == "3":
        print "text file interface"

printMenu(sys.argv[1])
