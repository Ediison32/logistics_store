
-------------------------------------########----------------------------

Este programa esta estructurado gestion de inventario, permitiendo añadir, consultar, actualizar, eliminar, productos que se encuentren o que quiera agregar al sistema. 

    1. para agregar un producto introdusca el numemero "1", depues el sistema le preguntara el nombre del producto, aqui el sistema le permite agregar tanto numeros como caracteres mayusculas, minusculas. Despues le pedira el precio del producto en esta peticion solo recibe numeros. Despues pedira la cantidad del productos al igual solo recibe numeros. Necesita minimo 5 productos para continuar con el menu, despues de los 5 puede o no agregar productos. 

    2.Para consultar productos es necesario ingresar el numero "2", despues nombre del producto que desea ver. Puede ingresar en mayusculas, minusculas y numero, finalmente preguntara si desea hacer una consulta escribe "yes" o de lo contrario oprime cualquier tecla. 

    3. para acutalizar el precio de un producto ingrese el "3", despues le pedira el nombre del producto a actualizar. Pede ingresar en mayusculas o minusculas, luego pedira el nuevo valor aqui solo se puede ingresar numero. Finalmente preguntara si desea hacer una consulta escribe "yes" o de lo contrario oprime cualquier tecla.

    4. Para elimiar un producto ingrese "4" le pedira el nombre del producto a eliminar puede ingresar mayusculas o minusculas este elimina tanto el producto como cantidad y precio. finalmente preguntara si desea hacer una consulta escribe "yes" o de lo contrario oprime cualquier tecla. 

    5. Para calcular el total del inventario solo es necesario ingresar el numero "5" y mostrar el total del inventario 
    
    6. Para ver todo el inventario solo es necesario agregar el valor "6" mostrando todo lo que tiene agregado. 

    7. para salir del sistema solo ingrese el valor "7" y el sistema se detendra.




    #Errores

    - El sistema captura los errores de entrada como escoger mal el menu. Si ingresa un valor erroneo se limpia la pantalla sale un error y saldra el menu. 

    - En las entradas numericas solo reciben valores numerericos de lo contrario hace la misma pregunta hasta que agrege un valor valido.

    - Es necesario tener minimo 5 producto en el inventario de lo contrario si no tiene y escoge consultar, actualizar, eliminar, calcular y ver inventario le saldra un mensaje indicando que no tiene nada en el inventario. 


    Ejemplos 


        producList = 
              [{'productName': 'banano', 'price': 45, 'availableQuantity':54},
              {'productName': 'manzana', 'price': 4500, 'availableQuantity': 254},
              {'productName': 'pera', 'price': 6000, 'availableQuantity': 100},
              {'productName': 'mango', 'price': 6000, 'availableQuantity': 100},
              {'productName': 'arroz', 'price': 6000, 'availableQuantity': 100}]



              Menu
 
        1. Add product.
        2. Check product. 
        3. Update price.
        4. Delete product. 
        5. Total value in inventory.
        6. Show inventory. 
        7. Finish.


        Entrada = 1 -->  Please enter the name of the product number 6: arroz
                          The product name already exist !
                          Do you want to adde another product? yes, to consult. press any key to exit:  yes

                          Please enter the name of the product number 6: coca
                          Please enter the price of the product: 4556
                          Please enter the quintity of the product: 5464
                              product coca added


        Entrada = 2 -->       Please enter an option: 2
                            Please enter the name of the product to search: sandia
                            The product does not exist !
                            Do you want to consult another product? yes, to consult. press any key to exit: yes 
                            Please enter the name of the product to search: pera
                                    | Product: pera | Price: 6000 | Quantity: 100 |


        Entrada = 3 -->       Please enter an option: 3
                            Please enter the name of the product you want to change the price: arroz
                            Please enter the new price:  500000000
                            Update product 
                            | Producto: arroz | Prece: 500000000.0 Quantity: 100 |

    
        Entrada = 4 -->       Please enter an option: 4
                            Please enter the name of the product you want to delete: coca
                            Product removed!
                            Do you want to consult again? yes, to consult. press any key to exit: yes
                            Please enter the name of the product you want to delete: arroz
                            Product removed!

        
        
        Entada = 5 -->      Please enter an option: 5

                            Total inventory 2345430


        Entrada = 6 --> |                SHOW INVENTORY   05/12/25
                        |---------------------------------------------------------------------- |
                        |1. Product: banano    | Price: 45 | Quantity: 54  |Total:2430
                        |2. Product: manzana    | Price: 4500 | Quantity: 254  |Total:1143000
                        |3. Product: pera    | Price: 6000 | Quantity: 100  |Total:600000
                        |4. Product: mango    | Price: 6000 | Quantity: 100  |Total:600000

                        Total inventory 2345430

        
        
        Entrada = 6-->   Please enter an option: 7
                        Thanks for using the program