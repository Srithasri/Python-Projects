a = int(input("Enter value a : "))
b = int(input("Enter value b : "))
def mini_cal():
    c = input("Enter Operation (add / sub / mul / div ): ")
    if(c=='add'):
        print(a+b)
    elif(c=='sub'):
        print(a-b)
    elif(c=='mul'):
        print(a*b)
    elif(c=='div'):
        print(a/b)
    else:
        print("Invalid operation")

mini_cal()