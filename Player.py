#############################
# Author : PZmyslony
# Version : 1.0
# Module : Player Class
# .
###########################
import math

class Player

	def __init__(self, health, mana, strength, dexterity, speed, defense, experience,equipmentattack, equipmentdefense, intelligence):
		health = 100
		mana = 25
		strength = 1
		dexterity = 1
		speed = 1
		defense = 1
		experience = 0
		equipmentattack = 0
		equipmentdefense = 0
		intelligence = 0
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