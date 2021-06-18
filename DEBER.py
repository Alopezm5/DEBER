class Clases:
    def __init__(self):
        pass

    def Operaciones(self):
        a=float(input("Ingresar primer valor"))
        b=float(input("Ingresar segudo valor"))
        suma=a+b
        resta=a-b
        multi=a*b
        div=a/b
        diven=a//b
        mod=a%b
        print("El resultado de la suma es:{},el de la resta es:{}, el de la multiplicación es:{}, el de la division es:{}".format(suma,resta,multi,div))

objclases=Clases()
objclases.Operaciones()
