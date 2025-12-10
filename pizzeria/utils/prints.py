from .consoleHelper import Limpiar_Pantalla
from .validaciones import *
from .segun import *

def menu_Tamaño_Pizza(): # Imprime el menu de tamaños y retorna la opcion elegida
	Limpiar_Pantalla()
	print("===============================================")
	print("||               MENU DE PIZZAS               ||")
	print("===============================================")
	print("||   Tamaño        ||        Precio (S/.)     ||")
	print("===============================================")
	print("||  [1] Mediana    ||          25.00          ||")
	print("||  [2] Grande     ||          35.00          ||")
	print("||  [3] ExtraGrande||          45.00          ||")
	print("||  [4] MegaGrande ||          50.00          ||")
	print("===============================================")
	print("||         Elige el tamaño de tu pizza        ||")
	print("===============================================\n")

	return input("Ingrese el numero de su eleccion: ")

def menu_Sabor_Pizza(): # Imprime el menu de sabores y retorna la opcion elegida
	Limpiar_Pantalla()
	print("=================================================")
	print("||            MENU DE SABORES DE PIZZA          ||")
	print("================================================")
	print("||   Opción   ||          Sabor de Pizza        ||")
	print("=================================================")
	print("||    [1]     ||   Pepperoni                    ||")
	print("||    [2]     ||   Hawaiana                     ||")
	print("||    [3]     ||   Cuatro Quesos                ||")
	print("||    [4]     ||   Vegetariana                  ||")
	print("||    [5]     ||   Pollo con Champiñones        ||")
	print("=================================================")
	print("||     + Elige el sabor que más te guste +      ||")
	print("=================================================")
	return input("Cual sabor de pizza desea: ")

def menu_Adicciones_Pizza(): # Imprime el menu de adicciones y retorna la opcion elegida
	Limpiar_Pantalla()
	print("=================================================")
	print("||            MENU DE ADICIONES EXTRA           ||")
	print("=================================================")
	print("||   Opcion   ||          Adicion Extra         ||")
	print("=================================================")
	print("||    [1]     ||   Extra Queso             +5   ||")
	print("||    [2]     ||   Extra Pepperoni         +6   ||")
	print("||    [3]     ||   Borde Relleno de Queso  +10  ||")
	print("=================================================")
	print("||     + Elige una adicion para tu pizza +      ||")
	print("=================================================\n")
	return input("Ingrese el numero de su eleccion: ")

def imprmir_mini_menu(lista): # crea mini menus con una lista

    dict_cosas = {}
    i = 0
    for cosa in lista:
        
        if cosa != "nombre" and cosa != "telefono" and cosa != "direccion":
            i += 1
            dict_cosas[i] = cosa
            print(f"{i}.   {cosa}")
    
    while True:
        cosa_num = input("Elige una: ")
        if not validar_opcion(cosa_num,1,i):
            cosa_num = int(cosa_num)
            break
        else:
            print("Opcion invalida")

    return dict_cosas[cosa_num]

def espaciador(string,caracteres): # Coloca espasios para tener mejor la factura
	return string + " "*(caracteres-len(string))

def pedido(pedido): # Crea la parte de la factura que tiene los pedidos
	frecuencia = pedido['frecuencia']
	tamaño = segun_tamaño_pizza(pedido['tamaño'])
	sabor = segun_sabor_pizza(pedido['sabor'])
	adiccion = segun_adiccion_pizza(pedido['adiccion'])
	valor_unitario = (segun_tamaño_pizza(pedido['tamaño'],0) + segun_adiccion_pizza(pedido['adiccion'],0))
	valor_total = valor_unitario * frecuencia
	print(f"|    {espaciador(str(frecuencia),5)}|  {espaciador(tamaño,22)}|  {espaciador(str(valor_unitario),7)}| {espaciador(str(valor_total),6)}|\n|         |  {espaciador(sabor,22)}|         |       |\n|         |  {espaciador(adiccion,22)}|         |       |")

def calcTotal(pedidos):
	total = 0
	for pedido in pedidos:
		frecuencia = pedido['frecuencia']
		valor_unitario = (segun_tamaño_pizza(pedido['tamaño'],0) + segun_adiccion_pizza(pedido['adiccion'],0))
		valor_total = valor_unitario * frecuencia
		total += valor_total
	return total


def factura(pedidos,propina,user={"nombre": "Persona","direccion": "Casa de persona","telefono": "000 000 0000"}): # Imprime la factura
	nombre = espaciador(user['nombre'],42)
	direccion = espaciador(user['direccion'],40)
	telefono = espaciador(str(user['telefono']),41)
	total_pagar = calcTotal(pedidos)

	print(f"+----------------------------------------------------+\n|                   F A C T U R A                    |\n+----------------------------------------------------+\n| Fecha: 04/01/2009      No. Factura: 000000001      |\n+----------------------------------------------------+\n| Cliente: {nombre}|\n| Dirección: {direccion}|\n| Teléfono: {telefono}|\n+----------------------------------------------------+\n|  Cant.  |      Descripción       |  P.Unit | Total |\n+----------------------------------------------------+")
	for i in pedidos:
		pedido(i)
	
	print(f"+----------------------------------------------------+\n|                              Subtotal: {espaciador(str(total_pagar),11)} |\n|                               Propina: {espaciador(str(total_pagar*0.05),11) if propina == 'si' else espaciador('0',11)} |\n|                         Total a pagar: {espaciador(str(round(total_pagar*1.05,2)),11) if propina == 'si' else espaciador(str(total_pagar),11) } |\n+----------------------------------------------------+\n|              ¡Gracias por su compra!               |\n+----------------------------------------------------+")