from nodoMRE import datoRE
class lMatrizR:
    def __init__(self):
        self.inicio = None

        #insercion
   
    def insertar(self,nombre,x,y,dato):
        nuevo = datoRE(nombre,x,y,dato)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def estaVacia(self): 
        if self.inicio is None: 
         return True

    def mostrarD(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '  ID_GRUPO: ' +str(tmp.id)+ ', X: ' + str(tmp.x)+ ', Y: ' + str(tmp.y)+ ', Dato: ' + str(tmp.dato))
            contador += 1
            tmp = tmp.siguiente

    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

    def reload(self,x,y,nValor): 
        tmp = self.inicio
        while tmp is not None: 
            if tmp.x == x and tmp.y == y: 
                print("valor anterior:", tmp.dato, "\tnuevo valor:", nValor)
                tmp.dato = nValor
                break
            else: 
                tmp = tmp.siguiente
                
    def busquedaPos(self, x, y):
        tmp = self.inicio
        while True:
            if tmp.x == x and tmp.y == y:
                return tmp.dato
            if tmp.siguiente == None:
                break
            else: 
                tmp = tmp.siguiente
        return None       