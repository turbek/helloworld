#Checks if string is number
def isnumber(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False


#tranforms string to number
def testinput(x):
    if isnumber(x) == True:
        return(float(x))
    else:
        print( x, "is not a number!")
        quit()

#keeps it in loop until testinput quits
while input == str or int:

    x = input("Enter a number: ")
    x = testinput(x)

    typeofsum = str(input("Enter an operation: "))

    y = input("Enter another number: ")
    y = testinput(y)

    #operations
    if typeofsum == "+":
        print ("Result: ", x + y, "\n")

    elif typeofsum == "-":
        print ("Result: ", x - y, "\n")

    elif typeofsum == "*":
        print ("Result: ", x * y, "\n")

    elif typeofsum == "/":
        print ("Result: ", x / y, "\n")
