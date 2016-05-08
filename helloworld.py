import sys

def getargument():
    try:
        len(sys.argv) > 0
        print("Hello " + sys.argv[1] + "!")
    except:
        print("Hello World!")

getargument()       
