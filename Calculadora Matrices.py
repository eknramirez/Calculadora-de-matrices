
# coding: utf-8

# In[17]:


print("Bienvenido a la calculadora de Matrices.\n")
print ("Escriba 9 si desea abrir su Calculadora\n7 si no Desea hacer nada")
Respuesta=int(input("Ingrese su Opcion para abrir la calculadora\n"))
if Respuesta==9:
    print ("ingresaste a la calculadora\n\nBienvenido")
    print ("Matrices para Clase Inteligencia Artificial")
    print("Ejercicio propuesto para clase de inteligencia artificial por parte del Ingeniero Carlos Londoño\n")
    print (" ")
    print ("MENU.\nPuedes elegir la operacion que desees Realizar.\n ")
    print ("[1] Suma de matrices\n[2] Restas de matrices\n[3] Multiplicacion de Matrices\n[4] Multiplicacion por un Numero\n[5] Transpuesta de una Matriz\n")
    print (" ")
#Modelo de la Matriz
    print ("Modelo de la Matriz")
    print ("Esta es la matriz en la cual ingresaras tus Datos: ")
    print ("")
    print ("[Fila1Colum1 __ Fila1Colum2 __ Fila1Colum3]")
    print ("[Fila2Colum1 __ Fila2Colum2 __ Fila2Colum3]")
    print ("[Fila3Colum1 __ Fila3Colum2 __ Fila3Colum3]")
    print (" ")
    print ("Esta es una Matriz de tipo 3x3.\nTres filas por tres columnas.\n")
# Forma para pedir los datos de la matriz suma  utilizando If.
    Opcion=int(input("Ingrese Opcion: ")) # si esta linea no tiene el int(input) si no loslo imput no valida el if
    if Opcion==1:
        print ("Ingrese los datos para  la Matriz Numero 1: ")
        print ("")
        VF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        VF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        VF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        VF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        VF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        VF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        VF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        VF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        VF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
    #vizualizar la matriz A en la pantalla
        print ("La matriz que ingresaste es la siguiente")
        print (" ")
        print ("MATRIZ # 1")
        print ("")
        print ("[    ", VF1C1, VF1C2, VF1C3, "    ]")
        print ("[    ", VF2C1, VF2C2, VF2C3, "    ]")
        print ("[    ", VF3C1, VF3C2, VF3C3, "    ]")
        print ("")
    # Pedir informacion de la matriz numero 2

        print (" Porfavor Ingrese los Valores para la  Matriz Numero 2: ")
        print ("")
        TF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        TF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        TF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        TF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        TF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        TF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        TF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        TF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        TF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
    # Vizualizar la matriz b con sus Valores
        print ("La matriz que ingresaste esla siguiente")
        print (" ")
        print ("MATRIZ Numero 2: ")
        print ("")
        print ("[", TF1C1, TF1C2, TF1C3, "]")
        print ("[", TF2C1, TF2C2, TF2C3, "]")
        print ("[", TF3C1, TF3C2, TF3C3, "]")
        print ("")

     #Operacion Suma de las dos matrices
        K1C1 = VF1C1 + TF1C1
        K1C2 = VF1C2 + TF1C2
        K1C3 = VF1C3 + TF1C3
        K2C1 = VF2C1 + TF2C1
        K2C2 = VF2C2 + TF2C2
        K2C3 = VF2C3 + TF2C3
        K3C1 = VF3C1 + TF3C1
        K3C2 = VF3C2 + TF3C2
        K3C3 = VF3C3 + TF3C3
        print("\n")

