#definicion del metodo
def turing_M (estado = None,#Estado inicial
              vacio = None,#Vacio
              reglas = [],#Reglas del automata
              arreglo = [],#Valores de entrada
              fin = None,#Estado final
              pos = 0):#Posicion

    st = estado
    if not arreglo: arreglo = [vacio]
    if pos <0 : pos += len(arreglo)#Movimiento de la posicion en las entradas
    if pos >= len(arreglo) or pos < 0 : raise Error ("Se inicializa mal la posicion") #Error cuando la posicion inicia mal
    
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas) #Se evalua cada regla del automata
    
    while True:
        print (st, '\t', end=" ")#Impresion con tabulacion
        for i, v in enumerate(arreglo):#Lectura de cada caracter de la lista
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == fin: break#Cuando la posicion llega al estado final termina
        if (st, arreglo[pos]) not in reglas: break#Termina de revisar las reglas
        
        #Valida las reglas dependiendo la posicion del puntero
        (v1,dr,s1) = reglas [(st, arreglo[pos])]
        arreglo[pos]=v1

        #Se define como se debe posicionar el puntero
        #Ya sea un movimiento por la izquierda o la derecha
        if dr == 'left':
            if pos > 0: pos -= 1
            else: arreglo.insert(0, vacio)
        if dr == 'right':
            pos += 1
            if pos >= len(arreglo): arreglo.append(vacio)
        st = s1

#Definicion del metodo
def duplica():
    print("Maquina de turing")
    print("Duplicación")
    print("Ingrese los caracteres a duplicar ej: aaa : ")
    caracter = input("Ingrese los caracteres: ")
    print("Resultado:")
    #Llamada al metodo
    turing_M (estado = 's1',#Estado incial
                vacio = 'b',#Caracter del vacio
                arreglo = list(caracter),#Valores de entrada
                fin = 's4',#Estado final
                reglas = map(tuple,
                              [
                            "s1 a 1 right s1".split(),
                            "s1 b b left s2".split(),
                            "s2 a a left s2".split(),
                            "s2 1 a right s3".split(),
                            "s3 a a right s3".split(),
                            "s3 b a left s2".split(),
                            "s2 b b right s4".split(),
                            ]   
                            )#Reglas del automata
                )

#Definicion del metodo
def adicion():
    print()
    print("Maquina de turing")
    print("suma 1 al valor binario ej: entrada 111=7 salida 1000=8")
    caracter = input("Ingrese el numero en binario: ")
    print("Resultado:")
    #Llamada al metodo
    turing_M (estado = 's1',#Estado inicial
                vacio = 'b',#Caracter del vacio
                arreglo = list(caracter),#Valores de entrada
                fin = 's3',#Estado final
                reglas = map(tuple,
                            [
                            "s1 1 1 right s1".split(),
                            "s1 0 0 right s1".split(),
                            "s1 b b left s2".split(),
                            "s2 1 0 left s2".split(),
                            "s2 0 1 right s3".split(),
                            "s2 0 1 left s3".split(),
                            "s2 b 1 left  s3".split(),
                            ]   
                            )#Reglas del automata
                )

while True:
    print("1 = duplicacion de caracteres")
    print("2 = suma un 1 a un binario")
    print("0 = salir")
    resp = int(input("Agregue una respuesta: "))#Entrada
    if resp == 1:
        duplica()#Llamada al metodo
    if resp == 2:
        adicion()#Llamada al metodo
    if resp == 0:
        break