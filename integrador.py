import random
"""
CONSIGNA: 
El trabajo práctico permite aplicar conceptos teóricos en un entorno práctico. 
Se propone que cada equipo encuentre y diseñe una situación problemática.
Cada grupo será conformado por 4 personas.
En el desarrollo del TP tendrán que utilizar: 
* Estructuras básicas (secuencial – decisión – iteración) 
* Datos estructurados (Listas) – máximos/mínimos, búsqueda, ordenamiento
* Programación modular - funciones
* Manejos de datos al azar (random)
No se pueden utilizar: archivos, manejo de excepciones, diccionarios, tuplas, conjuntos, ciclos 
infinitos, ruptura de ciclos, programación orientada a objetos, cadena de caracteres (strings)

IDEA: CAJERO AUTOMÁTICO:
- Egreso de Dinero
- Informes en base a las operaciones

ALCANCE:

Una entidad bancaria nos ha encargado el desarrollo de un sistema de cajero automático, el mismo debe permitir egresos de sumas de dinero. Se identifica el cajero con un numero random. Se ingresa una tarjeta al sistema, que va a tener números aleatorios. El cajero tiene un monto fijo total que se va debitando conforme se hace cada extracción. Además, tiene una suma fija de billetes (de 2000, de 1000, de 500 y de 100) que entrega. Por cada extracción se optimizará qué billetes van a ser brindados. El sistema termina al ingresar -1 como monto de extracción y deberá informar:
•	Lista de transacciones que se hicieron en el día (✔)
•	Lista de transacciones que se hicieron en el día por tarjeta (ascendiente y sin duplicados de tarjeta) (✔)
•	Consulta de cantidad de extracciones por tarjeta (✔)
•	La transacción (monto mínimo) que se extrajo en el día (✔)
•	La tarjeta que extrajo el monto máximo (acumulado por tarjeta)
"""

# QUEDA PENDIENTE: algoritmos de búsqueda y ordenamiento de listas

# Condicion de fin (-1) (✔)
# Egresos múltiplos de 100 (✔)
# Cortar cuando el cajero llege a 0 (✔)
# Variables
billetes_valores = [2000, 1000, 500, 100]  # Valores de los billetes ($54000 con los billetes que tenemos) #(✔)
billetes_cantidades = [10, 20, 30, 40]  # Cantidades de cada billete #(✔)
numeroDeCajero = random.randint(0, 6) #(✔)
tarjetas = [] #(✔)
egresos = []
egresosAcumulados = [] 

def tarjetaRandom(tarjetaExiste, listaDeTarjetas):
    if tarjetaExiste:
        tarjetas.append(listaDeTarjetas[-1])
    else:
        numeroRandom = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        print("Su num de tarjeta es: ",numeroRandom)
        tarjetas.append(numeroRandom)
    return tarjetas

def informarTransaciones(listaDeTarjetas, listaDeEgresos):
    print("------------------------------")
    print("\tEGRESOS DEL DÍA")
    print("------------------------------")
    print("EGRESO\tTARJETAS")
    for i in range(len(listaDeEgresos)):
        print("$%d\tN° %s" %(listaDeEgresos[i], listaDeTarjetas[i]))
    if listaDeEgresos: #La transacción (monto mínimo) que se extrajo en el día
        minimo_egreso = min(listaDeEgresos)
        print("\nEl egreso mínimo del día es: $", minimo_egreso)
    else:
        print("\nNo hay egresos registrados.")
    
    contarExtraccionesPorTarjeta(listaDeTarjetas)

def contarExtraccionesPorTarjeta(listaDeTarjetas):
    tarjetas_unicas = []
    cantidades = []

    for tarjeta in listaDeTarjetas:
        if tarjeta in tarjetas_unicas:
            index = tarjetas_unicas.index(tarjeta)
            cantidades[index] += 1
        else:
            tarjetas_unicas.append(tarjeta)
            cantidades.append(1)

    print("\nCantidad de extracciones por tarjeta:")
    for i in range(len(tarjetas_unicas)):
        print("Tarjeta N° %s : %d extracciones" % (tarjetas_unicas[i], cantidades[i]))

