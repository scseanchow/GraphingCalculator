import module
import GUI

def printMenu():
    print("Menu")
    choice = input("Enter your choice:")
    if choice == 1:
        print "Gui Interface"
        GUI.startGUI()
    elif choice == 2:
        print "command line interface"
    elif choice == 3:
        print "text interface"

printMenu()
