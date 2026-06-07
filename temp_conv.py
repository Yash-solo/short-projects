def CtoF(c):
    return (c*9/5)+32

def CtoK(c):
    return c+273

def FtoC(f):
    return (f-32)*5/9

def KtoC(k):
    return k-273

print("Hello world welcome to> Temparature converter")
print("1-*C to *K")
print("2-*C to *F")
print("3-*F to *C")
print("4-*K to *C")
try:
    choice = int(input("Enter what you have to chalculate:-"))
    if choice>0 and choice<5:
        if choice==1:
            c = int(input("Enter your temp in *C :-"))
            print("Temp in *k :-",CtoK(c))
        elif choice==2:
            c = int(input("Enter your temp in *C :-"))
            print("Temp in *F :-",CtoF(c))
        elif choice==3:
            f = int(input("Enter your temp in *F :-"))
            print("Temp in *C:-",FtoC(f))
        else:
            k = int(input("Enter your temp in *K :-"))
            print("Temp in *C:-")
    else:
        print("Please enter a number in range of 1-4")
except ValueError:
    print("Please enter a number")