def nuevoMovimiento(billetesValor, billetesCantidad, listaDeTarjetas, listaDeEgresos):
    continuar = True
    tarjetaExiste = True
    while continuar:
        consulta = int(input("""
                            ¿Desea realizar otro retiro?
                            1- SI
                            2- NO
                            -1 Salir
                            """))
        if consulta == -1:
            continuar = False
            print("Muchas gracias por elegirnos!")
            informarTransaciones(listaDeTarjetas, listaDeEgresos)
        elif consulta == 1:
            tarjetaRandom(tarjetaExiste, listaDeTarjetas)
            sacarPlata(billetesValor, billetesCantidad, listaDeTarjetas, listaDeEgresos)
            continuar = False
        elif consulta == 2:
            #Cuando el primer usario saca todo el dinero enseguida, se crea una 2da tarjeta
            #que no va a poder hacer egreso ya que total en el banco es 0
            tarjetaExiste = False
            print("""
                Muchas gracias por elegirnos! 
                Por favor, retire su tarjeta y deje pasar al siguiente usuario""")
            tarjetaRandom(tarjetaExiste, listaDeTarjetas)
            sacarPlata(billetesValor, billetesCantidad, listaDeTarjetas, listaDeEgresos)
            continuar = False
        else:
            print("Opción inválida, elija una opción correcta")

def sacarBilletes(index, importe, listaBilletes, listaCantidad):
    print("Hay ", listaCantidad[index], " billetes de ", listaBilletes[index])
    continuar = True
    totalFaltante = importe
    while listaCantidad[index] > 0 and continuar:
        if listaCantidad[index] == 0:
            print("No quedan más billetes de ", listaBilletes[index])
        else:
            billetes = importe // listaBilletes[index]
            cantidadDeBilletes = 0

            if billetes > listaCantidad[index]:
                cantidadDeBilletes = listaCantidad[index]
            else:
                cantidadDeBilletes = billetes
            
            listaCantidad[index] -= cantidadDeBilletes
            totalFaltante = importe - (cantidadDeBilletes * listaBilletes[index])
            continuar = False
            print("Se entregan: ", cantidadDeBilletes, " billetes de ", listaBilletes[index])
    return totalFaltante

def sacarPlata(billetesValor, billetesCantidad, listaDeTarjetas, listaDeEgresos):
    total = cantidaEnCajero(billetesValor, billetesCantidad)

    if total > 0:
        montoEgreso = int(input("Ingrese un importe de dinero a retirar: $"))
        while montoEgreso % 100 != 0:
            print("El cajero solo admite egresos múltiplos de 100")
            montoEgreso = int(input("Ingrese un importe de dinero a retirar: $"))

        while total < montoEgreso and total > 0:
            print("El monto supera la cantidad disponible en el cajero")
            montoEgreso = int(input("Ingrese un nuevo importe de dinero a retirar: $"))

        egresos.append(montoEgreso)
        for i in range(len(billetesCantidad)):
            if montoEgreso > 0:
                montoEgreso = sacarBilletes(i, montoEgreso, billetesValor, billetesCantidad)
        nuevoMovimiento(billetesValor, billetesCantidad, listaDeTarjetas, listaDeEgresos)
    else:
        print("El cajero ya no tiene dinero, muchas gracias por elegirnos!")
        informarTransaciones(listaDeTarjetas, listaDeEgresos)
        return

def cantidaEnCajero(billetesValor,billetesCantidad):
    cantidadTotal = 0
    for i in range(len(billetesCantidad)):
        cantidadTotal += billetesCantidad[i] * billetesValor[i]
    return cantidadTotal

def main(): # Funcion principal
    tarjetaExiste = False
    print("""
*******************************

Cajero Automático "MMMC" 💰💰💰

*******************************
""")
    print("Número de Cajero: #", numeroDeCajero)
    tarjetaRandom(tarjetaExiste, tarjetas)
    sacarPlata(billetes_valores, billetes_cantidades, tarjetas, egresos)

if __name__=='__main__': # Entry Point
    main()