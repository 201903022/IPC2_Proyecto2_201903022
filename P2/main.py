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
     opcion = int(input( " \n >>>>>>>>>>>>  Menu: <<<<<<<<<<<< \n 1) Cargar Archivo: \n 2)Procesar archivo \n 3) Escribir archivo de salida \n 4) Mostrar datos del estudiante \n 5) Generar gráfica \n 6) Salir \n \n Ingrese una opción \n>>>"))
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
            print("********NOTA ******** ")
            print("SI UN VALOR DE X ES MAYOR QUE N, O Y MAYOR QUE M NO SERÁ GUARDADO")
            ruta = input("Ingrese la ruta del archivo xml a utilizar " + '\n --->')
            
            #try: 
              #rutal = ""
              #print("")
              #with open(rutal,'r') as f: 
                #return True
            #except FileNotFoundError as e:
              #return False
            #except IOError as e: 
              #return False 
            
            tree = ET.parse(ruta)
            root = tree.getroot()
            
            id_matriz = 0
            #***COMPROBAR EL TAMAÑO DE LA MATRIZ SE ADECUADO 
            for elemen1 in root: 
                n = int(elemen1.attrib['n'])
                m = int(elemen1.attrib['m'] )
                nombreL = str(elemen1.attrib['nombre'])
                datos = ListaDato()
                idDato = 0
                for sub1 in elemen1: 
                  if ((int(sub1.attrib['x'])-1) > n ) or ((int(sub1.attrib['y'])-1) > m): 
                      print( "Error en la matriz: "+nombreL+  " INCORRECTO TAMAÑO EN X: "+str((sub1.attrib['x'])) + " Y: "+str(sub1.attrib['y']) + " POR LO TANTO NO SERÁ AGREGADO" )
                      tamaño_correcto = False
                  else: 
                       if (int(sub1.text)) != 0:
                         patron = 1
                       else: 
                         patron = 0                     
                       datos.insertar(idDato,
                              int(sub1.attrib['x']),
                              int(sub1.attrib['y']),
                              int(sub1.text),
                              patron)  
                       idDato += 1                     
                       tamaño_correcto = True  
                data.insertar(id_matriz,
                              elemen1.attrib['nombre'],
                              int(elemen1.attrib['n']) ,
                              int(elemen1.attrib['m'])
                              )
                id_matriz += 1
                clase_ma = data.getNodo(str.lower(elemen1.attrib['nombre']))
                clase_ma.dato = datos                                              
            data.mostrar()
       #FIN DE LA OPCION1  
        elif opcion == 2:
           print("******Opcion 2******") 
           print("Buscando patrones iguales")
           data.patrones()
           print("Empieza la suma de patrones: ")
           data.sumarA()           
        #***********************************************************************************   
        elif    opcion == 3: 
          ruta = input("Ingrese la ruta exacta: \n >>>")
          try: 
            
            x = ruta.split(".")
            if data.Rvacia(): 
             print("No ha seleccionado la opcón 2 por lo tanto no se puede realizar la opción3")
            else:
              if x[1] == "xml":
                data.write(ruta)
                print("Se escribió correctamente ")
              else: 
                print("Solo direcciones .xml")          
          except FileNotFoundError as e: 
            print("Hubo un error en el sistema")
          except IOError as e: 
            print(" ", e)
          
          
        elif opcion == 4: 
          print("Jonathán Alexander Sánchez Barrios")
          print(" 201903022")
          print("Introducción a la Programación 2 seccón D")
          print("Ingeniería en Ciencias y Sistemas")
          print("Primer Semestre 2021")

        elif opcion == 5: 
            print("Opción 3: \n")
            if data.getSize()>1: 
              print("Opciones según matriz: ")
              data.mostrarI()
              opcionA = int(input("Ingrese la opción de matriz que quiere visualizar: \n >>>")) - 1
              data.graficar(opcionA)
            else: 
             data.graficar1()
             
             
        elif opcion == 6: 
            Salir = True
        #fin de la opcion6: 

if __name__ == "__main__":
  menu()

                
                
                
                    





