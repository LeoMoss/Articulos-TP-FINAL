#! /usr/bin/python3
from repositorio import Repositorio
from art import Art
from cajon import Cajon

class RepositorioArt(Repositorio):
	'''Consulta y escribe objetos Art en el BD. '''

	def get_one(self, id_art):
		'''Recibe un id de art (número entero). Retorna un objeto Art. Si no
		lo encuentra, retorna None.'''
		consulta = "SELECT id, nombre, precio FROM arts WHERE id = ?"
		result = self.cursor.execute(consulta, [id_art]).fetchone()

		if result == None:
			return None
		else:
			return Art(result[1], result[2], result[0])

	def get_all(self):
		'''Retorna todas los arts que haya almacenadas en el BD'''
		consulta = "SELECT id, nombre, precio, marca, cajon FROM arts"
		result = self.cursor.execute(consulta).fetchall()

		lista_de_arts = []

		for unResultado in result:
			
			if unResultado[4] is not None:
				lista_de_arts.append(
				Cajon(unResultado[1], unResultado[2], unResultado[0], unResultado[3], unResultado[4])
				)
			else:
				lista_de_arts.append(
					Art(unResultado[1], unResultado[2], unResultado[0], unResultado[3])
					)
		return lista_de_arts

	def store(self, art):
		'''Recibe un objeto art y lo almacena en el Base de Datos
		En caso de éxito, retorna el id de el art, número generado por el base
		de datos. En caso de fracaso, retorna 0 (cero).'''
		if hasattr(art, "cbotellas"):
			try:
				query = "INSERT INTO arts (id, nombre, precio, marca, cajon) VALUES (?, ?, ?, ?, ?)"
				result = self.cursor.execute(query, [art.id, art.nombre, art.precio, art.marca, art.cbotellas])
			

				self.bd.commit()
				return art.id
			except:
				self.bd.rollback()
				return 0
		else:
			try:
				query = "INSERT INTO arts (id, nombre, precio, marca) VALUES (?, ?, ?, ?)"
				result = self.cursor.execute(query, [art.id, art.nombre, art.precio, art.marca])
			

				self.bd.commit()
				return art.id
			except:
				self.bd.rollback()
				return 0
		
	def delete(self, art):
		'''Recibe un objeto Art y lo elimina de el Base de Datos.
		Retorna True si tuvo éxito, False de lo contrario.'''
		try:
			query = "DELETE FROM arts WHERE id = ?"
			self.cursor.execute(query, [art.id])
			c = self.cursor.rowcount
			if c == 0:
				self.bd.rollback()
				return False
			else:
				self.bd.commit()
				return True
		except:
			self.bd.rollback()
			return False

	def update(self, art):
		'''Recibe un objeto art y actualiza sus datos en el base de datos
		(no se puede actualizar el id de el art, pero sí el resto de sus
		datos). Retorna True si tuvo éxito, False de lo contrario.'''
		try:
			query = "UPDATE arts SET nombre = ?, precio = ? WHERE id = ?"
			result = self.cursor.execute(query, [art.nombre, art.precio,
												 art.id])
			if result.rowcount == 0:
				self.bd.rollback()
				return False
			else:
				self.bd.commit()
				return True
		except:
			self.bd.rollback()
			return False

