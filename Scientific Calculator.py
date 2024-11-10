import math

def add(x , y):
    return x + y
def substract ( x ,y):
    return x - y
def multiply (x ,y):
    return x-y
def Divide( x , y):
    if y ==0:
        return "Error: Division by zero"
    return x/y 
def square_roots(x):
    if x < 0:
        return "Value Error Cannot take square root of a negative number"
    return math.sqrt(x)

def trigonometry(func , angle):
    angle_radian = math.radians(angle)
    if func == "Sin":
        return math.sin(angle_radian)
    elif func == "Cos":
        return math.cos(angle_radian)
    elif func == "tan":
        return math.tan(angle_radian)
    else:
        return "Error: Invalid trigonometric function"
    
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Trigonometry")

    while True:
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice in ( '1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter your secod number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {substract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {Divide(num1, num2)}")

        elif choice == '5':
                num = float(input("Enter number for square root: "))
                print(f"Result: {square_roots(num)}")

        elif choice == '6':
                func = input("Enter trigonometric function (sin/ cos / tan): ")
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {trigonometry(func , angle)}")

        else:
            print("INvalid input")

            next_calculation = input("Do you want to perforem another calculator? (yes/no): ")
            if next_calculation.lower() != 'yes':
                
                break
calculator()
