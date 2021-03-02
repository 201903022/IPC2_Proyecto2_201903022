from graphviz import Digraph
from dato import dato
from nodo import nodo
from listaGrupos import ListaGrupo

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
            print('\n'+str(contador) + '. ID G: ' + str(tmp.id)  +  '. Nombre: ' + str(tmp.nombre)  + ', N: ' + str(tmp.n) + ', M: '+ str(tmp.m))
            tmp.dato.mostrarD()
            contador += 1
            tmp = tmp.siguiente

    def mostrarI(self):
        tmp = self.primero
        while tmp is not None:
            print('NO. OPCION : ' + str(tmp.id)  +  '. NOMBRE: ' + str(tmp.nombre)  +  ' N: ' + str(tmp.n) +  ' M: ' + str(tmp.m) )            
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

    def getSize(self):
        tmp = self.primero
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont            
    def getLast(self): 
        return self.last
    def graficar1(self): 
        tmp = self.primero 
        while tmp is not None:
            dot = Digraph('G',filename= tmp.nombre)
            dot.node('A','Matrices')
            dot.node('B',tmp.nombre)
            dot.attr('node', shape='doublecircle')
            dot.node('C', 'N='+str(tmp.n))
            dot.node('D', 'M='+str(tmp.m))
            dot.attr('node', shape='circle')
            dot.edges(['AB','BC','BD'])
            for i in range(0,tmp.n): 
                for j in range(0,tmp.m): 
                    dot.node(str(tmp.dato.rId(i+1,j+1)),str(tmp.dato.busquedaPos(i+1,j+1)))
            for i in range(0,tmp.m): 
                p = "B"
                p = "B"+ str(i)      
                dot.edges([p])                          
            for i in range(0,(tmp.n-1)) : 
                k = i * tmp.m
                l = k + tmp.m 
                for j in range (k,l): 
                    ed = j
                    union = j+tmp.m
                    dot.edge(str(j),str(union))
            print(dot.source)
            dot.view()
            tmp = tmp.siguiente          

    def diagramaPor(self,valor): 
        tmp = self.primero 
        while tmp is not None:
            if tmp.id == valor: 
             dot = Digraph('G',filename='hello.gv' )
             dot.node('A','Matrices')
             dot.node('B',tmp.nombre)
             dot.attr('node', shape='doublecircle')
             dot.node('C', 'N='+str(tmp.n))
             dot.node('D', 'M='+str(tmp.m))
             dot.attr('node', shape='circle')
             dot.edges(['AB','BC','BD'])
             for i in range(0,tmp.n): 
                 for j in range(0,tmp.m): 
                      dot.node(str(tmp.dato.rId(i+1,j+1)),str(tmp.dato.busquedaPos(i+1,j+1)))
                 p2 = str(i)
                 p2 = p2 + str(i+tmp.m) 
                 dot.edges([p2]) 

             for i in range(0,tmp.m): 
                 p = "B"
                 p = "B"+ str(i)      
                 dot.edges([p])                    

             if tmp.n > 2: 
                 #k = tmp.n 
                 #l = tmp.n*2
                 for i in range(0,tmp.n): #0,1,2,3,4
                      k = i + tmp.n #5,6,7,8,9
                      l = k + tmp.m #9,10,11,12,13
                      if k > 9 or l > 9 : 
                          dot.edge(str(k),str(l))                         
                      else: 
                         p3 = str(k)
                         p3 = p3+ str(l)       
                         dot.edges([p3])
             if tmp.n > 3: 
                 print("tmp.n es mayor que 3")
                 k = tmp.n * 2 #10
                 l = k + tmp.m  #14                
                 for i in range(k,l): #10,11,12,13
                      k = i + tmp.n #15 ,16,17,18
                      l = k + tmp.m #19
                      if k > 9 or l > 9 : 
                          dot.edge(str(k),str(l))                         
                      else: 
                         p3 = str(k)
                         p3 = p3+ str(l)       
                         dot.edges([p3])                            
             if tmp.n > 4: 
                 print("tmp.n es mayor que 4")
                 k = tmp.n 
                 l = k + tmp.m               
                 for i in range(k,l): 
                      k = i + tmp.n
                      l = k + tmp.m
                      if k > 9 or l > 9 : 
                          dot.edge(str(k),str(l))                         
                      else: 
                         p3 = str(k)
                         p3 = p3+ str(l)       
                         dot.edges([p3])   
             print(dot.source)
             dot.view()
            tmp = tmp.siguiente 

    def graficar(self,valor): 
        tmp = self.primero 
        while tmp is not None:
            if tmp.id == valor: 
             dot = Digraph('G',filename= tmp.nombre)
             dot.node('A','Matrices')
             dot.node('B',tmp.nombre)
             dot.attr('node', shape='doublecircle')
             dot.node('C', 'N='+str(tmp.n))
             dot.node('D', 'M='+str(tmp.m))
             dot.attr('node', shape='circle')
             dot.edges(['AB','BC','BD'])
             for i in range(0,tmp.n): 
                 for j in range(0,tmp.m): 
                      dot.node(str(tmp.dato.rId(i+1,j+1)),str(tmp.dato.busquedaPos(i+1,j+1)))
             for i in range(0,tmp.m): 
                 p = "B"
                 p = "B"+ str(i)      
                 dot.edges([p])                          
             for i in range(0,(tmp.n-1)) : 
                 k = i * tmp.m
                 l = k + tmp.m 
                 for j in range (k,l): 
                     ed = j
                     union = j+tmp.m
                     dot.edge(str(j),str(union))
             print(dot.source)
             dot.view()
            tmp = tmp.siguiente                       
   
    def busquedaPatron(self,valor): 
        tmp = self.primero 
        while tmp is not None:
            contador_Grupos= 0
            grupos = ListaGrupo()
            for fil in range (1,tmp.n-1): 
             seCompara = True
             if grupos.estaVacia(): 
                 if agrupad(fil+1): 
                     seCompara = False
             if seCompara: 
                 grupos.insertar(contador_Grupos,fil+1)
            tmp = tmp.siguiente  
                      
        


 
