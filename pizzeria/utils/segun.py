def segun_sabor_pizza(sabor_pizza): # Segun la opcion elegida por el usuario retorna el sabor de pizza
	sabores = {1:"de peperoni",2:"sabor hawaiana",3:"sabor cuatro quesos",4:"sabor vegetariana",5:"de pollo con champiñones"}
	return sabores[sabor_pizza]

def segun_adiccion_pizza(adiccion_pizza,total_pagar = None): # Segun la opcion elegida por el usuario retorno un valor
	adicciones = {1:["con extra queso",5],2:["con extra peperoni",6],3:["con borde de queso",10],None:["sin adiciones",0]}
	if total_pagar == None: # Si no manda total a pagar 
		return adicciones[adiccion_pizza][0] # Solo mandamos el sabor de la pizza
	else: # Si manda totoal a pagar
		return total_pagar + adicciones[adiccion_pizza][1] # Retornamos el valor de la adiccion

def segun_tamaño_pizza(tamaño_pizza,total_pagar = None): # Segun la opcion elegida por el usuario retorno un valor
	tamaños = {1:["Una pizza mediana",25],2:["Una pizza grande",35],3:["Una pizza extra grande",45],4:["Una pizza mega grande",50]}
	if total_pagar == None: # Si no manda total a pagar 
		return tamaños[tamaño_pizza][0] # Solo mandamos el sabor de la pizza
	else: # Si manda totoal a pagar
		return total_pagar + tamaños[tamaño_pizza][1] # Retornamos el valor de la adiccion
	
def pedidos_lista(histoy_tamaño,history_sabor,history_adiccion):
	# Esta parte del codigo se encarga de calcular si una orden del usuario se repite
	pedidos = [] # todos los pedidos van en esta lista
	for i in range(len(histoy_tamaño)): 
		frecuencia = 0 # El numero de veces que se repite la orden
		for j in range(len(histoy_tamaño)):
			# Si la orden se repite le sumamos uno a la frecuencia
			if [histoy_tamaño[i],history_sabor[i],history_adiccion[i]] == [histoy_tamaño[j],history_sabor[j],history_adiccion[j]] :
				frecuencia+=1
		# Creamos el diccioario con la informacion del peido he incluimos la frecuencia
		x={"tamaño":histoy_tamaño[i],"sabor":history_sabor[i],"adiccion":history_adiccion[i],"frecuencia":frecuencia}
		if x not in pedidos: # Si no esta en la lista lo ponemos
			pedidos.append(x)
	return pedidos