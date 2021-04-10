#Faulty Calculator
#45*3=555,56+9=77,56/6=4

Oper=input("Please Enter A Operator : \n")
n1=int(input("please Enter number 1 : \n"))
n2=int(input("please Enter number 2 : \n"))

if ((Oper=='*' or Oper=='+' or Oper=='-' or Oper=='/' or Oper=='%')):

    if ((n1==45 and n2==3) and (Oper=='*' )):
        print("operation : 45 * 3 \nAnwser :555 ")
    elif ((n1==56 and n2==9) and (Oper=='+' )):
        print("Operation : 56 + 9 \nAnwser :77")
    elif ((n1==56 and n2==6) and (Oper=='/' )):
        print("Operation : 56 + 6 \nAnwser :4")
    else:
        print("Operation :",n1,Oper,n2)
        if Oper=='+':
            print("\nAnswer : ",(n1+n2))
        elif Oper=='-':
            print("\nAnswer : ", (n1 - n2))
        elif Oper=='*' :
            print("\nAnswer : ", (n1 * n2))
        elif Oper=='/' and (n1>0 and n2>0) :
            print("\nAnswer : ", (n1 * n2))
        elif Oper == '%':
            print("\nAnswer : ", ((n1 / 100)*n2))
        else:
            print("Error in Input...")
else:
    print("Sorry!!! Invalid Input...")




