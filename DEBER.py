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
        mod=a%b
        print("El resultado de la suma es:{},el de la resta es:{}, el de la multiplicación es:{}, el de la division es:{} y el modulo es:{}".format(suma,resta,multi,div,mod))
        
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
            venta=input("Desea ingresar mas venta").upper()
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
            con=input("Desea ingresar mas notas").upper()
        pro=acu/cont
        if pro>=7:
            print("El alumno esta aprobado")
        elif pro>=5:
            print(("El alumno esta en remedial"))
        else:
            print("El alumno esta reprobado")

    def trabajo_y_mayor(self):
        hora=int(input("Ingresar el numero de horas trabajadas por el empleado"))
        valor=float(input("Ingresar el valor de pago por cada hora"))
        hoex=hora-40
        tt=0
        if hora>40:
            if hoex>8:
                ho1=hoex-8
                tt=(valor*2*8)+(valor*3*ho1)
            else:
                tt=valor*2*hora
        else:
            tt=valor*hora
        print("El trabajador trabajo:{} de horas, cada hora es pagada con un valor de:{}, por lo tanto su pago es de:{}".format(hora,valor,tt))
        print("Ejercicio de mayor numero")
        a=int(input("Ingresar 1 valor"))
        b=int(input("Ingresar 2 valor"))
        c=int(input("Ingresar 3 valor"))
        if a>b and a>c:
            print("El primer valor ingresado es el mayor")
        elif b>c:
            print("El segundo valor ingresado es el mayor")
        elif a==b==c:
            print("Los tres valores ingresados son iguales")
        else:
            print("El tercer valor ingresado es el mayor")

    def conMulti(self):
        num=int(input("Ingresar un valor entero para la accion del 1 al 3"))
        con=int(input("Ingresar un numero "))
        if num==1:
            p=100*con
            print("La accion:{}, hace que el valor constante se multiple con el segun valor ingresado por lo tanto la respuesta es:{}".format(num,p))
        elif num==2:
            p = 100 ** num
            print("La accion:{}, hace que el valor constante se eleve con el segun valor ingresado por lo tanto la respuesta es:{}".format(num,p))
        elif num==3:
            p=100/num
            print("La accion:{}, hace que el valor constante se divida con el segun valor ingresado por lo tanto la respuesta es:{}".format(num,p))
        else:
            p=0
            print("No realiza ninguna accion por lo tanto su valor es reemplazo con",p)
        
    def ciForyWhi(self):
        n1=int(input("Ingresar un numero entero tope "))
        sum=0
        for i in range(n1):
            sum=sum+i
        print("La suma de:{} da un total de:{}".format(n1,sum))

        print("Ciclo while")
        n2=int(input("Ingresar un numero entero"))
        t1=0
        pro=1
        c=1
        while c<=n2:
            t1=t1+c
            pro=pro*c
            c+=1
        print("El  total de la suma de:{} es de:{} y el de los productos es de:{}".format(n2,t1,pro))

    def arreglo(self):
        A = int(input(u"Ingrese el tamaño de los arreglos"))
        B = []
        C = []
        for i in range(0, A):
            B.append(input("Ingrese nombre de las personas"))
        print("El arreglo de los nombres queda:",B)
        for j in range(0, A):
            C.append(len(B[j]))
        print("La longitud de cada arreglo es de:" ,C)
        
        
objclases=Clases()
objclases.Operaciones()
objclases.Oper_rela()
objclases.Circulo()
objclases.Secuencia()
objclases.Secu_mas()
objclases.Alumno()
objclases.trabajo_y_mayor()
objclases.conMulti()
objclases.ciForyWhi()
objclases.arreglo()

