import time
shopping_list = []
def show_menu():
    print("=======Shopping List Manager=======")
    print(" ")
    print("1- View all List")
    print("2- Add Item")
    print("3- Purchase Item")
    print("4- Show purchased Items")
    print("5- Delete shopping list")
    print("6- Exit app")
    print()

#add items
def add_items():
    product = input("Enter your item name here you wants to buy:- ")
    quant = input(f"Enter quantity of {product}:- ")
    shopping_list.append({"Products":product,"Quantity":quant,"buy":False})
    print("Item added succesfully\n")

#View all list
def View_list():
    print("\n ====Your Shopping List====")
    for i,j in enumerate(shopping_list , start=1):
        print(f"{i}- {j["Products"]}- {j["Quantity"]}")
    print()
    
#tick as buyed

#show_purchased
def show_purchased():
    for i,j in enumerate(shopping_list):
        if j["buy"]==True:
            print(f"{i+1}- {j["Products"]}- {j["Quantity"]}")
        else:
            None
    print()

#show cart items
def cart_item():
    for i,j in enumerate(shopping_list):
        if j["buy"]==False:
            print(f"{i+1}- {j["Products"]}- {j["Quantity"]}")
        else:
            None
    print()

def purchase():
    cart_item()
    n = int(input("Which item you wants to buy: "))
    shopping_list[n-1]["buy"]= True
    print("your item purchased succesfully\n")



#Exit app
def exit():
    
    print("Loading...........")
    time.sleep(3)
    print("App has closed")

for i in range(1000):
    show_menu()
    try :
        n = int(input("Enter your choice:- "))
        if n==1:
            View_list()
        elif n==2:
            add_items()
        elif n==3:
            purchase()
        
        elif n==4:
            show_purchased()
        elif n==5:  
            shopping_list.clear()
            print("Done")
        
        elif n==6:
            exit()
            time.sleep(2)
            break
        else:
            print("Plese enter a valid number")
    except ValueError():
        print("Please enter a number")