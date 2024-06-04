"""Un banco necesita para sus cajeros automáticos un programa que lea una
cantidad de dinero e imprima a cuántos billetes equivale, considerando que
existen billetes de $2000, $1000, $500, $100. Desarrollar dicho
programa de tal forma que se minimice la cantidad de billetes entregados por el
cajero."""

def sacarPlata(importe):
    billetes2000 = importe // 2000
    importe = importe % 2000

    billetes1000 = importe // 1000
    importe = importe % 1000

    billetes500 = importe // 500
    importe = importe % 500

    billetes100 = importe // 100
    importe = importe % 100

    billetes50 = importe // 50
    importe = importe % 50

    billetes10 = importe // 10
    importe = importe % 10

    billetes5 = importe // 5

    billetes1 = importe % 5

    print("Se entregan: ",billetes2000, "de 2000 -", billetes1000, "de 1000 -", billetes500, "de 500 -", billetes100,"de 100 -",billetes50,"de 50 -",billetes10,"de 10 -",billetes5,"de 5 -",billetes1,"de 1")

def main():
    importedeDinero = int(input("Ingrese un importe de dinero: $"))
    sacarPlata(importedeDinero)

if __name__=='__main__':
    main()

