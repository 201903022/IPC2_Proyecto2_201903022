from graphviz import Digraph
from dato import dato
from nodo import nodo

class ListaCircular: 
    def __init__(self): 
        self.primero = None
        self.last = None 
    def Vacia(self): 
        return self.primero == None
    
    def insertar(self,id,nombre,n,m): 
        nuevo  = nodo(id,nombre,n,m)        
        if self.primero is None: 
            self.primero = nuevo
        else: 
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo 
            nuevo.before = temporal

    def mostrar(self):
        tmp = self.primero
        contador = 1
        while tmp is not None:
            print('\n'+str(contador) + '. Nombre: ' + str(tmp.nombre)  + ', N: ' + str(tmp.n) + ', M: '+ str(tmp.m))
            tmp.dato.mostrarD()
            contador += 1
            tmp = tmp.siguiente
            

    def getNodo(self, valor):
        tmp = self.primero
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None
                      
    def addInicio(self,id,nombre,n,m): 
        if self.Vacia(): 
            self.primero = self.last = nodo(id,nombre,n,m)
            self.last.next = self.primero
        else : 
            aux = nodo(id,nombre,n,m)
            aux.next = self.primero
            self.primero = aux
            self.last.next = self.primero
 

    def addLast(self,id,nombre,n,m): 
        if self.Vacia(): 
            self.primero = self.last = nodo(id,nombre,n,m)
            self.last.next = self.primero
        else: 
            aux = self.last
            self.last = aux.next = nodo(id,nombre,n,m)
            self.last.next = self.primero

    def delete_node(self,key): 
        curr = self.primero
        prev = None
        while curr and curr.nombre != key: 
            prev = curr
            curr = curr.siguiente
        if prev is None: 
            self.primero = curr.siguiente
        elif curr: 
            prev.siguiente = curr.siguiente
            curr.siguiente = None

    def removeL(self): 
        if self.Vacia(): 
            print("Lista Vacía")
        elif self.primero == self.last: 
          self.primero = self.last = None
        else: 
          aux = self.primero
          while aux.next != self.last: 
              aux = aux.next
          aux.next = self.primero
          self.last = aux
    def Recorrer(self): 
        aux = self.primero
        while aux: 
            print(aux.data)
            aux = aux.next
            if aux == self.primero: 
                break
    def getLast(self): 
        return self.last
    def diagrama(self): 
        tmp = self.primero
        while tmp is not None:
            dot = Digraph('G',filename='hello.gv' ) 
            dot.node('A','Matrices')
            dot.node('B',tmp.nombre)
            dot.attr('node', shape='doublecircle')
            dot.node('C', 'N='+str(tmp.n))
            dot.node('D', 'M='+str(tmp.m))
            dot.attr('node', shape='circle')
            dot.edges(['AB','BC','BD'])
            for i in range(0,tmp.n): 
                idD = 0
                for j in range(0,tmp.m): 
                    dot.node(str(idD),str(tmp.dato.busquedaPos(i+1,j+1)))
                    p = "B"
                    p = p + str(idD)
                    dot.edges([p])
                    
                idD += 1

            print(dot.source)
            tmp = tmp.siguiente
        
        


 
