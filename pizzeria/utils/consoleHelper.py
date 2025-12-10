import os 
import time

def colorear(color,text): # Pinta en texto de la consola
    colors = dict(BLACK = '\033[30m',RED = '\033[31m',GREEN = '\033[32m',YELLOW = '\033[33m',BLUE = '\033[34m',MAGENTA = '\033[35m',CYAN = '\033[36m',WHITE = '\033[37m',RESET = '\033[0m')
    return f"{colors.get(color)}{text}{colors.get('RESET')}"

def Limpiar_Pantalla(): # Limpia la pantalla de la consola
	os.system("cls" if os.name == "nt" else "clear")

def tecla_para_continuar(mensaje): # Permite a usuario ver la informacion antes de que se limpie la pantalla
	input(f"Oprima enter para {mensaje}....")

def guardad_con_exito(): # Informa al usuario que todo se guardo con exito
	print("La opcion se ha guardado con exito....")
	tecla_para_continuar("validar su opcion")

def opcion_invalida(): # Informa al usuario que la opcion escogida es invalida
	print("OPCION INVALIDA")
	tecla_para_continuar("intentarlo nuevamente")

def cargando():
	loading = ""
	for i in range(1,11,1):
		Limpiar_Pantalla()
		print(loading)
		time.sleep(0.1)
		loading = loading + " |"