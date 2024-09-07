import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)
    in1 = float(input("Enter first number: "))
    cont = True
    while cont:
        operator=input("Enter the operation to perform i.e. '+','-','*','/': ")
        in2=float(input("Enter first number: "))
        result=operation[operator](in1, in2)
        print(f"{in1} {operator} {in2} = {result}")
        loop=input(f"Type 'y' to continue calculating with {in1}, or type 'n' for new calculation: ").lower()
        if loop=='n':
            cont=False
            print("/n" * 20)
            calculator()
        elif loop=='y':
            in1=result
        else:
            print("Enter Valid choice!!!")

calculator()


