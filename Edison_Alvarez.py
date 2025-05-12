
import os
import datetime
date = datetime.datetime.now()
producList = [{'productName': 'banano', 'price': 45, 'availableQuantity': 54},
              {'productName': 'manzana', 'price': 4500, 'availableQuantity': 254},
              {'productName': 'pera', 'price': 6000, 'availableQuantity': 100},
              {'productName': 'mango', 'price': 6000, 'availableQuantity': 100},
              {'productName': 'arroz', 'price': 6000, 'availableQuantity': 100}]

#producList=[]


#Input validation function.
def verify(msg, msge, type=str, extravalidation=None):   
    while True:
        try:
            data_type = type(input(msg))
            if extravalidation and not extravalidation(data_type):
                print(msge )
                continue
            return data_type
        except:
            print(msge)

    
# Product addition function.
def addProduct():  
    case = "yes" 
    while "yes" in case:
        flag=True

        productName = input(f"Please enter the name of the product number {len(producList)+1}: ")
        
        for name in producList:
            if name["productName"].lower().strip()== productName.lower().strip():
                print("The product name already exist !")
                flag =False
                continue
        if flag:
            price =verify("Please enter the price of the product: ","\tInvalid number, please try again ",float, lambda x: x >= 0)
            availableQuantity = verify("Please enter the quintity of the product: ", "\tInvalid number, please try again", int,lambda x: x >= 0)
            store ={
                "productName" : productName,
                "price":price,
                "availableQuantity": availableQuantity,
            } 
            producList.append(store)
            print(f"\tproduct {productName} added")
        case = input("Do you want to adde another product? yes, to consult. press any key to exit: ")       



# Function of consulting product
def consultProduct():  
    case = "yes" 
    
    if len(producList)> 0:
        while "yes" in case:
            productName=input(" Please enter the name of the product to search: ")
            flag = None
            for product in producList:
                    if product["productName"].lower().strip()== productName.lower().strip():
                        foundProduct = (f"\t| Product: {product["productName"]} | Price: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                        flag =True
                        print(foundProduct)
            if not flag:
                print(" The product does not exist !")   
            case = input("Do you want to consult another product? yes, to consult. press any key to exit: ")     

    else:
        os.system("clear")
        print("You have no added any products!")
        


#Function update
def updatePrices():  
    case = "yes" 
    if(len(producList) > 0):
        while "yes" in case:

            productName = input(" Please enter the name of the product you want to change the price: ").lower().strip()
            for product in producList:
                if product["productName"].lower().strip() == productName.lower().strip():
                   
                    value = verify("Please enter the new price:  ","\t Invalid number, please try again",float,lambda x: x >= 0)
                    product["price"] = value
                    print("Update product ")
                    print(f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                    flag =True
            if not flag:
                print(" The product does not exist !") 
            case = input("Do you want to consult again? yes, to consult. press any key to exit: ")
    else:
        os.system("clear")
        print("You have no added any products!")
            

# Function remove
def removeProduct():  
    if(len(producList) > 0):
        case = "yes" 
        while "yes" in case:
            productName = input(" Please enter the name of the product you want to delete: ")
            flag = None
            for i,product in enumerate(producList,0):
                    if product["productName"].lower().strip() == productName.lower().strip():
                        del producList[i]
                        print(f"Product removed!")
                        flag =True

            if not flag:
                    print(" The product does not exist !") 
            case = input("Do you want to consult again? yes, to consult. press any key to exit: ")
    else:
        os.system("clear")
        print("You have no added any products!")
        

#Function calcuate 
def calculateValue():  
    if(len(producList) > 0):
        calculate = sum( map( lambda product : product["price"] * product["availableQuantity"],producList))
        print(f"\n\tTotal inventory {calculate}")
        return calculate
    else:
        os.system("clear")
        print("You have no added any products!")



def showInventory():  #muestra la cantidad de producto 
    if len(producList)> 0:
        print(f"\n\t|\t\t SHOW INVENTORY   { date.strftime("%x")}")
        print("\t|"+ "-"*70+ " |")
        calculate =(lambda product : product["price"] * product["availableQuantity"])
        for i,product in enumerate(producList,1):
            
            print(f"\t|{i}. Product: {product["productName"]}    | Price: {product["price"]} | Quantity: {product["availableQuantity"]}  |Total:{calculate(product)}")
        calculateValue()
    else:
        os.system("clear")
        print("You have no added any products!")






menu=('''
         Menu\n 
    1. Add product.
    2. Check product. 
    3. Update price.
    4. Delete product. 
    5. Total value in inventory.
    6. Show inventory. 
    7. Finish.
    \n    Please enter an option: ''')

while True:

    case=input(menu)
    if case == '1':
        addProduct()
    elif case =='2':
        consultProduct()
    elif case == '3':
        updatePrices()
    elif case == '4':
        removeProduct()
    elif case == '5':
        calculateValue()
    elif case == '6':
        showInventory()
    elif case == "7":
        print("              Thanks for using the program")
        break
    else:
        os.system("clear")
        print("Error, please try again. ")
