def calcular_precio_producto(coste_producto):

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
    return iva_total


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
   :param tasa:
   :param iva_servicio:
   :return:
   '''
    iva_servicio = cantidad_horas * tasa
    return iva_servicio




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
    return iva_envio



# funcion para calcular el iva de servicio fuera
def calcular_iva_servicio_fuera(cantidad_horas, tasa):

    '''
   (float)-> float
   >>> calcular_iva_servicio_fuera(15,0.19)
   2.8

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
    return cantidad_horas


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass
