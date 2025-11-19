def addition():
    print("")
    add1 = input("First number to add: ")
    add2 = input("Second number to add: ")
    sum = float(add1) + float(add2)
    print(sum)
    print("")


def subtraction():
    print("")
    sub1 = input("Number that is being subtracted from: ")
    sub2 = input("Number that is subtracting: ")
    difference = float(sub1) - float(sub2)
    print(difference)
    print("")


def multiplication():
    print("")
    times1 = input("First number to be multiplied: ")
    times2 = input("Second number to be multiplied: ")
    product = float(times1) * float(times2)
    print(product)
    print("")


def division():
    print('')
    dividend = input("Number to be divided: ")
    divisor = input("Number that is dividing: ")
    if divisor != "0":
        quotient = float(dividend) / float(divisor)
        print(quotient)
        print("")
    else:
        print("Cannot divide by 0")
        print("")


def reduce_fraction():
    print('')
    numerator = input("Numerator: ")
    denominator = input("Denominator: ")
    answer =

    print("")


def main():
    while True:
        task = input(
            "What math function would you like to do? (+,-,*,/, reduce fraction) Press q to quit: ").lower()
        if task == "+" or task == "addition" or task == "add":
            addition()
        elif task == "-" or task == "subtraction" or task == "minus" or task == "subtract":
            subtraction()
        elif task == "*" or task == "multiplication" or task == "times":
            multiplication()
        elif task == "/" or task == "division" or task == "divide":
            division()
        elif task == "reduce fraction":
            reduce_fraction()
        elif task == "q" or task == "quit":
            print("Thank you.")
            print('')
            break
        else:
            print("Please input a valid function.")


main()