#Visualizacion Matriz "Resultado"
        print ("Resultado de la Suma de Matrices.")
        print ("")
        print ("[", K1C1, K1C2, K1C3, "]")
        print ("[", K2C1, K2C2, K2C3, "]")
        print ("[", K3C1, K3C2, K3C3, "]")
    #Resta de matrices
    if Opcion==2:
        print ("Has escogido Resta de matrices Cuadradas de 3X3")
        print ("Ingrese los datos para  la Matriz Numero 1: ")
        print ("")
        VF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        VF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        VF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        VF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        VF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        VF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        VF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        VF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        VF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
        print("\n")
    #vizualizar la matriz Numero 1 en la pantalla
        print ("La matriz que ingresaste es la siguiente")
        print (" ")
        print ("MATRIZ # 1")
        print ("")
        print ("[" , VF1C1, VF1C2, VF1C3,  "]")
        print ("[" , VF2C1, VF2C2, VF2C3,  "]")
        print ("[" , VF3C1, VF3C2, VF3C3,  "]")
        print ("")
    # Pedir informacion de la matriz b

        print (" Porfavor Ingrese los Valores para la  Matriz Numero 2: ")
        print ("")
        TF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        TF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        TF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        TF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        TF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        TF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        TF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        TF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        TF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
    # Vizualizar la matriz b con sus Valores
        print ("La matriz que ingresaste esla siguiente")
        print (" ")
        print ("Matriz Numero 2: ")
        print ("")
        print ("[", TF1C1, TF1C2, TF1C3, "]")
        print ("[", TF2C1, TF2C2, TF2C3, "]")
        print ("[", TF3C1, TF3C2, TF3C3, "]")
        print ("")

     #Operacion Resta de Matrices
        K1C1 = VF1C1 - TF1C1
        K1C2 = VF1C2 - TF1C2
        K1C3 = VF1C3 - TF1C3
        K2C1 = VF2C1 - TF2C1
        K2C2 = VF2C2 - TF2C2
        K2C3 = VF2C3 - TF2C3
        K3C1 = VF3C1 - TF3C1
        K3C2 = VF3C2 - TF3C2
        K3C3 = VF3C3 - TF3C3

#Visualizacion Matriz "Resultado"
        print ("El Resultado de la resta de Matrices de 3x3 es: ")
        print ("")
        print ("[", K1C1, K1C2, K1C3, "]")
        print ("[", K2C1, K2C2, K2C3, "]")
        print ("[", K3C1, K3C2, K3C3, "]")
    # multiplicacion de 2 matrices 3x3--------------------------------------
    if Opcion==3:
        print ("Multiplicacion de Matrices\n")
        print ("Ingrese la matriz que deseas multiplicar")

        print ("Ingrese los datos para  la Matriz Numero 1: ")
        print ("")
        VF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        VF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        VF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        VF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        VF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        VF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        VF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        VF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        VF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
        print("\n")

        print (" Porfavor Ingrese los Valores para la  Matriz Numero 2: ")
        print ("")
        TF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        TF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        TF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        TF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        TF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        TF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        TF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        TF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        TF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
#Falta el resultado de la multiplicacion

#Operacion Multiplicacion
        K1C1= (VF1C1 * TF1C1) + (VF1C2 * TF2C1) + ( VF1C3 * TF3C1)
        K1C2= (VF1C1 * TF1C2) + (VF1C2 * TF2C2) + ( VF1C3 * TF3C2)
        K1C3= (VF1C1 * TF1C3) + (VF1C2 * TF2C3) + ( VF1C3 * TF3C3)
        K2C1= (VF2C1 * TF1C1) + (VF2C2 * TF2C1) + ( VF2C3 * TF3C1)
        K2C2= (VF2C1 * TF1C2) + (VF2C2 * TF2C2) + ( VF2C3 * TF3C2)
        K2C3= (VF2C1 * TF1C3) + (VF2C2 * TF2C3) + ( VF2C3 * TF3C3)
        K3C1= (VF3C1 * TF1C1) + (VF3C2 * TF2C1) + ( VF3C3 * TF3C1)
        K3C2= (VF3C1 * TF1C2) + (VF3C2 * TF2C2) + ( VF3C3 * TF3C2)
        K3C3= (VF3C1 * TF1C3) + (VF3C2 * TF2C3) + ( VF3C3 * TF3C3)

