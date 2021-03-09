
from listaDato import ListaDato
from listaGrupos import ListaGrupo
from lMatrizR import lMatrizR
class nodo: 
    def __init__(self,id,nombre,n,m): 
        self.id = id
        self.nombre = nombre
        self.n = n
        self.m = m
        self.dato = ListaDato()
        self.grpPatron = ListaGrupo()
        self.resultante = lMatrizR()
        self.siguiente =  None
        self.anterior  =  None

        