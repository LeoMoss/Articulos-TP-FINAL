1#! /usr/bin/python3
from abm import Abm
import sys
class Menu:
	'''Mostrar un menú y responder a los opciones'''

	def __init__(self):
		self.abm = Abm()
		self.opciones= {
			"1": self.mostrar_articulos,
			"2": self.buscar_articulos,
			"3": self.agregar_articulo,
			"4": self.modificar_articulo,
			"5": self.eliminar_articulo,
			"6": self.estadisticas,
			"7": self.salir
		}

	def mostrar_menu(self):
		'''Muestra el menú de opciones'''
		print("""
Menú del abm:
1. Mostrar todos los articulos
2. Buscar Art
3. Agregar Art
4. Modificar Art
5. Eliminar Art
6. Estadisticas
7. Salir
""")

	def ejecutar(self):
		'''Mostrar el menu y responder a los opciones.'''
		while True:
			self.mostrar_menu()
			opcion = input("Ingresar un opción: ")

			# Guardamos en el variable accion el método que corresponde a el
			# opción elegida por el usuario. Por ejemplo, si opcion tiene el 
			# valor 1, accion va a guardar el valor correspondiente a 
			# self.opciones[1], es decir: self.mostrar_arts
			accion = self.opciones.get(opcion)

			# Si hay algún valor guardado en accion, ejecutamos el método que
			#tiene ese nombre, y si no mostramos un error:
			if accion:
				accion()
			else:
				print("{0} no es un opción válida".format(opcion))

	def mostrar_articulos(self, arts=None):
		'''Si recibe como parámetro un lista de arts, muestra id, nombre y
		precio de esos arts. Si no recibe el parámetro, muestra id, nombre
		y precio de todas los arts'''
		if arts is None:
			arts =  self.abm.arts
		for art in arts:
			print('Codigo: ', art.id)
			print('Nombre: ', art.nombre)
			print('Marca: ', art.marca)
			if hasattr(art, 'cbotellas'):
				print('Cantidad de botellas: ', art.cbotellas)
			print('Precio: $', art.precio)
			print('-' * 40)
	
	def buscar_articulos(self):
		'''Solicita al usuario un cadena de búsqueda y muestra los arts que 
		coinciden con el mismo, si es que hay alguna'''
		'''sub_opcion = input(" Buscar por: \n | 1-Codigo | 2-Nombre | 3-Marca: ") 
		if sub_opcion == "1":
			id_art = int(input("Codigo: "))
			arts = self.abm.buscar_por_id(id_art)
			if arts:
				self.mostrar_articulos(arts)
			else:
				print("No se encontro Articulo")
		elif sub_opcion == "2":
			filtro = input("Nombre: ")
			if arts:
				self.mostrar_articulos(arts)
			else:
				print("No se encontro Articulo")
		elif sub_opcion == "3":
			print("Contruir 404")
		else: 
			print("no es una opcion valida")'''
			
		sub_opcion = (input("Buscar en;  \n| 1-Nombre y/o Marca | 2-Nombre | 3-Marca | 4-Codigo:  "))
		if sub_opcion == "1":
			filtro = input("Buscar: ")
			arts = self.abm.buscar(filtro)
			if arts:
				self.mostrar_articulos(arts)
			else:
				print("Ningun articulo coincide con la búsqueda")
		elif sub_opcion == "2":
			filtro = input("Buscar: ")
			arts = self.abm.buscar_n(filtro)
			if arts:
				self.mostrar_articulos(arts)
			else:
				print("Ningun articulo coincide con la búsqueda")
		elif sub_opcion == "3":
			filtro = input("Buscar: ")
			arts = self.abm.buscar_m(filtro)
			if arts:
				self.mostrar_articulos(arts)
			else:
				print("Ninguna articulo coincide con la búsqueda")
		elif sub_opcion == "4":
			while True:
				try:
					id_art = int(input("Ingrese Codigo de producto: "))
					break
				except ValueError:
					print("Debes escribir un número.")
			art = self.abm.buscar_por_id(id_art)
			if art:
				#print('Codigo: ', art.id)
				print('Nombre: ', art.nombre)
				print('Marca: ', art.marca)
				if hasattr(art, 'cbotellas'):
					print('Cantidad de botellas: ', art.cbotellas)
				print('Precio: $', art.precio)
			else:
				print("Ninguna articulo coincide con la búsqueda")
		else:
			print("No es una opcion valida")

		'''if arts:
			self.mostrar_articulos(arts)
		else:
			print("Ninguna articulo coincide con la búsqueda")'''

	def agregar_articulo(self):
		'''Solicita un nombre al usuario y agrega un nuevo art con ese nombre'''
		while True:
			try:
				id_art = int(input("Ingrese Codigo de producto: "))
				break
			except ValueError:
				print("Debes escribir un número.")
		existe = self.abm.buscar_por_id(id_art)
		if existe == None:
			#nombre = input("Nombre: ")
			marca = input("Marca: ")
			while True:
				try:
					precio = float(input("Precio: "))

					break
				except ValueError:
					print("Debes escribir un número.")
			sub_opcion = int(input("Es un: | 1-Cajon | 2-Artiulo : "))
			if sub_opcion == 1:
				nombre = "Cajon"
				cbotellas = int(input("Ingrese cantidad de botellas que entran en el cajon :"))
				art = self.abm.nuevo_cajon(nombre, precio, id_art, marca, cbotellas)
			elif sub_opcion == 2:
				nombre = input("Nombre: ")
				art = self.abm.nuevo_art(nombre, precio, id_art, marca)
			else:
				print("Elija una opcion valida")
		else:
			print("Ya existe el codigo de articulo")
		

	def modificar_articulo(self):
		'''Solicita el id de un art y el nuevo nombre y/o precio que tendrá
		el mismo.  Busca el art con el id ingresado, y actualiza su nombre y/o
		precio.'''
		id_art = int(input("Ingrese el id de el art a modificar: "))
		art = self.abm.buscar_por_id(id_art)
		if art != None:
			sub_opcion = (input("Que desea modificar? \n| 1-Nombre | 2-Marca | 3-Precio :  "))
			if sub_opcion == "1":
				if not hasattr (art, "cbotellas"):
					nombre = input("Ingrese el nombre de el art: ")
					self.abm.modificar_articulo(id_art, nombre)
				else:
					print("No se puede modificar el nombre de los cajones")
			elif sub_opcion == "2":
				marca = input("Ingrese la marca de el art: ")
				self.abm.modificar_marca(id_art, marca)
			elif sub_opcion == "3":
				while True:
					try:
						precio = float(input("Precio: "))
						self.abm.modificar_precio(id_art, precio)
						break
					except ValueError:
						print("Debes escribir un número.")
			else:
				print("no es una opcion valida")
		else:
			print("No se encontro el articulo")

	def salir(self):
		'''Muestra un mensaje y sale del sistema'''
		print("Gracias por utilizar el sistema.")
		sys.exit(0)
		
	def eliminar_articulo(self):
		id_art = int(input("Ingrese el id de el art a eliminar: "))
		self.abm.eliminar_articulo(id_art)
		
	def estadisticas(self):
		arts =  self.abm.arts
		suma = 0
		mayor = None
		menor = None
		ccajones = 0
		cbotellas = 0
		costo_cajon = 0
		mayores = []
		menores = []
		
		for art in arts:
			
			if not hasattr(art, "cbotellas"):
				suma += art.precio

			if not mayor and not hasattr(art, "cbotellas"):
				mayor = art
				
			
			if mayor.precio < art.precio and not hasattr(art, "cbotellas"):
				mayor = art
				
			
			if not menor and not hasattr(art, "cbotellas"):
				menor = art
				
				
			
			if menor.precio > art.precio and not hasattr(art, "cbotellas"):
				menor = art

				

			
			if hasattr(art, "cbotellas"):
				ccajones += 1
				cbotellas += art.cbotellas
				costo_cajon += art.precio

		''' Busco si Mayor y Menor estan repetidos y lo agrego a la lista respectiva'''	
		for art in arts:
			if mayor.precio == art.precio and not hasattr(art, "cbotellas"):
				mayores.append(art)
			if menor.precio == art.precio and not hasattr(art, "cbotellas"):
				menores.append(art)
		
		
		
		cantidad = len(arts) - ccajones
		promedio = suma / cantidad
		promedio_cajon = costo_cajon / ccajones
		print("Cantidad de articulos : ", cantidad)
		print("El promedio de costo de articulos es: $", promedio)
		
		if len(mayores) > 1:
			print("Los arituclos con mayor costo son: ")
			for unMayor in mayores:
				print(unMayor.nombre, "$ ", unMayor.precio)
		else:
			print("El articulo", mayor.nombre, "es el mas caro y cuesta: $", mayor.precio)

		
		if len(menores) > 1:
			print("Hay", len(menores), "articulos con el menor costo y son:"  )
			for unMenor in menores:
				print(unMenor.nombre, " con un costo de: ", unMenor.precio)
		else:
			print("El articulo", menor.nombre, "es el mas barato y cuesta: $", menor.precio)
		

		print("Cantidad de cajones: ", ccajones)
		print("Cantidad de botellas: ", cbotellas)
		print("Promedio costo de cajones: ", promedio_cajon)
	
		
		


#Esta parte del código está fuera de el clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar(). 
if __name__ == "__main__":
	Menu().ejecutar()
