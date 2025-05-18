# Function that will print the menu to the user
def area_menu():
    print("Menu:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("Enter a number option: ")

# Display the menu
area_menu()

# Try will exectue a block of code and if any error is thrown then the program will directly goes
# into the 'except' block
try:
    # The input() function will take input as a string. And the int function will convert the string to integer in base 10.
    # But if anything is entered other than some numerical value it will throw the error(namely ValueError).
    menu_option = int(input("Enter the number of your choice: "))

    # Check which option was selected
    if menu_option == 1:
        print("You selected: Rectangle")
        length=float(input("Length of the rectangle:")) #Using float insted of integer as input can be in decimal
        depth=float(input("Depth of the rectangle:"))
        area=round(length*depth,3) #Roudning the result to 3 decimal places
        print("The area of the Rectangle shape is: "+str(area)+" metres") #str function will convert the float value in string for printing the message
    elif menu_option == 2:
        print("You selected: Square")
        side=float(input("Side of the square:"))
        area=round(side*side,3)
        print("The area of the Square shape is: "+str(area)+" metres")
    elif menu_option == 3:
        print("You selected: Triangle")
        base=float(input("Base of the triangle:"))
        depth=float(input("Height of the triangle:"))
        area=round((base*depth)/2,3)
        print("The area of the Triangle shape is: "+str(area)+" metres")
    else:
        print("Incorrect shape option selected")
except ValueError:
    print("Invalid input data! Enter an integer value as an option") #If a non numerical value is entered. This line will handle it.