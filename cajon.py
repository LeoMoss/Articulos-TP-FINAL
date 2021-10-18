#! /usr/bin/python3
from art import Art

''' Crea objetos Cajon ( para guardar botellas de cocacola y otros envases) 
los cajones tienen un nombre, marca, cantidad de botellas, y un estado''' 
class Cajon(Art):
	def __init__(self, nombre, precio, id_art, marca, cbotellas):
		self.cbotellas = cbotellas
		super().__init__(nombre, precio, id_art, marca)
		

