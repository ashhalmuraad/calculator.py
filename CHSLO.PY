#functions by ashhal
import math

def area_circle(r):
    print("Area of circle is:", math.pi * r**2)

def area_square(side):
    print("Area of square is :", side**2)

def area_rectangle(width, length):
    print("Area of rectangle is:", width * length)

def area_triangle(base, height):
    print("Area of triangle is:", (base * height) / 2)

def sphere(r):
    print("Volume of sphere is:", (4 * math.pi * r**3) / 3)

def cube(side):
    print("Volume of cube is:", side**3)

def cuboid(length, width, height):
    print("Volume of cuboid is:", length * width * height)

def cone():
    pass


# Advance calculator
while True:
    print("\nCHSLO CALC")
    print("1.DMAS")
    print("2.Bills")
    print("3.Roots and Squares")
    print("4.Geometry")
    print("5.Exit")

    choose = input("Choose your action, enter the digit: ")

    if choose == "1":
        print("Ashhal's Calculator")
        op = input("Choose an operation (+, -, *, /): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == "*":
            print("Result:", num1 * num2)
        elif op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")

    elif choose == "2":
        print("Note: The electricity bill works on tariff/slab system")
        units = float(input("Enter your used units: "))

        if units <= 100:
            print("Your monthly bill is:", units * 12.5 + 1200)
        elif units <= 200:
            print("Your monthly bill is:", units * 26.5 + 1200)
        elif units <= 300:
            print("Your monthly bill is:", units * 38 + 1200)
        elif units <= 400:
            print("Your monthly bill is:", units * 65 + 1200)

    elif choose == "3":
        choice = input("1.Root or 2.Square or 3.Cube Root or 4.Cube: ")

        if choice == "1":
            number = float(input("Enter the number to root: "))
            print(number**0.5)

        elif choice == "2":
            number = float(input("Enter the number to square: "))
            print(number**2)

        elif choice == "3":
            number = float(input("Enter the number to cube root: "))
            print(number**(1/3))

        elif choice == "4":
            number = float(input("Enter the number to cube: "))
            print(number**3)

        else:
            print("Invalid option")

    elif choose == "4":
        choice = input("Choose operation: 1.Area or 2.Volumes: ")

        if choice == "1":
            shape = input("1.Circle, 2.Square, 3.Rectangle, 4.Triangle: ")

            if shape == "1":
                r = float(input("Enter the radius: "))
                area_circle(r)

            elif shape == "2":
                side = float(input("Enter the side: "))
                area_square(side)

            elif shape == "3":
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                area_rectangle(width, length)

            elif shape == "4":
                height = float(input("Enter the height: "))
                base = float(input("Enter the base: "))
                area_triangle(base, height)

        elif choice == "2":
            shape = input("1.Sphere, 2.Cube, 3.Cuboid, 4.Cone: ")

            if shape == "1":
                r = float(input("Enter the radius: "))
                sphere(r)

            elif shape == "2":
                side = float(input("Enter the side: "))
                cube(side)

            elif shape == "3":
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                cuboid(length, width, height)

            elif shape == "4":
                cone()

    elif choose == "5":
        print("Thank you for using CHSLO!")
        break

    else:
        print("Invalid option.")
    