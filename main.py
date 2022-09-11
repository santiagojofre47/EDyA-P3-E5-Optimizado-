from claseListaContenido import ListaSecuecial

if __name__ == '__main__':
    objLista = ListaSecuecial()
    print('ANTES DE SUPRIMIR')
    objLista.insertar(10)
    objLista.insertar(5)
    objLista.insertar(7)
    objLista.insertar(5)
    objLista.insertar(2)
    objLista.insertar(10)
    objLista.recorrer()
    print('---- LUEGO DE SUPRIMIR ----')
    objLista.suprimir_repetidos()
    objLista.recorrer()
   

