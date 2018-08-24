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
    print("el valor del producto es.." ,coste_producto_comision)
    return  coste_producto_comision
    #print("precio del producto...",coste_producto_comision)
coste_producto = calcular_precio_producto(float(input("digite el costo del producto...")))

def calcular_precio_servicio(cantidad_horas):
   '''
    calcular el precio del servicio por hora

    >>>calcular_precio_servicio(20)
    2000000

    >>>calcular_precio_servicio(12)
    1200000

    >>>calcular_precio_servicio(22)
    2200000

    : param cantidad_horas: (num) cantidad de horas
    : return: (num) precio servicio total por horas

    '''

   coste_precio_servicio = cantidad_horas * 10000
   return coste_precio_servicio

cantidad_horas = calcular_precio_servicio(float(input("digite el precio del servicio")))




def calcular_precio_servicio_extras(cantidad_horas):
    '''
    calcular el precio del servicio por hora mas el 25%

    >>>calcular_precio_servicio_extras(4)
    500000.0

    >>>calcular_precio_servicio_extras(6)
    750000.0

    >>>calcular_precio_servicio_extras(9)
    1125000.0

    : param cantidad_horas: (num) cantidad de horas
    : return: (num) precio servicio total por horas mas 25%

    '''

    tarifa_horas=(cantidad_horas*100000)
    coste_precio_servicio_extras= tarifa_horas+(tarifa_horas*0.25)
    return  coste_precio_servicio_extras

cantidad_horas = calcular_precio_servicio_extras(float(input("horas extras")))




def calcular_costo_envio(kilometros):
    '''
    calcular el precio del envio

    >>>calcular_costo_envio(25)
    2875

    >>>calcular_costo_envio(100)
  11500

    >>>calcular_costo_envio(329)
   37835

    : param kilometros: (num) cantidad de kilometros a la que se envia el producto
    : return: (num) precio del envio

    '''


    coste_envio= kilometros*115
    return  coste_envio

# funcion para calcular producto fuera
def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    '''

    :param coste_producto:
    :param kilometros:
    :return:
    '''

    coste_envio = kilometros * 115
    precio_producto_envio = coste_producto+coste_envio
    return  precio_producto_envio


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
   (float)-> floatt

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

    :param coste_producto_1: costo del primer producto.
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

