from nodoMR import datoR
class ListaGrupo:
    def __init__(self):
        self.inicio = None

        #insercion
    def insertar(self,noG,fila):
        nuevo = datoR(noG,fila)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

        #mostrar
    
    def estaVacia(self): 
        tmp = self.inicio
        if self.inicio is None: 
            return True
        tmp = tmp.siguiente

    def mostrarD(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            #print(str(contador) + '  NOMBREL: ' +str(tmp.nombreL)+ '. X: ' + str(tmp.x)  + ', Y: ' + str(tmp.y) + ', valor: '+ str(tmp.dato))
            contador += 1
            tmp = tmp.siguiente
            

            #tamanio
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

    
        