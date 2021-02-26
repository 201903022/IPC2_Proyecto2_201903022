
from listaDato import ListaDato
class nodo: 
    def __init__(self,id,nombre,n,m): 
        self.id = id
        self.nombre = nombre
        self.n = n
        self.m = m
        self.dato = ListaDato()
        self.siguiente =  None
        self.anterior  =  None