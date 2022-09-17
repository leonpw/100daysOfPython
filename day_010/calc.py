
def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1 / n2
def multiply(n1,n2):
    return n1 * n2

operations = {
    '+' : add,
    '-' : substract,
    '/' : divide,
    '*' : multiply,
}

shouldContinue = True
valueSet = False
while shouldContinue:
    
    if valueSet:
        input1 = answer
        print(f"We continue with {input1}")
    else:
        input1 = int(input("What is the first number? "))
        
    for operation in operations:
        print(operation)
        
    choose_operation = input("Give me an operation: ")
    
    input2 = int(input("What is the second number? "))

    answer = operations[choose_operation](input1,input2)
    print(f"The answer is: {input1} {choose_operation} {input2} = {answer}")
    
    if input(f'Should we continue with {answer}? [y][n]: ') == 'y':
        shouldContinue = True
        valueSet = True
    else:
        valueSet = False
        if (input('Should we continue at all? [y][n]: ')) == 'n':
            shouldContinue = False
    
