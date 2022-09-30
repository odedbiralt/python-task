def ex(number) :
    d1 = number%10
    d2 = number//10
    mul = d1* d2
    return mul

def main() :
    number1 = int(input("enter num"))
    a=ex(number1)
    number2 = int(input("enter num"))
    b=ex(number2)
    if (a>b) :
        print("number1=",number1)
    elif (a<b) :
        print("number2=", number2)
    else :
        print ("equals")

main()
