from xml.dom import minidom
import xml.etree.ElementTree as ET
from listaCircular import ListaCircular
from Matrices import Matriz
from listaDato import ListaDato

data = ListaCircular()
nombre = ""

def pedirOpcion ():
  correcto = False
  opcion = 0
  while (not correcto):
    try:
     opcion = int(input( "Menu: \n 1) Cargar Archivo: \n 2)Procesar archivo \n 3) Escribir archivo de salida \n 4) Mostrar datos del estudiante \n 5) Generar gráfica \n 6) Salir \n-->"))
     correcto = True
    except ValueError:
      print('Error, introduce un numero entero')
  return opcion

def menu(): 
    opcion = 0
    Salir = False
    while not Salir: 
        opcion = pedirOpcion()
        #*********************************************************************************************
        #************************OPCION 1 DEL MENU()*********************************************
        if opcion == 1: 
            ruta = input("Ingrese la ruta del archivo xml a utilizar " + '\n --->')
            tree = ET.parse(ruta)
            root = tree.getroot()
            id_matriz = 0
            #***COMPROBAR EL TAMAÑO DE LA MATRIZ SE ADECUADO 
            for elemen1 in root: 
                n = int(elemen1.attrib['n'])
                m = int(elemen1.attrib['m'] )
                nombreL = str(elemen1.attrib['nombre'])
                datos = ListaDato()
                for sub1 in elemen1: 
                  if ((int(sub1.attrib['x'])-1) > n ) or ((int(sub1.attrib['y'])-1) > m): 
                      print( "Error en la matriz: "+nombreL+  " INCORRECTO TAMAÑO EN X: "+str((sub1.attrib['x'])) + " Y: "+str(sub1.attrib['y']) + " POR LO TANTO NO SERÁ AGREGADO" )
                      tamaño_correcto = False
                  else: 
                       if (int(sub1.text)) != 0:
                         patron = 1
                       else: 
                         patron = 0                     
                       datos.insertar(nombreL,
                              int(sub1.attrib['x']),
                              int(sub1.attrib['y']),
                              int(sub1.text),
                              patron)                       
                       tamaño_correcto = True  
                data.insertar(id_matriz,
                              elemen1.attrib['nombre'],
                              int(elemen1.attrib['n']) ,
                              int(elemen1.attrib['m'])
                              )
                id_matriz += 1
                clase_ma = data.getNodo(str.lower(elemen1.attrib['nombre']))
                print(clase_ma)
                clase_ma.dato = datos                                              
            data.mostrar()
       #FIN DE LA OPCION1  
        elif opcion == 3: 
            print("Opción 3: \n")
            data.diagrama()

        elif opcion == 6: 
            Salir = True
        #fin de la opcion6: 

if __name__ == "__main__":
  menu()

                
                
                
                    





