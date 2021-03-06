from nodoMR import datoR
class ListaGrupo:
    def __init__(self):
        self.inicio = None

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
        if self.inicio is None: 
            return True

    def mostrarD(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '  ID_GRUPO: ' +str(tmp.noG)+ ', Fila_Perteneciente: ' + str(tmp.fila))
            contador += 1
            tmp = tmp.siguiente

    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

    def enGrupo(self,fila):
        tmp = self.inicio
        while tmp is not None:
            if tmp.fila == fila: 
                return True
            tmp = tmp.siguiente
        return False

    def ultimoN(self):
        tmp = self.inicio
        while tmp.siguiente is not None:           
            tmp = tmp.siguiente
        return tmp.noG

    def contarID(self,valor): 
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            if tmp.noG == valor: 
                cont += 1
            tmp = tmp.siguiente
        return cont

    def getFila(self,valor):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            if tmp.noG == valor: 
             return tmp.fila
            tmp = tmp.siguiente
        return cont       

    def getFilaIgnore(self,grupo,ignorar): 
        tmp = self.inicio
        while tmp is not None: 
            if tmp.noG == grupo: 
                if ignorar == 0: 
                    return tmp.fila
                else: 
                    ignorar -= 1
            tmp = tmp.siguiente
      

    
        