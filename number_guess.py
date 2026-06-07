import random as rd
real_num = rd.randint(1,100)
count=0
for i in range(10000):
    print()
    try:
        num = int(input("Guess a number between 1-100:"))
        if num>0 and num<=100:
            if num==real_num:
              print("Congrats you guess right number")
              count+=1
              print("you took",count,"attempts to guess right number")
              break
            else:
                print("wrong number")
                count+=1
                if num>real_num:
                 print("Your number is greater than price number")
                else:
                    print("Your number is less than price number")
        else:
            print("Please choose between 0-100")
    except ValueError:
       print("please enter a number!")