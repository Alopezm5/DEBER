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
        
    def Secu_mas(self):
        com=int(input("Ingresar valor de comision"))
        sueldo=float(input("Ingrese sueldo base"))
        venta="SI"
        acu=0
        while venta=="SI":
            val=float(input("Ingresar valor de la venta"))
            acu=acu+val
            venta=input("Desea ingresar mas venta")
        tt=acu*(com/100)
        tot=sueldo+tt
        print("El empleado gano un total de:{} de comisiones, por lo tanto su sueldo este mes es de:{}".format(tt,tot))

    def Alumno(self):
        con="SI"
        acu=0
        cont=0
        while con=="SI":
            nota=float(input("Ingresar nota del alumno"))
            if nota>0 and nota<=10:
                pass
            else:
                nota=float(input("Ingrese nota en el rango 0-10"))
            acu=acu+nota
            cont=+1
            con=input("Desea ingresar mas notas")
        pro=acu/cont
        if pro>=7:
            print("El alumno esta aprobado")
        elif pro>=5:
            print(("El alumno esta en remedial"))
        else:
            print("El alumno esta reprobado")

        
objclases=Clases()
objclases.Operaciones()
objclases.Oper_rela()
objclases.Circulo()
objclases.Secuencia()
objclases.Secu_mas()
objclases.Alumno()
