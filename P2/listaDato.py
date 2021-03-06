from dato import dato
class ListaDato:
    def __init__(self):
        self.inicio = None

    def insertar(self,nombreL, x, y, datoG,patron):
        nuevo = dato(nombreL, x,y,datoG,patron)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

        #mostrar
   
    def mostrarD(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '  NOMBREL: ' +str(tmp.nombreL)+ '. X: ' + str(tmp.x)  + ', Y: ' + str(tmp.y) + ', valor: '+ str(tmp.dato)+
                  ' Patron Correspondiente: '+str(tmp.patron))
            contador += 1
            tmp = tmp.siguiente
            
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

        #busqueda y retorno
    
    def getNodo(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.x) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None

    def getV(self, x,y):
        tmp = self.inicio
        while tmp is not None:
            if tmp.x == x and tmp.y == y:
                return tmp.dato
            tmp = tmp.siguiente
        return None
    
    def mostrarPor(self, nombreL):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombreL == nombreL:
                print('ID : ' +str.lower(tmp.nombreL)+'Posición de X: ' +str.lower(tmp.x)+' Posición de Y: ' +str.lower(tmp.y)+' # Patrón: ' +str.lower(tmp.patron))
            tmp = tmp.siguiente
        return None

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

    def busquedaPatron(self, x, y):
        tmp = self.inicio
        while True:
            if tmp.x == x and tmp.y == y:
                return tmp.patron
            if tmp.siguiente == None:
                break
            else: 
                tmp = tmp.siguiente
        return None  

    def rId(self, x, y):
        tmp = self.inicio
        while True:
            if tmp.x == x and tmp.y == y:
                return tmp.nombreL
            if tmp.siguiente == None:
                break
            else: 
                tmp = tmp.siguiente
        return None        
        