import os
os.system("cls")

Menu = """
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
"""

Butacas = """
+------------------------------+
|          ESCENARIO           |
+------------------------------+
|1  2  3  4  5  6  7  8  9  10 |
|11 12 13 14 15 16 17 18 19 20 |
|21 22 23 24 25 26 27 28 29 30 |
|31 32 33 34 35 36 37 38 39 40 |
|41 42 43 44 45 46 47 48 49 50 |
|51 52 53 54 55 56 57 58 59 60 |
|61 62 63 64 65 66 67 68 69 70 |
|71 72 73 74 75 76 77 78 79 80 |
|81 82 83 84 85 86 87 88 89 90 |
|91 92 93 94 95 96 97 98 99 100|
+------------------------------+
"""

listaAsistentes = ['Seba','Alvaro','Nacho']
listaRut = ['12345678','43218765','98765432']
listaButacasPlat = [11,1,3,4]
listaButacasGold = [33]
listaButacasSilv = [60]

EndPlatinum = 0
Entradas = 0
def comprar_funcion():
    while True:
        asistentes = input("Escriba su nombre: ")
        if len(asistentes) >= 1:
            listaAsistentes.append(asistentes)
            break
        else:
            print("Introduzca un nombre valido")
    while True:
        RutAsistentes = input("Escriba su rut, sin digito verificador: ")
        if len(RutAsistentes) == 8:
            listaRut.append(RutAsistentes)
            break
        else:
            print("Introduzca un rut valido")
    while True:
        opc = int(input(f"""Eliga sus butacas, maximo 3 entradas. \n {Butacas} \n
        Los precios de las entradas son los siguientes:
        1.Platinum, $120.000 (Asientos del 1 al 20).
        2.Gold,     $80.000  (Asientos del 21 al 50).
        3.Silver,   $50.000  (Asientos del 51 al 100.
        Butacas Platinum en uso: {listaButacasPlat}
        Butacas Gold en uso: {listaButacasGold}
        Butacas Silver en uso: {listaButacasSilv}
        """))
        if opc >= 1 and opc <= 20:
            print("Butaca elegida correctamente!")
            listaButacasPlat.append(opc)
            break
            
        elif opc > 20 and opc <= 50:
                print("Butaca elegida correctamente!")
                listaButacasGold.append(opc)
                break
                
        elif opc > 50 and opc <= 100:
                print("Butaca elegida correctamente!")
                listaButacasSilv.append(opc)
                break
                
        else:
             print("Butaca no valida")

def funcion_ubicaciones():
     print("Opcion ubicaciones disponibles")
     print(Butacas)
     print(f""" Butacas Platinum en uso: {listaButacasPlat}
        Butacas Gold en uso: {listaButacasGold}
        Butacas Silver en uso: {listaButacasSilv}
        """)
     

def funcion_listado():
     print("Aqui esta el listado de asistentes por RUN, ordenados de menor a mayor")
     listaRut.sort()
     print(listaRut)

def funcion_ganancias():
     valorPlat = len(listaButacasPlat) * 120000
     ValorGold = len(listaButacasGold) * 80000
     valorSilver = len(listaButacasSilv) * 50000
     totalButacas = len(listaButacasPlat) + len(listaButacasGold) + len(listaButacasSilv)
     totalvalor = valorPlat + ValorGold + valorSilver
     print("+------------------+---------------+--------------+")
     print("|  Tipo de entrada |   Cantidad    |      Total   |")
     print("+------------------+---------------+--------------+")
     print(f"|Platinum $120.000 |{len(listaButacasPlat)}              |{valorPlat}        |")
     print("+------------------+---------------+--------------+")
     print(f"|Gold $80.000      |{len(listaButacasGold)}              |{ValorGold}         |")
     print("+------------------+---------------+--------------+")
     print(f"|Silver $50.000    |{len(listaButacasSilv)}              |{valorSilver}         |")
     print("+------------------+---------------+--------------+")
     print(f"|     TOTAL        |{totalButacas}              |{totalvalor}        |")
     print("+------------------+---------------+--------------+")






import datetime
hora = datetime.datetime.now()

Nombreyapellido = input("Hola, bienvenido al servicio de la productora Creativos.cl, su nombre y apellido: ")
while True:        
    opcMenu = int(input(Menu))
    if opcMenu == 1:
        comprar_funcion()
    elif opcMenu == 2:
         funcion_ubicaciones()
    elif opcMenu == 3:
         funcion_listado()
    elif opcMenu == 4:
         funcion_ganancias()
    elif opcMenu == 5:
         print(f"Gracias por ocupar el servicio {Nombreyapellido}, fecha de uso: {hora}")
         input("Enter para terminar")
         break
    else:
         print("Opcion no valida")
         




         

