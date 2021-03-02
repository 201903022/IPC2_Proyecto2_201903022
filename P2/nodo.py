
from listaDato import ListaDato
from listaGrupos import ListaGrupo
class nodo: 
    def __init__(self,id,nombre,n,m): 
        self.id = id
        self.nombre = nombre
        self.n = n
        self.m = m
        self.dato = ListaDato()
        self.grpPatron = ListaGrupo()
        self.siguiente =  None
        self.anterior  =  None

        