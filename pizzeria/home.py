import time
from utils.prints import *
from utils.consoleHelper import *
from utils.validaciones import *
from utils.jsonFileHandler import *

USER_DATA_BASE_PATH = "./dataBase/users.json"

# Se imprimer un pequeño mensaje
Limpiar_Pantalla()
print("+----------Dominos Pizza----------+")
print("+------------BIENBENIDO-----------+")
print("Este es nuestro menu digital para facilitar sus pedidos")

print("Desea usar un pedido pasado")
usar_pedido_pasado = validarSI_NO("-->")
if usar_pedido_pasado == "si":

	print("Usar pedido pasado: ")

	users = readFile(USER_DATA_BASE_PATH)
	while True:
		codigo_usuario = input("Digite su codifo de usuario:")
		if foundCode(users, codigo_usuario):
			break
		else:
			print("Ese codigo no existe")

	print(f"Bienvenido {users[codigo_usuario]['nombre']}")
	propina = validarSI_NO("Desea dejar una propina del 5 % de su compra")
	while True:

		pedido_Elegido = imprmir_mini_menu(users[codigo_usuario])
		factura(users[codigo_usuario][pedido_Elegido],propina,users[codigo_usuario])
		realizar_pedido = validarSI_NO("Desea realizar el pedido")

		if realizar_pedido == "si":
			break
		else:
			print("Como no quiere ordenar ese pedido seleccione otro")

else:
	# Incializo una varaibles
	histoy_tamaño = [] # Se agrega a la lista los tamaños de los pedidos
	history_sabor = [] # Se agrega a la lista los sabores de los pedidos
	history_adiccion = [] # Se agrega a la lista las adicciones de los pedidos

	while True: # Repetir hasta que el usuario ya no quiera pedir mas pizzas
		while True: # Repetimos hasta que usuario coloque la opcion correcta
			tamaño_pizza = menu_Tamaño_Pizza()
			if validar_opcion(tamaño_pizza,1,4):
				opcion_invalida()
			else:
				guardad_con_exito()
				tamaño_pizza = int(tamaño_pizza)
				histoy_tamaño.append(tamaño_pizza)
				break
			
		while True: # Repetimos hasta que usuario coloque la opcion correcta
			sabor_pizza = menu_Sabor_Pizza()
			if validar_opcion(sabor_pizza,1,5):
				opcion_invalida()
			else:
				guardad_con_exito()
				sabor_pizza = int(sabor_pizza)
				history_sabor.append(sabor_pizza)
				break
			
		Limpiar_Pantalla()
		print(f"Contamos con adiciones como\nExtra peperoni\nExtra queso\nBorde de queso")
		op = validarSI_NO("Desea ordenar alguna adicion")

		if op == "si" : # si quiere adicciones
			while True: # Repetimos hasta que usuario coloque la opcion correcta
				adiccion_pizza = menu_Adicciones_Pizza()
				if validar_opcion(adiccion_pizza,1,3):
					opcion_invalida()
				else:
					guardad_con_exito()
					adiccion_pizza = int(adiccion_pizza)
					break
		else: # Si no quiere adicciones colocamos None
			adiccion_pizza = None

		# Guardamos la adiccion en el historial
		history_adiccion.append(adiccion_pizza)

		total_pagar = segun_tamaño_pizza(histoy_tamaño[len(histoy_tamaño)-1],0) + segun_adiccion_pizza(history_adiccion[len(history_adiccion)-1],0)
		# Imprimimos la orden del usuario
		Limpiar_Pantalla()
		print( "Orden final")
		print(f"{segun_tamaño_pizza(tamaño_pizza)} {segun_sabor_pizza(sabor_pizza)} {segun_adiccion_pizza(adiccion_pizza)}")
		print(f"con un total a pagar de {colorear('YELLOW',total_pagar)}")
		print("Si desea pedir otra pizza digite no")
		concluir_orden = validarSI_NO("Desea concluir su orden") # Preguntamos si quiere pedir otra pizza 

		if concluir_orden == "si": # Si quiere concluir la orden break
			break

	# Esta parte del codigo se encarga de calcular si una orden del usuario se repite
	pedidos = pedidos_lista(histoy_tamaño,history_sabor,history_adiccion)

	# Pedimos informacion al usuario sobre el pedido
	propina = validarSI_NO("Desea dejar una propina del 5 % de su compra")
	print("para finalizar su pedido necesitamos unos cuantos datos")
	registrado = True if  validarSI_NO("ya se encuentra registrad@?") == "si" else False 

	while True:
		if not registrado: # Si no esta registrado
			Limpiar_Pantalla()
			print("====Ingrese los datos====")
			# Guardamos la informacion del usuario
			info = {
				"nombre":validar_caracteres(40,"Porfavor digite su nombre"),
				"direccion":validar_caracteres(40,"Porfavor digite su direccion"),
				"telefono":validar_caracteres(40,"Porfavor digite su telefono")
			}
			guardar = True if  validarSI_NO("desea guardar la informacion?") == "si" else False 
			if guardar: # si la quiere guardar la ponemos en el archivo JSON
				users = readFile(USER_DATA_BASE_PATH)
				while True:
					codigo_usuario = input("Porfavor digite su codigo de usuairio\neste debe ser unico: ") # Guardamos un codigo para ese usuario
					if foundCode(users,codigo_usuario):
						print("lo lamento el codigo ya existe\nIntentelo nuevamente")
					else:
						break
				info[input("Descripcion del pedido: ")] = pedidos
				users[codigo_usuario] = info
				saveFile(USER_DATA_BASE_PATH,users)	

			# Animacion del carga
			cargando()
			#Imprime la factura
			Limpiar_Pantalla()
			users = readFile(USER_DATA_BASE_PATH)
			factura(pedidos,propina,info)

			break
		else: # Ya esta registrado
			encontrado = False
			while True:
				print("si no se acuerda vuelva a registrarse con C")
				codigo_usuario = input("Porfavor digite su codigo de usuario: ")
				users = readFile(USER_DATA_BASE_PATH)
				if foundCode(users,codigo_usuario):
					print("perfecto ya encontramos su informacion")
					users[codigo_usuario][input("Descripcion del pedido: ")] = pedidos

					# Animacion del carga
					cargando()
					#Imprime la factura
					Limpiar_Pantalla()
					factura(pedidos,propina,users[codigo_usuario])

					saveFile(USER_DATA_BASE_PATH,users)
					encontrado = True
					break
				elif codigo_usuario.lower() == "c":
					registrado = False
					break
				else:
					print("el usuario no existe")

			if encontrado:
				break


# Organizar todo mejor en funciones
# Modular mas las cosas
# Arreglar la estetica del proyecto







