from .consoleHelper import *

def validar_opcion(var,min,max): # Validamos que la opcion este dentro del rango
    numeros = []
    for i in range(min,max+1): # Creamos una lista con los posibles numero que puede tener
        numeros.append(str(i))
    if var not in numeros: # si la variable esta en esa lista de numeros
        return True
    else: # si no esta
        return False

def validarSI_NO(text): # Valida que lo que alla escrito el usuario sea si o no
	while True:
		concluir_orden = input(f"{text}(si/no): ")
		if concluir_orden == "si" or concluir_orden == "no": # si es si o no se rompe el while
			break
		else: # vulve a preguntar
			opcion_invalida()
	
	return concluir_orden

def validar_caracteres(max_caracteres,mensaje): # Valida que lo escito por el ususario no se pase de los caracteres establecidos
	while True:
		x = input(f"{mensaje}(maximo de caracteres {max_caracteres}): ")
		if len(x) > max_caracteres: # condicion que valida los caracteres
			opcion_invalida()
		else:
			break
	return x

def foundCode(users,userCode): # Esta funcion busca el codigo en la base de datos 
	for code in users: # Devuelve si existe o no
		if code == userCode:
			return True
	False