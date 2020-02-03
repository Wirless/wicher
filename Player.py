#############################
# Author : PZmyslony
# Version : 1.0
# Module : Player Class
# .
###########################
import math

class Player:

	def __init__(self):
		self.health = 100
		self.mana = 25
		self.strength = 1
		self.dexterity = 1
		self.speed = 1
		self.defense = 1
		self.experience = 0
		self.equipmentattack = 0
		self.equipmentdefense = 0
		self.intelligence = 0
		return self
	
	def move(self, position, newposition):
		position = newposition
		print(f"Player previous position {position}\n player new position {newposition}")
		return position, newposition

	def attack(self, strength,equipmentattack):
		damage = strength+equipmentattack
		print(f"player output damage for next turn is {damage}")
		return damage
		
	def block(self, defense, equipmentdefense):
		block = defense+equipmentdefense
		print(f"Player output defense for next turn is {block}")
		return block
	
	def spellcast(self, mana, intelligence, spell, spellcost, spellmindmg):
		cast = (spellcost+spellmindmg)*intelligence
		print(f"Player output spell damage for next turn is {cast}")
		return cast
