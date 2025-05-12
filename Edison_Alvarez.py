
import os
producList = []

#verifica el estado de la entrada 
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

    
def addProduct():  
    case = "yes" 
    while "yes" in case:
        productName = input("Please enter the name of the product: ")
        for name in producList:
            if name["productName"]== productName:
                print("The product name already exist !")
                break
        price =verify("Please enter the price of the product: ","\tInvalid number, please try again ",float, lambda x: x >= 0)
        availableQuantity = verify("Please enter the quintity of the product: ", "\tInvalid number, please try again", int,lambda x: x >= 0)
        store ={
            "productName" : productName,
            "price":price,
            "availableQuantity": availableQuantity,
        } 
        producList.append(store)
        print(f"\tproduct {productName} added")
        
            #print(producList)      
        case = input("Do you want to add another product? yes, to add: ")


def consultProduct():  # consultar producto
    if len(producList)> 0:
        productName=input(" Please enter the name of the product to search: ")
        flag = None
        for product in producList:
                if product["productName"]== productName:
                    foundProduct = (f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                    flag =True
                    print(foundProduct)
        if not flag:
            print(" The product does not exist !")        
    else:
        os.system("clear")
        print("You have no added any products!")



def updatePrices():  # actualizar presios

    if(len(producList) > 0):

        productName = input(" Please enter the name of the product to search: ")
        flag = None
        for product in producList:
            if product["productName"] == productName:
                #value = float(input("Please enter the new prece:  "))
                value = verify("Please enter the new prece:  ","\t Invalid number, please try again",float,lambda x: x >= 0)
                product["price"] = value
                print("Update product ")
                print(f"\t| Producto: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} |")
                flag =True
        if not flag:
            print(" The product does not exist !") 
    else:
        os.system("clear")
        print("You have no added any products!")


def removeProduct():  # eliminar producto
    if(len(producList) > 0):
            productName = input(" Please enter the name of the product you want to delete: ")
            flag = None
            for i,product in enumerate(producList,0):
                    if product["productName"] == productName:
                        del producList[i]
                        print(f"Product removed!")
                        flag =True

            if not flag:
                    print(" The product does not exist !") 
    else:
        os.system("clear")
        print("You have no added any products!")


def calculateValue():  # calcular el total del inventario 
    if(len(producList) > 0):
        calculate = sum( map( lambda product : product["price"] * product["availableQuantity"],producList))
        print(f"\n\tTotal inventory {calculate}")
    else:
        os.system("clear")
        print("You have no added any products!")


def showInventory():  #muestra la cantidad de producto 
    if len(producList)> 0:
        print("\n\t|\t\t SHOW INVENTORY ")
        print("\t|"+ "-"*60+ " |")
        for product in producList:
            print(f"\t| Product: {product["productName"]} | Prece: {product["price"]} | Quantity: {product["availableQuantity"]} ")
            
    else:
        os.system("clear")
        print("You have no added any products!")



menu=('''
    Selecciones\n 
    1. Add product.
    2. Check product. 
    3. Update price.
    4. Delete product. 
    5. Total value in inventory.
    6. Show inventory. 
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
    else:
        os.system("clear")
        print("Error, please try again. ")
