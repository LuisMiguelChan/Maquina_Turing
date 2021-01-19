def turing_M (estado = None,
              vacio = None,
              reglas = [],
              arreglo = [],
              fin = None,
              pos = 0):

    st = estado
    if not arreglo: arreglo = [vacio]
    if pos <0 : pos += len(arreglo)
    if pos >= len(arreglo) or pos < 0 : raise Error ("Se inicializa mal la posicion")
    
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(arreglo):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == fin: break
        if (st, arreglo[pos]) not in reglas: break
        
        (v1,dr,s1) = reglas [(st, arreglo[pos])]
        arreglo[pos]=v1
    
        if dr == 'left':
            if pos > 0: pos -= 1
            else: arreglo.insert(0, vacio)
        if dr == 'right':
            pos += 1
            if pos >= len(arreglo): arreglo.append(vacio)
        st = s1

def duplica():
    print("Maquina de turing")
    print("Duplicación")
    print("Ingrese los caracteres a duplicar ej: aaa : ")
    caracter = input("Ingrese los caracteres: ")
    print("Resultado:")
    turing_M (est = 's1',
                white = 'b',
                lista = list(caracter),
                final = 's4',
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
                            )
                )

def adicion():
    print()
    print("Maquina de turing")
    print("suma 1 al valor binario ej: entrada 111=7 salida 1000=8")
    caracter = input("Ingrese el numero en binario: ")
    print("Resultado:")
    turing_M (est = 's1',
                white = 'b',
                lista = list(caracter),
                final = 's3',
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
                            )
                )

while True:
    print("1 = duplicacion de caracteres")
    print("2 = suma un 1 a un binario")
    print("0 = salir")
    resp = int(input("Agregue una respuesta: "))
    if resp == 1:
        duplica()
    if resp == 2:
        adicion()
    if resp == 0:
        break