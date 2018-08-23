def calcular_precio_producto(coste_producto):

    '''
     (float)-> float
    #casos de prueba
    >>> calcular_precio_producto(200)
    300.0

    >>> calcular_precio_producto(300)
    450.0

    >>> calcular_precio_producto(600)
    900.0


    :param coste_producto:
    :return:
    '''
    # procesos
    coste_producto_comision= coste_producto+(coste_producto*0.5)
    #print("el valor del producto es.." ,coste_producto_comision)
    return  coste_producto_comision
    #print("precio del producto...",coste_producto_comision)
coste_producto = calcular_precio_producto(float(input("digite el costo del producto...")))

def calcular_precio_servicio(cantidad_horas):
    '''
    >>> calcular_precio_servicio(10)

    >>> calcular_precio_servicio(20)

    >>> calcular_precio_servicio(50)

    :param cantidad_horas:
    :return:
    '''
    pass


def calcular_precio_servicio_extras(cantidad_horas):
    '''
    >>> calcular_precio_servicio_extras(15)

    >>> calcular_precio_servicio_extras(25)

    >>> calcular_precio_servicio_extras(35)

    :param cantidad_horas:
    :return:
    '''
    pass


def calcular_costo_envio(kilometros):
    '''
    >>> calcular_costo_envio(50)

    >>> calcular_costo_envio(60)

    >>> calcular_costo_envio(70)

    :param kilometros:
    :return:
    '''
    pass

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):

    pass


# funcion para calcular el iba de un producto
def calcular_iva_producto(coste_producto, tasa):
    '''

   :param coste_producto:
   :param tasa:
   :param iva_total:
   :return:
   '''
    iva_total= coste_producto*tasa
    print("el iva a cobrar es..",iva_total)
    return iva_total
    #print("el iva a cobrar es..",iva_total)
tasa= calcular_iva_producto(coste_producto, float(input("digite la tasa...")))
# funcion para calcular el iva de un servicio
def calcular_iva_servicio(cantidad_horas, tasa):

    '''
   (float)-> float

   :param cantidad_horas:
   :param tasa::
   :param iva_servicio:
   :return:
   '''
    iva_servicio = cantidad_horas * tasa
    print("el iva del servicio es de...",iva_servicio)
    return iva_servicio
    #print("el iva del servicio es de...",iva_servicio)
cantidad_horas = calcular_iva_servicio(float(input("digite la cantidad de horas....")), tasa= float(input("digite la tasa para el iva de servicio...")))

def calcular_iva_envio(kilometros, tasa):

    '''
   (float)-> float

   :param kilometros:
   :param tasa:
   :param iva_envio:
   :return:
   '''

    iva_envio = kilometros * tasa
    print("el iva para el envio es...",iva_envio)
    return iva_envio
    #print("el iva para el envio es...",iva_envio)
kilometros = calcular_iva_envio(float(input("digite los kilometros a recorrer...")), tasa = float(input("digite la tasa a manejar para los kilometros...")))


# funcion para calcular el iva de servicio fuera
def calcular_iva_servicio_fuera(cantidad_horas, tasa):

    '''
   (float)-> float

   :param cantidad_horas:
   :param tasa:
   :param iva_afuera:
   :return:
   '''

    iva_fuera = cantidad_horas * tasa
    print(" iva a fuera por servicio es...",iva_fuera)
    return iva_fuera
    #print(" iva a fuera por servicio es...",iva_fuera)

cantidad_horas = calcular_iva_servicio_fuera(float(input("digite las horas extras...")),float(input("digite la tasa para las horas extras...")))

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
