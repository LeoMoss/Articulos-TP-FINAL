#! /usr/bin/python3
from art import Art
from repositorioArt import RepositorioArt
from cajon import Cajon
class Abm:
	'''Representa una colección de Articulos '''

	def __init__(self):
		self.repo = RepositorioArt()
		self.arts = self.repo.get_all()


	def nuevo_art(self, nombre, precio, id_art, marca):
		'''Crea un nuevo art y el agrega a el lista de arts'''
		art = Art(nombre, precio, id_art, marca)
		self.repo.store(art)
		self.arts.append(art)
		return art

	def buscar_por_id(self, id_art):
		'''Buscar el art con el id dado'''
		#Debe retornar el art con el id dado, o None si no existe dicho art.
		for art in self.arts:
			if id_art == art.id:
				return art
		return None


	def modificar_articulo(self, id_art, nombre):
		'''Busca el art con el id dado y modifica el nombre'''
		# Busca el art por id, usando el método anterior.
		art = self.buscar_por_id(id_art)
		# Si lo encontró, actualiza el nombre de el art y retorna True:
		if art:
			art.nombre = nombre
			self.repo.update(art)
			return True
		# pero si no lo encontró, retorna False:
		return False
	
	def modificar_marca(self, id_art, marca):
		'''Busca el art con el id dado y modifica la marca'''
		
		art = self.buscar_por_id(id_art)
		# Si lo encontró, actualiza el nombre de el art y retorna True:
		if art:
			art.marca = marca
			self.repo.update(art)
			return True
		# pero si no lo encontró, retorna False:
		return False

	def modificar_precio(self, id_art, precio):
		'''Busca el art con el id dado y modifica los precio'''
		art = self.buscar_por_id(id_art)
		# Si lo encontró, actualiza el nombre de el art y retorna True:
		if art:
			art.precio = precio
			self.repo.update(art)
			return True 
			
		# pero si no lo encontró, retorna False:
		return False

	def buscar(self, filtro):
		'''Retorna una lista de todos los arts que coincidan con el filtro 
		dado, en el nombre o en la marca'''

		'''arts = []
		for art in self.arts:
			if art.coincide(filtro):
				arts.append(art)
				return arts'''
		arts = Art.coincide(self, filtro)
		return arts
	
	def buscar_n(self, filtro):
		
		arts = []
		for art in self.arts:
			if filtro in art.nombre:
				arts.append(art)
		return arts
	
	def buscar_m(self, filtro):
		
		arts = []
		for art in self.arts:
			if filtro in art.marca:
				arts.append(art)
		return arts
		

	def eliminar_articulo(self, id_art):
		art = self.buscar_por_id(id_art)
		if art:
			self.repo.delete(art)
			self.arts.remove(art)
			print("Se elimino el art")
			return True
		else:
			print("No se encontro el art")
			return False
			
	def nuevo_cajon(self, nombre, precio, id_art, marca, cbotellas):
		art = Cajon(nombre, precio, id_art, marca, cbotellas)
		self.arts.append(art)
		self.repo.store(art)
		
		
	'''def nueva_tarea(self, texto, etiquetas, responsable, fecha_vencimiento):
		nota = Tarea(texto, etiquetas, responsable, fecha_vencimiento)		
		self.notas.append(nota)'''

