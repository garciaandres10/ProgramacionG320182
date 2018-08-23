#coste_producto = (float(input("digite el costo del producto...")))

def calcular_precio_producto(coste_producto):

    '''
     (float)-> float
    #casos de prueba
    >>> calcular_precio_producto(200)
    238.00
    >>> calcular_precio_producto(300)
    357.00
    >>> calcular_precio_producto(600)
    714.00

    :param coste_producto:
    :return:
    '''
    # procesos
    pass


def calcular_precio_servicio(cantidad_horas):
    pass


def calcular_precio_servicio_extras(cantidad_horas):
    pass


def calcular_costo_envio(kilometros):
    pass

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):

    pass


# funcion para calcular el iba de un producto
def calcular_iva_producto(coste_producto, tasa):
    '''
   (float)-> float
   >>> calcular_iva_producto(200,0.19)
   38.0
   >>> calcular_iva_producto(300,0.19)
   57.0
   >>> calcular_iva_producto(600,0.19)
   114.0

   :param coste_producto:
   :param tasa:
   :param iva_total:
   :return:
   '''
    iva_total= coste_producto*tasa
    print("el iva a cobrar es..",iva_total)
    return iva_total
#tasa = calcular_iva_producto(coste_producto,float(input("digite la tasa...")))
# funcion para calcular el iva de un servicio
def calcular_iva_servicio(cantidad_horas, tasa):

    '''
   (float)-> float
   >>> calcular_iva_servicio(100,0.19)
   19.0
   >>> calcular_iva_servicio(150,0.19)
   28.5
   >>> calcular_iva_servicio(200,0.19)
   38.0

   :param cantidad_horas:
   :param tasa::
   :param iva_servicio:
   :return:
   '''
    iva_servicio = cantidad_horas * tasa
    print("el iva del servicio es de...",iva_servicio)
    return iva_servicio
#cantidad_horas = calcular_iva_servicio(float(input("digite la cantidad de horas....")), tasa= float(input("digite la tasa para el iva de servicio...")))

def calcular_iva_envio(kilometros, tasa):

    '''
   (float)-> float
   >>> calcular_iva_envio(20,0.19)
   3.8
   >>> calcular_iva_envio(50,0.19)
   9.5
   >>> calcular_iva_envio(100,0.19)
   19.0

   :param kilometros:
   :param tasa:
   :param iva_envio:
   :return:
   '''

    iva_envio = kilometros * tasa
    print("el iva para el envio es...",iva_envio)
    return iva_envio

#kilometros = calcular_iva_envio(float(input("digite los kilometros a recorrer...")), tasa = float(input("digite la tasa a manejar para los kilometros...")))


# funcion para calcular el iva de servicio fuera
def calcular_iva_servicio_fuera(cantidad_horas, tasa):

    '''
   (float)-> float
   >>> calcular_iva_servicio_fuera(15,0.19)
   2.85

   >>> calcular_iva_servicio_fuera(25,0.19)
   4.75

   >>> calcular_iva_servicio_fuera(35,0.19)
   6.65

   :param cantidad_horas:
   :param tasa:
   :param iva_afuera:
   :return:
   '''

    iva_fuera = cantidad_horas * tasa
    print(" iva a fuera por servicio es...",iva_fuera)
    return iva_fuera

#cantidad_horas = calcular_iva_servicio_fuera(float(input("digite las horas extras...")),float(input("digite la tasa para las horas extras...")))

#calcula el recaudo total de todos los locales
def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    '''
    # casos de prueba:

    :param coste_producto_1: costo del primer producto
    :param coste_producto_2: costo del segundo producto
    :param coste_producto_3: costo del tercer producto
    :return: el costo total del producto
    '''
    #procesos

    pass
# calcula el recudo total de las horas extras
def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    '''
    #Casos de prueba


    :param horas_1: numero de horas extras del primer cliente
    :param horas_2: numero de horas extras del segundo cliente
    :param horas_3: numero de horas extras del tercer cliente
    :param horas_4: numero de horas extras del cuarto cliente
    :return:  retorna el recaudo total de horas
    '''
    # procesos:
    pass

# funcion para el recaudo total mixto
def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    '''

    #casos de prueba

    :param coste_producto_1: costo del primer producto
    :param coste_producto_2: costo del segundo producto
    :param horas_1:  horas del primer servicio
    :param horas_2: horas del segundo servicio
    :return: retorna el total
    '''
    #proceso:
    pass
