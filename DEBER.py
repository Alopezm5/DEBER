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
        
    def Oper_rela(self):
        i=float(input("Ingresar primer valor"))
        j=float(input("Ingresar segudo valor"))
        k=float(input("Ingresar tercer valor"))
        if i<=j:
            print("El primer valor es menor o igual al segundo")
        elif(i+j)>k:
            print("la suma de los dos primeros valores ingresados son mayor al tercer valor")
        elif k<i:
            print("El ultimo valor es menor al segundo")
        elif (j+k)>(i+5):
            print("La suma de los dos ultimos valores ingresados es mayor al primer valor sumado 5")
        else:
            print("No aplica ninguna de las condiciones")
     
    def Circulo(self):
        print("Calculo area de un circulo")
        r=float(input("Ingresar radio del circulo"))
        pi=3.1416
        ar=pi*r
        print("El area del circulo es:",ar)
        
objclases=Clases()
objclases.Operaciones()
objclases.Oper_rela()
objclases.Circulo()
