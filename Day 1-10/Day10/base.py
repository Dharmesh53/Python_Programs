import operations

result=int(input("Enter the first number:\n"))
again='yes'
while again=='yes':

    op=str(input("Enter the operation ( + , - , * , / ): \n"))
    nextNo=int(input("Enter the second number:\n"))

    if(op=='+'):
        result=operations.add(result,nextNo)
    elif(op=='-'):
        result=operations.minus(result,nextNo)
    elif(op=='*'):
        result=operations.multi(result,nextNo)
    else:
        result=operations.divide(result,nextNo)

    print("==========================================")
    print(f"Result of your operations is: {result} ")
    print("==========================================")
    
    again=str(input(f"Do you want to do more operations with {result} ,type 'yes' or 'no'\n"))
