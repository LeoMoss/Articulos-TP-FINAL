#! /usr/bin/python3
class Art:
	'''Representa un art en el abm. Tiene id. nombre, precio (separadas 
	por espacios) y se puede buscar por nombre'''
	def __init__(self, nombre, precio, id_art, marca):
		'''Inicializa el art con un nombre, con precio, id'''
		self.nombre = nombre
		self.precio = precio
		self.id = id_art
		self.marca = marca

	def coincide(self, filtro):
		'''Determina si el art coincide con el filtro de búsqueda. Retorna 
		True si es así y False de lo contrario
		
		Busca tanto en el nombre como en los precio y distingue mayúsculas de
		minúsculas '''
		arts = []
		for art in self.arts:
			if filtro in art.nombre or filtro in art.marca:
				arts.append(art)
		return arts