#Visualizacion Matriz "Resultado"
        print ("Matriz de Resultado")
        print ("\n")
        print ("[", K1C1, K1C2, K1C3, "]")
        print ("[", K2C1, K2C2, K2C3, "]")
        print ("[", K3C1, K3C2, K3C3, "]")
        print ("")
        print ("")
#Multiplicacion de un escalar por una matriz.
    if Opcion==4:
        print ("Multiplicacion de una Escalar por una matriz\n")
        print ("Ingrese la matriz que deseas multiplicar")

        print ("Ingrese los datos para  la Matriz Numero 1: ")
        print ("")
        VF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        VF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        VF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        VF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        VF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        VF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        VF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        VF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        VF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
        print("\n")

        print ("Ingresa el Escalar")

        Escalar=int(input("Ingrese el numero Escalar: "))

    #Visualizacion Matriz que vamos a multiplicar
        print ("Aqui te Mostramos la Matriz que ingresaste: ")
        print (" ")
        print ("[", VF1C1, VF1C2, VF1C3, "]")
        print ("[", VF2C1, VF2C2, VF2C3, "]")
        print ("[", VF3C1, VF3C2, VF3C3, "]")
        print (" ")
        print ("este es el Escalar")
        print (Escalar)      

#Operacion Multiplicacion por numero

        RESULTF1C1 = Escalar * VF1C1
        RESULTF1C2 = Escalar * VF1C2
        RESULTF1C3 = Escalar * VF1C3
        RESULTF2C1 = Escalar * VF2C1
        RESULTF2C2 = Escalar * VF2C2
        RESULTF2C3 = Escalar * VF2C3
        RESULTF3C1 = Escalar * VF3C1
        RESULTF3C2 = Escalar * VF3C2
        RESULTF3C3 = Escalar * VF3C3

#Visualizacion Matriz "Resultado"
        print ("El Resultado de la multiplicacion es: ")
        print (" ")
        print ("[", RESULTF1C1, RESULTF1C2, RESULTF1C3, "]")
        print ("[", RESULTF2C1, RESULTF2C2, RESULTF2C3, "]")
        print ("[", RESULTF3C1, RESULTF3C2, RESULTF3C3, "]")
        print (" ")
#Operacion la Transpuesta de una matriz.
    if Opcion==5:
        print ("Sacar la Transpuesta a una matriz\n")

        print ("Ingresa la Matriz a la que quieres Sacar la transpuesta\n")

        VF1C1=int(input("Ingrese el valor de Fila1 y Columna 1:"))
        VF1C2=int(input("Ingrese el valor de Fila1 y Columna2: "))
        VF1C3=int(input("Ingrese el valor de Fila1 y Columna3: "))
        VF2C1=int(input("Ingrese el valor de Fila2 y Columna1: "))
        VF2C2=int(input("Ingrese el valor de Fila2 y Colunma2: "))
        VF2C3=int(input("Ingrese el valor de Fila2 y Columna3: "))
        VF3C1=int(input("Ingrese el valor de Fila3 y Columna1: "))
        VF3C2=int(input("Ingrese el valor de Fila3 y Columna2: "))
        VF3C3=int(input("Ingrese el valor de Fila3 y Columna3: "))
        print("\n")


        print ("Aqui te Mostramos la Matriz que ingresaste: ")
        print (" ")
        print ("[", VF1C1, VF1C2, VF1C3, "]")
        print ("[", VF2C1, VF2C2, VF2C3, "]")
        print ("[", VF3C1, VF3C2, VF3C3, "]")
        print (" \nSu Transpuesta es\n:")
        
        

        print ("[", VF1C1, VF2C1, VF3C1, "]")
        print ("[", VF1C2, VF2C2, VF3C2, "]")
        print ("[", VF1C3, VF2C3, VF3C3, "]")
        print (" ")
if Respuesta==7:
    print("No vas a Realizar Ninguna operacion")
    

